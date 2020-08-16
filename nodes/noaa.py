#!/usr/bin/env python3
"""
Polyglot v2 node server NOAA weather data
Copyright (C) 2020 Robert Paauwe
"""

try:
    import polyinterface
except ImportError:
    import pgc_interface as polyinterface
import sys
import time
import datetime
import requests
import socket
import math
import re
import json
import node_funcs
from datetime import timedelta
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
#from nodes import uom

LOGGER = polyinterface.LOGGER

@node_funcs.add_functions_as_methods(node_funcs.functions)
class Controller(polyinterface.Controller):
    id = 'weather'
    #id = 'controller'
    hint = [0,0,0,0]
    def __init__(self, polyglot):
        super(Controller, self).__init__(polyglot)
        self.name = 'NOAA Weather'
        self.address = 'weather'
        self.primary = self.address
        self.configured = False
        self.latitude = 0
        self.longitude = 0
        self.force = True

        self.params = node_funcs.NSParameters([{
            'name': 'Station',
            'default': 'set me',
            'isRequired': True,
            'notice': 'NOAA station must be set',
            },
            ])


        self.poly.onConfig(self.process_config)

    # Process changes to customParameters
    def process_config(self, config):
        (valid, changed) = self.params.update_from_polyglot(config)
        if changed and not valid:
            LOGGER.debug('-- configuration not yet valid')
            self.removeNoticesAll()
            self.params.send_notices(self)
        elif changed and valid:
            LOGGER.debug('-- configuration is valid')
            self.removeNoticesAll()
            self.configured = True
        elif valid:
            LOGGER.debug('-- configuration not changed, but is valid')

    def start(self):
        LOGGER.info('Starting node server')
        self.check_params()
        self.discover()
        LOGGER.info('Node server started')

        # Do an initial query to get filled in as soon as possible
        self.query_conditions()
        self.force = False

    def longPoll(self):
        LOGGER.debug('longpoll')
        pass

    def shortPoll(self):
        self.query_conditions()

    def query_conditions(self):
        # Query for the current conditions. We can do this fairly
        # frequently, probably as often as once a minute.

        if not self.configured:
            LOGGER.info('Skipping connection because we aren\'t configured yet.')
            return


        try:
            request = 'http://w1.weather.gov/xml/current_obs/'
            request += self.params.get('Station') + '.xml'

            c = requests.get(request)
            xdata = c.text
            c.close()
            LOGGER.debug(xdata)

            if xdata == None:
                LOGGER.error('Current condition query returned no data')
                return
        
            LOGGER.debug('Parse XML and set drivers')
            noaa = ET.fromstring(xdata)
            for item in noaa:
                LOGGER.debug(item.tag)
                if item.tag == 'temp_f':
                    LOGGER.debug(item.attrib)
                if item.tag == 'temp_c':
                    LOGGER.debug(item.attrib)
                if item.tag == 'relative_humdity':
                    LOGGER.debug(item.attrib)
                if item.tag == 'wind_dir':
                    LOGGER.debug(item.attrib)
                if item.tag == 'wind_degrees':
                    LOGGER.debug(item.attrib)
                if item.tag == 'wind_mph':
                    LOGGER.debug(item.attrib)
                if item.tag == 'wind_kt':
                    LOGGER.debug(item.attrib)
                if item.tag == 'pressure_in':
                    LOGGER.debug(item.attrib)
                if item.tag == 'dewpoint_f':
                    LOGGER.debug(item.attrib)
                if item.tag == 'dewpoint_c':
                    LOGGER.debug(item.attrib)
                if item.tag == 'heat_index_f':
                    LOGGER.debug(item.attrib)
                if item.tag == 'heat_index_c':
                    LOGGER.debug(item.attrib)
                if item.tag == 'visibility_mi':
                    LOGGER.debug(item.attrib)

            return
            if 'temp' in jdata:
                self.update_driver('CLITEMP', jdata['temp']['value'])

            if 'humidity' in jdata:
                self.update_driver('CLIHUM', jdata['humidity']['value'])
            if 'baro_pressure' in jdata:
                self.update_driver('BARPRES', jdata['baro_pressure']['value'])
            if 'wind_speed' in jdata:
                self.update_driver('SPEED', jdata['wind_speed']['value'])
            if 'wind_gust' in jdata:
                self.update_driver('GV5', jdata['wind_gust']['value'])
            if 'wind_direction' in jdata:
                self.update_driver('WINDDIR', jdata['wind_direction']['value'])
            if 'visibility' in jdata:
                self.update_driver('DISTANC', jdata['visibility']['value'])
            if 'precipitation' in jdata:
                self.update_driver('RAINRT', jdata['precipitation']['value'])
            if 'dewpoint' in jdata:
                self.update_driver('DEWPT', jdata['dewpoint']['value'])
            if 'feels_like' in jdata:
                self.update_driver('GV2', jdata['feels_like']['value'])
            if 'surface_shortwave_radiation' in jdata:
                self.update_driver('SOLRAD', jdata['surface_shortwave_radiation']['value'])
            if 'cloud_cover' in jdata:
                self.update_driver('GV14', jdata['cloud_cover']['value'])
            if 'weather_code' in jdata:
                LOGGER.debug('weather code = ' + jdata['weather_code']['value'])
                self.update_driver('GV13', wx.weather_code(jdata['weather_code']['value']))
            if 'moon_phase' in jdata:
                self.update_driver('GV9', wx.moon_phase(jdata['moon_phase']['value']))
            if 'epa_aqi' in jdata:
                self.update_driver('GV17', jdata['epa_aqi']['value'])

        except Exception as e:
            LOGGER.error('Current observation update failure')
            LOGGER.error(e)

    def query(self):
        for node in self.nodes:
            self.nodes[node].reportDrivers()

    def discover(self, *args, **kwargs):
        # Create any additional nodes here
        LOGGER.info("In Discovery...")

    # Delete the node server from Polyglot
    def delete(self):
        LOGGER.info('Removing node server')

    def stop(self):
        LOGGER.info('Stopping node server')

    def update_profile(self, command):
        st = self.poly.installprofile()
        return st

    def check_params(self):
        self.removeNoticesAll()

        if self.params.get_from_polyglot(self):
            LOGGER.debug('All required parameters are set!')
            self.configured = True
            LOGGER.debug('Configuration required.')
            LOGGER.debug('Station = ' + self.params.get('Station'))
            self.params.send_notices(self)

    def remove_notices_all(self, command):
        self.removeNoticesAll()

    def set_logging_level(self, level=None):
        if level is None:
            try:
                # level = self.getDriver('GVP')
                level = self.get_saved_log_level()
            except:
                LOGGER.error('set_logging_level: get saved log level failed.')

            if level is None:
                level = 30

            level = int(level)
        else:
            level = int(level['value'])

        # self.setDriver('GVP', level, True, True)
        self.save_log_level(level)
        LOGGER.info('set_logging_level: Setting log level to %d' % level)
        LOGGER.setLevel(level)

    commands = {
            'UPDATE_PROFILE': update_profile,
            'REMOVE_NOTICES_ALL': remove_notices_all,
            'DEBUG': set_logging_level,
            }

    # For this node server, all of the info is available in the single
    # controller node.
    drivers = [
            {'driver': 'ST', 'value': 1, 'uom': 2},   # node server status
            {'driver': 'CLITEMP', 'value': 0, 'uom': 4},   # temperature
            {'driver': 'CLIHUM', 'value': 0, 'uom': 22},   # humidity
            {'driver': 'DEWPT', 'value': 0, 'uom': 4},     # dewpoint
            {'driver': 'BARPRES', 'value': 0, 'uom': 117}, # pressure
            {'driver': 'WINDDIR', 'value': 0, 'uom': 76},  # direction
            {'driver': 'SPEED', 'value': 0, 'uom': 49},    # wind speed
            {'driver': 'GV5', 'value': 0, 'uom': 49},      # gust speed
            {'driver': 'GV2', 'value': 0, 'uom': 4},       # feels like
            {'driver': 'RAINRT', 'value': 0, 'uom': 46},   # rain
            {'driver': 'GV13', 'value': 0, 'uom': 25},     # climate conditions
            {'driver': 'GV14', 'value': 0, 'uom': 22},     # cloud conditions
            {'driver': 'GV9', 'value': 0, 'uom': 56},      # moon phase
            {'driver': 'DISTANC', 'value': 0, 'uom': 83},  # visibility
            {'driver': 'SOLRAD', 'value': 0, 'uom': 74},   # solar radiataion
            {'driver': 'GV17', 'value': 0, 'uom': 56},     # aqi
            {'driver': 'GVP', 'value': 30, 'uom': 25},     # log level
            ]


