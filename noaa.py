#!/usr/bin/env python3
"""
Polyglot v3 node server NOAA weather data
Copyright (C) 2020,2021 Robert Paauwe
"""

import udi_interface
import sys
import time
from nodes import noaa

LOGGER = udi_interface.LOGGER

if __name__ == "__main__":
    try:
        polyglot = udi_interface.Interface([noaa.Controller])
        polyglot.start('2.0.6')
        noaa.Controller(polyglot, 'controller', 'controller', 'NOAA Weather')
        polyglot.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
        

