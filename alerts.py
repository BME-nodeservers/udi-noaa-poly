#!/usr/bin/python3

alerts = ['911 Telephone Outage',
'Administrative Message',
'Air Quality Alert',
'Air Stagnation Advisory',
'Arroyo And Small Stream Flood Advisory',
'Ashfall Advisory',
'Ashfall Warning',
'Avalanche Advisory',
'Avalanche Warning',
'Avalanche Watch',
'Beach Hazards Statement',
'Blizzard Warning',
'Blizzard Watch',
'Blowing Dust Advisory',
'Blowing Dust Warning',
'Blue Alert',
'Brisk Wind Advisory',
'Child Abduction Emergency',
'Civil Danger Warning',
'Civil Emergency Message',
'Coastal Flood Advisory',
'Coastal Flood Statement',
'Coastal Flood Warning',
'Coastal Flood Watch',
'Dense Fog Advisory',
'Dense Smoke Advisory',
'Dust Advisory',
'Dust Storm Warning',
'Earthquake Warning',
'Evacuation - Immediate',
'Excessive Heat Warning',
'Excessive Heat Watch',
'Extreme Cold Warning',
'Extreme Cold Watch',
'Extreme Fire Danger',
'Extreme Wind Warning',
'Fire Warning',
'Fire Weather Watch',
'Flash Flood Statement',
'Flash Flood Warning',
'Flash Flood Watch',
'Flood Advisory',
'Flood Statement',
'Flood Warning',
'Flood Watch',
'Freeze Warning',
'Freeze Watch',
'Freezing Fog Advisory',
'Freezing Rain Advisory',
'Freezing Spray Advisory',
'Frost Advisory',
'Gale Warning',
'Gale Watch',
'Hard Freeze Warning',
'Hard Freeze Watch',
'Hazardous Materials Warning',
'Hazardous Seas Warning',
'Hazardous Seas Watch',
'Hazardous Weather Outlook',
'Heat Advisory',
'Heavy Freezing Spray Warning',
'Heavy Freezing Spray Watch',
'High Surf Advisory',
'High Surf Warning',
'High Wind Warning',
'High Wind Watch',
'Hurricane Force Wind Warning',
'Hurricane Force Wind Watch',
'Hurricane Local Statement',
'Hurricane Warning',
'Hurricane Watch',
'Hydrologic Advisory',
'Hydrologic Outlook',
'Ice Storm Warning',
'Lake Effect Snow Advisory',
'Lake Effect Snow Warning',
'Lake Effect Snow Watch',
'Lake Wind Advisory',
'Lakeshore Flood Advisory',
'Lakeshore Flood Statement',
'Lakeshore Flood Warning',
'Lakeshore Flood Watch',
'Law Enforcement Warning',
'Local Area Emergency',
'Low Water Advisory',
'Marine Weather Statement',
'Nuclear Power Plant Warning',
'Radiological Hazard Warning',
'Red Flag Warning',
'Rip Current Statement',
'Severe Thunderstorm Warning',
'Severe Thunderstorm Watch',
'Severe Weather Statement',
'Shelter In Place Warning',
'Short Term Forecast',
'Small Craft Advisory',
'Small Craft Advisory For Hazardous Seas',
'Small Craft Advisory For Rough Bar',
'Small Craft Advisory For Winds',
'Small Stream Flood Advisory',
'Snow Squall Warning',
'Special Marine Warning',
'Special Weather Statement',
'Storm Surge Warning',
'Storm Surge Watch',
'Storm Warning',
'Storm Watch',
'Test',
'Tornado Warning',
'Tornado Watch',
'Tropical Depression Local Statement',
'Tropical Storm Local Statement',
'Tropical Storm Warning',
'Tropical Storm Watch',
'Tsunami Advisory',
'Tsunami Warning',
'Tsunami Watch',
'Typhoon Local Statement',
'Typhoon Warning',
'Typhoon Watch',
'Urban And Small Stream Flood Advisory',
'Volcano Warning',
'Wind Advisory',
'Wind Chill Advisory',
'Wind Chill Warning',
'Wind Chill Watch',
'Winter Storm Warning'
]


x = 1
for a in alerts:
    #print('	elif alert == \'{}\': return {}'.format(a, x))
    print('EN_ALERT-{} = {}'.format(x, a))
    x += 1