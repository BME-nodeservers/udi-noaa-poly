# NOAA weather condition phrases mapping to NLS strings

def phrase_to_id(phrase):
    if phrase == 'Mostly Cloudy':
        return 1
    elif phrase == 'Mostly Cloudy with Haze':
        return 2
    elif phrase == 'Mostly Cloudy and Breezy':
        return 3
    elif phrase == 'Fair':
        return 4
    elif phrase == 'Clear':
        return 5
    elif phrase == 'Fair with Haze':
        return 6
    elif phrase == 'Fair and Breezy':
        return 7
    elif phrase == 'Clear and Breezy':
        return 8
    elif phrase == 'A Few CloudsA Few Clouds with Haze':
        return 9
    elif phrase == 'A Few Clouds and Breezy':
        return 10
    elif phrase == 'Partly Cloudy':
        return 11
    elif phrase == 'Partly Cloudy with Haze':
        return 254
    elif phrase == 'Partly Cloudy and Breezy':
        return 12
    elif phrase == 'Overcast':
        return 13
    elif phrase == 'Overcast with Haze':
        return 255
    elif phrase == 'Overcast and Breezy':
        return 14
    elif phrase == 'Fog/MistFog':
        return 15
    elif phrase == 'Freezing Fog':
        return 16
    elif phrase == 'Shallow Fog':
        return 17
    elif phrase == 'Partial Fog':
        return 18
    elif phrase == 'Patches of Fog':
        return 19
    elif phrase == 'Fog in Vicinity':
        return 20
    elif phrase == 'Freezing Fog in Vicinity':
        return 21
    elif phrase == 'Shallow Fog in Vicinity':
        return 22
    elif phrase == 'Partial Fog in Vicinity':
        return 23
    elif phrase == 'Patches of Fog in Vicinity':
        return 24
    elif phrase == 'Showers in Vicinity Fog':
        return 25
    elif phrase == 'Light Freezing Fog':
        return 26
    elif phrase == 'Heavy Freezing Fog':
        return 27
    elif phrase == 'Smoke':
        return 28
    elif phrase == 'Freezing Rain':
        return 29
    elif phrase == 'Freezing Drizzle':
        return 256
    elif phrase == 'Light Freezing Rain':
        return 30
    elif phrase == 'Light Freezing Drizzle':
        return 31
    elif phrase == 'Heavy Freezing Rain':
        return 32
    elif phrase == 'Heavy Freezing Drizzle':
        return 33
    elif phrase == 'Freezing Rain in Vicinity':
        return 34
    elif phrase == 'Freezing Drizzle in Vicinity':
        return 35
    elif phrase == 'Ice Pellets':
        return 36
    elif phrase == 'Light Ice Pellets':
        return 257
    elif phrase == 'Heavy Ice Pellets':
        return 37
    elif phrase == 'Ice Pellets in Vicinity':
        return 38
    elif phrase == 'Showers Ice Pellets':
        return 39
    elif phrase == 'Thunderstorm Ice Pellets':
        return 40
    elif phrase == 'Ice Crystals':
        return 41
    elif phrase == 'Hail':
        return 42
    elif phrase == 'Small Hail/Snow Pellets':
        return 43
    elif phrase == 'Light Small Hail/Snow Pellets':
        return 44
    elif phrase == 'Heavy small Hail/Snow Pellets':
        return 45
    elif phrase == 'Showers Hail':
        return 46
    elif phrase == 'Hail Showers':
        return 47
    elif phrase == 'Freezing Rain Snow':
        return 48
    elif phrase == 'Light Freezing Rain Snow':
        return 258
    elif phrase == 'Heavy Freezing Rain Snow':
        return 49
    elif phrase == 'Freezing Drizzle Snow':
        return 50
    elif phrase == 'Light Freezing Drizzle Snow':
        return 51
    elif phrase == 'Heavy Freezing Drizzle Snow':
        return 52
    elif phrase == 'Snow Freezing Rain':
        return 53
    elif phrase == 'Light Snow Freezing Rain':
        return 54
    elif phrase == 'Heavy Snow Freezing Rain':
        return 55
    elif phrase == 'Snow Freezing Drizzle':
        return 56
    elif phrase == 'Light Snow Freezing Drizzle':
        return 57
    elif phrase == 'Heavy Snow Freezing Drizzle':
        return 58
    elif phrase == 'Rain Ice Pellets':
        return 59
    elif phrase == 'Light Rain Ice Pellets':
        return 259
    elif phrase == 'Heavy Rain Ice Pellets':
        return 60
    elif phrase == 'Drizzle Ice Pellets':
        return 61
    elif phrase == 'Light Drizzle Ice Pellets':
        return 62
    elif phrase == 'Heavy Drizzle Ice Pellets':
        return 63
    elif phrase == 'Ice Pellets Rain':
        return 64
    elif phrase == 'Light Ice Pellets Rain':
        return 65
    elif phrase == 'Heavy Ice Pellets Rain':
        return 66
    elif phrase == 'Ice Pellets Drizzle':
        return 67
    elif phrase == 'Light Ice Pellets Drizzle':
        return 68
    elif phrase == 'Heavy Ice Pellets Drizzle':
        return 69
    elif phrase == 'Rain Snow':
        return 70
    elif phrase == 'Light Rain Snow':
        return 260
    elif phrase == 'Heavy Rain Snow':
        return 71
    elif phrase == 'Snow Rain':
        return 72
    elif phrase == 'Light Snow Rain':
        return 73
    elif phrase == 'Heavy Snow Rain':
        return 74
    elif phrase == 'Drizzle Snow':
        return 75
    elif phrase == 'Light Drizzle Snow':
        return 76
    elif phrase == 'Heavy Drizzle Snow':
        return 77
    elif phrase == 'Snow Drizzle':
        return 78
    elif phrase == 'Light Snow Drizzle':
        return 79
    elif phrase == 'Heavy Drizzle Snow':
        return 80
    elif phrase == 'Rain Showers':
        return 81
    elif phrase == 'Light Rain Showers':
        return 261
    elif phrase == 'Light Rain and Breezy':
        return 82
    elif phrase == 'Heavy Rain Showers':
        return 83
    elif phrase == 'Rain Showers in Vicinity':
        return 84
    elif phrase == 'Light Showers Rain':
        return 85
    elif phrase == 'Heavy Showers Rain':
        return 86
    elif phrase == 'Showers Rain':
        return 87
    elif phrase == 'Showers Rain in Vicinity':
        return 88
    elif phrase == 'Rain Showers Fog/Mist':
        return 89
    elif phrase == 'Light Rain Showers Fog/Mist':
        return 90
    elif phrase == 'Heavy Rain Showers Fog/Mist':
        return 91
    elif phrase == 'Rain Showers in Vicinity Fog/Mist':
        return 92
    elif phrase == 'Light Showers Rain Fog/Mist':
        return 93
    elif phrase == 'Heavy Showers Rain Fog/Mist':
        return 94
    elif phrase == 'Showers Rain Fog/Mist':
        return 95
    elif phrase == 'Showers Rain in Vicinity Fog/Mist':
        return 96
    elif phrase == 'Thunderstorm':
        return 97
    elif phrase == 'Thunderstorm Rain':
        return 262
    elif phrase == 'Light Thunderstorm Rain':
        return 98
    elif phrase == 'Heavy Thunderstorm Rain':
        return 99
    elif phrase == 'Thunderstorm Rain Fog/Mist':
        return 100
    elif phrase == 'Light Thunderstorm Rain Fog/Mist':
        return 101
    elif phrase == 'Heavy Thunderstorm Rain Fog and Windy':
        return 102
    elif phrase == 'Heavy Thunderstorm Rain Fog/Mist':
        return 103
    elif phrase == 'Thunderstorm Showers in Vicinity':
        return 104
    elif phrase == 'Light Thunderstorm Rain Haze':
        return 105
    elif phrase == 'Heavy Thunderstorm Rain Haze':
        return 106
    elif phrase == 'Thunderstorm Fog':
        return 107
    elif phrase == 'Light Thunderstorm Rain Fog':
        return 108
    elif phrase == 'Heavy Thunderstorm Rain Fog':
        return 109
    elif phrase == 'Thunderstorm Light Rain':
        return 110
    elif phrase == 'Thunderstorm Heavy Rain':
        return 111
    elif phrase == 'Thunderstorm Rain Fog/Mist':
        return 112
    elif phrase == 'Thunderstorm Light Rain Fog/Mist':
        return 113
    elif phrase == 'Thunderstorm Heavy Rain Fog/Mist':
        return 114
    elif phrase == 'Thunderstorm in Vicinity Fog/Mist':
        return 115
    elif phrase == 'Thunderstorm Showers in Vicinity':
        return 116
    elif phrase == 'Thunderstorm in Vicinity Haze':
        return 117
    elif phrase == 'Thunderstorm Haze in Vicinity':
        return 118
    elif phrase == 'Thunderstorm Light Rain Haze':
        return 119
    elif phrase == 'Thunderstorm Heavy Rain Haze':
        return 120
    elif phrase == 'Thunderstorm Fog':
        return 121
    elif phrase == 'Thunderstorm Light Rain Fog':
        return 122
    elif phrase == 'Thunderstorm Heavy Rain Fog':
        return 123
    elif phrase == 'Thunderstorm Hail':
        return 124
    elif phrase == 'Light Thunderstorm Rain Hail':
        return 125
    elif phrase == 'Heavy Thunderstorm Rain Hail':
        return 126
    elif phrase == 'Thunderstorm Rain Hail Fog/Mist':
        return 127
    elif phrase == 'Light Thunderstorm Rain Hail Fog/Mist':
        return 128
    elif phrase == 'Heavy Thunderstorm Rain Hail Fog/Hail':
        return 129
    elif phrase == 'Thunderstorm Showers in Vicinity Hail':
        return 130
    elif phrase == 'Light Thunderstorm Rain Hail Haze':
        return 131
    elif phrase == 'Heavy Thunderstorm Rain Hail Haze':
        return 132
    elif phrase == 'Thunderstorm Hail Fog':
        return 133
    elif phrase == 'Light Thunderstorm Rain Hail Fog':
        return 134
    elif phrase == 'Heavy Thunderstorm Rain Hail Fog':
        return 135
    elif phrase == 'Thunderstorm Light Rain Hail':
        return 136
    elif phrase == 'Thunderstorm Heavy Rain Hail':
        return 137
    elif phrase == 'Thunderstorm Rain Hail Fog/Mist':
        return 138
    elif phrase == 'Thunderstorm Light Rain Hail Fog/Mist':
        return 139
    elif phrase == 'Thunderstorm Heavy Rain Hail Fog/Mist':
        return 140
    elif phrase == 'Thunderstorm in Vicinity Hail':
        return 141
    elif phrase == 'Thunderstorm in Vicinity Hail Haze':
        return 142
    elif phrase == 'Thunderstorm Haze in Vicinity Hail':
        return 143
    elif phrase == 'Thunderstorm Light Rain Hail Haze':
        return 144
    elif phrase == 'Thunderstorm Heavy Rain Hail Haze':
        return 145
    elif phrase == 'Thunderstorm Hail Fog':
        return 146
    elif phrase == 'Thunderstorm Light Rain Hail Fog':
        return 147
    elif phrase == 'Thunderstorm Heavy Rain Hail Fog':
        return 148
    elif phrase == 'Thunderstorm Small Hail/Snow Pellets':
        return 149
    elif phrase == 'Thunderstorm Rain Small Hail/Snow Pellets':
        return 150
    elif phrase == 'Light Thunderstorm Rain Small Hail/Snow Pellets':
        return 151
    elif phrase == 'Heavy Thunderstorm Rain Small Hail/Snow Pellets':
        return 152
    elif phrase == 'Snow':
        return 153
    elif phrase == 'Light Snow':
        return 263
    elif phrase == 'Heavy Snow':
        return 154
    elif phrase == 'Snow Showers':
        return 155
    elif phrase == 'Light Snow Showers':
        return 156
    elif phrase == 'Heavy Snow Showers':
        return 157
    elif phrase == 'Showers Snow':
        return 158
    elif phrase == 'Light Showers Snow':
        return 159
    elif phrase == 'Heavy Showers Snow':
        return 160
    elif phrase == 'Snow Fog/Mist':
        return 161
    elif phrase == 'Light Snow Fog/Mist':
        return 162
    elif phrase == 'Heavy Snow Fog/Mist':
        return 163
    elif phrase == 'Snow Showers Fog/Mist':
        return 164
    elif phrase == 'Light Snow Showers Fog/Mist':
        return 165
    elif phrase == 'Heavy Snow Showers Fog/Mist':
        return 166
    elif phrase == 'Showers Snow Fog/Mist':
        return 167
    elif phrase == 'Light Showers Snow Fog/Mist':
        return 168
    elif phrase == 'Heavy Showers Snow Fog/Mist':
        return 169
    elif phrase == 'Snow Fog':
        return 170
    elif phrase == 'Light Snow Fog':
        return 171
    elif phrase == 'Heavy Snow Fog':
        return 172
    elif phrase == 'Snow Showers Fog':
        return 173
    elif phrase == 'Light Snow Showers Fog':
        return 174
    elif phrase == 'Heavy Snow Showers Fog':
        return 175
    elif phrase == 'Showers Snow Fog':
        return 176
    elif phrase == 'Light Showers Snow Fog':
        return 177
    elif phrase == 'Heavy Showers Snow Fog':
        return 178
    elif phrase == 'Showers in Vicinity Snow':
        return 179
    elif phrase == 'Snow Showers in Vicinity':
        return 180
    elif phrase == 'Snow Showers in Vicinity Fog/Mist':
        return 181
    elif phrase == 'Snow Showers in Vicinity Fog':
        return 182
    elif phrase == 'Low Drifting Snow':
        return 183
    elif phrase == 'Blowing Snow':
        return 184
    elif phrase == 'Snow Low Drifting Snow':
        return 185
    elif phrase == 'Snow Blowing Snow':
        return 186
    elif phrase == 'Light Snow Low Drifting Snow':
        return 187
    elif phrase == 'Light Snow Blowing Snow':
        return 188
    elif phrase == 'Light Snow Blowing Snow Fog/Mist':
        return 189
    elif phrase == 'Heavy Snow Low Drifting Snow':
        return 190
    elif phrase == 'Heavy Snow Blowing Snow':
        return 191
    elif phrase == 'Thunderstorm Snow':
        return 192
    elif phrase == 'Light Thunderstorm Snow':
        return 193
    elif phrase == 'Heavy Thunderstorm Snow':
        return 194
    elif phrase == 'Snow Grains':
        return 195
    elif phrase == 'Light Snow Grains':
        return 196
    elif phrase == 'Heavy Snow Grains':
        return 197
    elif phrase == 'Heavy Blowing Snow':
        return 198
    elif phrase == 'Blowing Snow in Vicinity':
        return 199
    elif phrase == 'Windy':
        return 200
    elif phrase == 'Breezy':
        return 264
    elif phrase == 'Fair and Windy':
        return 201
    elif phrase == 'A Few Clouds and Windy':
        return 202
    elif phrase == 'Partly Cloudy and Windy':
        return 203
    elif phrase == 'Mostly Cloudy and Windy':
        return 204
    elif phrase == 'Overcast and Windy':
        return 205
    elif phrase == 'Showers in Vicinity':
        return 206
    elif phrase == 'Showers in Vicinity Fog/Mist':
        return 265
    elif phrase == 'Showers in Vicinity Fog':
        return 207
    elif phrase == 'Showers in Vicinity Haze':
        return 208
    elif phrase == 'Freezing Rain RainLight Freezing Rain Rain':
        return 209
    elif phrase == 'Heavy Freezing Rain Rain':
        return 210
    elif phrase == 'Rain Freezing Rain':
        return 211
    elif phrase == 'Light Rain Freezing Rain':
        return 212
    elif phrase == 'Heavy Rain Freezing Rain':
        return 213
    elif phrase == 'Freezing Drizzle Rain':
        return 214
    elif phrase == 'Light Freezing Drizzle Rain':
        return 215
    elif phrase == 'Heavy Freezing Drizzle Rain':
        return 216
    elif phrase == 'Rain Freezing Drizzle':
        return 217
    elif phrase == 'Light Rain Freezing Drizzle':
        return 218
    elif phrase == 'Heavy Rain Freezing Drizzle':
        return 219
    elif phrase == 'Thunderstorm in Vicinity':
        return 220
    elif phrase == 'Thunderstorm in Vicinity Fog':
        return 266
    elif phrase == 'Thunderstorm in Vicinity Haze':
        return 221
    elif phrase == 'Light RainDrizzle':
        return 222
    elif phrase == 'Light Drizzle':
        return 223
    elif phrase == 'Heavy Drizzle':
        return 224
    elif phrase == 'Light Rain Fog/Mist':
        return 225
    elif phrase == 'Drizzle Fog/Mist':
        return 226
    elif phrase == 'Light Drizzle Fog/Mist':
        return 227
    elif phrase == 'Heavy Drizzle Fog/Mist':
        return 228
    elif phrase == 'Light Rain Fog':
        return 229
    elif phrase == 'Drizzle Fog':
        return 230
    elif phrase == 'Light Drizzle Fog':
        return 231
    elif phrase == 'Heavy Drizzle Fog':
        return 232
    elif phrase == 'Rain':
        return 233
    elif phrase == 'Heavy Rain':
        return 267
    elif phrase == 'Rain Fog/Mist':
        return 234
    elif phrase == 'Heavy Rain Fog/Mist':
        return 235
    elif phrase == 'Rain Fog':
        return 236
    elif phrase == 'Heavy Rain Fog':
        return 237
    elif phrase == 'Funnel Cloud':
        return 238
    elif phrase == 'Funnel Cloud in Vicinity':
        return 268
    elif phrase == 'Tornado/Water Spout':
        return 239
    elif phrase == 'DustLow Drifting Dust':
        return 240
    elif phrase == 'Blowing Dust':
        return 241
    elif phrase == 'Sand':
        return 242
    elif phrase == 'Blowing Sand':
        return 243
    elif phrase == 'Low Drifting Sand':
        return 244
    elif phrase == 'Dust/Sand Whirls':
        return 245
    elif phrase == 'Dust/Sand Whirls in Vicinity':
        return 246
    elif phrase == 'Dust Storm':
        return 247
    elif phrase == 'Heavy Dust Storm':
        return 248
    elif phrase == 'Dust Storm in Vicinity':
        return 249
    elif phrase == 'Sand Storm':
        return 250
    elif phrase == 'Heavy Sand Storm':
        return 251
    elif phrase == 'Sand Storm in Vicinity':
        return 252
    elif phrase == 'Haze':
        return 253
    else:
        return 0


# Alert list here: alerts.weather.gov/cap/product_list.txt

def alert_to_id(alert):

    if alert == '911 Telephone Outage': return 1
    elif alert == 'Administrative Message': return 2
    elif alert == 'Air Quality Alert': return 3
    elif alert == 'Air Stagnation Advisory': return 4
    elif alert == 'Arroyo And Small Stream Flood Advisory': return 5
    elif alert == 'Ashfall Advisory': return 6
    elif alert == 'Ashfall Warning': return 7
    elif alert == 'Avalanche Advisory': return 8
    elif alert == 'Avalanche Warning': return 9
    elif alert == 'Avalanche Watch': return 10
    elif alert == 'Beach Hazards Statement': return 11
    elif alert == 'Blizzard Warning': return 12
    elif alert == 'Blizzard Watch': return 13
    elif alert == 'Blowing Dust Advisory': return 14
    elif alert == 'Blowing Dust Warning': return 15
    elif alert == 'Blue Alert': return 16
    elif alert == 'Brisk Wind Advisory': return 17
    elif alert == 'Child Abduction Emergency': return 18
    elif alert == 'Civil Danger Warning': return 19
    elif alert == 'Civil Emergency Message': return 20
    elif alert == 'Coastal Flood Advisory': return 21
    elif alert == 'Coastal Flood Statement': return 22
    elif alert == 'Coastal Flood Warning': return 23
    elif alert == 'Coastal Flood Watch': return 24
    elif alert == 'Dense Fog Advisory': return 25
    elif alert == 'Dense Smoke Advisory': return 26
    elif alert == 'Dust Advisory': return 27
    elif alert == 'Dust Storm Warning': return 28
    elif alert == 'Earthquake Warning': return 29
    elif alert == 'Evacuation - Immediate': return 30
    elif alert == 'Excessive Heat Warning': return 31
    elif alert == 'Excessive Heat Watch': return 32
    elif alert == 'Extreme Cold Warning': return 33
    elif alert == 'Extreme Cold Watch': return 34
    elif alert == 'Extreme Fire Danger': return 35
    elif alert == 'Extreme Wind Warning': return 36
    elif alert == 'Fire Warning': return 37
    elif alert == 'Fire Weather Watch': return 38
    elif alert == 'Flash Flood Statement': return 39
    elif alert == 'Flash Flood Warning': return 40
    elif alert == 'Flash Flood Watch': return 41
    elif alert == 'Flood Advisory': return 42
    elif alert == 'Flood Statement': return 43
    elif alert == 'Flood Warning': return 44
    elif alert == 'Flood Watch': return 45
    elif alert == 'Freeze Warning': return 46
    elif alert == 'Freeze Watch': return 47
    elif alert == 'Freezing Fog Advisory': return 48
    elif alert == 'Freezing Rain Advisory': return 49
    elif alert == 'Freezing Spray Advisory': return 50
    elif alert == 'Frost Advisory': return 51
    elif alert == 'Gale Warning': return 52
    elif alert == 'Gale Watch': return 53
    elif alert == 'Hard Freeze Warning': return 54
    elif alert == 'Hard Freeze Watch': return 55
    elif alert == 'Hazardous Materials Warning': return 56
    elif alert == 'Hazardous Seas Warning': return 57
    elif alert == 'Hazardous Seas Watch': return 58
    elif alert == 'Hazardous Weather Outlook': return 59
    elif alert == 'Heat Advisory': return 60
    elif alert == 'Heavy Freezing Spray Warning': return 61
    elif alert == 'Heavy Freezing Spray Watch': return 62
    elif alert == 'High Surf Advisory': return 63
    elif alert == 'High Surf Warning': return 64
    elif alert == 'High Wind Warning': return 65
    elif alert == 'High Wind Watch': return 66
    elif alert == 'Hurricane Force Wind Warning': return 67
    elif alert == 'Hurricane Force Wind Watch': return 68
    elif alert == 'Hurricane Local Statement': return 69
    elif alert == 'Hurricane Warning': return 70
    elif alert == 'Hurricane Watch': return 71
    elif alert == 'Hydrologic Advisory': return 72
    elif alert == 'Hydrologic Outlook': return 73
    elif alert == 'Ice Storm Warning': return 74
    elif alert == 'Lake Effect Snow Advisory': return 75
    elif alert == 'Lake Effect Snow Warning': return 76
    elif alert == 'Lake Effect Snow Watch': return 77
    elif alert == 'Lake Wind Advisory': return 78
    elif alert == 'Lakeshore Flood Advisory': return 79
    elif alert == 'Lakeshore Flood Statement': return 80
    elif alert == 'Lakeshore Flood Warning': return 81
    elif alert == 'Lakeshore Flood Watch': return 82
    elif alert == 'Law Enforcement Warning': return 83
    elif alert == 'Local Area Emergency': return 84
    elif alert == 'Low Water Advisory': return 85
    elif alert == 'Marine Weather Statement': return 86
    elif alert == 'Nuclear Power Plant Warning': return 87
    elif alert == 'Radiological Hazard Warning': return 88
    elif alert == 'Red Flag Warning': return 89
    elif alert == 'Rip Current Statement': return 90
    elif alert == 'Severe Thunderstorm Warning': return 91
    elif alert == 'Severe Thunderstorm Watch': return 92
    elif alert == 'Severe Weather Statement': return 93
    elif alert == 'Shelter In Place Warning': return 94
    elif alert == 'Short Term Forecast': return 95
    elif alert == 'Small Craft Advisory': return 96
    elif alert == 'Small Craft Advisory For Hazardous Seas': return 97
    elif alert == 'Small Craft Advisory For Rough Bar': return 98
    elif alert == 'Small Craft Advisory For Winds': return 99
    elif alert == 'Small Stream Flood Advisory': return 100
    elif alert == 'Snow Squall Warning': return 101
    elif alert == 'Special Marine Warning': return 102
    elif alert == 'Special Weather Statement': return 103
    elif alert == 'Storm Surge Warning': return 104
    elif alert == 'Storm Surge Watch': return 105
    elif alert == 'Storm Warning': return 105
    elif alert == 'Storm Watch': return 107
    elif alert == 'Test': return 108
    elif alert == 'Tornado Warning': return 109
    elif alert == 'Tornado Watch': return 110
    elif alert == 'Tropical Depression Local Statement': return 111
    elif alert == 'Tropical Storm Local Statement': return 112
    elif alert == 'Tropical Storm Warning': return 113
    elif alert == 'Tropical Storm Watch': return 114
    elif alert == 'Tsunami Advisory': return 115
    elif alert == 'Tsunami Warning': return 116
    elif alert == 'Tsunami Watch': return 117
    elif alert == 'Typhoon Local Statement': return 118
    elif alert == 'Typhoon Warning': return 119
    elif alert == 'Typhoon Watch': return 120
    elif alert == 'Urban And Small Stream Flood Advisory': return 121
    elif alert == 'Volcano Warning': return 122
    elif alert == 'Wind Advisory': return 123
    elif alert == 'Wind Chill Advisory': return 124
    elif alert == 'Wind Chill Warning': return 125
    elif alert == 'Wind Chill Watch': return 126
    elif alert == 'Winter Storm Warning': return 127
    else:
        return 0

def status_to_id(alert):
    if alert == 'Actual':
        return 1
    elif alert == 'Exercise':
        return 2
    elif alert == 'System':
        return 3
    elif alert == 'Test':
        return 4
    elif alert == 'Draft':
        return 5
    else:
        return 0

def type_to_id(alert):
    if alert == 'Alert':
        return 1
    elif alert == 'Update':
        return 2
    elif alert == 'Cancel':
        return 3
    elif alert == 'Ack':
        return 4
    elif alert == 'Error':
        return 5
    else:
        return 0

def category_to_id(alert):
    if alert == 'Geo':
        return 1
    elif alert == 'Met':
        return 2
    elif alert == 'Safety':
        return 3
    elif alert == 'Security':
        return 4
    elif alert == 'Rescue':
        return 5
    elif alert == 'Fire':
        return 6
    elif alert == 'Health':
        return 7
    elif alert == 'Env':
        return 8
    elif alert == 'Transport':
        return 9
    elif alert == 'Infra':
        return 10
    elif alert == 'CBRNE':
        return 11
    elif alert == 'Other':
        return 12
    else:
        return 0

def urgency_to_id(alert):
    if alert == 'Immediate':
        return 1
    elif alert == 'Expected':
        return 2
    elif alert == 'Future':
        return 3
    elif alert == 'Past':
        return 4
    elif alert == 'Unknown':
        return 5
    else:
        return 0

def severity_to_id(alert):
    if alert == 'Extreme':
        return 1
    elif alert == 'Severe':
        return 2
    elif alert == 'Moderate':
        return 3
    elif alert == 'Minor':
        return 4
    elif alert == 'Unknown':
        return 5
    else:
        return 0

def certainy_to_id(alert):
    if alert == 'Observed':
        return 1
    elif alert == 'Likely':
        return 2
    elif alert == 'Possible':
        return 3
    elif alert == 'Unlikely':
        return 4
    elif alert == 'Unknown':
        return 5
    else:
        return 0


