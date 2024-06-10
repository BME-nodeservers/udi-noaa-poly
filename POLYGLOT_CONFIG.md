The NOAA weather node server has the following user configuration
parameters:

- Station : The NOAA weather station identifier, typically an airport code. Go to https://forecast.weather.gov/xml/current_obs/ to look up the station for your area.
- Alert zone/county code: The NOAA alert area code. Go to https://alerts.weather.gov to look up the area code for your state/county/zone.

The shortPoll configuration option specifies how often to poll NOAA, in seconds.

The longPoll configuration option specifies how often to poll for alerts, in seconds.
