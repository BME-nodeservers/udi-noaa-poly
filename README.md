
# NOAA weather service

This is a node server to pull weather data from the NOAA weather network and make it available to a [Universal Devices ISY994i](https://www.universal-devices.com/residential/ISY) [Polyglot interface](http://www.universal-devices.com/developers/polyglot/docs/) with  [Polyglot V2](https://github.com/Einstein42/udi-polyglotv2)

(c) 2020 Robert Paauwe

## Installation

1. Backup Your ISY in case of problems!
   * Really, do the backup, please
2. Go to the Polyglot Store in the UI and install.
3. Add NodeServer in Polyglot Web
   * After the install completes, Polyglot will reboot your ISY, you can watch the status in the main polyglot log.
4. Once your ISY is back up open the Admin Console.
5. Configure the node server per configuration section below.

### Node Settings
The settings for this node are:

#### Short Poll
   * How often to poll the NOAA weather service for current condition data (in seconds). Note that the PWS partner plan only allows for 1000 requests per day so set this appropriately. Also note that two queries are made during each poll.
#### Long Poll
	* Not used
	* Your AERIS client ID, needed to authorize the connection the the AERIS API.
#### Station
	* The weather station to use for for weather data. Go to https://w1.weather.gov/xml/current_obs/ to look up the station for your area.

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

## Requirements
1. Polyglot V2.
2. ISY firmware 5.0.x or later

# Upgrading

Open the Polyglot web page, go to nodeserver store and click "Update" for "NOAA Weather".

Then restart the NOAA nodeserver by selecting it in the Polyglot dashboard and select Control -> Restart, then watch the log to make sure everything goes well.

The nodeserver keeps track of the version number and when a profile rebuild is necessary.  The profile/version.txt will contain the profile_version which is updated in server.json when the profile should be rebuilt.

# Release Notes

- 1.0.0 08/16/2020
   - Initial public release
