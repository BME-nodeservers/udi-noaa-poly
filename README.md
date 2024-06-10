
# NOAA weather service

This is a node server to pull weather data from the NOAA weather network and make it
available to a [Universal Devices ISY994i](https://www.universal-devices.com/residential/ISY)
[Polyglot interface](http://www.universal-devices.com/developers/polyglot/docs/) with
Polyglot V3 running on a [Polisy](https://www.universal-devices.com/product/polisy/)

(c) 2020,2021 Robert Paauwe

## Installation

1. Backup Your ISY in case of problems!
   * Really, do the backup, please
2. Go to the Polyglot Store in the UI and install.
3. From the Polyglot dashboard, select the NOAA node server and configure (see configuration options below).
4. Once configured, the NOAA node server should update the ISY with the proper nodes and begin filling in the node data.
5. Restart the Admin Console so that it can properly display the new node server nodes.

### Node Settings
The settings for this node are:

#### Short Poll
   * How often to poll the NOAA weather service for current condition data (in seconds). 
#### Long Poll
	* How often to poll for alert data (in seconds).  Must be larger than short poll.
#### Station
	* The weather station to use for for weather data. Go to https://forecast.weather.gov/xml/current_obs/ to look up the station for your area.
#### Alert zone/county code
	* The code from alerts.weather.gov that specify the zone or county you want alerts for.  Look up the code on the site and enter it here, it will typically be a 6 character code.

## Node substitution variables
### Current condition node
 * sys.node.[address].ST      (Node sever online)
 * sys.node.[address].CLITEMP (current temperature)
 * sys.node.[address].CLIHUM  (current humidity)
 * sys.node.[address].DEWPT   (current dew point)
 * sys.node.[address].BARPRES (current barometric pressure)
 * sys.node.[address].SPEED   (current wind speed)
 * sys.node.[address].WINDDIR (current wind direction )
 * sys.node.[address].DISTANC (current visibility)
 * sys.node.[address].GV13    (current weather conditions)

 ### Alert infomation
 * sys.node.[address].GV21    (Alert text)
 * sys.node.[address].GV22    (Alert status)
 * sys.node.[address].GV23    (Alert message type)
 * sys.node.[address].GV24    (Alert category)
 * sys.node.[address].GV25    (Alert severity)
 * sys.node.[address].GV26    (Alert urgency)
 * sys.node.[address].GV27    (Alert certainy)

## Requirements
1. Polyglot V3.
2. ISY firmware 5.3.x or later

# Release Notes
- 2.0.2 05/29/2022
   - Use new PG3 tristate status
   - Update to latest UDI_Interface
   - Send version number from start
- 2.0.1 04/18/2022
   - Update to use the latest udi_interface module
- 2.0.0 03/01/2021
   - Updated to run on Polyglot Version 3
- 1.1.2 02/16/2021
   - fix typo with Exception
- 1.1.1 02/10/2021
   - Fix id for Winter Storm Warning
- 1.1.0 12/20/2020
   - Add alert data from alerts.weather.gov 
- 1.0.0 08/16/2020
   - Initial public release
