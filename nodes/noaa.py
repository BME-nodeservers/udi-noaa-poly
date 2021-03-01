#!/usr/bin/env python3
"""
Polyglot v3 node server NOAA weather data
Copyright (C) 2020,2021 Robert Paauwe
"""

import udi_interface
import sys
import time
import datetime
import requests
import socket
import math
import re
import json
from datetime import timedelta
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from nodes import uom
from nodes import conditions

LOGGER = udi_interface.LOGGER
Custom = udi_interface.Custom

class Controller(udi_interface.Node):
    id = 'weather'
    def __init__(self, polyglot, primary, address, name):
        super(Controller, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.name = name
        self.address = address
        self.primary = primary

        self.Parameters = Custom(polyglot, 'customparams')
        self.Notices = Custom(polyglot, 'notices')

        self.configured = False
        self.latitude = 0
        self.longitude = 0
        self.force = True

        self.poly.subscribe(self.poly.CUSTOMPARAMS, self.parameterHandler)
        self.poly.subscribe(self.poly.START, self.start, self.address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.poly.subscribe(self.poly.ADDNODEDONE, self.nodesDoneHandler)
        self.poly.ready()
        self.poly.addNode(self)

        """
        self.params = node_funcs.NSParameters([{
            'name': 'Station',
            'default': 'set me',
            'isRequired': True,
            'notice': 'NOAA station must be set',
            },
            {
            'name': 'Alert zone/county code',
            'default': 'set me',
            'isRequired': False,
            'notice': 'NOAA Zone/County code for Weather alerts.',
            },
            ])
        """



    # Process changes to customParameters
    def parameterHandler(self, params):
        self.configurd = False
        self.Parameters.load(params)
        
        self.Notices.clear()
        if self.Parameters.Station is not None:
            self.configurd = True
        else:
            LOGGER.debug('Missing station configuration')
            self.Notices['station'] = 'Please enter a NOAA station ID'


    def start(self):
        LOGGER.info('Starting node server')
        self.poly.updateProfile()
        self.setCustomParamsDoc()
        self.uom = uom.get_uom('imperial')
        
        while not self.configured:
            time.sleep(10)

        LOGGER.info('Node server started')

        # Do an initial query to get filled in as soon as possible
        self.query_conditions()
        if self.Parameters['Alert zone/county code'] is not None:
            self.query_alerts(self.Parameters['Alert zone/county code'])
        self.force = False

    def poll(self, polltype):
        if polltype == 'shortPoll':
            self.query_conditions()
        else:
            if self.Parameters['Alert zone/county code'] is not None:
                self.query_alerts(self.Parameters['Alert zone/county code'])

    def update_driver(self, driver, value, force=False, prec=3):
        try:
            if value == None or value == "None":
                value = "0"
            self.setDriver(driver, round(float(value), prec), True, force, self.uom[driver])
            LOGGER.debug('setDriver (%s, %f)' %(driver, float(value)))
        except:
            LOGGER.warning('Missing data for driver ' + driver)

    def query_conditions(self):
        # Query for the current conditions. We can do this fairly
        # frequently, probably as often as once a minute.

        if not self.configured:
            LOGGER.info('Skipping connection because we aren\'t configured yet.')
            return


        try:
            request = 'http://w1.weather.gov/xml/current_obs/'
            request += self.Parameters['Station'] + '.xml'

            c = requests.get(request)
            xdata = c.text
            c.close()
            #LOGGER.debug(xdata)

            if xdata == None:
                LOGGER.error('Current condition query returned no data')
                return
        
            LOGGER.debug('Parse XML and set drivers')
            noaa = ET.fromstring(xdata)
            for item in noaa:
                LOGGER.debug(item.tag + ' = ' + item.text)
                if item.tag == 'temp_f':
                    self.update_driver('CLITEMP', item.text)
                if item.tag == 'temp_c':
                    LOGGER.debug(item.text)
                if item.tag == 'relative_humidity':
                    self.update_driver('CLIHUM', item.text)
                if item.tag == 'wind_dir':
                    LOGGER.debug(item.text)
                if item.tag == 'wind_degrees':
                    self.update_driver('WINDDIR', item.text)
                if item.tag == 'wind_mph':
                    self.update_driver('SPEED', item.text)
                if item.tag == 'wind_kt':
                    LOGGER.debug(item.text)
                if item.tag == 'pressure_in':
                    self.update_driver('BARPRES', item.text)
                if item.tag == 'dewpoint_f':
                    self.update_driver('DEWPT', item.text)
                if item.tag == 'dewpoint_c':
                    LOGGER.debug(item.text)
                if item.tag == 'heat_index_f':
                    LOGGER.debug(item.text)
                if item.tag == 'heat_index_c':
                    LOGGER.debug(item.text)
                if item.tag == 'visibility_mi':
                    self.update_driver('DISTANC', item.text)
                if item.tag == 'weather':
                    self.update_driver('GV13', conditions.phrase_to_id(item.text))

        except Exception as e:
            LOGGER.error('Current observation update failure')
            LOGGER.error(e)

    def query_alerts(self, code):
        if not self.configured:
            LOGGER.info('Skipping alerts because we aren\'t configured yet.')
            return


        try:
            request = 'https://alerts.weather.gov/cap/wwaatmget.php?'
            request += 'x=' + code + '&y=1'

            c = requests.get(request)
            xdata = c.text
            c.close()
            #LOGGER.debug(xdata)

            if xdata == None:
                LOGGER.error('Weather alert query returned no data')
                return
        
            LOGGER.debug('Parse XML and set drivers')
            noaa = ET.fromstring(xdata)

            """ We're looking for:
            <cap:event>Dense Fog Advisory</cap:event>
            <cap:effective>2020-12-19T18:23:00-08:00</cap:effective>
            <cap:expires>2020-12-20T11:00:00-08:00</cap:expires>
            <cap:status>Actual</cap:status>
            <cap:msgType>Alert</cap:msgType>
            <cap:category>Met</cap:category>
            <cap:urgency>Expected</cap:urgency>
            <cap:severity>Minor</cap:severity>
            <cap:certainty>Likely</cap:certainty>
            """
            for entry in noaa:
                if entry.tag == '{http://www.w3.org/2005/Atom}entry':
                    for item in entry:
                        if item.text:
                            LOGGER.debug(item.tag + ' = ' + item.text)
                            if 'event' in item.tag:
                                LOGGER.debug('ALERT: ' + item.text)
                                self.update_driver('GV21', conditions.alert_to_id(item.text))
                            if 'effective' in item.tag:
                                LOGGER.debug('EFFECTIVE: ' + item.text)
                            if 'expires' in item.tag:
                                LOGGER.debug('EXPIRES: ' + item.text)
                                #self.update_driver('TIME', item.text)
                                #self.update_driver('TIME', 100343434)
                            if 'status' in item.tag:
                                LOGGER.debug('STATUS: ' + item.text)
                                self.update_driver('GV22', conditions.status_to_id(item.text))
                            if 'msgType' in item.tag:
                                LOGGER.debug('TYPE: ' + item.text)
                                self.update_driver('GV23', conditions.type_to_id(item.text))
                            if 'category' in item.tag:
                                LOGGER.debug('CATEGORY: ' + item.text)
                                self.update_driver('GV24', conditions.category_to_id(item.text))
                            if 'severity' in item.tag:
                                LOGGER.debug('SEVERITY: ' + item.text)
                                self.update_driver('GV25', conditions.severity_to_id(item.text))
                            if 'urgency' in item.tag:
                                LOGGER.debug('URGENCY: ' + item.text)
                                self.update_driver('GV26', conditions.urgency_to_id(item.text))
                            if 'certainy' in item.tag:
                                LOGGER.debug('CERTAINY: ' + item.text)
                                self.update_driver('GV27', conditions.certainy_to_id(item.text))

        except Exception as e:
            LOGGER.error('Weather alert update failure')
            LOGGER.error(e)

    def query(self, cmd=None):
        self.query_conditions()
        if self.Parameters['Alert zone/county code'] is not None:
            self.query_alerts(self.Parameters['Alert zone/county code'])

    def discover(self, *args, **kwargs):
        # Create any additional nodes here
        LOGGER.info("In Discovery...")

    # Delete the node server from Polyglot
    def delete(self):
        LOGGER.info('Removing node server')

    def stop(self):
        LOGGER.info('Stopping node server')

    commands = {
            'QUERY':  do_query,
            'UPDATE_PROFILE': update_profile,
            }

    # For this node server, all of the info is available in the single
    # controller node.
    drivers = [
            {'driver': 'ST', 'value': 1, 'uom': 2},   # node server status
            {'driver': 'CLITEMP', 'value': 0, 'uom': 17},  # temperature
            {'driver': 'CLIHUM', 'value': 0, 'uom': 22},   # humidity
            {'driver': 'DEWPT', 'value': 0, 'uom': 17},    # dewpoint
            {'driver': 'BARPRES', 'value': 0, 'uom': 117}, # pressure
            {'driver': 'WINDDIR', 'value': 0, 'uom': 76},  # direction
            {'driver': 'SPEED', 'value': 0, 'uom': 49},    # wind speed
            {'driver': 'DISTANC', 'value': 0, 'uom': 83},  # visibility
            {'driver': 'GV13', 'value': 0, 'uom': 25},     # weather
            {'driver': 'GV21', 'value': 0, 'uom': 25},     # alert
            {'driver': 'GV22', 'value': 0, 'uom': 25},     # status
            {'driver': 'GV23', 'value': 0, 'uom': 25},     # type
            {'driver': 'GV24', 'value': 0, 'uom': 25},     # category
            {'driver': 'GV25', 'value': 0, 'uom': 25},     # severity
            {'driver': 'GV26', 'value': 0, 'uom': 25},     # urgnecy
            {'driver': 'GV27', 'value': 0, 'uom': 25},     # certainy
            {'driver': 'GVP', 'value': 30, 'uom': 25},     # log level
            ]


