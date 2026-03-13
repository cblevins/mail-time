# Transit Times Outlier Report

Flags values where a year's transit time deviates ≥15 hours from the median
of other years for the same route. Checks whether a 3↔8 digit substitution
(common OCR confusion in 19th-century typefaces) explains the discrepancy.

**Years compared:** 1882, 1883, 1892, 1902, 1908  
*(1883 data loaded from `1883-transit-times-google.csv` and merged into `transit-times-merged.csv`)*

## Summary

| Category | Count | Description |
|----------|-------|-------------|
| HIGH | 18 | 3↔8 substitution resolves the outlier (within 5h of median) — likely errors |
| MEDIUM | 8 | 3↔8 substitution partially explains the outlier (within 10h) — probably errors |
| LOW | 615 | Outlier unexplained by 3↔8 — may be other error types or route changes |
| HISTORICAL | 648 | 1882 value higher than later years — likely genuine historical variation, not an error |

## HIGH (18 cases)
*Strong evidence of 3↔8 transcription error — recommend correcting these*

### Mesilla, New Mexico → Charleston, South Carolina (1882)
- Values by year: **1882: 24:04*** | **1883: 124:04**  *(asterisk = flagged)*
- Flagged value: **24:04**, deviation 100.0 h from other-years median (124.07 h)
- Suggested correction: **124:04** via `prepend '1' to H: 24->124`, within 0.0 h of median
- Error type: `missing_digit`

### Deadwood, Dakota → Omaha, Nebraska (1883)
- Values by year: **1882: 81:25** | **1883: 81:25*** | **1892: 27:20** | **1902: 25:20**  *(asterisk = flagged)*
- Flagged value: **81:25**, deviation 54.1 h from other-years median (27.33 h)
- Suggested correction: **31:25** via `H: 81->31`, within 4.1 h of median
- Error type: `8to3`

### Deadwood, Dakota → Omaha, Nebraska (1882)
- Values by year: **1882: 81:25*** | **1883: 81:25** | **1892: 27:20** | **1902: 25:20**  *(asterisk = flagged)*
- Flagged value: **81:25**, deviation 54.1 h from other-years median (27.33 h)
- Suggested correction: **31:25** via `H: 81->31`, within 4.1 h of median
- Error type: `8to3`

### Charleston, South Carolina → Cincinnati, Ohio (1892)
- Values by year: **1882: 43:15** | **1883: 43:15** | **1892: 89:05*** | **1902: 30:05** | **1908: 30:05**  *(asterisk = flagged)*
- Flagged value: **89:05**, deviation 52.4 h from other-years median (36.66 h)
- Suggested correction: **39:05** via `H: 89->39`, within 2.4 h of median
- Error type: `8to3`

### Pittsburg, Pennsylvania → Omaha, Nebraska (1908)
- Values by year: **1902: 84:00** | **1908: 34:00***  *(asterisk = flagged)*
- Flagged value: **34:00**, deviation 50.0 h from other-years median (84.00 h)
- Suggested correction: **84:00** via `H: 34->84`, within 0.0 h of median
- Error type: `3to8`

### Pittsburg, Pennsylvania → Omaha, Nebraska (1902)
- Values by year: **1902: 84:00*** | **1908: 34:00**  *(asterisk = flagged)*
- Flagged value: **84:00**, deviation 50.0 h from other-years median (34.00 h)
- Suggested correction: **34:00** via `H: 84->34`, within 0.0 h of median
- Error type: `8to3`

### Pittsburgh, Pennsylvania → Omaha, Nebraska (1892)
- Values by year: **1882: 34:15** | **1883: 34:15** | **1892: 84:00***  *(asterisk = flagged)*
- Flagged value: **84:00**, deviation 49.8 h from other-years median (34.25 h)
- Suggested correction: **34:00** via `H: 84->34`, within 0.2 h of median
- Error type: `8to3`

### Manchester, New Hampshire → Chicago, Illinois (1902)
- Values by year: **1892: 33:15** | **1902: 82:15*** | **1908: 32:00**  *(asterisk = flagged)*
- Flagged value: **82:15**, deviation 49.6 h from other-years median (32.62 h)
- Suggested correction: **32:15** via `H: 82->32`, within 0.4 h of median
- Error type: `8to3`

### Providence, Rhode Island → Chicago, Illinois (1902)
- Values by year: **1882: 38:05** | **1883: 38:05** | **1892: 32:45** | **1902: 82:45*** | **1908: 32:45**  *(asterisk = flagged)*
- Flagged value: **82:45**, deviation 47.3 h from other-years median (35.41 h)
- Suggested correction: **32:45** via `H: 82->32`, within 2.7 h of median
- Error type: `8to3`

### Morgan City, Louisiana → Cincinnati, Ohio (1892)
- Values by year: **1882: 38:35** | **1883: 38:35** | **1892: 81:40*** | **1902: 30:40** | **1908: 30:40**  *(asterisk = flagged)*
- Flagged value: **81:40**, deviation 47.0 h from other-years median (34.62 h)
- Suggested correction: **31:40** via `H: 81->31`, within 3.0 h of median
- Error type: `8to3`

### Newport, Rhode Island → Chicago, Illinois (1902)
- Values by year: **1882: 41:10** | **1883: 41:10** | **1892: 35:15** | **1902: 85:15*** | **1908: 35:15**  *(asterisk = flagged)*
- Flagged value: **85:15**, deviation 47.0 h from other-years median (38.21 h)
- Suggested correction: **35:15** via `H: 85->35`, within 3.0 h of median
- Error type: `8to3`

### Buffalo, New York → Charleston, South Carolina (1902)
- Values by year: **1882: 41:20** | **1883: 41:20** | **1892: 48:00** | **1902: 88:00*** | **1908: 38:00**  *(asterisk = flagged)*
- Flagged value: **88:00**, deviation 46.7 h from other-years median (41.33 h)
- Suggested correction: **38:00** via `H: 88->38`, within 3.3 h of median
- Error type: `8to3`

### Huntington, West Virginia → Cincinnati, Ohio (1902)
- Values by year: **1882: 41:20** | **1883: 41:20** | **1892: 5:00** | **1902: 5:00*** | **1908: 5:00**  *(asterisk = flagged)*
- Flagged value: **5:00**, deviation 18.2 h from other-years median (23.16 h)
- Suggested correction: **25:00** via `prepend '2' to H: 5->25`, within 1.8 h of median
- Error type: `missing_digit`

### Huntington, West Virginia → Cincinnati, Ohio (1892)
- Values by year: **1882: 41:20** | **1883: 41:20** | **1892: 5:00*** | **1902: 5:00** | **1908: 5:00**  *(asterisk = flagged)*
- Flagged value: **5:00**, deviation 18.2 h from other-years median (23.16 h)
- Suggested correction: **25:00** via `prepend '2' to H: 5->25`, within 1.8 h of median
- Error type: `missing_digit`

### Huntington, West Virginia → Cincinnati, Ohio (1908)
- Values by year: **1882: 41:20** | **1883: 41:20** | **1892: 5:00** | **1902: 5:00** | **1908: 5:00***  *(asterisk = flagged)*
- Flagged value: **5:00**, deviation 18.2 h from other-years median (23.16 h)
- Suggested correction: **25:00** via `prepend '2' to H: 5->25`, within 1.8 h of median
- Error type: `missing_digit`

### Charleston, West Virginia → Cincinnati, Ohio (1908)
- Values by year: **1882: 38:48** | **1883: 38:48** | **1892: 6:00** | **1902: 6:00** | **1908: 6:00***  *(asterisk = flagged)*
- Flagged value: **6:00**, deviation 16.4 h from other-years median (22.40 h)
- Suggested correction: **26:00** via `prepend '2' to H: 6->26`, within 3.6 h of median
- Error type: `missing_digit`

### Charleston, West Virginia → Cincinnati, Ohio (1902)
- Values by year: **1882: 38:48** | **1883: 38:48** | **1892: 6:00** | **1902: 6:00*** | **1908: 6:00**  *(asterisk = flagged)*
- Flagged value: **6:00**, deviation 16.4 h from other-years median (22.40 h)
- Suggested correction: **26:00** via `prepend '2' to H: 6->26`, within 3.6 h of median
- Error type: `missing_digit`

### Charleston, West Virginia → Cincinnati, Ohio (1892)
- Values by year: **1882: 38:48** | **1883: 38:48** | **1892: 6:00*** | **1902: 6:00** | **1908: 6:00**  *(asterisk = flagged)*
- Flagged value: **6:00**, deviation 16.4 h from other-years median (22.40 h)
- Suggested correction: **26:00** via `prepend '2' to H: 6->26`, within 3.6 h of median
- Error type: `missing_digit`

## MEDIUM (8 cases)
*Probable 3↔8 error — verify against source PDF before correcting*

### Albany, New York → Charleston, South Carolina (1902)
- Values by year: **1882: 37:45** | **1883: 37:45** | **1892: 38:00** | **1902: 82:00*** | **1908: 32:00**  *(asterisk = flagged)*
- Flagged value: **82:00**, deviation 44.2 h from other-years median (37.75 h)
- Suggested correction: **32:00** via `H: 82->32`, within 5.8 h of median
- Error type: `8to3`

### Montgomery, Alabama → Chicago, Illinois (1908)
- Values by year: **1882: 40:45** | **1883: 40:45** | **1892: 34:00** | **1902: 31:00** | **1908: 81:00***  *(asterisk = flagged)*
- Flagged value: **81:00**, deviation 43.6 h from other-years median (37.38 h)
- Suggested correction: **31:00** via `H: 81->31`, within 6.4 h of median
- Error type: `8to3`

### Deadwood, Dakota → Chicago, Illinois (1882)
- Values by year: **1882: 82:00*** | **1883: 82:00** | **1892: 39:50** | **1902: 39:50**  *(asterisk = flagged)*
- Flagged value: **82:00**, deviation 42.2 h from other-years median (39.83 h)
- Suggested correction: **32:00** via `H: 82->32`, within 7.8 h of median
- Error type: `8to3`

### Deadwood, Dakota → Chicago, Illinois (1883)
- Values by year: **1882: 82:00** | **1883: 82:00*** | **1892: 39:50** | **1902: 39:50**  *(asterisk = flagged)*
- Flagged value: **82:00**, deviation 42.2 h from other-years median (39.83 h)
- Suggested correction: **32:00** via `H: 82->32`, within 7.8 h of median
- Error type: `8to3`

### Deadwood, Dakota → Chicago, Illinois (1892)
- Values by year: **1882: 82:00** | **1883: 82:00** | **1892: 39:50*** | **1902: 39:50**  *(asterisk = flagged)*
- Flagged value: **39:50**, deviation 42.2 h from other-years median (82.00 h)
- Suggested correction: **89:50** via `H: 39->89`, within 7.8 h of median
- Error type: `3to8`

### Deadwood, Dakota → Chicago, Illinois (1902)
- Values by year: **1882: 82:00** | **1883: 82:00** | **1892: 39:50** | **1902: 39:50***  *(asterisk = flagged)*
- Flagged value: **39:50**, deviation 42.2 h from other-years median (82.00 h)
- Suggested correction: **89:50** via `H: 39->89`, within 7.8 h of median
- Error type: `3to8`

### Montpelier, Vermont → Cincinnati, Ohio (1892)
- Values by year: **1882: 44:37** | **1883: 44:37** | **1892: 81:35*** | **1902: 35:35** | **1908: 35:35**  *(asterisk = flagged)*
- Flagged value: **81:35**, deviation 41.5 h from other-years median (40.10 h)
- Suggested correction: **31:35** via `H: 81->31`, within 8.5 h of median
- Error type: `8to3`

### Frankfort, Kentucky → Omaha, Nebraska (1908)
- Values by year: **1882: 47:35** | **1883: 47:35** | **1892: 30:15** | **1902: 30:00** | **1908: 80:00***  *(asterisk = flagged)*
- Flagged value: **80:00**, deviation 41.1 h from other-years median (38.91 h)
- Suggested correction: **30:00** via `H: 80->30`, within 8.9 h of median
- Error type: `8to3`

## LOW (615 cases)
*Outlier with no clear digit-substitution explanation — could be route change, data entry error, or other cause*

### Olympia, Washington → Pittsburgh, Pennsylvania (1902)
- Values by year: **1883: 269:35** | **1892: 114:15** | **1902: 101:15***  *(asterisk = flagged)*
- Flagged value: **101:15**, deviation 90.7 h from other-years median (191.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Pittsburgh, Pennsylvania (1902)
- Values by year: **1883: 247:05** | **1892: 110:50** | **1902: 105:50***  *(asterisk = flagged)*
- Flagged value: **105:50**, deviation 73.1 h from other-years median (178.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Pittsburgh, Pennsylvania (1892)
- Values by year: **1883: 269:35** | **1892: 114:15*** | **1902: 101:15**  *(asterisk = flagged)*
- Flagged value: **114:15**, deviation 71.2 h from other-years median (185.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Pittsburgh, Pennsylvania (1902)
- Values by year: **1883: 243:05** | **1892: 112:50** | **1902: 107:50***  *(asterisk = flagged)*
- Flagged value: **107:50**, deviation 70.1 h from other-years median (177.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Pittsburgh, Pennsylvania (1892)
- Values by year: **1883: 247:05** | **1892: 110:50*** | **1902: 105:50**  *(asterisk = flagged)*
- Flagged value: **110:50**, deviation 65.6 h from other-years median (176.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Pittsburgh, Pennsylvania (1892)
- Values by year: **1883: 243:05** | **1892: 112:50*** | **1902: 107:50**  *(asterisk = flagged)*
- Flagged value: **112:50**, deviation 62.6 h from other-years median (175.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Saint Louis, Missouri (1902)
- Values by year: **1882: 99:55** | **1883: 99:55** | **1892: 51:00** | **1902: 40:00***  *(asterisk = flagged)*
- Flagged value: **40:00**, deviation 59.9 h from other-years median (99.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 154:05** | **1883: 154:05** | **1892: 100:00** | **1902: 96:30***  *(asterisk = flagged)*
- Flagged value: **96:30**, deviation 57.6 h from other-years median (154.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Omaha, Nebraska (1902)
- Values by year: **1882: 81:25** | **1883: 81:25** | **1892: 27:20** | **1902: 25:20***  *(asterisk = flagged)*
- Flagged value: **25:20**, deviation 56.1 h from other-years median (81.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Boston, Massachusetts (1902)
- Values by year: **1882: 124:18** | **1883: 124:13** | **1892: 73:50** | **1902: 68:50***  *(asterisk = flagged)*
- Flagged value: **68:50**, deviation 55.4 h from other-years median (124.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Las Cruces, New Mexico → San Francisco, California (1892)
- Values by year: **1892: 98:15*** | **1902: 43:45** | **1908: 43:45**  *(asterisk = flagged)*
- Flagged value: **98:15**, deviation 54.5 h from other-years median (43.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Omaha, Nebraska (1892)
- Values by year: **1882: 81:25** | **1883: 81:25** | **1892: 27:20*** | **1902: 25:20**  *(asterisk = flagged)*
- Flagged value: **27:20**, deviation 54.1 h from other-years median (81.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 154:05** | **1883: 154:05** | **1892: 100:00*** | **1902: 96:30**  *(asterisk = flagged)*
- Flagged value: **100:00**, deviation 54.1 h from other-years median (154.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Charleston, South Carolina (1902)
- Values by year: **1882: 144:29** | **1883: 144:29** | **1892: 90:45** | **1902: 90:45***  *(asterisk = flagged)*
- Flagged value: **90:45**, deviation 53.7 h from other-years median (144.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Charleston, South Carolina (1892)
- Values by year: **1882: 144:29** | **1883: 144:29** | **1892: 90:45*** | **1902: 90:45**  *(asterisk = flagged)*
- Flagged value: **90:45**, deviation 53.7 h from other-years median (144.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → San Francisco, California (1902)
- Values by year: **1882: 147:54** | **1883: 147:54** | **1892: 102:45** | **1902: 94:45***  *(asterisk = flagged)*
- Flagged value: **94:45**, deviation 53.1 h from other-years median (147.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Cincinnati, Ohio (1902)
- Values by year: **1882: 99:45** | **1883: 99:45** | **1892: 47:00** | **1902: 47:00***  *(asterisk = flagged)*
- Flagged value: **47:00**, deviation 52.8 h from other-years median (99.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Cincinnati, Ohio (1892)
- Values by year: **1882: 99:45** | **1883: 99:45** | **1892: 47:00*** | **1902: 47:00**  *(asterisk = flagged)*
- Flagged value: **47:00**, deviation 52.8 h from other-years median (99.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### West Point, New York → San Francisco, California (1892)
- Values by year: **1882: 162:32** | **1883: 162:32** | **1892: 110:15***  *(asterisk = flagged)*
- Flagged value: **110:15**, deviation 52.3 h from other-years median (162.53 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → San Francisco, California (1908)
- Values by year: **1882: 170:40** | **1883: 170:40** | **1892: 139:15** | **1902: 105:45** | **1908: 102:45***  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 52.2 h from other-years median (154.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lynchburg, Virginia → San Francisco, California (1908)
- Values by year: **1882: 150:22** | **1883: 150:22** | **1902: 99:45** | **1908: 98:28***  *(asterisk = flagged)*
- Flagged value: **98:28**, deviation 51.9 h from other-years median (150.37 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → San Francisco, California (1902)
- Values by year: **1882: 127:37** | **1883: 127:37** | **1892: 80:45** | **1902: 75:45***  *(asterisk = flagged)*
- Flagged value: **75:45**, deviation 51.9 h from other-years median (127.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → San Francisco, California (1908)
- Values by year: **1882: 167:25** | **1883: 167:25** | **1892: 101:15** | **1902: 83:45** | **1908: 82:28***  *(asterisk = flagged)*
- Flagged value: **82:28**, deviation 51.9 h from other-years median (134.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Harrisburg, Pennsylvania → San Francisco, California (1908)
- Values by year: **1882: 141:09** | **1883: 141:00** | **1902: 89:45** | **1908: 89:28***  *(asterisk = flagged)*
- Flagged value: **89:28**, deviation 51.5 h from other-years median (141.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Harrisburg, Pennsylvania → San Francisco, California (1902)
- Values by year: **1882: 141:09** | **1883: 141:00** | **1902: 89:45*** | **1908: 89:28**  *(asterisk = flagged)*
- Flagged value: **89:45**, deviation 51.2 h from other-years median (141.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lynchburg, Virginia → San Francisco, California (1902)
- Values by year: **1882: 150:22** | **1883: 150:22** | **1902: 99:45*** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 50.6 h from other-years median (150.37 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → San Francisco, California (1902)
- Values by year: **1882: 167:25** | **1883: 167:25** | **1892: 101:15** | **1902: 83:45*** | **1908: 82:28**  *(asterisk = flagged)*
- Flagged value: **83:45**, deviation 50.6 h from other-years median (134.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Boston, Massachusetts (1892)
- Values by year: **1882: 124:18** | **1883: 124:13** | **1892: 73:50*** | **1902: 68:50**  *(asterisk = flagged)*
- Flagged value: **73:50**, deviation 50.4 h from other-years median (124.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → San Francisco, California (1908)
- Values by year: **1882: 164:53** | **1883: 164:53** | **1892: 102:15** | **1902: 84:45** | **1908: 83:28***  *(asterisk = flagged)*
- Flagged value: **83:28**, deviation 50.1 h from other-years median (133.56 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Wayne, Indiana → San Francisco, California (1908)
- Values by year: **1882: 123:10** | **1883: 123:10** | **1902: 75:45** | **1908: 73:45***  *(asterisk = flagged)*
- Flagged value: **73:45**, deviation 49.4 h from other-years median (123.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → San Francisco, California (1902)
- Values by year: **1882: 170:40** | **1883: 170:40** | **1892: 139:15** | **1902: 105:45*** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **105:45**, deviation 49.2 h from other-years median (154.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Saint Louis, Missouri (1892)
- Values by year: **1882: 99:55** | **1883: 99:55** | **1892: 51:00*** | **1902: 40:00**  *(asterisk = flagged)*
- Flagged value: **51:00**, deviation 48.9 h from other-years median (99.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → San Francisco, California (1902)
- Values by year: **1882: 164:53** | **1883: 164:53** | **1892: 102:15** | **1902: 84:45*** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **84:45**, deviation 48.8 h from other-years median (133.56 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Baltimore, Maryland (1902)
- Values by year: **1882: 114:00** | **1883: 114:00** | **1892: 71:30** | **1902: 65:30***  *(asterisk = flagged)*
- Flagged value: **65:30**, deviation 48.5 h from other-years median (114.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → San Francisco, California (1908)
- Values by year: **1882: 202:35** | **1883: 202:35** | **1892: 139:15** | **1902: 122:45** | **1908: 122:28***  *(asterisk = flagged)*
- Flagged value: **122:28**, deviation 48.4 h from other-years median (170.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → San Francisco, California (1902)
- Values by year: **1882: 202:35** | **1883: 202:35** | **1892: 139:15** | **1902: 122:45*** | **1908: 122:28**  *(asterisk = flagged)*
- Flagged value: **122:45**, deviation 48.2 h from other-years median (170.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Wayne, Indiana → San Francisco, California (1902)
- Values by year: **1882: 123:10** | **1883: 123:10** | **1902: 75:45*** | **1908: 73:45**  *(asterisk = flagged)*
- Flagged value: **75:45**, deviation 47.4 h from other-years median (123.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → San Francisco, California (1892)
- Values by year: **1882: 127:37** | **1883: 127:37** | **1892: 80:45*** | **1902: 75:45**  *(asterisk = flagged)*
- Flagged value: **80:45**, deviation 46.9 h from other-years median (127.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Washington, District of Columbia (1902)
- Values by year: **1882: 112:50** | **1883: 112:50** | **1892: 72:48** | **1902: 66:30***  *(asterisk = flagged)*
- Flagged value: **66:30**, deviation 46.3 h from other-years median (112.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 96:55** | **1883: 96:55** | **1892: 54:50** | **1902: 50:50***  *(asterisk = flagged)*
- Flagged value: **50:50**, deviation 46.1 h from other-years median (96.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → San Francisco, California (1892)
- Values by year: **1882: 147:54** | **1883: 147:54** | **1892: 102:45*** | **1902: 94:45**  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 45.1 h from other-years median (147.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → San Francisco, California (1908)
- Values by year: **1882: 169:37** | **1883: 169:37** | **1892: 133:15** | **1902: 106:45** | **1908: 106:28***  *(asterisk = flagged)*
- Flagged value: **106:28**, deviation 45.0 h from other-years median (151.43 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montpelier, Vermont → San Francisco, California (1908)
- Values by year: **1882: 170:05** | **1883: 170:05** | **1892: 127:15** | **1902: 103:45** | **1908: 103:45***  *(asterisk = flagged)*
- Flagged value: **103:45**, deviation 44.9 h from other-years median (148.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montpelier, Vermont → San Francisco, California (1902)
- Values by year: **1882: 170:05** | **1883: 170:05** | **1892: 127:15** | **1902: 103:45*** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **103:45**, deviation 44.9 h from other-years median (148.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → San Francisco, California (1908)
- Values by year: **1882: 196:50** | **1883: 196:50** | **1892: 138:15** | **1902: 124:45** | **1908: 122:45***  *(asterisk = flagged)*
- Flagged value: **122:45**, deviation 44.8 h from other-years median (167.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → San Francisco, California (1902)
- Values by year: **1882: 169:37** | **1883: 169:37** | **1892: 133:15** | **1902: 106:45*** | **1908: 106:28**  *(asterisk = flagged)*
- Flagged value: **106:45**, deviation 44.7 h from other-years median (151.43 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → New York, New York (1902)
- Values by year: **1882: 109:40** | **1883: 109:40** | **1892: 69:30** | **1902: 65:30***  *(asterisk = flagged)*
- Flagged value: **65:30**, deviation 44.2 h from other-years median (109.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dubuque, Iowa → San Francisco, California (1902)
- Values by year: **1882: 124:54** | **1883: 124:54** | **1892: 84:15** | **1902: 60:45*** | **1908: 67:08**  *(asterisk = flagged)*
- Flagged value: **60:45**, deviation 43.8 h from other-years median (104.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albany, New York → San Francisco, California (1908)
- Values by year: **1882: 154:25** | **1883: 154:25** | **1892: 107:45** | **1902: 89:15** | **1908: 87:28***  *(asterisk = flagged)*
- Flagged value: **87:28**, deviation 43.6 h from other-years median (131.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cairo, Illinois → San Francisco, California (1908)
- Values by year: **1882: 130:31** | **1883: 130:31** | **1892: 106:15** | **1902: 79:00** | **1908: 75:00***  *(asterisk = flagged)*
- Flagged value: **75:00**, deviation 43.4 h from other-years median (118.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → San Francisco, California (1902)
- Values by year: **1882: 197:00** | **1883: 197:00** | **1892: 138:45** | **1902: 124:45*** | **1908: 124:45**  *(asterisk = flagged)*
- Flagged value: **124:45**, deviation 43.1 h from other-years median (167.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → San Francisco, California (1908)
- Values by year: **1882: 197:00** | **1883: 197:00** | **1892: 138:45** | **1902: 124:45** | **1908: 124:45***  *(asterisk = flagged)*
- Flagged value: **124:45**, deviation 43.1 h from other-years median (167.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → San Francisco, California (1908)
- Values by year: **1882: 186:00** | **1883: 186:00** | **1892: 131:45** | **1902: 117:45** | **1908: 115:45***  *(asterisk = flagged)*
- Flagged value: **115:45**, deviation 43.1 h from other-years median (158.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → San Francisco, California (1908)
- Values by year: **1882: 169:34** | **1883: 169:30** | **1892: 84:15** | **1902: 83:45** | **1908: 83:45***  *(asterisk = flagged)*
- Flagged value: **83:45**, deviation 43.1 h from other-years median (126.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → San Francisco, California (1902)
- Values by year: **1882: 169:34** | **1883: 169:30** | **1892: 84:15** | **1902: 83:45*** | **1908: 83:45**  *(asterisk = flagged)*
- Flagged value: **83:45**, deviation 43.1 h from other-years median (126.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → San Francisco, California (1902)
- Values by year: **1882: 196:50** | **1883: 196:50** | **1892: 138:15** | **1902: 124:45*** | **1908: 122:45**  *(asterisk = flagged)*
- Flagged value: **124:45**, deviation 42.8 h from other-years median (167.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New York, New York → San Francisco, California (1908)
- Values by year: **1882: 159:15** | **1883: 159:15** | **1892: 111:15** | **1902: 97:45** | **1908: 92:28***  *(asterisk = flagged)*
- Flagged value: **92:28**, deviation 42.8 h from other-years median (135.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Baltimore, Maryland (1892)
- Values by year: **1882: 114:00** | **1883: 114:00** | **1892: 71:30*** | **1902: 65:30**  *(asterisk = flagged)*
- Flagged value: **71:30**, deviation 42.5 h from other-years median (114.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → San Francisco, California (1892)
- Values by year: **1882: 169:34** | **1883: 169:30** | **1892: 84:15*** | **1902: 83:45** | **1908: 83:45**  *(asterisk = flagged)*
- Flagged value: **84:15**, deviation 42.4 h from other-years median (126.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, Delaware → San Francisco, California (1902)
- Values by year: **1882: 147:16** | **1883: 147:10** | **1892: 126:15** | **1902: 94:25*** | **1908: 94:25**  *(asterisk = flagged)*
- Flagged value: **94:25**, deviation 42.3 h from other-years median (136.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, Delaware → San Francisco, California (1908)
- Values by year: **1882: 147:16** | **1883: 147:10** | **1892: 126:15** | **1902: 94:25** | **1908: 94:25***  *(asterisk = flagged)*
- Flagged value: **94:25**, deviation 42.3 h from other-years median (136.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Omaha, Nebraska → San Francisco, California (1902)
- Values by year: **1882: 97:05** | **1883: 97:06** | **1892: 92:15** | **1902: 52:30*** | **1908: 55:30**  *(asterisk = flagged)*
- Flagged value: **52:30**, deviation 42.2 h from other-years median (94.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → San Francisco, California (1908)
- Values by year: **1882: 163:10** | **1883: 163:10** | **1892: 115:00** | **1902: 98:55** | **1908: 96:55***  *(asterisk = flagged)*
- Flagged value: **96:55**, deviation 42.2 h from other-years median (139.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 96:55** | **1883: 96:55** | **1892: 54:50*** | **1902: 50:50**  *(asterisk = flagged)*
- Flagged value: **54:50**, deviation 42.1 h from other-years median (96.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, North Carolina → San Francisco, California (1908)
- Values by year: **1882: 160:13** | **1883: 160:13** | **1892: 134:45** | **1902: 105:45** | **1908: 105:28***  *(asterisk = flagged)*
- Flagged value: **105:28**, deviation 42.0 h from other-years median (147.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 132:30** | **1883: 132:30** | **1892: 108:30** | **1902: 90:39***  *(asterisk = flagged)*
- Flagged value: **90:39**, deviation 41.9 h from other-years median (132.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Raleigh, North Carolina → San Francisco, California (1908)
- Values by year: **1882: 158:52** | **1883: 158:52** | **1892: 139:45** | **1902: 107:45** | **1908: 107:28***  *(asterisk = flagged)*
- Flagged value: **107:28**, deviation 41.8 h from other-years median (149.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albany, New York → San Francisco, California (1902)
- Values by year: **1882: 154:25** | **1883: 154:25** | **1892: 107:45** | **1902: 89:15*** | **1908: 87:28**  *(asterisk = flagged)*
- Flagged value: **89:15**, deviation 41.8 h from other-years median (131.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, North Carolina → San Francisco, California (1902)
- Values by year: **1882: 160:13** | **1883: 160:13** | **1892: 134:45** | **1902: 105:45*** | **1908: 105:28**  *(asterisk = flagged)*
- Flagged value: **105:45**, deviation 41.7 h from other-years median (147.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Georgia → San Francisco, California (1902)
- Values by year: **1882: 162:05** | **1883: 162:05** | **1892: 126:40** | **1902: 102:45*** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 41.6 h from other-years median (144.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Georgia → San Francisco, California (1908)
- Values by year: **1882: 162:05** | **1883: 162:05** | **1892: 126:40** | **1902: 102:45** | **1908: 102:45***  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 41.6 h from other-years median (144.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Raleigh, North Carolina → San Francisco, California (1902)
- Values by year: **1882: 158:52** | **1883: 158:52** | **1892: 139:45** | **1902: 107:45*** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **107:45**, deviation 41.6 h from other-years median (149.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → San Francisco, California (1908)
- Values by year: **1882: 173:15** | **1883: 173:15** | **1892: 126:15** | **1902: 112:45** | **1908: 108:28***  *(asterisk = flagged)*
- Flagged value: **108:28**, deviation 41.3 h from other-years median (149.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → San Francisco, California (1902)
- Values by year: **1882: 186:00** | **1883: 186:00** | **1892: 131:45** | **1902: 117:45*** | **1908: 115:45**  *(asterisk = flagged)*
- Flagged value: **117:45**, deviation 41.1 h from other-years median (158.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Maine → San Francisco, California (1908)
- Values by year: **1882: 166:35** | **1883: 166:35** | **1892: 130:15** | **1902: 107:45** | **1908: 107:28***  *(asterisk = flagged)*
- Flagged value: **107:28**, deviation 40.9 h from other-years median (148.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Maine → San Francisco, California (1902)
- Values by year: **1882: 166:35** | **1883: 166:35** | **1892: 130:15** | **1902: 107:45*** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **107:45**, deviation 40.7 h from other-years median (148.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Providence, Rhode Island → San Francisco, California (1908)
- Values by year: **1882: 163:30** | **1883: 163:30** | **1892: 118:45** | **1902: 100:45** | **1908: 100:28***  *(asterisk = flagged)*
- Flagged value: **100:28**, deviation 40.7 h from other-years median (141.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → San Francisco, California (1908)
- Values by year: **1882: 148:00** | **1883: 148:00** | **1892: 124:40** | **1902: 102:45** | **1908: 95:45***  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 40.6 h from other-years median (136.34 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Santa Fe, New Mexico → San Francisco, California (1892)
- Values by year: **1882: 71:41** | **1892: 77:15*** | **1902: 34:05** | **1908: 36:45**  *(asterisk = flagged)*
- Flagged value: **77:15**, deviation 40.5 h from other-years median (36.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hartford, Connecticut → San Francisco, California (1908)
- Values by year: **1882: 160:27** | **1883: 160:27** | **1892: 114:00** | **1902: 99:45** | **1908: 96:45***  *(asterisk = flagged)*
- Flagged value: **96:45**, deviation 40.5 h from other-years median (137.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → San Francisco, California (1908)
- Values by year: **1882: 162:29** | **1883: 162:20** | **1892: 112:00** | **1902: 97:45** | **1908: 96:45***  *(asterisk = flagged)*
- Flagged value: **96:45**, deviation 40.4 h from other-years median (137.16 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Providence, Rhode Island → San Francisco, California (1902)
- Values by year: **1882: 163:30** | **1883: 163:30** | **1892: 118:45** | **1902: 100:45*** | **1908: 100:28**  *(asterisk = flagged)*
- Flagged value: **100:45**, deviation 40.4 h from other-years median (141.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### White River Junction, Vermont → San Francisco, California (1908)
- Values by year: **1882: 166:45** | **1883: 166:45** | **1892: 125:15** | **1902: 105:45** | **1908: 105:45***  *(asterisk = flagged)*
- Flagged value: **105:45**, deviation 40.2 h from other-years median (146.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### White River Junction, Vermont → San Francisco, California (1902)
- Values by year: **1882: 166:45** | **1883: 166:45** | **1892: 125:15** | **1902: 105:45*** | **1908: 105:45**  *(asterisk = flagged)*
- Flagged value: **105:45**, deviation 40.2 h from other-years median (146.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → New York, New York (1892)
- Values by year: **1882: 109:40** | **1883: 109:40** | **1892: 69:30*** | **1902: 65:30**  *(asterisk = flagged)*
- Flagged value: **69:30**, deviation 40.2 h from other-years median (109.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → San Francisco, California (1902)
- Values by year: **1882: 163:10** | **1883: 163:10** | **1892: 115:00** | **1902: 98:55*** | **1908: 96:55**  *(asterisk = flagged)*
- Flagged value: **98:55**, deviation 40.2 h from other-years median (139.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Washington, District of Columbia (1892)
- Values by year: **1882: 112:50** | **1883: 112:50** | **1892: 72:48*** | **1902: 66:30**  *(asterisk = flagged)*
- Flagged value: **72:48**, deviation 40.0 h from other-years median (112.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → San Francisco, California (1892)
- Values by year: **1882: 156:20** | **1883: 156:20** | **1892: 90:20*** | **1902: 103:45** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **90:20**, deviation 39.7 h from other-years median (130.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 107:20** | **1883: 107:20** | **1892: 69:40** | **1902: 67:40***  *(asterisk = flagged)*
- Flagged value: **67:40**, deviation 39.7 h from other-years median (107.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Boston, Massachusetts (1908)
- Values by year: **1882: 173:10** | **1883: 173:10** | **1892: 128:09** | **1902: 115:00** | **1908: 111:00***  *(asterisk = flagged)*
- Flagged value: **111:00**, deviation 39.7 h from other-years median (150.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Newport, Rhode Island → San Francisco, California (1908)
- Values by year: **1882: 166:35** | **1883: 166:35** | **1892: 119:15** | **1902: 103:45** | **1908: 103:28***  *(asterisk = flagged)*
- Flagged value: **103:28**, deviation 39.4 h from other-years median (142.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → San Francisco, California (1902)
- Values by year: **1882: 162:29** | **1883: 162:20** | **1892: 112:00** | **1902: 97:45*** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **97:45**, deviation 39.4 h from other-years median (137.16 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cairo, Illinois → San Francisco, California (1902)
- Values by year: **1882: 130:31** | **1883: 130:31** | **1892: 106:15** | **1902: 79:00*** | **1908: 75:00**  *(asterisk = flagged)*
- Flagged value: **79:00**, deviation 39.4 h from other-years median (118.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, South Carolina → San Francisco, California (1908)
- Values by year: **1882: 169:15** | **1883: 169:15** | **1892: 126:15** | **1902: 110:45** | **1908: 108:28***  *(asterisk = flagged)*
- Flagged value: **108:28**, deviation 39.3 h from other-years median (147.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rome, New York → San Francisco, California (1908)
- Values by year: **1882: 152:05** | **1883: 152:05** | **1892: 103:15** | **1902: 88:45** | **1908: 88:28***  *(asterisk = flagged)*
- Flagged value: **88:28**, deviation 39.2 h from other-years median (127.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Omaha, Nebraska → San Francisco, California (1908)
- Values by year: **1882: 97:05** | **1883: 97:06** | **1892: 92:15** | **1902: 52:30** | **1908: 55:30***  *(asterisk = flagged)*
- Flagged value: **55:30**, deviation 39.2 h from other-years median (94.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Charleston, South Carolina (1892)
- Values by year: **1882: 190:20** | **1883: 190:20** | **1892: 115:45*** | **1902: 119:30** | **1908: 119:30**  *(asterisk = flagged)*
- Flagged value: **115:45**, deviation 39.2 h from other-years median (154.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → San Francisco, California (1902)
- Values by year: **1882: 161:35** | **1883: 161:35** | **1892: 116:15** | **1902: 99:45*** | **1908: 99:45**  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 39.2 h from other-years median (138.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → San Francisco, California (1908)
- Values by year: **1882: 161:35** | **1883: 161:35** | **1892: 116:15** | **1902: 99:45** | **1908: 99:45***  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 39.2 h from other-years median (138.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Newport, Rhode Island → San Francisco, California (1902)
- Values by year: **1882: 166:35** | **1883: 166:35** | **1892: 119:15** | **1902: 103:45*** | **1908: 103:28**  *(asterisk = flagged)*
- Flagged value: **103:45**, deviation 39.2 h from other-years median (142.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rome, New York → San Francisco, California (1902)
- Values by year: **1882: 152:05** | **1883: 152:05** | **1892: 103:15** | **1902: 88:45*** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **88:45**, deviation 38.9 h from other-years median (127.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Pittsburgh, Pennsylvania (1892)
- Values by year: **1883: 140:25** | **1892: 69:00*** | **1902: 75:00**  *(asterisk = flagged)*
- Flagged value: **69:00**, deviation 38.7 h from other-years median (107.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → San Francisco, California (1902)
- Values by year: **1882: 165:34** | **1883: 165:34** | **1892: 88:15** | **1902: 88:15*** | **1908: 88:15**  *(asterisk = flagged)*
- Flagged value: **88:15**, deviation 38.7 h from other-years median (126.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → San Francisco, California (1908)
- Values by year: **1882: 165:34** | **1883: 165:34** | **1892: 88:15** | **1902: 88:15** | **1908: 88:15***  *(asterisk = flagged)*
- Flagged value: **88:15**, deviation 38.7 h from other-years median (126.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → San Francisco, California (1892)
- Values by year: **1882: 165:34** | **1883: 165:34** | **1892: 88:15*** | **1902: 88:15** | **1908: 88:15**  *(asterisk = flagged)*
- Flagged value: **88:15**, deviation 38.7 h from other-years median (126.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kalamazoo, Michigan → San Francisco, California (1908)
- Values by year: **1882: 126:12** | **1883: 126:12** | **1892: 100:15** | **1902: 74:45** | **1908: 74:45***  *(asterisk = flagged)*
- Flagged value: **74:45**, deviation 38.5 h from other-years median (113.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kalamazoo, Michigan → San Francisco, California (1902)
- Values by year: **1882: 126:12** | **1883: 126:12** | **1892: 100:15** | **1902: 74:45*** | **1908: 74:45**  *(asterisk = flagged)*
- Flagged value: **74:45**, deviation 38.5 h from other-years median (113.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Frankfort, Kentucky → San Francisco, California (1908)
- Values by year: **1882: 147:30** | **1883: 147:30** | **1892: 96:15** | **1902: 83:45** | **1908: 83:28***  *(asterisk = flagged)*
- Flagged value: **83:28**, deviation 38.4 h from other-years median (121.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cape May, New Jersey → San Francisco, California (1908)
- Values by year: **1882: 147:40** | **1883: 147:40** | **1892: 116:45** | **1902: 96:00** | **1908: 94:00***  *(asterisk = flagged)*
- Flagged value: **94:00**, deviation 38.2 h from other-years median (132.21 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → San Francisco, California (1902)
- Values by year: **1882: 165:39** | **1883: 165:35** | **1892: 102:15** | **1902: 95:45*** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 38.2 h from other-years median (133.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → San Francisco, California (1908)
- Values by year: **1882: 165:39** | **1883: 165:35** | **1892: 102:15** | **1902: 95:45** | **1908: 95:45***  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 38.2 h from other-years median (133.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Buffalo, New York → San Francisco, California (1908)
- Values by year: **1882: 143:30** | **1883: 143:30** | **1892: 99:45** | **1902: 83:45** | **1908: 83:28***  *(asterisk = flagged)*
- Flagged value: **83:28**, deviation 38.2 h from other-years median (121.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Frankfort, Kentucky → San Francisco, California (1902)
- Values by year: **1882: 147:30** | **1883: 147:30** | **1892: 96:15** | **1902: 83:45*** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **83:45**, deviation 38.1 h from other-years median (121.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Charleston, South Carolina (1908)
- Values by year: **1882: 190:20** | **1883: 190:20** | **1892: 115:45** | **1902: 115:00** | **1908: 115:00***  *(asterisk = flagged)*
- Flagged value: **115:00**, deviation 38.0 h from other-years median (153.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Charleston, South Carolina (1902)
- Values by year: **1882: 190:20** | **1883: 190:20** | **1892: 115:45** | **1902: 115:00*** | **1908: 115:00**  *(asterisk = flagged)*
- Flagged value: **115:00**, deviation 38.0 h from other-years median (153.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Buffalo, New York → San Francisco, California (1902)
- Values by year: **1882: 143:30** | **1883: 143:30** | **1892: 99:45** | **1902: 83:45*** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **83:45**, deviation 37.9 h from other-years median (121.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sherman, Texas → San Francisco, California (1908)
- Values by year: **1882: 143:40** | **1883: 145:40** | **1892: 123:13** | **1902: 95:45** | **1908: 95:45***  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 37.7 h from other-years median (133.44 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sherman, Texas → San Francisco, California (1902)
- Values by year: **1882: 143:40** | **1883: 145:40** | **1892: 123:13** | **1902: 95:45*** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 37.7 h from other-years median (133.44 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Philadelphia, Pennsylvania (1892)
- Values by year: **1882: 107:20** | **1883: 107:20** | **1892: 69:40*** | **1902: 67:40**  *(asterisk = flagged)*
- Flagged value: **69:40**, deviation 37.7 h from other-years median (107.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Santa Fe, New Mexico → San Francisco, California (1902)
- Values by year: **1882: 71:41** | **1892: 77:15** | **1902: 34:05*** | **1908: 36:45**  *(asterisk = flagged)*
- Flagged value: **34:05**, deviation 37.6 h from other-years median (71.68 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New York, New York → San Francisco, California (1902)
- Values by year: **1882: 159:15** | **1883: 159:15** | **1892: 111:15** | **1902: 97:45*** | **1908: 92:28**  *(asterisk = flagged)*
- Flagged value: **97:45**, deviation 37.5 h from other-years median (135.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albuquerque, New Mexico → San Francisco, California (1892)
- Values by year: **1892: 74:15*** | **1902: 36:45** | **1908: 36:45**  *(asterisk = flagged)*
- Flagged value: **74:15**, deviation 37.5 h from other-years median (36.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hartford, Connecticut → San Francisco, California (1902)
- Values by year: **1882: 160:27** | **1883: 160:27** | **1892: 114:00** | **1902: 99:45*** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 37.5 h from other-years median (137.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dubuque, Iowa → San Francisco, California (1908)
- Values by year: **1882: 124:54** | **1883: 124:54** | **1892: 84:15** | **1902: 60:45** | **1908: 67:08***  *(asterisk = flagged)*
- Flagged value: **67:08**, deviation 37.4 h from other-years median (104.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Massachusetts → San Francisco, California (1908)
- Values by year: **1882: 158:05** | **1883: 158:05** | **1892: 112:15** | **1902: 100:45** | **1908: 97:45***  *(asterisk = flagged)*
- Flagged value: **97:45**, deviation 37.4 h from other-years median (135.16 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → San Francisco, California (1902)
- Values by year: **1882: 127:06** | **1883: 127:06** | **1892: 99:45** | **1902: 89:45***  *(asterisk = flagged)*
- Flagged value: **89:45**, deviation 37.4 h from other-years median (127.10 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, South Carolina → San Francisco, California (1902)
- Values by year: **1882: 169:15** | **1883: 169:15** | **1892: 126:15** | **1902: 110:45*** | **1908: 108:28**  *(asterisk = flagged)*
- Flagged value: **110:45**, deviation 37.0 h from other-years median (147.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → San Francisco, California (1902)
- Values by year: **1882: 173:15** | **1883: 173:15** | **1892: 126:15** | **1902: 112:45*** | **1908: 108:28**  *(asterisk = flagged)*
- Flagged value: **112:45**, deviation 37.0 h from other-years median (149.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dover, Delaware → San Francisco, California (1908)
- Values by year: **1882: 149:14** | **1883: 149:18** | **1892: 118:15** | **1902: 96:45** | **1908: 96:45***  *(asterisk = flagged)*
- Flagged value: **96:45**, deviation 37.0 h from other-years median (133.74 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dover, Delaware → San Francisco, California (1902)
- Values by year: **1882: 149:14** | **1883: 149:18** | **1892: 118:15** | **1902: 96:45*** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **96:45**, deviation 37.0 h from other-years median (133.74 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Charleston, South Carolina (1892)
- Values by year: **1882: 190:20** | **1883: 190:20** | **1892: 115:45*** | **1902: 115:00** | **1908: 115:00**  *(asterisk = flagged)*
- Flagged value: **115:45**, deviation 36.9 h from other-years median (152.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Detroit, Michigan → San Francisco, California (1902)
- Values by year: **1882: 131:02** | **1883: 131:02** | **1892: 104:15** | **1902: 80:45*** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **80:45**, deviation 36.9 h from other-years median (117.64 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Detroit, Michigan → San Francisco, California (1908)
- Values by year: **1882: 131:02** | **1883: 131:02** | **1892: 104:15** | **1902: 80:45** | **1908: 80:45***  *(asterisk = flagged)*
- Flagged value: **80:45**, deviation 36.9 h from other-years median (117.64 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → San Francisco, California (1902)
- Values by year: **1882: 156:45** | **1883: 156:45** | **1892: 128:15** | **1902: 105:45*** | **1908: 112:15**  *(asterisk = flagged)*
- Flagged value: **105:45**, deviation 36.8 h from other-years median (142.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Grafton, West Virginia → San Francisco, California (1908)
- Values by year: **1882: 135:47** | **1883: 135:47** | **1892: 106:15** | **1902: 85:45** | **1908: 84:28***  *(asterisk = flagged)*
- Flagged value: **84:28**, deviation 36.5 h from other-years median (121.02 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bay City, Michigan → San Francisco, California (1908)
- Values by year: **1882: 135:17** | **1883: 135:17** | **1892: 101:15** | **1902: 82:45** | **1908: 81:45***  *(asterisk = flagged)*
- Flagged value: **81:45**, deviation 36.5 h from other-years median (118.27 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Concord, New Hampshire → San Francisco, California (1902)
- Values by year: **1882: 166:00** | **1883: 166:00** | **1892: 118:15** | **1902: 105:45*** | **1908: 105:45**  *(asterisk = flagged)*
- Flagged value: **105:45**, deviation 36.4 h from other-years median (142.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Concord, New Hampshire → San Francisco, California (1908)
- Values by year: **1882: 166:00** | **1883: 166:00** | **1892: 118:15** | **1902: 105:45** | **1908: 105:45***  *(asterisk = flagged)*
- Flagged value: **105:45**, deviation 36.4 h from other-years median (142.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cape May, New Jersey → San Francisco, California (1902)
- Values by year: **1882: 147:40** | **1883: 147:40** | **1892: 116:45** | **1902: 96:00*** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **96:00**, deviation 36.2 h from other-years median (132.21 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Staunton, Virginia → San Francisco, California (1908)
- Values by year: **1882: 151:35** | **1883: 151:35** | **1892: 119:15** | **1902: 102:45** | **1908: 99:28***  *(asterisk = flagged)*
- Flagged value: **99:28**, deviation 35.9 h from other-years median (135.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Richmond, Virginia → San Francisco, California (1908)
- Values by year: **1882: 149:08** | **1883: 149:08** | **1892: 119:15** | **1902: 99:45** | **1908: 98:28***  *(asterisk = flagged)*
- Flagged value: **98:28**, deviation 35.7 h from other-years median (134.19 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wheeling, West Virginia → San Francisco, California (1908)
- Values by year: **1882: 134:35** | **1883: 134:35** | **1892: 103:15** | **1902: 83:45** | **1908: 83:15***  *(asterisk = flagged)*
- Flagged value: **83:15**, deviation 35.7 h from other-years median (118.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Boston, Massachusetts (1902)
- Values by year: **1882: 173:10** | **1883: 173:10** | **1892: 128:09** | **1902: 115:00*** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **115:00**, deviation 35.7 h from other-years median (150.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chicago, Illinois → San Francisco, California (1908)
- Values by year: **1882: 121:24** | **1883: 121:24** | **1892: 80:15** | **1902: 69:25** | **1908: 65:15***  *(asterisk = flagged)*
- Flagged value: **65:15**, deviation 35.6 h from other-years median (100.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Madison, Wisconsin → San Francisco, California (1908)
- Values by year: **1882: 132:19** | **1883: 132:19** | **1892: 86:15** | **1902: 73:45** | **1908: 73:45***  *(asterisk = flagged)*
- Flagged value: **73:45**, deviation 35.5 h from other-years median (109.28 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Madison, Wisconsin → San Francisco, California (1902)
- Values by year: **1882: 132:19** | **1883: 132:19** | **1892: 86:15** | **1902: 73:45*** | **1908: 73:45**  *(asterisk = flagged)*
- Flagged value: **73:45**, deviation 35.5 h from other-years median (109.28 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bay City, Michigan → San Francisco, California (1902)
- Values by year: **1882: 135:17** | **1883: 135:17** | **1892: 101:15** | **1902: 82:45*** | **1908: 81:45**  *(asterisk = flagged)*
- Flagged value: **82:45**, deviation 35.5 h from other-years median (118.27 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Milwaukee, Wisconsin → San Francisco, California (1908)
- Values by year: **1882: 125:14** | **1883: 125:14** | **1892: 89:15** | **1902: 71:45** | **1908: 71:45***  *(asterisk = flagged)*
- Flagged value: **71:45**, deviation 35.5 h from other-years median (107.24 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Milwaukee, Wisconsin → San Francisco, California (1902)
- Values by year: **1882: 125:14** | **1883: 125:14** | **1892: 89:15** | **1902: 71:45*** | **1908: 71:45**  *(asterisk = flagged)*
- Flagged value: **71:45**, deviation 35.5 h from other-years median (107.24 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charlotte, North Carolina → San Francisco, California (1908)
- Values by year: **1882: 158:10** | **1883: 158:10** | **1892: 127:45** | **1902: 107:45** | **1908: 107:28***  *(asterisk = flagged)*
- Flagged value: **107:28**, deviation 35.5 h from other-years median (142.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Charleston, South Carolina (1908)
- Values by year: **1882: 190:20** | **1883: 190:20** | **1892: 115:45** | **1902: 119:30** | **1908: 119:30***  *(asterisk = flagged)*
- Flagged value: **119:30**, deviation 35.4 h from other-years median (154.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Charleston, South Carolina (1902)
- Values by year: **1882: 190:20** | **1883: 190:20** | **1892: 115:45** | **1902: 119:30*** | **1908: 119:30**  *(asterisk = flagged)*
- Flagged value: **119:30**, deviation 35.4 h from other-years median (154.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Grafton, West Virginia → San Francisco, California (1902)
- Values by year: **1882: 135:47** | **1883: 135:47** | **1892: 106:15** | **1902: 85:45*** | **1908: 84:28**  *(asterisk = flagged)*
- Flagged value: **85:45**, deviation 35.3 h from other-years median (121.02 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charlotte, North Carolina → San Francisco, California (1902)
- Values by year: **1882: 158:10** | **1883: 158:10** | **1892: 127:45** | **1902: 107:45*** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **107:45**, deviation 35.2 h from other-years median (142.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wheeling, West Virginia → San Francisco, California (1902)
- Values by year: **1882: 134:35** | **1883: 134:35** | **1892: 103:15** | **1902: 83:45*** | **1908: 83:15**  *(asterisk = flagged)*
- Flagged value: **83:45**, deviation 35.2 h from other-years median (118.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Santa Fe, New Mexico → San Francisco, California (1908)
- Values by year: **1882: 71:41** | **1892: 77:15** | **1902: 34:05** | **1908: 36:45***  *(asterisk = flagged)*
- Flagged value: **36:45**, deviation 34.9 h from other-years median (71.68 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Knoxville, Tennessee → San Francisco, California (1908)
- Values by year: **1882: 150:28** | **1883: 150:28** | **1892: 116:15** | **1902: 98:45** | **1908: 98:28***  *(asterisk = flagged)*
- Flagged value: **98:28**, deviation 34.9 h from other-years median (133.36 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Smith, Arkansas → San Francisco, California (1908)
- Values by year: **1882: 141:21** | **1883: 141:21** | **1892: 105:15** | **1902: 88:45** | **1908: 88:35***  *(asterisk = flagged)*
- Flagged value: **88:35**, deviation 34.7 h from other-years median (123.30 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Washington, District of Columbia → San Francisco, California (1902)
- Values by year: **1882: 145:15** | **1883: 145:15** | **1892: 112:15** | **1902: 94:05*** | **1908: 95:05**  *(asterisk = flagged)*
- Flagged value: **94:05**, deviation 34.7 h from other-years median (128.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### St. Louis, Missouri → San Francisco, California (1892)
- Values by year: **1882: 118:24** | **1883: 113:24** | **1892: 81:15***  *(asterisk = flagged)*
- Flagged value: **81:15**, deviation 34.6 h from other-years median (115.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Pittsburgh, Pennsylvania (1902)
- Values by year: **1883: 164:15** | **1892: 109:00** | **1902: 102:00***  *(asterisk = flagged)*
- Flagged value: **102:00**, deviation 34.6 h from other-years median (136.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Philadelphia, Pennsylvania → San Francisco, California (1908)
- Values by year: **1882: 143:55** | **1883: 143:55** | **1892: 112:15** | **1902: 93:45** | **1908: 93:28***  *(asterisk = flagged)*
- Flagged value: **93:28**, deviation 34.6 h from other-years median (128.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Knoxville, Tennessee → San Francisco, California (1902)
- Values by year: **1882: 150:28** | **1883: 150:28** | **1892: 116:15** | **1902: 98:45*** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **98:45**, deviation 34.6 h from other-years median (133.36 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Smith, Arkansas → San Francisco, California (1902)
- Values by year: **1882: 141:21** | **1883: 141:21** | **1892: 105:15** | **1902: 88:45*** | **1908: 88:35**  *(asterisk = flagged)*
- Flagged value: **88:45**, deviation 34.5 h from other-years median (123.30 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Richmond, Virginia → San Francisco, California (1902)
- Values by year: **1882: 149:08** | **1883: 149:08** | **1892: 119:15** | **1902: 99:45*** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 34.4 h from other-years median (134.19 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Massachusetts → San Francisco, California (1902)
- Values by year: **1882: 158:05** | **1883: 158:05** | **1892: 112:15** | **1902: 100:45*** | **1908: 97:45**  *(asterisk = flagged)*
- Flagged value: **100:45**, deviation 34.4 h from other-years median (135.16 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Charleston, South Carolina (1902)
- Values by year: **1882: 166:57** | **1883: 166:57** | **1892: 141:45** | **1902: 120:00*** | **1908: 120:00**  *(asterisk = flagged)*
- Flagged value: **120:00**, deviation 34.4 h from other-years median (154.35 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Charleston, South Carolina (1908)
- Values by year: **1882: 166:57** | **1883: 166:57** | **1892: 141:45** | **1902: 120:00** | **1908: 120:00***  *(asterisk = flagged)*
- Flagged value: **120:00**, deviation 34.4 h from other-years median (154.35 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Philadelphia, Pennsylvania → San Francisco, California (1902)
- Values by year: **1882: 143:55** | **1883: 143:55** | **1892: 112:15** | **1902: 93:45*** | **1908: 93:28**  *(asterisk = flagged)*
- Flagged value: **93:45**, deviation 34.3 h from other-years median (128.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Trenton, New Jersey → San Francisco, California (1908)
- Values by year: **1882: 141:45** | **1883: 141:45** | **1892: 110:22** | **1902: 92:45** | **1908: 91:45***  *(asterisk = flagged)*
- Flagged value: **91:45**, deviation 34.3 h from other-years median (126.06 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Norfolk, Virginia → San Francisco, California (1908)
- Values by year: **1882: 152:35** | **1883: 152:35** | **1892: 116:15** | **1902: 100:45** | **1908: 100:28***  *(asterisk = flagged)*
- Flagged value: **100:28**, deviation 33.9 h from other-years median (134.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Boston, Massachusetts (1908)
- Values by year: **1882: 157:10** | **1883: 157:10** | **1892: 117:30** | **1902: 105:30** | **1908: 103:30***  *(asterisk = flagged)*
- Flagged value: **103:30**, deviation 33.8 h from other-years median (137.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Decatur, Alabama → San Francisco, California (1902)
- Values by year: **1882: 142:00** | **1883: 142:00** | **1892: 108:45** | **1902: 91:35*** | **1908: 97:25**  *(asterisk = flagged)*
- Flagged value: **91:35**, deviation 33.8 h from other-years median (125.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Annapolis, Maryland → San Francisco, California (1908)
- Values by year: **1882: 144:49** | **1883: 144:49** | **1892: 114:15** | **1902: 95:45** | **1908: 95:45***  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 33.8 h from other-years median (129.53 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Annapolis, Maryland → San Francisco, California (1902)
- Values by year: **1882: 144:49** | **1883: 144:49** | **1892: 114:15** | **1902: 95:45*** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 33.8 h from other-years median (129.53 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Washington, District of Columbia → San Francisco, California (1908)
- Values by year: **1882: 145:15** | **1883: 145:15** | **1892: 112:15** | **1902: 94:05** | **1908: 95:05***  *(asterisk = flagged)*
- Flagged value: **95:05**, deviation 33.7 h from other-years median (128.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Norfolk, Virginia → San Francisco, California (1902)
- Values by year: **1882: 152:35** | **1883: 152:35** | **1892: 116:15** | **1902: 100:45*** | **1908: 100:28**  *(asterisk = flagged)*
- Flagged value: **100:45**, deviation 33.7 h from other-years median (134.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Memphis, Tennessee → San Francisco, California (1908)
- Values by year: **1882: 145:00** | **1883: 145:00** | **1892: 99:15** | **1902: 88:45** | **1908: 88:28***  *(asterisk = flagged)*
- Flagged value: **88:28**, deviation 33.7 h from other-years median (122.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → San Francisco, California (1902)
- Values by year: **1882: 148:00** | **1883: 148:00** | **1892: 124:40** | **1902: 102:45*** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 33.6 h from other-years median (136.34 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cleveland, Ohio → San Francisco, California (1902)
- Values by year: **1882: 132:42** | **1883: 132:42** | **1892: 94:15** | **1902: 79:55*** | **1908: 79:55**  *(asterisk = flagged)*
- Flagged value: **79:55**, deviation 33.6 h from other-years median (113.47 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cleveland, Ohio → San Francisco, California (1908)
- Values by year: **1882: 132:42** | **1883: 132:42** | **1892: 94:15** | **1902: 79:55** | **1908: 79:55***  *(asterisk = flagged)*
- Flagged value: **79:55**, deviation 33.6 h from other-years median (113.47 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → San Francisco, California (1902)
- Values by year: **1882: 150:20** | **1883: 150:20** | **1892: 108:15** | **1902: 95:45*** | **1908: 106:45**  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 33.5 h from other-years median (129.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Memphis, Tennessee → San Francisco, California (1902)
- Values by year: **1882: 145:00** | **1883: 145:00** | **1892: 99:15** | **1902: 88:45*** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **88:45**, deviation 33.4 h from other-years median (122.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Baltimore, Maryland → San Francisco, California (1902)
- Values by year: **1882: 142:55** | **1883: 142:55** | **1892: 113:15** | **1902: 94:45*** | **1908: 94:45**  *(asterisk = flagged)*
- Flagged value: **94:45**, deviation 33.3 h from other-years median (128.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Baltimore, Maryland → San Francisco, California (1908)
- Values by year: **1882: 142:55** | **1883: 142:55** | **1892: 113:15** | **1902: 94:45** | **1908: 94:45***  *(asterisk = flagged)*
- Flagged value: **94:45**, deviation 33.3 h from other-years median (128.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Trenton, New Jersey → San Francisco, California (1902)
- Values by year: **1882: 141:45** | **1883: 141:45** | **1892: 110:22** | **1902: 92:45*** | **1908: 91:45**  *(asterisk = flagged)*
- Flagged value: **92:45**, deviation 33.3 h from other-years median (126.06 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cumberland, Maryland → San Francisco, California (1902)
- Values by year: **1882: 136:45** | **1883: 136:45** | **1892: 105:15** | **1902: 87:45*** | **1908: 87:45**  *(asterisk = flagged)*
- Flagged value: **87:45**, deviation 33.2 h from other-years median (121.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cumberland, Maryland → San Francisco, California (1908)
- Values by year: **1882: 136:45** | **1883: 136:45** | **1892: 105:15** | **1902: 87:45** | **1908: 87:45***  *(asterisk = flagged)*
- Flagged value: **87:45**, deviation 33.2 h from other-years median (121.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Leavenworth, Kansas → San Francisco, California (1908)
- Values by year: **1882: 109:09** | **1883: 109:09** | **1892: 80:15** | **1902: 61:45** | **1908: 61:28***  *(asterisk = flagged)*
- Flagged value: **61:28**, deviation 33.2 h from other-years median (94.70 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbia, South Carolina → San Francisco, California (1908)
- Values by year: **1882: 162:45** | **1883: 162:45** | **1892: 124:15** | **1902: 110:45** | **1908: 110:28***  *(asterisk = flagged)*
- Flagged value: **110:28**, deviation 33.0 h from other-years median (143.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pittsburgh, Pennsylvania → San Francisco, California (1892)
- Values by year: **1882: 132:15** | **1883: 132:15** | **1892: 99:15***  *(asterisk = flagged)*
- Flagged value: **99:15**, deviation 33.0 h from other-years median (132.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Leavenworth, Kansas → San Francisco, California (1902)
- Values by year: **1882: 109:09** | **1883: 109:09** | **1892: 80:15** | **1902: 61:45*** | **1908: 61:28**  *(asterisk = flagged)*
- Flagged value: **61:45**, deviation 33.0 h from other-years median (94.70 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Cincinnati, Ohio (1908)
- Values by year: **1882: 141:30** | **1883: 141:30** | **1892: 115:50** | **1902: 95:50** | **1908: 95:50***  *(asterisk = flagged)*
- Flagged value: **95:50**, deviation 32.8 h from other-years median (128.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atlanta, Georgia → San Francisco, California (1908)
- Values by year: **1882: 150:30** | **1883: 150:30** | **1892: 120:40** | **1902: 102:45** | **1908: 102:45***  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 32.8 h from other-years median (135.59 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atlanta, Georgia → San Francisco, California (1902)
- Values by year: **1882: 150:30** | **1883: 150:30** | **1892: 120:40** | **1902: 102:45*** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 32.8 h from other-years median (135.59 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Cincinnati, Ohio (1902)
- Values by year: **1882: 141:30** | **1883: 141:30** | **1892: 115:50** | **1902: 95:50*** | **1908: 95:50**  *(asterisk = flagged)*
- Flagged value: **95:50**, deviation 32.8 h from other-years median (128.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Toledo, Ohio → San Francisco, California (1908)
- Values by year: **1882: 129:16** | **1883: 129:16** | **1892: 91:45** | **1902: 77:45** | **1908: 77:45***  *(asterisk = flagged)*
- Flagged value: **77:45**, deviation 32.8 h from other-years median (110.51 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Toledo, Ohio → San Francisco, California (1902)
- Values by year: **1882: 129:16** | **1883: 129:16** | **1892: 91:45** | **1902: 77:45*** | **1908: 77:45**  *(asterisk = flagged)*
- Flagged value: **77:45**, deviation 32.8 h from other-years median (110.51 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbia, South Carolina → San Francisco, California (1902)
- Values by year: **1882: 162:45** | **1883: 162:45** | **1892: 124:15** | **1902: 110:45*** | **1908: 110:28**  *(asterisk = flagged)*
- Flagged value: **110:45**, deviation 32.8 h from other-years median (143.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 94:30** | **1883: 94:30** | **1892: 69:50** | **1902: 61:50***  *(asterisk = flagged)*
- Flagged value: **61:50**, deviation 32.7 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Staunton, Virginia → San Francisco, California (1902)
- Values by year: **1882: 151:35** | **1883: 151:35** | **1892: 119:15** | **1902: 102:45*** | **1908: 99:28**  *(asterisk = flagged)*
- Flagged value: **102:45**, deviation 32.7 h from other-years median (135.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lansing, Michigan → San Francisco, California (1902)
- Values by year: **1882: 129:22** | **1883: 129:22** | **1892: 97:15** | **1902: 80:45*** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **80:45**, deviation 32.6 h from other-years median (113.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lansing, Michigan → San Francisco, California (1908)
- Values by year: **1882: 129:22** | **1883: 129:22** | **1892: 97:15** | **1902: 80:45** | **1908: 80:45***  *(asterisk = flagged)*
- Flagged value: **80:45**, deviation 32.6 h from other-years median (113.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Williamsport, Pennsylvania → San Francisco, California (1908)
- Values by year: **1882: 135:50** | **1883: 136:50** | **1892: 109:15** | **1902: 90:00** | **1908: 90:00***  *(asterisk = flagged)*
- Flagged value: **90:00**, deviation 32.5 h from other-years median (122.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Williamsport, Pennsylvania → San Francisco, California (1902)
- Values by year: **1882: 135:50** | **1883: 136:50** | **1892: 109:15** | **1902: 90:00*** | **1908: 90:00**  *(asterisk = flagged)*
- Flagged value: **90:00**, deviation 32.5 h from other-years median (122.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Baltimore, Maryland (1908)
- Values by year: **1882: 166:00** | **1883: 166:00** | **1892: 121:00** | **1902: 111:00** | **1908: 111:00***  *(asterisk = flagged)*
- Flagged value: **111:00**, deviation 32.5 h from other-years median (143.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Baltimore, Maryland (1902)
- Values by year: **1882: 166:00** | **1883: 166:00** | **1892: 121:00** | **1902: 111:00*** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **111:00**, deviation 32.5 h from other-years median (143.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Nashville, Tennessee → San Francisco, California (1908)
- Values by year: **1882: 133:40** | **1883: 138:40** | **1892: 96:15** | **1902: 82:45** | **1908: 82:28***  *(asterisk = flagged)*
- Flagged value: **82:28**, deviation 32.5 h from other-years median (114.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Nashville, Tennessee → San Francisco, California (1902)
- Values by year: **1882: 133:40** | **1883: 138:40** | **1892: 96:15** | **1902: 82:45*** | **1908: 82:28**  *(asterisk = flagged)*
- Flagged value: **82:45**, deviation 32.2 h from other-years median (114.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Charleston, South Carolina (1908)
- Values by year: **1882: 143:50** | **1883: 143:50** | **1892: 109:45** | **1902: 94:45** | **1908: 94:45***  *(asterisk = flagged)*
- Flagged value: **94:45**, deviation 32.0 h from other-years median (126.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Charleston, South Carolina (1902)
- Values by year: **1882: 143:50** | **1883: 143:50** | **1892: 109:45** | **1902: 94:45*** | **1908: 94:45**  *(asterisk = flagged)*
- Flagged value: **94:45**, deviation 32.0 h from other-years median (126.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Boston, Massachusetts (1902)
- Values by year: **1882: 157:10** | **1883: 157:10** | **1892: 117:30** | **1902: 105:30*** | **1908: 103:30**  *(asterisk = flagged)*
- Flagged value: **105:30**, deviation 31.8 h from other-years median (137.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Chicago, Illinois (1902)
- Values by year: **1882: 141:25** | **1883: 141:25** | **1892: 90:25** | **1902: 84:30*** | **1908: 84:30**  *(asterisk = flagged)*
- Flagged value: **84:30**, deviation 31.4 h from other-years median (115.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Chicago, Illinois (1908)
- Values by year: **1882: 141:25** | **1883: 141:25** | **1892: 90:25** | **1902: 84:30** | **1908: 84:30***  *(asterisk = flagged)*
- Flagged value: **84:30**, deviation 31.4 h from other-years median (115.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chicago, Illinois → San Francisco, California (1902)
- Values by year: **1882: 121:24** | **1883: 121:24** | **1892: 80:15** | **1902: 69:25*** | **1908: 65:15**  *(asterisk = flagged)*
- Flagged value: **69:25**, deviation 31.4 h from other-years median (100.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → New York, New York (1902)
- Values by year: **1882: 169:05** | **1883: 169:05** | **1892: 121:00** | **1902: 114:00*** | **1908: 114:00**  *(asterisk = flagged)*
- Flagged value: **114:00**, deviation 31.0 h from other-years median (145.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → New York, New York (1908)
- Values by year: **1882: 169:05** | **1883: 169:05** | **1892: 121:00** | **1902: 114:00** | **1908: 114:00***  *(asterisk = flagged)*
- Flagged value: **114:00**, deviation 31.0 h from other-years median (145.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Baltimore, Maryland (1908)
- Values by year: **1882: 146:55** | **1883: 146:55** | **1892: 121:00** | **1902: 103:00** | **1908: 103:00***  *(asterisk = flagged)*
- Flagged value: **103:00**, deviation 31.0 h from other-years median (133.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Baltimore, Maryland (1902)
- Values by year: **1882: 146:55** | **1883: 146:55** | **1892: 121:00** | **1902: 103:00*** | **1908: 103:00**  *(asterisk = flagged)*
- Flagged value: **103:00**, deviation 31.0 h from other-years median (133.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbus, Ohio → San Francisco, California (1902)
- Values by year: **1882: 124:00** | **1883: 124:00** | **1892: 102:15** | **1902: 82:15*** | **1908: 82:15**  *(asterisk = flagged)*
- Flagged value: **82:15**, deviation 30.9 h from other-years median (113.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbus, Ohio → San Francisco, California (1908)
- Values by year: **1882: 124:00** | **1883: 124:00** | **1892: 102:15** | **1902: 82:15** | **1908: 82:15***  *(asterisk = flagged)*
- Flagged value: **82:15**, deviation 30.9 h from other-years median (113.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chattanooga, Tennessee → San Francisco, California (1908)
- Values by year: **1882: 137:05** | **1883: 137:05** | **1892: 109:15** | **1902: 92:45** | **1908: 92:28***  *(asterisk = flagged)*
- Flagged value: **92:28**, deviation 30.7 h from other-years median (123.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 166:05** | **1883: 166:05** | **1892: 119:00** | **1902: 112:00*** | **1908: 112:00**  *(asterisk = flagged)*
- Flagged value: **112:00**, deviation 30.5 h from other-years median (142.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 166:05** | **1883: 166:05** | **1892: 119:00** | **1902: 112:00** | **1908: 112:00***  *(asterisk = flagged)*
- Flagged value: **112:00**, deviation 30.5 h from other-years median (142.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Washington, District of Columbia (1902)
- Values by year: **1882: 143:57** | **1883: 143:57** | **1892: 119:00** | **1902: 101:00*** | **1908: 101:00**  *(asterisk = flagged)*
- Flagged value: **101:00**, deviation 30.5 h from other-years median (131.47 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Washington, District of Columbia (1908)
- Values by year: **1882: 143:57** | **1883: 143:57** | **1892: 119:00** | **1902: 101:00** | **1908: 101:00***  *(asterisk = flagged)*
- Flagged value: **101:00**, deviation 30.5 h from other-years median (131.47 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chattanooga, Tennessee → San Francisco, California (1902)
- Values by year: **1882: 137:05** | **1883: 137:05** | **1892: 109:15** | **1902: 92:45*** | **1908: 92:28**  *(asterisk = flagged)*
- Flagged value: **92:45**, deviation 30.4 h from other-years median (123.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → San Francisco, California (1908)
- Values by year: **1882: 156:45** | **1883: 156:45** | **1892: 128:15** | **1902: 105:45** | **1908: 112:15***  *(asterisk = flagged)*
- Flagged value: **112:15**, deviation 30.2 h from other-years median (142.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Washington, District of Columbia (1908)
- Values by year: **1882: 148:27** | **1883: 148:27** | **1892: 120:00** | **1902: 104:00** | **1908: 104:00***  *(asterisk = flagged)*
- Flagged value: **104:00**, deviation 30.2 h from other-years median (134.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Pittsburgh, Pennsylvania (1902)
- Values by year: **1883: 137:27** | **1892: 97:00** | **1902: 87:00***  *(asterisk = flagged)*
- Flagged value: **87:00**, deviation 30.2 h from other-years median (117.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Washington, District of Columbia (1902)
- Values by year: **1882: 148:27** | **1883: 148:27** | **1892: 120:00** | **1902: 104:00*** | **1908: 104:00**  *(asterisk = flagged)*
- Flagged value: **104:00**, deviation 30.2 h from other-years median (134.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atchison, Kansas → San Francisco, California (1908)
- Values by year: **1882: 108:07** | **1883: 108:07** | **1892: 79:15** | **1902: 63:45** | **1908: 63:28***  *(asterisk = flagged)*
- Flagged value: **63:28**, deviation 30.2 h from other-years median (93.68 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → Omaha, Nebraska (1908)
- Values by year: **1883: 53:20** | **1892: 38:00** | **1902: 38:00** | **1908: 68:00***  *(asterisk = flagged)*
- Flagged value: **68:00**, deviation 30.0 h from other-years median (38.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atchison, Kansas → San Francisco, California (1902)
- Values by year: **1882: 108:07** | **1883: 108:07** | **1892: 79:15** | **1902: 63:45*** | **1908: 63:28**  *(asterisk = flagged)*
- Flagged value: **63:45**, deviation 29.9 h from other-years median (93.68 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Washington, District of Columbia (1892)
- Values by year: **1882: 167:20** | **1883: 167:20** | **1892: 110:00*** | **1902: 112:30** | **1908: 112:30**  *(asterisk = flagged)*
- Flagged value: **110:00**, deviation 29.9 h from other-years median (139.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 105:35** | **1883: 105:35** | **1892: 85:50** | **1902: 75:50***  *(asterisk = flagged)*
- Flagged value: **75:50**, deviation 29.8 h from other-years median (105.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Pittsburgh, Pennsylvania (1902)
- Values by year: **1883: 140:25** | **1892: 69:00** | **1902: 75:00***  *(asterisk = flagged)*
- Flagged value: **75:00**, deviation 29.7 h from other-years median (104.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Burlington, Iowa → San Francisco, California (1908)
- Values by year: **1882: 113:29** | **1883: 113:29** | **1892: 75:15** | **1902: 64:45** | **1908: 64:45***  *(asterisk = flagged)*
- Flagged value: **64:45**, deviation 29.6 h from other-years median (94.36 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Burlington, Iowa → San Francisco, California (1902)
- Values by year: **1882: 113:29** | **1883: 113:29** | **1892: 75:15** | **1902: 64:45*** | **1908: 64:45**  *(asterisk = flagged)*
- Flagged value: **64:45**, deviation 29.6 h from other-years median (94.36 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Evansville, Indiana → San Francisco, California (1908)
- Values by year: **1882: 120:40** | **1883: 120:40** | **1892: 90:45** | **1902: 77:45** | **1908: 76:15***  *(asterisk = flagged)*
- Flagged value: **76:15**, deviation 29.5 h from other-years median (105.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prairie du Chien, Wisconsin → San Francisco, California (1902)
- Values by year: **1882: 128:06** | **1883: 128:06** | **1892: 89:15** | **1902: 79:45*** | **1908: 79:45**  *(asterisk = flagged)*
- Flagged value: **79:45**, deviation 28.9 h from other-years median (108.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prairie du Chien, Wisconsin → San Francisco, California (1908)
- Values by year: **1882: 128:06** | **1883: 128:06** | **1892: 89:15** | **1902: 79:45** | **1908: 79:45***  *(asterisk = flagged)*
- Flagged value: **79:45**, deviation 28.9 h from other-years median (108.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → New York, New York (1908)
- Values by year: **1882: 147:30** | **1883: 147:30** | **1892: 111:50** | **1902: 100:50** | **1908: 100:50***  *(asterisk = flagged)*
- Flagged value: **100:50**, deviation 28.8 h from other-years median (129.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → New York, New York (1902)
- Values by year: **1882: 147:30** | **1883: 147:30** | **1892: 111:50** | **1902: 100:50*** | **1908: 100:50**  *(asterisk = flagged)*
- Flagged value: **100:50**, deviation 28.8 h from other-years median (129.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Boston, Massachusetts (1908)
- Values by year: **1882: 161:10** | **1883: 161:10** | **1892: 111:30** | **1902: 108:30** | **1908: 107:30***  *(asterisk = flagged)*
- Flagged value: **107:30**, deviation 28.8 h from other-years median (136.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Des Moines, Iowa → San Francisco, California (1902)
- Values by year: **1882: 106:44** | **1883: 106:44** | **1892: 72:15** | **1902: 60:45*** | **1908: 64:53**  *(asterisk = flagged)*
- Flagged value: **60:45**, deviation 28.7 h from other-years median (89.49 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Indianapolis, Indiana → San Francisco, California (1902)
- Values by year: **1882: 118:03** | **1883: 118:03** | **1892: 89:45** | **1902: 75:15*** | **1908: 75:15**  *(asterisk = flagged)*
- Flagged value: **75:15**, deviation 28.6 h from other-years median (103.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Indianapolis, Indiana → San Francisco, California (1908)
- Values by year: **1882: 118:03** | **1883: 118:03** | **1892: 89:45** | **1902: 75:15** | **1908: 75:15***  *(asterisk = flagged)*
- Flagged value: **75:15**, deviation 28.6 h from other-years median (103.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 136:25** | **1883: 136:25** | **1892: 108:50** | **1902: 107:50***  *(asterisk = flagged)*
- Flagged value: **107:50**, deviation 28.6 h from other-years median (136.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → San Francisco, California (1892)
- Values by year: **1882: 165:39** | **1883: 165:35** | **1892: 102:15*** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **102:15**, deviation 28.4 h from other-years median (130.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jefferson City, Missouri → San Francisco, California (1902)
- Values by year: **1882: 119:42** | **1883: 119:42** | **1892: 78:15** | **1902: 70:45*** | **1908: 70:45**  *(asterisk = flagged)*
- Flagged value: **70:45**, deviation 28.2 h from other-years median (98.97 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jefferson City, Missouri → San Francisco, California (1908)
- Values by year: **1882: 119:42** | **1883: 119:42** | **1892: 78:15** | **1902: 70:45** | **1908: 70:45***  *(asterisk = flagged)*
- Flagged value: **70:45**, deviation 28.2 h from other-years median (98.97 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kansas City, Missouri → San Francisco, California (1902)
- Values by year: **1882: 111:27** | **1883: 111:27** | **1892: 75:15** | **1902: 65:15*** | **1908: 65:15**  *(asterisk = flagged)*
- Flagged value: **65:15**, deviation 28.1 h from other-years median (93.35 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kansas City, Missouri → San Francisco, California (1908)
- Values by year: **1882: 111:27** | **1883: 111:27** | **1892: 75:15** | **1902: 65:15** | **1908: 65:15***  *(asterisk = flagged)*
- Flagged value: **65:15**, deviation 28.1 h from other-years median (93.35 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Saint Louis, Missouri (1908)
- Values by year: **1882: 106:47** | **1883: 106:47** | **1892: 90:40** | **1902: 70:40** | **1908: 70:40***  *(asterisk = flagged)*
- Flagged value: **70:40**, deviation 28.1 h from other-years median (98.72 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Saint Louis, Missouri (1902)
- Values by year: **1882: 106:47** | **1883: 106:47** | **1892: 90:40** | **1902: 70:40*** | **1908: 70:40**  *(asterisk = flagged)*
- Flagged value: **70:40**, deviation 28.1 h from other-years median (98.72 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → San Francisco, California (1892)
- Values by year: **1882: 148:20** | **1883: 148:20** | **1892: 93:20*** | **1902: 94:15** | **1908: 94:15**  *(asterisk = flagged)*
- Flagged value: **93:20**, deviation 28.0 h from other-years median (121.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Evansville, Indiana → San Francisco, California (1902)
- Values by year: **1882: 120:40** | **1883: 120:40** | **1892: 90:45** | **1902: 77:45*** | **1908: 76:15**  *(asterisk = flagged)*
- Flagged value: **77:45**, deviation 28.0 h from other-years median (105.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Decatur, Alabama → San Francisco, California (1908)
- Values by year: **1882: 142:00** | **1883: 142:00** | **1892: 108:45** | **1902: 91:35** | **1908: 97:25***  *(asterisk = flagged)*
- Flagged value: **97:25**, deviation 28.0 h from other-years median (125.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Boston, Massachusetts (1902)
- Values by year: **1882: 161:10** | **1883: 161:10** | **1892: 111:30** | **1902: 108:30*** | **1908: 107:30**  *(asterisk = flagged)*
- Flagged value: **108:30**, deviation 27.8 h from other-years median (136.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cincinnati, Ohio → San Francisco, California (1908)
- Values by year: **1882: 123:45** | **1883: 123:45** | **1892: 97:15** | **1902: 82:45** | **1908: 82:45***  *(asterisk = flagged)*
- Flagged value: **82:45**, deviation 27.8 h from other-years median (110.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cincinnati, Ohio → San Francisco, California (1902)
- Values by year: **1882: 123:45** | **1883: 123:45** | **1892: 97:15** | **1902: 82:45*** | **1908: 82:45**  *(asterisk = flagged)*
- Flagged value: **82:45**, deviation 27.8 h from other-years median (110.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → New York, New York (1908)
- Values by year: **1882: 150:55** | **1883: 150:55** | **1892: 114:30** | **1902: 106:00** | **1908: 105:00***  *(asterisk = flagged)*
- Flagged value: **105:00**, deviation 27.7 h from other-years median (132.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 136:25** | **1883: 136:25** | **1892: 108:50*** | **1902: 107:50**  *(asterisk = flagged)*
- Flagged value: **108:50**, deviation 27.6 h from other-years median (136.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 142:35** | **1883: 142:35** | **1892: 115:40** | **1902: 101:40*** | **1908: 101:40**  *(asterisk = flagged)*
- Flagged value: **101:40**, deviation 27.5 h from other-years median (129.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 142:35** | **1883: 142:35** | **1892: 115:40** | **1902: 101:40** | **1908: 101:40***  *(asterisk = flagged)*
- Flagged value: **101:40**, deviation 27.5 h from other-years median (129.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Washington, District of Columbia (1902)
- Values by year: **1882: 167:20** | **1883: 167:20** | **1892: 110:00** | **1902: 112:30*** | **1908: 112:30**  *(asterisk = flagged)*
- Flagged value: **112:30**, deviation 27.4 h from other-years median (139.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Washington, District of Columbia (1908)
- Values by year: **1882: 167:20** | **1883: 167:20** | **1892: 110:00** | **1902: 112:30** | **1908: 112:30***  *(asterisk = flagged)*
- Flagged value: **112:30**, deviation 27.4 h from other-years median (139.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Boston, Massachusetts (1908)
- Values by year: **1882: 151:35** | **1883: 151:35** | **1892: 120:50** | **1902: 108:50** | **1908: 108:50***  *(asterisk = flagged)*
- Flagged value: **108:50**, deviation 27.4 h from other-years median (136.21 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Boston, Massachusetts (1902)
- Values by year: **1882: 151:35** | **1883: 151:35** | **1892: 120:50** | **1902: 108:50*** | **1908: 108:50**  *(asterisk = flagged)*
- Flagged value: **108:50**, deviation 27.4 h from other-years median (136.21 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → San Francisco, California (1892)
- Values by year: **1882: 127:06** | **1883: 127:06** | **1892: 99:45*** | **1902: 89:45**  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 27.4 h from other-years median (127.10 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Louisville, Kentucky → San Francisco, California (1902)
- Values by year: **1882: 122:45** | **1883: 122:45** | **1892: 93:15** | **1902: 80:45*** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **80:45**, deviation 27.2 h from other-years median (108.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Las Cruces, New Mexico → San Francisco, California (1908)
- Values by year: **1892: 98:15** | **1902: 43:45** | **1908: 43:45***  *(asterisk = flagged)*
- Flagged value: **43:45**, deviation 27.2 h from other-years median (71.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Louisville, Kentucky → San Francisco, California (1908)
- Values by year: **1882: 122:45** | **1883: 122:45** | **1892: 93:15** | **1902: 80:45** | **1908: 80:45***  *(asterisk = flagged)*
- Flagged value: **80:45**, deviation 27.2 h from other-years median (108.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Las Cruces, New Mexico → San Francisco, California (1902)
- Values by year: **1892: 98:15** | **1902: 43:45*** | **1908: 43:45**  *(asterisk = flagged)*
- Flagged value: **43:45**, deviation 27.2 h from other-years median (71.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Shreveport, Louisiana → San Francisco, California (1902)
- Values by year: **1882: 147:46** | **1883: 147:46** | **1892: 106:15** | **1902: 99:55*** | **1908: 99:55**  *(asterisk = flagged)*
- Flagged value: **99:55**, deviation 27.1 h from other-years median (127.01 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Shreveport, Louisiana → San Francisco, California (1908)
- Values by year: **1882: 147:46** | **1883: 147:46** | **1892: 106:15** | **1902: 99:55** | **1908: 99:55***  *(asterisk = flagged)*
- Flagged value: **99:55**, deviation 27.1 h from other-years median (127.01 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 131:55** | **1883: 131:55** | **1892: 104:50*** | **1902: 104:50**  *(asterisk = flagged)*
- Flagged value: **104:50**, deviation 27.1 h from other-years median (131.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 131:55** | **1883: 131:55** | **1892: 104:50** | **1902: 104:50***  *(asterisk = flagged)*
- Flagged value: **104:50**, deviation 27.1 h from other-years median (131.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → San Francisco, California (1902)
- Values by year: **1882: 148:20** | **1883: 148:20** | **1892: 93:20** | **1902: 94:15*** | **1908: 94:15**  *(asterisk = flagged)*
- Flagged value: **94:15**, deviation 27.0 h from other-years median (121.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → San Francisco, California (1908)
- Values by year: **1882: 148:20** | **1883: 148:20** | **1892: 93:20** | **1902: 94:15** | **1908: 94:15***  *(asterisk = flagged)*
- Flagged value: **94:15**, deviation 27.0 h from other-years median (121.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → New York, New York (1908)
- Values by year: **1882: 107:00** | **1883: 107:00** | **1892: 89:30** | **1902: 71:30** | **1908: 71:30***  *(asterisk = flagged)*
- Flagged value: **71:30**, deviation 26.8 h from other-years median (98.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → New York, New York (1902)
- Values by year: **1882: 107:00** | **1883: 107:00** | **1892: 89:30** | **1902: 71:30*** | **1908: 71:30**  *(asterisk = flagged)*
- Flagged value: **71:30**, deviation 26.8 h from other-years median (98.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Baltimore, Maryland (1902)
- Values by year: **1882: 142:25** | **1883: 142:25** | **1892: 111:00** | **1902: 100:00*** | **1908: 100:00**  *(asterisk = flagged)*
- Flagged value: **100:00**, deviation 26.7 h from other-years median (126.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Baltimore, Maryland (1908)
- Values by year: **1882: 142:25** | **1883: 142:25** | **1892: 111:00** | **1902: 100:00** | **1908: 100:00***  *(asterisk = flagged)*
- Flagged value: **100:00**, deviation 26.7 h from other-years median (126.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → New York, New York (1902)
- Values by year: **1882: 150:55** | **1883: 150:55** | **1892: 114:30** | **1902: 106:00*** | **1908: 105:00**  *(asterisk = flagged)*
- Flagged value: **106:00**, deviation 26.7 h from other-years median (132.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 68:30** | **1883: 68:30** | **1892: 41:50*** | **1902: 50:50**  *(asterisk = flagged)*
- Flagged value: **41:50**, deviation 26.7 h from other-years median (68.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Topeka, Kansas → San Francisco, California (1908)
- Values by year: **1882: 107:50** | **1883: 107:50** | **1892: 82:15** | **1902: 68:45** | **1908: 68:28***  *(asterisk = flagged)*
- Flagged value: **68:28**, deviation 26.6 h from other-years median (95.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Omaha, Nebraska (1908)
- Values by year: **1882: 71:50** | **1883: 71:50** | **1892: 35:10** | **1902: 27:10** | **1908: 27:10***  *(asterisk = flagged)*
- Flagged value: **27:10**, deviation 26.3 h from other-years median (53.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Omaha, Nebraska (1902)
- Values by year: **1882: 71:50** | **1883: 71:50** | **1892: 35:10** | **1902: 27:10*** | **1908: 27:10**  *(asterisk = flagged)*
- Flagged value: **27:10**, deviation 26.3 h from other-years median (53.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Topeka, Kansas → San Francisco, California (1902)
- Values by year: **1882: 107:50** | **1883: 107:50** | **1892: 82:15** | **1902: 68:45*** | **1908: 68:28**  *(asterisk = flagged)*
- Flagged value: **68:45**, deviation 26.3 h from other-years median (95.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → San Francisco, California (1908)
- Values by year: **1882: 156:20** | **1883: 156:20** | **1892: 90:20** | **1902: 103:45** | **1908: 103:45***  *(asterisk = flagged)*
- Flagged value: **103:45**, deviation 26.3 h from other-years median (130.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → San Francisco, California (1902)
- Values by year: **1882: 156:20** | **1883: 156:20** | **1892: 90:20** | **1902: 103:45*** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **103:45**, deviation 26.3 h from other-years median (130.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jackson, Mississippi → San Francisco, California (1902)
- Values by year: **1882: 139:40** | **1883: 139:40** | **1892: 104:15** | **1902: 95:45*** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 26.2 h from other-years median (121.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jackson, Mississippi → San Francisco, California (1908)
- Values by year: **1882: 139:40** | **1883: 139:40** | **1892: 104:15** | **1902: 95:45** | **1908: 95:45***  *(asterisk = flagged)*
- Flagged value: **95:45**, deviation 26.2 h from other-years median (121.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Charleston, South Carolina (1902)
- Values by year: **1882: 171:27** | **1883: 171:27** | **1892: 120:45** | **1902: 120:00*** | **1908: 120:00**  *(asterisk = flagged)*
- Flagged value: **120:00**, deviation 26.1 h from other-years median (146.10 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Charleston, South Carolina (1908)
- Values by year: **1882: 171:27** | **1883: 171:27** | **1892: 120:45** | **1902: 120:00** | **1908: 120:00***  *(asterisk = flagged)*
- Flagged value: **120:00**, deviation 26.1 h from other-years median (146.10 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Baltimore, Maryland (1892)
- Values by year: **1892: 126:35*** | **1902: 100:35** | **1908: 100:35**  *(asterisk = flagged)*
- Flagged value: **126:35**, deviation 26.0 h from other-years median (100.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → New York, New York (1908)
- Values by year: **1883: 151:11** | **1892: 120:00** | **1902: 94:00** | **1908: 94:00***  *(asterisk = flagged)*
- Flagged value: **94:00**, deviation 26.0 h from other-years median (120.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → New York, New York (1902)
- Values by year: **1883: 151:11** | **1892: 120:00** | **1902: 94:00*** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **94:00**, deviation 26.0 h from other-years median (120.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → New York, New York (1892)
- Values by year: **1883: 151:11** | **1892: 120:00*** | **1902: 94:00** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **120:00**, deviation 26.0 h from other-years median (94.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Boston, Massachusetts (1902)
- Values by year: **1882: 134:25** | **1883: 134:25** | **1892: 100:30** | **1902: 91:30*** | **1908: 91:30**  *(asterisk = flagged)*
- Flagged value: **91:30**, deviation 26.0 h from other-years median (117.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → New York, New York (1908)
- Values by year: **1882: 146:25** | **1883: 146:25** | **1892: 110:30** | **1902: 103:30** | **1908: 102:30***  *(asterisk = flagged)*
- Flagged value: **102:30**, deviation 26.0 h from other-years median (128.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Boston, Massachusetts (1908)
- Values by year: **1882: 134:25** | **1883: 134:25** | **1892: 100:30** | **1902: 91:30** | **1908: 91:30***  *(asterisk = flagged)*
- Flagged value: **91:30**, deviation 26.0 h from other-years median (117.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → Charleston, South Carolina (1883)
- Values by year: **1883: 50:50*** | **1892: 76:45** | **1902: 76:45** | **1908: 76:45**  *(asterisk = flagged)*
- Flagged value: **50:50**, deviation 25.9 h from other-years median (76.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 144:30** | **1883: 144:30** | **1892: 108:40** | **1902: 100:40*** | **1908: 100:40**  *(asterisk = flagged)*
- Flagged value: **100:40**, deviation 25.9 h from other-years median (126.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 144:30** | **1883: 144:30** | **1892: 108:40** | **1902: 100:40** | **1908: 100:40***  *(asterisk = flagged)*
- Flagged value: **100:40**, deviation 25.9 h from other-years median (126.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Chicago, Illinois (1902)
- Values by year: **1882: 114:50** | **1883: 114:50** | **1892: 90:50** | **1902: 77:00*** | **1908: 77:00**  *(asterisk = flagged)*
- Flagged value: **77:00**, deviation 25.8 h from other-years median (102.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Chicago, Illinois (1908)
- Values by year: **1882: 114:50** | **1883: 114:50** | **1892: 90:50** | **1902: 77:00** | **1908: 77:00***  *(asterisk = flagged)*
- Flagged value: **77:00**, deviation 25.8 h from other-years median (102.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Manchester, New Hampshire → Chicago, Illinois (1908)
- Values by year: **1892: 33:15** | **1902: 82:15** | **1908: 32:00***  *(asterisk = flagged)*
- Flagged value: **32:00**, deviation 25.8 h from other-years median (57.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sioux City, Iowa → San Francisco, California (1908)
- Values by year: **1882: 105:36** | **1883: 105:36** | **1892: 71:15** | **1902: 62:45** | **1908: 62:45***  *(asterisk = flagged)*
- Flagged value: **62:45**, deviation 25.7 h from other-years median (88.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sioux City, Iowa → San Francisco, California (1902)
- Values by year: **1882: 105:36** | **1883: 105:36** | **1892: 71:15** | **1902: 62:45*** | **1908: 62:45**  *(asterisk = flagged)*
- Flagged value: **62:45**, deviation 25.7 h from other-years median (88.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Baltimore, Maryland (1908)
- Values by year: **1882: 53:05** | **1883: 53:05** | **1892: 42:00** | **1902: 22:00** | **1908: 22:00***  *(asterisk = flagged)*
- Flagged value: **22:00**, deviation 25.5 h from other-years median (47.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Baltimore, Maryland (1902)
- Values by year: **1882: 53:05** | **1883: 53:05** | **1892: 42:00** | **1902: 22:00*** | **1908: 22:00**  *(asterisk = flagged)*
- Flagged value: **22:00**, deviation 25.5 h from other-years median (47.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → New York, New York (1902)
- Values by year: **1882: 86:40** | **1883: 86:40** | **1892: 76:30** | **1902: 56:03*** | **1908: 56:30**  *(asterisk = flagged)*
- Flagged value: **56:03**, deviation 25.5 h from other-years median (81.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Baltimore, Maryland (1902)
- Values by year: **1882: 80:15** | **1883: 80:15** | **1892: 75:30** | **1902: 52:30*** | **1908: 52:30**  *(asterisk = flagged)*
- Flagged value: **52:30**, deviation 25.4 h from other-years median (77.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Baltimore, Maryland (1908)
- Values by year: **1882: 80:15** | **1883: 80:15** | **1892: 75:30** | **1902: 52:30** | **1908: 52:30***  *(asterisk = flagged)*
- Flagged value: **52:30**, deviation 25.4 h from other-years median (77.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Baltimore, Maryland (1908)
- Values by year: **1882: 144:25** | **1883: 144:25** | **1892: 107:55** | **1902: 100:55** | **1908: 100:55***  *(asterisk = flagged)*
- Flagged value: **100:55**, deviation 25.2 h from other-years median (126.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Baltimore, Maryland (1902)
- Values by year: **1882: 144:25** | **1883: 144:25** | **1892: 107:55** | **1902: 100:55*** | **1908: 100:55**  *(asterisk = flagged)*
- Flagged value: **100:55**, deviation 25.2 h from other-years median (126.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Chicago, Illinois (1908)
- Values by year: **1882: 119:30** | **1883: 119:30** | **1892: 90:50** | **1902: 80:00** | **1908: 80:00***  *(asterisk = flagged)*
- Flagged value: **80:00**, deviation 25.2 h from other-years median (105.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Chicago, Illinois (1902)
- Values by year: **1882: 119:30** | **1883: 119:30** | **1892: 90:50** | **1902: 80:00*** | **1908: 80:00**  *(asterisk = flagged)*
- Flagged value: **80:00**, deviation 25.2 h from other-years median (105.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → New York, New York (1908)
- Values by year: **1882: 86:40** | **1883: 86:40** | **1892: 76:30** | **1902: 56:03** | **1908: 56:30***  *(asterisk = flagged)*
- Flagged value: **56:30**, deviation 25.1 h from other-years median (81.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Charleston, South Carolina (1892)
- Values by year: **1892: 148:10*** | **1902: 123:10** | **1908: 123:10**  *(asterisk = flagged)*
- Flagged value: **148:10**, deviation 25.0 h from other-years median (123.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Washington, District of Columbia (1892)
- Values by year: **1892: 127:25*** | **1902: 102:25** | **1908: 102:25**  *(asterisk = flagged)*
- Flagged value: **127:25**, deviation 25.0 h from other-years median (102.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Boston, Massachusetts (1892)
- Values by year: **1883: 156:11** | **1892: 127:50*** | **1902: 102:50** | **1908: 102:50**  *(asterisk = flagged)*
- Flagged value: **127:50**, deviation 25.0 h from other-years median (102.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Boston, Massachusetts (1902)
- Values by year: **1883: 156:11** | **1892: 127:50** | **1902: 102:50*** | **1908: 102:50**  *(asterisk = flagged)*
- Flagged value: **102:50**, deviation 25.0 h from other-years median (127.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Boston, Massachusetts (1908)
- Values by year: **1883: 156:11** | **1892: 127:50** | **1902: 102:50** | **1908: 102:50***  *(asterisk = flagged)*
- Flagged value: **102:50**, deviation 25.0 h from other-years median (127.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Charleston, South Carolina (1892)
- Values by year: **1882: 171:27** | **1883: 171:27** | **1892: 120:45*** | **1902: 120:00** | **1908: 120:00**  *(asterisk = flagged)*
- Flagged value: **120:45**, deviation 25.0 h from other-years median (145.72 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → New York, New York (1902)
- Values by year: **1882: 146:25** | **1883: 146:25** | **1892: 110:30** | **1902: 103:30*** | **1908: 102:30**  *(asterisk = flagged)*
- Flagged value: **103:30**, deviation 25.0 h from other-years median (128.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Boston, Massachusetts (1908)
- Values by year: **1882: 93:13** | **1883: 93:13** | **1892: 83:20** | **1902: 63:20** | **1908: 63:20***  *(asterisk = flagged)*
- Flagged value: **63:20**, deviation 24.9 h from other-years median (88.27 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Boston, Massachusetts (1902)
- Values by year: **1882: 93:13** | **1883: 93:13** | **1892: 83:20** | **1902: 63:20*** | **1908: 63:20**  *(asterisk = flagged)*
- Flagged value: **63:20**, deviation 24.9 h from other-years median (88.27 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → New York, New York (1892)
- Values by year: **1882: 79:25** | **1883: 79:25** | **1892: 54:30*** | **1902: 60:30**  *(asterisk = flagged)*
- Flagged value: **54:30**, deviation 24.9 h from other-years median (79.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pittsburgh, Pennsylvania → Omaha, Nebraska (1883)
- Values by year: **1882: 34:15** | **1883: 34:15*** | **1892: 84:00**  *(asterisk = flagged)*
- Flagged value: **34:15**, deviation 24.9 h from other-years median (59.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pittsburgh, Pennsylvania → Omaha, Nebraska (1882)
- Values by year: **1882: 34:15*** | **1883: 34:15** | **1892: 84:00**  *(asterisk = flagged)*
- Flagged value: **34:15**, deviation 24.9 h from other-years median (59.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Illinois → San Francisco, California (1902)
- Values by year: **1882: 117:25** | **1883: 117:25** | **1892: 85:15** | **1902: 76:35*** | **1908: 77:35**  *(asterisk = flagged)*
- Flagged value: **76:35**, deviation 24.8 h from other-years median (101.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 94:30** | **1883: 94:30** | **1892: 69:50*** | **1902: 61:50**  *(asterisk = flagged)*
- Flagged value: **69:50**, deviation 24.7 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 84:30** | **1883: 84:30** | **1892: 73:10** | **1902: 54:10*** | **1908: 54:10**  *(asterisk = flagged)*
- Flagged value: **54:10**, deviation 24.7 h from other-years median (78.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 84:30** | **1883: 84:30** | **1892: 73:10** | **1902: 54:10** | **1908: 54:10***  *(asterisk = flagged)*
- Flagged value: **54:10**, deviation 24.7 h from other-years median (78.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Des Moines, Iowa → San Francisco, California (1908)
- Values by year: **1882: 106:44** | **1883: 106:44** | **1892: 72:15** | **1902: 60:45** | **1908: 64:53***  *(asterisk = flagged)*
- Flagged value: **64:53**, deviation 24.6 h from other-years median (89.49 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Washington, District of Columbia (1908)
- Values by year: **1882: 145:45** | **1883: 145:45** | **1892: 106:55** | **1902: 101:55** | **1908: 101:55***  *(asterisk = flagged)*
- Flagged value: **101:55**, deviation 24.4 h from other-years median (126.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Washington, District of Columbia (1902)
- Values by year: **1882: 145:45** | **1883: 145:45** | **1892: 106:55** | **1902: 101:55*** | **1908: 101:55**  *(asterisk = flagged)*
- Flagged value: **101:55**, deviation 24.4 h from other-years median (126.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → San Francisco, California (1892)
- Values by year: **1882: 167:25** | **1883: 167:25** | **1892: 101:15*** | **1902: 83:45** | **1908: 82:28**  *(asterisk = flagged)*
- Flagged value: **101:15**, deviation 24.3 h from other-years median (125.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 147:05** | **1883: 147:05** | **1892: 110:40** | **1902: 104:40*** | **1908: 104:40**  *(asterisk = flagged)*
- Flagged value: **104:40**, deviation 24.2 h from other-years median (128.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 147:05** | **1883: 147:05** | **1892: 110:40** | **1902: 104:40** | **1908: 104:40***  *(asterisk = flagged)*
- Flagged value: **104:40**, deviation 24.2 h from other-years median (128.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Pittsburgh, Pennsylvania (1892)
- Values by year: **1883: 164:15** | **1892: 109:00*** | **1902: 102:00**  *(asterisk = flagged)*
- Flagged value: **109:00**, deviation 24.1 h from other-years median (133.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Philadelphia, Pennsylvania (1902)
- Values by year: **1883: 146:33** | **1892: 118:00** | **1902: 94:00*** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **94:00**, deviation 24.0 h from other-years median (118.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Philadelphia, Pennsylvania (1892)
- Values by year: **1883: 146:33** | **1892: 118:00*** | **1902: 94:00** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **118:00**, deviation 24.0 h from other-years median (94.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 132:30** | **1883: 132:30** | **1892: 108:30*** | **1902: 90:39**  *(asterisk = flagged)*
- Flagged value: **108:30**, deviation 24.0 h from other-years median (132.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Philadelphia, Pennsylvania (1908)
- Values by year: **1883: 146:33** | **1892: 118:00** | **1902: 94:00** | **1908: 94:00***  *(asterisk = flagged)*
- Flagged value: **94:00**, deviation 24.0 h from other-years median (118.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Saint Louis, Missouri (1908)
- Values by year: **1882: 128:22** | **1883: 128:22** | **1892: 86:30** | **1902: 83:30** | **1908: 83:30***  *(asterisk = flagged)*
- Flagged value: **83:30**, deviation 23.9 h from other-years median (107.43 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Saint Louis, Missouri (1902)
- Values by year: **1882: 128:22** | **1883: 128:22** | **1892: 86:30** | **1902: 83:30*** | **1908: 83:30**  *(asterisk = flagged)*
- Flagged value: **83:30**, deviation 23.9 h from other-years median (107.43 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Manchester, New Hampshire → Chicago, Illinois (1892)
- Values by year: **1892: 33:15*** | **1902: 82:15** | **1908: 32:00**  *(asterisk = flagged)*
- Flagged value: **33:15**, deviation 23.9 h from other-years median (57.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Chicago, Illinois (1902)
- Values by year: **1882: 79:45** | **1883: 79:45** | **1892: 58:48** | **1902: 45:30*** | **1908: 45:30**  *(asterisk = flagged)*
- Flagged value: **45:30**, deviation 23.8 h from other-years median (69.28 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Chicago, Illinois (1908)
- Values by year: **1882: 79:45** | **1883: 79:45** | **1892: 58:48** | **1902: 45:30** | **1908: 45:30***  *(asterisk = flagged)*
- Flagged value: **45:30**, deviation 23.8 h from other-years median (69.28 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Illinois → San Francisco, California (1908)
- Values by year: **1882: 117:25** | **1883: 117:25** | **1892: 85:15** | **1902: 76:35** | **1908: 77:35***  *(asterisk = flagged)*
- Flagged value: **77:35**, deviation 23.8 h from other-years median (101.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → San Francisco, California (1892)
- Values by year: **1882: 116:27** | **1883: 116:27** | **1892: 92:45*** | **1902: 96:15**  *(asterisk = flagged)*
- Flagged value: **92:45**, deviation 23.7 h from other-years median (116.45 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Trenton, New Jersey → Charleston, South Carolina (1892)
- Values by year: **1882: 33:30** | **1883: 33:30** | **1892: 52:31*** | **1902: 24:17** | **1908: 24:17**  *(asterisk = flagged)*
- Flagged value: **52:31**, deviation 23.6 h from other-years median (28.89 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Boston, Massachusetts (1892)
- Values by year: **1882: 72:13** | **1883: 72:13** | **1892: 36:30*** | **1902: 48:00** | **1908: 43:00**  *(asterisk = flagged)*
- Flagged value: **36:30**, deviation 23.6 h from other-years median (60.11 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → San Francisco, California (1908)
- Values by year: **1882: 125:34** | **1883: 125:34** | **1892: 88:15** | **1902: 85:45** | **1908: 83:28***  *(asterisk = flagged)*
- Flagged value: **83:28**, deviation 23.4 h from other-years median (106.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → San Francisco, California (1892)
- Values by year: **1882: 202:35** | **1883: 202:35** | **1892: 139:15*** | **1902: 122:45** | **1908: 122:28**  *(asterisk = flagged)*
- Flagged value: **139:15**, deviation 23.4 h from other-years median (162.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Omaha, Nebraska (1892)
- Values by year: **1882: 69:18** | **1883: 69:18** | **1892: 26:30*** | **1902: 30:30** | **1908: 30:30**  *(asterisk = flagged)*
- Flagged value: **26:30**, deviation 23.4 h from other-years median (49.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Boston, Massachusetts (1892)
- Values by year: **1882: 161:10** | **1883: 161:10** | **1892: 111:30*** | **1902: 108:30** | **1908: 107:30**  *(asterisk = flagged)*
- Flagged value: **111:30**, deviation 23.3 h from other-years median (134.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → Omaha, Nebraska (1908)
- Values by year: **1882: 73:37** | **1883: 73:37** | **1892: 67:00** | **1902: 47:00** | **1908: 47:00***  *(asterisk = flagged)*
- Flagged value: **47:00**, deviation 23.3 h from other-years median (70.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → Omaha, Nebraska (1902)
- Values by year: **1882: 73:37** | **1883: 73:37** | **1892: 67:00** | **1902: 47:00*** | **1908: 47:00**  *(asterisk = flagged)*
- Flagged value: **47:00**, deviation 23.3 h from other-years median (70.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hannibal, Missouri → San Francisco, California (1902)
- Values by year: **1882: 121:34** | **1883: 121:34** | **1892: 84:15** | **1902: 79:45*** | **1908: 79:45**  *(asterisk = flagged)*
- Flagged value: **79:45**, deviation 23.2 h from other-years median (102.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hannibal, Missouri → San Francisco, California (1908)
- Values by year: **1882: 121:34** | **1883: 121:34** | **1892: 84:15** | **1902: 79:45** | **1908: 79:45***  *(asterisk = flagged)*
- Flagged value: **79:45**, deviation 23.2 h from other-years median (102.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → New York, New York (1892)
- Values by year: **1892: 124:55*** | **1902: 102:00** | **1908: 102:00**  *(asterisk = flagged)*
- Flagged value: **124:55**, deviation 22.9 h from other-years median (102.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → San Francisco, California (1908)
- Values by year: **1882: 97:01** | **1883: 97:01** | **1892: 68:15** | **1902: 60:45** | **1908: 59:45***  *(asterisk = flagged)*
- Flagged value: **59:45**, deviation 22.9 h from other-years median (82.63 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → San Francisco, California (1892)
- Values by year: **1882: 164:53** | **1883: 164:53** | **1892: 102:15*** | **1902: 84:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **102:15**, deviation 22.6 h from other-years median (124.81 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → San Francisco, California (1892)
- Values by year: **1882: 196:50** | **1883: 196:50** | **1892: 138:15*** | **1902: 124:45** | **1908: 122:45**  *(asterisk = flagged)*
- Flagged value: **138:15**, deviation 22.5 h from other-years median (160.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → San Francisco, California (1908)
- Values by year: **1882: 150:20** | **1883: 150:20** | **1892: 108:15** | **1902: 95:45** | **1908: 106:45***  *(asterisk = flagged)*
- Flagged value: **106:45**, deviation 22.5 h from other-years median (129.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Chicago, Illinois (1892)
- Values by year: **1882: 141:25** | **1883: 141:25** | **1892: 90:25*** | **1902: 84:30** | **1908: 84:30**  *(asterisk = flagged)*
- Flagged value: **90:25**, deviation 22.5 h from other-years median (112.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Little Rock, Arkansas → San Francisco, California (1908)
- Values by year: **1882: 131:26** | **1883: 131:28** | **1892: 102:15** | **1902: 94:35** | **1908: 94:35***  *(asterisk = flagged)*
- Flagged value: **94:35**, deviation 22.3 h from other-years median (116.84 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Little Rock, Arkansas → San Francisco, California (1902)
- Values by year: **1882: 131:26** | **1883: 131:28** | **1892: 102:15** | **1902: 94:35*** | **1908: 94:35**  *(asterisk = flagged)*
- Flagged value: **94:35**, deviation 22.3 h from other-years median (116.84 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Maine → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 31:15** | **1883: 31:15** | **1892: 53:30*** | **1902: 25:30**  *(asterisk = flagged)*
- Flagged value: **53:30**, deviation 22.2 h from other-years median (31.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → San Francisco, California (1892)
- Values by year: **1882: 197:00** | **1883: 197:00** | **1892: 138:45*** | **1902: 124:45** | **1908: 124:45**  *(asterisk = flagged)*
- Flagged value: **138:45**, deviation 22.1 h from other-years median (160.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Chicago, Illinois (1892)
- Values by year: **1882: 119:50** | **1883: 119:50** | **1892: 82:40*** | **1902: 89:40** | **1908: 89:40**  *(asterisk = flagged)*
- Flagged value: **82:40**, deviation 22.1 h from other-years median (104.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rock Island, Illinois → San Francisco, California (1902)
- Values by year: **1882: 116:39** | **1883: 116:39** | **1892: 80:15** | **1902: 76:25*** | **1908: 79:25**  *(asterisk = flagged)*
- Flagged value: **76:25**, deviation 22.0 h from other-years median (98.45 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Charleston, South Carolina (1902)
- Values by year: **1882: 143:02** | **1883: 143:02** | **1892: 115:00** | **1902: 107:00*** | **1908: 107:00**  *(asterisk = flagged)*
- Flagged value: **107:00**, deviation 22.0 h from other-years median (129.01 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Charleston, South Carolina (1908)
- Values by year: **1882: 143:02** | **1883: 143:02** | **1892: 115:00** | **1902: 107:00** | **1908: 107:00***  *(asterisk = flagged)*
- Flagged value: **107:00**, deviation 22.0 h from other-years median (129.01 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Baltimore, Maryland (1902)
- Values by year: **1883: 149:08** | **1892: 116:30** | **1902: 94:30*** | **1908: 94:30**  *(asterisk = flagged)*
- Flagged value: **94:30**, deviation 22.0 h from other-years median (116.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Baltimore, Maryland (1908)
- Values by year: **1883: 149:08** | **1892: 116:30** | **1902: 94:30** | **1908: 94:30***  *(asterisk = flagged)*
- Flagged value: **94:30**, deviation 22.0 h from other-years median (116.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Baltimore, Maryland (1892)
- Values by year: **1883: 149:08** | **1892: 116:30*** | **1902: 94:30** | **1908: 94:30**  *(asterisk = flagged)*
- Flagged value: **116:30**, deviation 22.0 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → San Francisco, California (1902)
- Values by year: **1882: 97:01** | **1883: 97:01** | **1892: 68:15** | **1902: 60:45*** | **1908: 59:45**  *(asterisk = flagged)*
- Flagged value: **60:45**, deviation 21.9 h from other-years median (82.63 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Saint Louis, Missouri (1892)
- Values by year: **1882: 83:10** | **1883: 83:10** | **1892: 49:25*** | **1902: 59:25** | **1908: 59:25**  *(asterisk = flagged)*
- Flagged value: **49:25**, deviation 21.9 h from other-years median (71.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Philadelphia, Pennsylvania (1892)
- Values by year: **1892: 124:10*** | **1902: 102:25** | **1908: 102:25**  *(asterisk = flagged)*
- Flagged value: **124:10**, deviation 21.8 h from other-years median (102.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Washington, District of Columbia (1892)
- Values by year: **1882: 108:52** | **1883: 108:52** | **1892: 71:00*** | **1902: 76:00** | **1908: 76:00**  *(asterisk = flagged)*
- Flagged value: **71:00**, deviation 21.4 h from other-years median (92.43 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → Charleston, South Carolina (1902)
- Values by year: **1882: 72:06** | **1883: 72:08** | **1892: 50:45** | **1902: 50:45***  *(asterisk = flagged)*
- Flagged value: **50:45**, deviation 21.4 h from other-years median (72.10 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → Charleston, South Carolina (1892)
- Values by year: **1882: 72:06** | **1883: 72:08** | **1892: 50:45*** | **1902: 50:45**  *(asterisk = flagged)*
- Flagged value: **50:45**, deviation 21.4 h from other-years median (72.10 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Pittsburgh, Pennsylvania (1902)
- Values by year: **1892: 113:15** | **1902: 91:55***  *(asterisk = flagged)*
- Flagged value: **91:55**, deviation 21.3 h from other-years median (113.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Pittsburgh, Pennsylvania (1892)
- Values by year: **1892: 113:15*** | **1902: 91:55**  *(asterisk = flagged)*
- Flagged value: **113:15**, deviation 21.3 h from other-years median (91.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Charleston, South Carolina (1892)
- Values by year: **1882: 92:29** | **1883: 92:59** | **1892: 50:00*** | **1902: 50:00** | **1908: 50:00**  *(asterisk = flagged)*
- Flagged value: **50:00**, deviation 21.2 h from other-years median (71.24 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Charleston, South Carolina (1908)
- Values by year: **1882: 92:29** | **1883: 92:59** | **1892: 50:00** | **1902: 50:00** | **1908: 50:00***  *(asterisk = flagged)*
- Flagged value: **50:00**, deviation 21.2 h from other-years median (71.24 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Charleston, South Carolina (1902)
- Values by year: **1882: 92:29** | **1883: 92:59** | **1892: 50:00** | **1902: 50:00*** | **1908: 50:00**  *(asterisk = flagged)*
- Flagged value: **50:00**, deviation 21.2 h from other-years median (71.24 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Charleston, South Carolina (1902)
- Values by year: **1882: 98:59** | **1883: 98:59** | **1892: 77:45** | **1902: 77:45***  *(asterisk = flagged)*
- Flagged value: **77:45**, deviation 21.2 h from other-years median (98.98 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Charleston, South Carolina (1892)
- Values by year: **1882: 98:59** | **1883: 98:59** | **1892: 77:45*** | **1902: 77:45**  *(asterisk = flagged)*
- Flagged value: **77:45**, deviation 21.2 h from other-years median (98.98 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → San Francisco, California (1902)
- Values by year: **1882: 125:34** | **1883: 125:34** | **1892: 88:15** | **1902: 85:45*** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **85:45**, deviation 21.2 h from other-years median (106.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Washington, District of Columbia (1892)
- Values by year: **1882: 59:12** | **1883: 59:12** | **1892: 76:30*** | **1902: 51:30** | **1908: 51:30**  *(asterisk = flagged)*
- Flagged value: **76:30**, deviation 21.1 h from other-years median (55.35 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Washington, District of Columbia (1908)
- Values by year: **1882: 120:02** | **1883: 120:02** | **1892: 100:00** | **1902: 89:00** | **1908: 89:00***  *(asterisk = flagged)*
- Flagged value: **89:00**, deviation 21.0 h from other-years median (110.02 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Washington, District of Columbia (1902)
- Values by year: **1882: 120:02** | **1883: 120:02** | **1892: 100:00** | **1902: 89:00*** | **1908: 89:00**  *(asterisk = flagged)*
- Flagged value: **89:00**, deviation 21.0 h from other-years median (110.02 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Washington, District of Columbia (1892)
- Values by year: **1882: 75:00** | **1883: 75:00** | **1892: 54:00*** | **1902: 62:00**  *(asterisk = flagged)*
- Flagged value: **54:00**, deviation 21.0 h from other-years median (75.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### West Point, New York → Omaha, Nebraska (1892)
- Values by year: **1882: 65:32** | **1883: 65:32** | **1892: 44:45***  *(asterisk = flagged)*
- Flagged value: **44:45**, deviation 20.8 h from other-years median (65.53 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → New York, New York (1892)
- Values by year: **1882: 169:05** | **1883: 169:05** | **1892: 121:00*** | **1902: 114:00** | **1908: 114:00**  *(asterisk = flagged)*
- Flagged value: **121:00**, deviation 20.5 h from other-years median (141.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 107:35** | **1883: 107:35** | **1892: 86:40** | **1902: 76:40** | **1908: 76:40***  *(asterisk = flagged)*
- Flagged value: **76:40**, deviation 20.5 h from other-years median (97.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 107:35** | **1883: 107:35** | **1892: 86:40** | **1902: 76:40*** | **1908: 76:40**  *(asterisk = flagged)*
- Flagged value: **76:40**, deviation 20.5 h from other-years median (97.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → San Francisco, California (1892)
- Values by year: **1882: 150:20** | **1883: 150:20** | **1892: 108:15*** | **1902: 95:45** | **1908: 106:45**  *(asterisk = flagged)*
- Flagged value: **108:15**, deviation 20.3 h from other-years median (128.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Boston, Massachusetts (1908)
- Values by year: **1882: 65:31** | **1883: 65:31** | **1892: 48:00** | **1902: 49:00** | **1908: 37:00***  *(asterisk = flagged)*
- Flagged value: **37:00**, deviation 20.3 h from other-years median (57.26 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Smith, Arkansas → Charleston, South Carolina (1883)
- Values by year: **1882: 57:32** | **1883: 57:32*** | **1892: 78:45** | **1902: 78:45** | **1908: 76:45**  *(asterisk = flagged)*
- Flagged value: **57:32**, deviation 20.2 h from other-years median (77.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Smith, Arkansas → Charleston, South Carolina (1882)
- Values by year: **1882: 57:32*** | **1883: 57:32** | **1892: 78:45** | **1902: 78:45** | **1908: 76:45**  *(asterisk = flagged)*
- Flagged value: **57:32**, deviation 20.2 h from other-years median (77.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Staunton, Virginia → Charleston, South Carolina (1892)
- Values by year: **1882: 31:35** | **1883: 31:35** | **1892: 44:00*** | **1902: 16:00** | **1908: 16:00**  *(asterisk = flagged)*
- Flagged value: **44:00**, deviation 20.2 h from other-years median (23.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Cincinnati, Ohio (1902)
- Values by year: **1882: 119:55** | **1883: 119:55** | **1892: 101:30** | **1902: 90:30*** | **1908: 90:30**  *(asterisk = flagged)*
- Flagged value: **90:30**, deviation 20.2 h from other-years median (110.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Cincinnati, Ohio (1908)
- Values by year: **1882: 119:55** | **1883: 119:55** | **1892: 101:30** | **1902: 90:30** | **1908: 90:30***  *(asterisk = flagged)*
- Flagged value: **90:30**, deviation 20.2 h from other-years median (110.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → San Francisco, California (1902)
- Values by year: **1882: 116:27** | **1883: 116:27** | **1892: 92:45** | **1902: 96:15***  *(asterisk = flagged)*
- Flagged value: **96:15**, deviation 20.2 h from other-years median (116.45 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → San Francisco, California (1892)
- Values by year: **1882: 186:00** | **1883: 186:00** | **1892: 131:45*** | **1902: 117:45** | **1908: 115:45**  *(asterisk = flagged)*
- Flagged value: **131:45**, deviation 20.1 h from other-years median (151.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → Omaha, Nebraska (1908)
- Values by year: **1882: 73:10** | **1883: 73:10** | **1892: 73:00** | **1902: 53:00** | **1908: 53:00***  *(asterisk = flagged)*
- Flagged value: **53:00**, deviation 20.1 h from other-years median (73.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → Omaha, Nebraska (1902)
- Values by year: **1882: 73:10** | **1883: 73:10** | **1892: 73:00** | **1902: 53:00*** | **1908: 53:00**  *(asterisk = flagged)*
- Flagged value: **53:00**, deviation 20.1 h from other-years median (73.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Philadelphia, Pennsylvania (1892)
- Values by year: **1882: 166:05** | **1883: 166:05** | **1892: 119:00*** | **1902: 112:00** | **1908: 112:00**  *(asterisk = flagged)*
- Flagged value: **119:00**, deviation 20.0 h from other-years median (139.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Washington, District of Columbia (1902)
- Values by year: **1883: 148:58** | **1892: 115:20** | **1902: 95:20*** | **1908: 95:20**  *(asterisk = flagged)*
- Flagged value: **95:20**, deviation 20.0 h from other-years median (115.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Charleston, South Carolina (1892)
- Values by year: **1883: 189:45** | **1892: 125:15*** | **1902: 105:15** | **1908: 105:15**  *(asterisk = flagged)*
- Flagged value: **125:15**, deviation 20.0 h from other-years median (105.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Charleston, South Carolina (1902)
- Values by year: **1883: 189:45** | **1892: 125:15** | **1902: 105:15*** | **1908: 105:15**  *(asterisk = flagged)*
- Flagged value: **105:15**, deviation 20.0 h from other-years median (125.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Charleston, South Carolina (1908)
- Values by year: **1883: 189:45** | **1892: 125:15** | **1902: 105:15** | **1908: 105:15***  *(asterisk = flagged)*
- Flagged value: **105:15**, deviation 20.0 h from other-years median (125.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Saint Louis, Missouri (1902)
- Values by year: **1883: 112:20** | **1892: 85:30** | **1902: 65:30*** | **1908: 65:30**  *(asterisk = flagged)*
- Flagged value: **65:30**, deviation 20.0 h from other-years median (85.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Saint Louis, Missouri (1908)
- Values by year: **1883: 112:20** | **1892: 85:30** | **1902: 65:30** | **1908: 65:30***  *(asterisk = flagged)*
- Flagged value: **65:30**, deviation 20.0 h from other-years median (85.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Washington, District of Columbia (1892)
- Values by year: **1883: 148:58** | **1892: 115:20*** | **1902: 95:20** | **1908: 95:20**  *(asterisk = flagged)*
- Flagged value: **115:20**, deviation 20.0 h from other-years median (95.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Washington, District of Columbia (1908)
- Values by year: **1883: 148:58** | **1892: 115:20** | **1902: 95:20** | **1908: 95:20***  *(asterisk = flagged)*
- Flagged value: **95:20**, deviation 20.0 h from other-years median (115.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Saint Louis, Missouri (1892)
- Values by year: **1883: 112:20** | **1892: 85:30*** | **1902: 65:30** | **1908: 65:30**  *(asterisk = flagged)*
- Flagged value: **85:30**, deviation 20.0 h from other-years median (65.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cleveland, Ohio → Charleston, South Carolina (1892)
- Values by year: **1882: 41:55** | **1883: 41:55** | **1892: 60:45*** | **1902: 39:45** | **1908: 39:45**  *(asterisk = flagged)*
- Flagged value: **60:45**, deviation 19.9 h from other-years median (40.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → Omaha, Nebraska (1902)
- Values by year: **1882: 106:35** | **1883: 106:35** | **1892: 73:00** | **1902: 70:00*** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **70:00**, deviation 19.8 h from other-years median (89.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → Omaha, Nebraska (1908)
- Values by year: **1882: 106:35** | **1883: 106:35** | **1892: 73:00** | **1902: 70:00** | **1908: 70:00***  *(asterisk = flagged)*
- Flagged value: **70:00**, deviation 19.8 h from other-years median (89.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 105:35** | **1883: 105:35** | **1892: 85:50*** | **1902: 75:50**  *(asterisk = flagged)*
- Flagged value: **85:50**, deviation 19.8 h from other-years median (105.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### St. Louis, Missouri → Charleston, South Carolina (1892)
- Values by year: **1882: 58:12** | **1883: 53:12** | **1892: 36:10***  *(asterisk = flagged)*
- Flagged value: **36:10**, deviation 19.5 h from other-years median (55.70 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Saint Louis, Missouri (1908)
- Values by year: **1882: 72:30** | **1883: 72:30** | **1892: 67:30** | **1902: 50:30** | **1908: 50:30***  *(asterisk = flagged)*
- Flagged value: **50:30**, deviation 19.5 h from other-years median (70.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Saint Louis, Missouri (1902)
- Values by year: **1882: 72:30** | **1883: 72:30** | **1892: 67:30** | **1902: 50:30*** | **1908: 50:30**  *(asterisk = flagged)*
- Flagged value: **50:30**, deviation 19.5 h from other-years median (70.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 117:25** | **1883: 117:25** | **1892: 102:55** | **1902: 97:55***  *(asterisk = flagged)*
- Flagged value: **97:55**, deviation 19.5 h from other-years median (117.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Saint Louis, Missouri (1892)
- Values by year: **1882: 128:22** | **1883: 128:22** | **1892: 86:30*** | **1902: 83:30** | **1908: 83:30**  *(asterisk = flagged)*
- Flagged value: **86:30**, deviation 19.4 h from other-years median (105.93 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Philadelphia, Pennsylvania (1892)
- Values by year: **1882: 77:05** | **1883: 77:05** | **1892: 57:40*** | **1902: 62:40**  *(asterisk = flagged)*
- Flagged value: **57:40**, deviation 19.4 h from other-years median (77.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Omaha, Nebraska (1902)
- Values by year: **1882: 69:18** | **1883: 69:18** | **1892: 26:30** | **1902: 30:30*** | **1908: 30:30**  *(asterisk = flagged)*
- Flagged value: **30:30**, deviation 19.4 h from other-years median (49.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Boston, Massachusetts (1902)
- Values by year: **1882: 97:08** | **1883: 97:08** | **1892: 79:50** | **1902: 69:05*** | **1908: 69:50**  *(asterisk = flagged)*
- Flagged value: **69:05**, deviation 19.4 h from other-years median (88.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Omaha, Nebraska (1908)
- Values by year: **1882: 69:18** | **1883: 69:18** | **1892: 26:30** | **1902: 30:30** | **1908: 30:30***  *(asterisk = flagged)*
- Flagged value: **30:30**, deviation 19.4 h from other-years median (49.90 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Frankfort, Kentucky → San Francisco, California (1892)
- Values by year: **1882: 147:30** | **1883: 147:30** | **1892: 96:15*** | **1902: 83:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **96:15**, deviation 19.4 h from other-years median (115.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 88:25** | **1883: 88:25** | **1892: 69:40** | **1902: 59:40*** | **1908: 59:40**  *(asterisk = flagged)*
- Flagged value: **59:40**, deviation 19.4 h from other-years median (79.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 88:25** | **1883: 88:25** | **1892: 69:40** | **1902: 59:40** | **1908: 59:40***  *(asterisk = flagged)*
- Flagged value: **59:40**, deviation 19.4 h from other-years median (79.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Boston, Massachusetts (1902)
- Values by year: **1882: 146:15** | **1883: 146:15** | **1892: 119:35** | **1902: 113:35*** | **1908: 113:35**  *(asterisk = flagged)*
- Flagged value: **113:35**, deviation 19.3 h from other-years median (132.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Boston, Massachusetts (1908)
- Values by year: **1882: 146:15** | **1883: 146:15** | **1892: 119:35** | **1902: 113:35** | **1908: 113:35***  *(asterisk = flagged)*
- Flagged value: **113:35**, deviation 19.3 h from other-years median (132.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Maine → Omaha, Nebraska (1908)
- Values by year: **1882: 70:35** | **1883: 70:35** | **1892: 64:00** | **1902: 48:00** | **1908: 48:00***  *(asterisk = flagged)*
- Flagged value: **48:00**, deviation 19.3 h from other-years median (67.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Maine → Omaha, Nebraska (1902)
- Values by year: **1882: 70:35** | **1883: 70:35** | **1892: 64:00** | **1902: 48:00*** | **1908: 48:00**  *(asterisk = flagged)*
- Flagged value: **48:00**, deviation 19.3 h from other-years median (67.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 67:05** | **1883: 67:05** | **1892: 47:50** | **1902: 47:50***  *(asterisk = flagged)*
- Flagged value: **47:50**, deviation 19.2 h from other-years median (67.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 67:05** | **1883: 67:05** | **1892: 47:50*** | **1902: 47:50**  *(asterisk = flagged)*
- Flagged value: **47:50**, deviation 19.2 h from other-years median (67.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rock Island, Illinois → San Francisco, California (1908)
- Values by year: **1882: 116:39** | **1883: 116:39** | **1892: 80:15** | **1902: 76:25** | **1908: 79:25***  *(asterisk = flagged)*
- Flagged value: **79:25**, deviation 19.0 h from other-years median (98.45 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Omaha, Nebraska (1908)
- Values by year: **1883: 109:00** | **1892: 89:00** | **1902: 70:00** | **1908: 70:00***  *(asterisk = flagged)*
- Flagged value: **70:00**, deviation 19.0 h from other-years median (89.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pueblo, Colorado → San Francisco, California (1908)
- Values by year: **1882: 82:15** | **1883: 82:15** | **1892: 75:15** | **1902: 59:45** | **1908: 59:45***  *(asterisk = flagged)*
- Flagged value: **59:45**, deviation 19.0 h from other-years median (78.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Omaha, Nebraska (1892)
- Values by year: **1883: 109:00** | **1892: 89:00*** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **89:00**, deviation 19.0 h from other-years median (70.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pueblo, Colorado → San Francisco, California (1902)
- Values by year: **1882: 82:15** | **1883: 82:15** | **1892: 75:15** | **1902: 59:45*** | **1908: 59:45**  *(asterisk = flagged)*
- Flagged value: **59:45**, deviation 19.0 h from other-years median (78.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Omaha, Nebraska (1902)
- Values by year: **1883: 109:00** | **1892: 89:00** | **1902: 70:00*** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **70:00**, deviation 19.0 h from other-years median (89.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → New York, New York (1902)
- Values by year: **1882: 79:25** | **1883: 79:25** | **1892: 54:30** | **1902: 60:30***  *(asterisk = flagged)*
- Flagged value: **60:30**, deviation 18.9 h from other-years median (79.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → New York, New York (1902)
- Values by year: **1882: 90:35** | **1883: 90:35** | **1892: 73:00** | **1902: 63:00*** | **1908: 63:00**  *(asterisk = flagged)*
- Flagged value: **63:00**, deviation 18.8 h from other-years median (81.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → New York, New York (1908)
- Values by year: **1882: 90:35** | **1883: 90:35** | **1892: 73:00** | **1902: 63:00** | **1908: 63:00***  *(asterisk = flagged)*
- Flagged value: **63:00**, deviation 18.8 h from other-years median (81.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albuquerque, New Mexico → San Francisco, California (1908)
- Values by year: **1892: 74:15** | **1902: 36:45** | **1908: 36:45***  *(asterisk = flagged)*
- Flagged value: **36:45**, deviation 18.8 h from other-years median (55.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albuquerque, New Mexico → San Francisco, California (1902)
- Values by year: **1892: 74:15** | **1902: 36:45*** | **1908: 36:45**  *(asterisk = flagged)*
- Flagged value: **36:45**, deviation 18.8 h from other-years median (55.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Baltimore, Maryland (1908)
- Values by year: **1882: 118:30** | **1883: 118:30** | **1892: 99:00** | **1902: 90:00** | **1908: 90:00***  *(asterisk = flagged)*
- Flagged value: **90:00**, deviation 18.8 h from other-years median (108.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Baltimore, Maryland (1902)
- Values by year: **1882: 118:30** | **1883: 118:30** | **1892: 99:00** | **1902: 90:00*** | **1908: 90:00**  *(asterisk = flagged)*
- Flagged value: **90:00**, deviation 18.8 h from other-years median (108.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Baltimore, Maryland (1908)
- Values by year: **1882: 107:20** | **1883: 107:20** | **1892: 80:00** | **1902: 75:00** | **1908: 75:00***  *(asterisk = flagged)*
- Flagged value: **75:00**, deviation 18.7 h from other-years median (93.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Baltimore, Maryland (1902)
- Values by year: **1882: 107:20** | **1883: 107:20** | **1892: 80:00** | **1902: 75:00*** | **1908: 75:00**  *(asterisk = flagged)*
- Flagged value: **75:00**, deviation 18.7 h from other-years median (93.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Boston, Massachusetts (1908)
- Values by year: **1882: 97:08** | **1883: 97:08** | **1892: 79:50** | **1902: 69:05** | **1908: 69:50***  *(asterisk = flagged)*
- Flagged value: **69:50**, deviation 18.6 h from other-years median (88.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → Charleston, South Carolina (1902)
- Values by year: **1882: 78:59** | **1883: 78:50** | **1892: 60:15** | **1902: 60:15***  *(asterisk = flagged)*
- Flagged value: **60:15**, deviation 18.6 h from other-years median (78.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → Charleston, South Carolina (1892)
- Values by year: **1882: 78:59** | **1883: 78:50** | **1892: 60:15*** | **1902: 60:15**  *(asterisk = flagged)*
- Flagged value: **60:15**, deviation 18.6 h from other-years median (78.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → New York, New York (1902)
- Values by year: **1882: 117:35** | **1883: 117:35** | **1892: 96:30** | **1902: 88:30*** | **1908: 88:30**  *(asterisk = flagged)*
- Flagged value: **88:30**, deviation 18.5 h from other-years median (107.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → New York, New York (1908)
- Values by year: **1882: 117:35** | **1883: 117:35** | **1892: 96:30** | **1902: 88:30** | **1908: 88:30***  *(asterisk = flagged)*
- Flagged value: **88:30**, deviation 18.5 h from other-years median (107.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 77:19** | **1883: 77:19** | **1892: 58:50** | **1902: 58:50***  *(asterisk = flagged)*
- Flagged value: **58:50**, deviation 18.5 h from other-years median (77.32 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 77:19** | **1883: 77:19** | **1892: 58:50*** | **1902: 58:50**  *(asterisk = flagged)*
- Flagged value: **58:50**, deviation 18.5 h from other-years median (77.32 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Saint Louis, Missouri (1902)
- Values by year: **1882: 53:10** | **1883: 53:10** | **1892: 16:20** | **1902: 16:20*** | **1908: 16:20**  *(asterisk = flagged)*
- Flagged value: **16:20**, deviation 18.4 h from other-years median (34.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Saint Louis, Missouri (1892)
- Values by year: **1882: 53:10** | **1883: 53:10** | **1892: 16:20*** | **1902: 16:20** | **1908: 16:20**  *(asterisk = flagged)*
- Flagged value: **16:20**, deviation 18.4 h from other-years median (34.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Saint Louis, Missouri (1908)
- Values by year: **1882: 53:10** | **1883: 53:10** | **1892: 16:20** | **1902: 16:20** | **1908: 16:20***  *(asterisk = flagged)*
- Flagged value: **16:20**, deviation 18.4 h from other-years median (34.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → Washington, District of Columbia (1883)
- Values by year: **1883: 44:00*** | **1892: 62:20** | **1902: 62:20** | **1908: 62:20**  *(asterisk = flagged)*
- Flagged value: **44:00**, deviation 18.3 h from other-years median (62.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Baltimore, Maryland (1892)
- Values by year: **1882: 76:10** | **1883: 76:10** | **1892: 58:00*** | **1902: 61:00**  *(asterisk = flagged)*
- Flagged value: **58:00**, deviation 18.2 h from other-years median (76.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Chicago, Illinois (1902)
- Values by year: **1882: 48:50** | **1883: 48:50** | **1892: 15:30** | **1902: 14:00*** | **1908: 14:00**  *(asterisk = flagged)*
- Flagged value: **14:00**, deviation 18.2 h from other-years median (32.16 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Chicago, Illinois (1908)
- Values by year: **1882: 48:50** | **1883: 48:50** | **1892: 15:30** | **1902: 14:00** | **1908: 14:00***  *(asterisk = flagged)*
- Flagged value: **14:00**, deviation 18.2 h from other-years median (32.16 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 33:50** | **1883: 33:50** | **1892: 15:40*** | **1902: 15:40**  *(asterisk = flagged)*
- Flagged value: **15:40**, deviation 18.2 h from other-years median (33.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 33:50** | **1883: 33:50** | **1892: 15:40** | **1902: 15:40***  *(asterisk = flagged)*
- Flagged value: **15:40**, deviation 18.2 h from other-years median (33.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Baltimore, Maryland (1908)
- Values by year: **1882: 84:10** | **1883: 84:10** | **1892: 72:00** | **1902: 60:00** | **1908: 60:00***  *(asterisk = flagged)*
- Flagged value: **60:00**, deviation 18.1 h from other-years median (78.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Baltimore, Maryland (1902)
- Values by year: **1882: 84:10** | **1883: 84:10** | **1892: 72:00** | **1902: 60:00*** | **1908: 60:00**  *(asterisk = flagged)*
- Flagged value: **60:00**, deviation 18.1 h from other-years median (78.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 118:35** | **1883: 118:35** | **1892: 96:25** | **1902: 89:25*** | **1908: 89:25**  *(asterisk = flagged)*
- Flagged value: **89:25**, deviation 18.1 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 118:35** | **1883: 118:35** | **1892: 96:25** | **1902: 89:25** | **1908: 89:25***  *(asterisk = flagged)*
- Flagged value: **89:25**, deviation 18.1 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → San Francisco, California (1892)
- Values by year: **1882: 162:29** | **1883: 162:20** | **1892: 112:00*** | **1902: 97:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **112:00**, deviation 18.0 h from other-years median (130.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Cincinnati, Ohio (1902)
- Values by year: **1883: 125:05** | **1892: 102:50** | **1902: 84:50*** | **1908: 84:50**  *(asterisk = flagged)*
- Flagged value: **84:50**, deviation 18.0 h from other-years median (102.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Cincinnati, Ohio (1892)
- Values by year: **1883: 125:05** | **1892: 102:50*** | **1902: 84:50** | **1908: 84:50**  *(asterisk = flagged)*
- Flagged value: **102:50**, deviation 18.0 h from other-years median (84.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Las Cruces, New Mexico → Charleston, South Carolina (1892)
- Values by year: **1892: 121:45*** | **1902: 103:45** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **121:45**, deviation 18.0 h from other-years median (103.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Cincinnati, Ohio (1908)
- Values by year: **1883: 125:05** | **1892: 102:50** | **1902: 84:50** | **1908: 84:50***  *(asterisk = flagged)*
- Flagged value: **84:50**, deviation 18.0 h from other-years median (102.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Cincinnati, Ohio (1902)
- Values by year: **1883: 151:40** | **1892: 120:50** | **1902: 103:00*** | **1908: 103:00**  *(asterisk = flagged)*
- Flagged value: **103:00**, deviation 17.8 h from other-years median (120.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Cincinnati, Ohio (1908)
- Values by year: **1883: 151:40** | **1892: 120:50** | **1902: 103:00** | **1908: 103:00***  *(asterisk = flagged)*
- Flagged value: **103:00**, deviation 17.8 h from other-years median (120.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Cincinnati, Ohio (1892)
- Values by year: **1883: 151:40** | **1892: 120:50*** | **1902: 103:00** | **1908: 103:00**  *(asterisk = flagged)*
- Flagged value: **120:50**, deviation 17.8 h from other-years median (103.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Henderson, Kentucky → San Francisco, California (1908)
- Values by year: **1882: 124:00** | **1883: 124:00** | **1892: 90:15** | **1902: 89:45** | **1908: 89:20***  *(asterisk = flagged)*
- Flagged value: **89:20**, deviation 17.8 h from other-years median (107.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → Omaha, Nebraska (1908)
- Values by year: **1882: 65:35** | **1883: 65:35** | **1892: 50:00** | **1902: 40:00** | **1908: 40:00***  *(asterisk = flagged)*
- Flagged value: **40:00**, deviation 17.8 h from other-years median (57.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → Omaha, Nebraska (1902)
- Values by year: **1882: 65:35** | **1883: 65:35** | **1892: 50:00** | **1902: 40:00*** | **1908: 40:00**  *(asterisk = flagged)*
- Flagged value: **40:00**, deviation 17.8 h from other-years median (57.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rock Island, Illinois → San Francisco, California (1892)
- Values by year: **1882: 116:39** | **1883: 116:39** | **1892: 80:15*** | **1902: 76:25** | **1908: 79:25**  *(asterisk = flagged)*
- Flagged value: **80:15**, deviation 17.8 h from other-years median (98.03 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 34:46** | **1883: 34:46** | **1892: 17:00*** | **1902: 17:00**  *(asterisk = flagged)*
- Flagged value: **17:00**, deviation 17.8 h from other-years median (34.77 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 34:46** | **1883: 34:46** | **1892: 17:00** | **1902: 17:00***  *(asterisk = flagged)*
- Flagged value: **17:00**, deviation 17.8 h from other-years median (34.77 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 68:30** | **1883: 68:30** | **1892: 41:50** | **1902: 50:50***  *(asterisk = flagged)*
- Flagged value: **50:50**, deviation 17.7 h from other-years median (68.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Baltimore, Maryland (1908)
- Values by year: **1882: 47:20** | **1883: 47:20** | **1892: 36:00** | **1902: 32:00** | **1908: 24:00***  *(asterisk = flagged)*
- Flagged value: **24:00**, deviation 17.7 h from other-years median (41.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Memphis, Tennessee → San Francisco, California (1892)
- Values by year: **1882: 145:00** | **1883: 145:00** | **1892: 99:15*** | **1902: 88:45** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **99:15**, deviation 17.6 h from other-years median (116.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Concord, New Hampshire → San Francisco, California (1892)
- Values by year: **1882: 166:00** | **1883: 166:00** | **1892: 118:15*** | **1902: 105:45** | **1908: 105:45**  *(asterisk = flagged)*
- Flagged value: **118:15**, deviation 17.6 h from other-years median (135.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Shreveport, Louisiana → San Francisco, California (1892)
- Values by year: **1882: 147:46** | **1883: 147:46** | **1892: 106:15*** | **1902: 99:55** | **1908: 99:55**  *(asterisk = flagged)*
- Flagged value: **106:15**, deviation 17.6 h from other-years median (123.84 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Frankfort, Kentucky → Omaha, Nebraska (1902)
- Values by year: **1882: 47:35** | **1883: 47:35** | **1892: 30:15** | **1902: 30:00*** | **1908: 80:00**  *(asterisk = flagged)*
- Flagged value: **30:00**, deviation 17.6 h from other-years median (47.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Chicago, Illinois (1908)
- Values by year: **1882: 90:50** | **1883: 90:50** | **1892: 67:50** | **1902: 61:50** | **1908: 61:50***  *(asterisk = flagged)*
- Flagged value: **61:50**, deviation 17.5 h from other-years median (79.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Baltimore, Maryland (1892)
- Values by year: **1882: 166:00** | **1883: 166:00** | **1892: 121:00*** | **1902: 111:00** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **121:00**, deviation 17.5 h from other-years median (138.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hot Springs, Arkansas → San Francisco, California (1902)
- Values by year: **1883: 135:28** | **1892: 108:15** | **1902: 90:45*** | **1908: 90:45**  *(asterisk = flagged)*
- Flagged value: **90:45**, deviation 17.5 h from other-years median (108.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hot Springs, Arkansas → San Francisco, California (1892)
- Values by year: **1883: 135:28** | **1892: 108:15*** | **1902: 90:45** | **1908: 90:45**  *(asterisk = flagged)*
- Flagged value: **108:15**, deviation 17.5 h from other-years median (90.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Chicago, Illinois (1902)
- Values by year: **1882: 90:50** | **1883: 90:50** | **1892: 67:50** | **1902: 61:50*** | **1908: 61:50**  *(asterisk = flagged)*
- Flagged value: **61:50**, deviation 17.5 h from other-years median (79.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hot Springs, Arkansas → San Francisco, California (1908)
- Values by year: **1883: 135:28** | **1892: 108:15** | **1902: 90:45** | **1908: 90:45***  *(asterisk = flagged)*
- Flagged value: **90:45**, deviation 17.5 h from other-years median (108.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → San Francisco, California (1892)
- Values by year: **1882: 125:34** | **1883: 125:34** | **1892: 88:15*** | **1902: 85:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **88:15**, deviation 17.4 h from other-years median (105.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Henderson, Kentucky → San Francisco, California (1902)
- Values by year: **1882: 124:00** | **1883: 124:00** | **1892: 90:15** | **1902: 89:45*** | **1908: 89:20**  *(asterisk = flagged)*
- Flagged value: **89:45**, deviation 17.4 h from other-years median (107.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → New York, New York (1892)
- Values by year: **1882: 57:40** | **1883: 57:40** | **1892: 32:00*** | **1902: 41:00** | **1908: 41:00**  *(asterisk = flagged)*
- Flagged value: **32:00**, deviation 17.3 h from other-years median (49.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Frankfort, Kentucky → Omaha, Nebraska (1892)
- Values by year: **1882: 47:35** | **1883: 47:35** | **1892: 30:15*** | **1902: 30:00** | **1908: 80:00**  *(asterisk = flagged)*
- Flagged value: **30:15**, deviation 17.3 h from other-years median (47.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Boston, Massachusetts (1902)
- Values by year: **1882: 122:05** | **1883: 122:05** | **1892: 89:30** | **1902: 88:30*** | **1908: 88:30**  *(asterisk = flagged)*
- Flagged value: **88:30**, deviation 17.3 h from other-years median (105.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Boston, Massachusetts (1908)
- Values by year: **1882: 122:05** | **1883: 122:05** | **1892: 89:30** | **1902: 88:30** | **1908: 88:30***  *(asterisk = flagged)*
- Flagged value: **88:30**, deviation 17.3 h from other-years median (105.79 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Boston, Massachusetts (1892)
- Values by year: **1892: 124:00*** | **1902: 106:45** | **1908: 106:45**  *(asterisk = flagged)*
- Flagged value: **124:00**, deviation 17.2 h from other-years median (106.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New York, New York → San Francisco, California (1892)
- Values by year: **1882: 159:15** | **1883: 159:15** | **1892: 111:15*** | **1902: 97:45** | **1908: 92:28**  *(asterisk = flagged)*
- Flagged value: **111:15**, deviation 17.2 h from other-years median (128.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → Baltimore, Maryland (1883)
- Values by year: **1883: 46:20*** | **1892: 63:30** | **1902: 63:30** | **1908: 63:30**  *(asterisk = flagged)*
- Flagged value: **46:20**, deviation 17.2 h from other-years median (63.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rome, New York → San Francisco, California (1892)
- Values by year: **1882: 152:05** | **1883: 152:05** | **1892: 103:15*** | **1902: 88:45** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **103:15**, deviation 17.2 h from other-years median (120.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Massachusetts → San Francisco, California (1892)
- Values by year: **1882: 158:05** | **1883: 158:05** | **1892: 112:15*** | **1902: 100:45** | **1908: 97:45**  *(asterisk = flagged)*
- Flagged value: **112:15**, deviation 17.2 h from other-years median (129.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Charleston, South Carolina (1902)
- Values by year: **1882: 99:02** | **1883: 99:02** | **1892: 65:15** | **1902: 65:00*** | **1908: 65:00**  *(asterisk = flagged)*
- Flagged value: **65:00**, deviation 17.1 h from other-years median (82.14 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Charleston, South Carolina (1908)
- Values by year: **1882: 99:02** | **1883: 99:02** | **1892: 65:15** | **1902: 65:00** | **1908: 65:00***  *(asterisk = flagged)*
- Flagged value: **65:00**, deviation 17.1 h from other-years median (82.14 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 47:57** | **1883: 47:57** | **1892: 33:50** | **1902: 30:50***  *(asterisk = flagged)*
- Flagged value: **30:50**, deviation 17.1 h from other-years median (47.95 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Boston, Massachusetts (1908)
- Values by year: **1882: 72:13** | **1883: 72:13** | **1892: 36:30** | **1902: 48:00** | **1908: 43:00***  *(asterisk = flagged)*
- Flagged value: **43:00**, deviation 17.1 h from other-years median (60.11 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Boston, Massachusetts (1892)
- Values by year: **1882: 81:56** | **1883: 81:56** | **1892: 64:50*** | **1902: 64:50**  *(asterisk = flagged)*
- Flagged value: **64:50**, deviation 17.1 h from other-years median (81.93 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Boston, Massachusetts (1902)
- Values by year: **1882: 81:56** | **1883: 81:56** | **1892: 64:50** | **1902: 64:50***  *(asterisk = flagged)*
- Flagged value: **64:50**, deviation 17.1 h from other-years median (81.93 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Georgia → Chicago, Illinois (1892)
- Values by year: **1882: 49:35** | **1883: 49:35** | **1892: 25:25*** | **1902: 35:25** | **1908: 35:25**  *(asterisk = flagged)*
- Flagged value: **25:25**, deviation 17.1 h from other-years median (42.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Baltimore, Maryland (1892)
- Values by year: **1883: 279:55** | **1892: 127:35*** | **1902: 110:35** | **1908: 110:35**  *(asterisk = flagged)*
- Flagged value: **127:35**, deviation 17.0 h from other-years median (110.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 50:00** | **1883: 50:00** | **1892: 38:00** | **1902: 33:00** | **1908: 27:00***  *(asterisk = flagged)*
- Flagged value: **27:00**, deviation 17.0 h from other-years median (44.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Baltimore, Maryland (1902)
- Values by year: **1883: 279:55** | **1892: 127:35** | **1902: 110:35*** | **1908: 110:35**  *(asterisk = flagged)*
- Flagged value: **110:35**, deviation 17.0 h from other-years median (127.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Baltimore, Maryland (1908)
- Values by year: **1883: 279:55** | **1892: 127:35** | **1902: 110:35** | **1908: 110:35***  *(asterisk = flagged)*
- Flagged value: **110:35**, deviation 17.0 h from other-years median (127.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jefferson City, Missouri → San Francisco, California (1892)
- Values by year: **1882: 119:42** | **1883: 119:42** | **1892: 78:15*** | **1902: 70:45** | **1908: 70:45**  *(asterisk = flagged)*
- Flagged value: **78:15**, deviation 17.0 h from other-years median (95.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Washington, District of Columbia (1892)
- Values by year: **1882: 145:45** | **1883: 145:45** | **1892: 106:55*** | **1902: 101:55** | **1908: 101:55**  *(asterisk = flagged)*
- Flagged value: **106:55**, deviation 16.9 h from other-years median (123.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 44:53** | **1883: 44:53** | **1892: 32:00** | **1902: 28:00***  *(asterisk = flagged)*
- Flagged value: **28:00**, deviation 16.9 h from other-years median (44.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Madison, Wisconsin → San Francisco, California (1892)
- Values by year: **1882: 132:19** | **1883: 132:19** | **1892: 86:15*** | **1902: 73:45** | **1908: 73:45**  *(asterisk = flagged)*
- Flagged value: **86:15**, deviation 16.8 h from other-years median (103.03 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Charleston, South Carolina (1892)
- Values by year: **1882: 99:02** | **1883: 99:02** | **1892: 65:15*** | **1902: 65:00** | **1908: 65:00**  *(asterisk = flagged)*
- Flagged value: **65:15**, deviation 16.8 h from other-years median (82.02 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → San Francisco, California (1892)
- Values by year: **1882: 173:15** | **1883: 173:15** | **1892: 126:15*** | **1902: 112:45** | **1908: 108:28**  *(asterisk = flagged)*
- Flagged value: **126:15**, deviation 16.8 h from other-years median (143.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Henderson, Kentucky → San Francisco, California (1892)
- Values by year: **1882: 124:00** | **1883: 124:00** | **1892: 90:15*** | **1902: 89:45** | **1908: 89:20**  *(asterisk = flagged)*
- Flagged value: **90:15**, deviation 16.6 h from other-years median (106.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → Charleston, South Carolina (1892)
- Values by year: **1882: 36:20** | **1883: 36:20** | **1892: 48:30*** | **1902: 27:30** | **1908: 27:30**  *(asterisk = flagged)*
- Flagged value: **48:30**, deviation 16.6 h from other-years median (31.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Chicago, Illinois (1908)
- Values by year: **1882: 46:18** | **1883: 46:18** | **1892: 16:50** | **1902: 15:34** | **1908: 15:00***  *(asterisk = flagged)*
- Flagged value: **15:00**, deviation 16.6 h from other-years median (31.57 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Charleston, South Carolina (1902)
- Values by year: **1882: 154:52** | **1883: 154:52** | **1892: 133:45** | **1902: 127:45*** | **1908: 127:45**  *(asterisk = flagged)*
- Flagged value: **127:45**, deviation 16.6 h from other-years median (144.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Charleston, South Carolina (1908)
- Values by year: **1882: 154:52** | **1883: 154:52** | **1892: 133:45** | **1902: 127:45** | **1908: 127:45***  *(asterisk = flagged)*
- Flagged value: **127:45**, deviation 16.6 h from other-years median (144.31 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Saint Louis, Missouri (1902)
- Values by year: **1882: 50:38** | **1883: 50:38** | **1892: 17:40** | **1902: 17:40*** | **1908: 17:40**  *(asterisk = flagged)*
- Flagged value: **17:40**, deviation 16.5 h from other-years median (34.15 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Saint Louis, Missouri (1892)
- Values by year: **1882: 50:38** | **1883: 50:38** | **1892: 17:40*** | **1902: 17:40** | **1908: 17:40**  *(asterisk = flagged)*
- Flagged value: **17:40**, deviation 16.5 h from other-years median (34.15 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Saint Louis, Missouri (1908)
- Values by year: **1882: 50:38** | **1883: 50:38** | **1892: 17:40** | **1902: 17:40** | **1908: 17:40***  *(asterisk = flagged)*
- Flagged value: **17:40**, deviation 16.5 h from other-years median (34.15 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Washington, District of Columbia (1902)
- Values by year: **1882: 108:52** | **1883: 108:52** | **1892: 71:00** | **1902: 76:00*** | **1908: 76:00**  *(asterisk = flagged)*
- Flagged value: **76:00**, deviation 16.4 h from other-years median (92.43 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Washington, District of Columbia (1908)
- Values by year: **1882: 108:52** | **1883: 108:52** | **1892: 71:00** | **1902: 76:00** | **1908: 76:00***  *(asterisk = flagged)*
- Flagged value: **76:00**, deviation 16.4 h from other-years median (92.43 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atlanta, Georgia → Boston, Massachusetts (1902)
- Values by year: **1882: 50:20** | **1883: 50:20** | **1892: 43:30** | **1902: 30:30*** | **1908: 30:30**  *(asterisk = flagged)*
- Flagged value: **30:30**, deviation 16.4 h from other-years median (46.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atlanta, Georgia → Boston, Massachusetts (1908)
- Values by year: **1882: 50:20** | **1883: 50:20** | **1892: 43:30** | **1902: 30:30** | **1908: 30:30***  *(asterisk = flagged)*
- Flagged value: **30:30**, deviation 16.4 h from other-years median (46.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hannibal, Missouri → San Francisco, California (1892)
- Values by year: **1882: 121:34** | **1883: 121:34** | **1892: 84:15*** | **1902: 79:45** | **1908: 79:45**  *(asterisk = flagged)*
- Flagged value: **84:15**, deviation 16.4 h from other-years median (100.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Buffalo, New York → Cincinnati, Ohio (1892)
- Values by year: **1882: 17:20** | **1883: 17:20** | **1892: 33:00*** | **1902: 16:00** | **1908: 16:00**  *(asterisk = flagged)*
- Flagged value: **33:00**, deviation 16.3 h from other-years median (16.66 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Omaha, Nebraska (1908)
- Values by year: **1882: 96:40** | **1883: 96:40** | **1892: 100:30** | **1902: 80:30** | **1908: 80:30***  *(asterisk = flagged)*
- Flagged value: **80:30**, deviation 16.2 h from other-years median (96.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Omaha, Nebraska (1902)
- Values by year: **1882: 96:40** | **1883: 96:40** | **1892: 100:30** | **1902: 80:30*** | **1908: 80:30**  *(asterisk = flagged)*
- Flagged value: **80:30**, deviation 16.2 h from other-years median (96.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Saint Louis, Missouri (1892)
- Values by year: **1882: 58:10** | **1883: 58:10** | **1892: 42:00*** | **1902: 42:00**  *(asterisk = flagged)*
- Flagged value: **42:00**, deviation 16.2 h from other-years median (58.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Saint Louis, Missouri (1902)
- Values by year: **1882: 58:10** | **1883: 58:10** | **1892: 42:00** | **1902: 42:00***  *(asterisk = flagged)*
- Flagged value: **42:00**, deviation 16.2 h from other-years median (58.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hartford, Connecticut → San Francisco, California (1892)
- Values by year: **1882: 160:27** | **1883: 160:27** | **1892: 114:00*** | **1902: 99:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **114:00**, deviation 16.1 h from other-years median (130.10 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Washington, District of Columbia (1908)
- Values by year: **1882: 44:10** | **1883: 44:10** | **1892: 34:00** | **1902: 31:00** | **1908: 23:00***  *(asterisk = flagged)*
- Flagged value: **23:00**, deviation 16.1 h from other-years median (39.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → San Francisco, California (1892)
- Values by year: **1882: 163:10** | **1883: 163:10** | **1892: 115:00*** | **1902: 98:55** | **1908: 96:55**  *(asterisk = flagged)*
- Flagged value: **115:00**, deviation 16.0 h from other-years median (131.04 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → Boston, Massachusetts (1902)
- Values by year: **1882: 55:55** | **1883: 55:35** | **1892: 49:30** | **1902: 36:30*** | **1908: 36:30**  *(asterisk = flagged)*
- Flagged value: **36:30**, deviation 16.0 h from other-years median (52.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → Boston, Massachusetts (1908)
- Values by year: **1882: 55:55** | **1883: 55:35** | **1892: 49:30** | **1902: 36:30** | **1908: 36:30***  *(asterisk = flagged)*
- Flagged value: **36:30**, deviation 16.0 h from other-years median (52.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Charleston, South Carolina (1902)
- Values by year: **1883: 304:37** | **1892: 149:10** | **1902: 133:10*** | **1908: 133:10**  *(asterisk = flagged)*
- Flagged value: **133:10**, deviation 16.0 h from other-years median (149.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Charleston, South Carolina (1892)
- Values by year: **1883: 304:37** | **1892: 149:10*** | **1902: 133:10** | **1908: 133:10**  *(asterisk = flagged)*
- Flagged value: **149:10**, deviation 16.0 h from other-years median (133.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Washington, District of Columbia (1908)
- Values by year: **1883: 278:37** | **1892: 128:25** | **1902: 112:25** | **1908: 112:25***  *(asterisk = flagged)*
- Flagged value: **112:25**, deviation 16.0 h from other-years median (128.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Ogden, Utah → Chicago, Illinois (1892)
- Values by year: **1892: 60:30*** | **1902: 44:30** | **1908: 44:30**  *(asterisk = flagged)*
- Flagged value: **60:30**, deviation 16.0 h from other-years median (44.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Washington, District of Columbia (1902)
- Values by year: **1883: 278:37** | **1892: 128:25** | **1902: 112:25*** | **1908: 112:25**  *(asterisk = flagged)*
- Flagged value: **112:25**, deviation 16.0 h from other-years median (128.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Washington, District of Columbia (1892)
- Values by year: **1883: 278:37** | **1892: 128:25*** | **1902: 112:25** | **1908: 112:25**  *(asterisk = flagged)*
- Flagged value: **128:25**, deviation 16.0 h from other-years median (112.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Charleston, South Carolina (1908)
- Values by year: **1883: 304:37** | **1892: 149:10** | **1902: 133:10** | **1908: 133:10***  *(asterisk = flagged)*
- Flagged value: **133:10**, deviation 16.0 h from other-years median (149.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Chicago, Illinois (1902)
- Values by year: **1882: 46:18** | **1883: 46:18** | **1892: 16:50** | **1902: 15:34*** | **1908: 15:00**  *(asterisk = flagged)*
- Flagged value: **15:34**, deviation 16.0 h from other-years median (31.57 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Boston, Massachusetts (1902)
- Values by year: **1882: 69:25** | **1883: 69:25** | **1892: 57:30** | **1902: 47:30*** | **1908: 47:30**  *(asterisk = flagged)*
- Flagged value: **47:30**, deviation 16.0 h from other-years median (63.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Boston, Massachusetts (1908)
- Values by year: **1882: 69:25** | **1883: 69:25** | **1892: 57:30** | **1902: 47:30** | **1908: 47:30***  *(asterisk = flagged)*
- Flagged value: **47:30**, deviation 16.0 h from other-years median (63.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → New York, New York (1908)
- Values by year: **1882: 52:25** | **1883: 52:25** | **1892: 40:30** | **1902: 35:30** | **1908: 30:30***  *(asterisk = flagged)*
- Flagged value: **30:30**, deviation 16.0 h from other-years median (46.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Philadelphia, Pennsylvania (1908)
- Values by year: **1882: 56:55** | **1883: 56:55** | **1892: 45:00** | **1902: 35:00** | **1908: 35:00***  *(asterisk = flagged)*
- Flagged value: **35:00**, deviation 16.0 h from other-years median (50.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Philadelphia, Pennsylvania (1902)
- Values by year: **1882: 56:55** | **1883: 56:55** | **1892: 45:00** | **1902: 35:00*** | **1908: 35:00**  *(asterisk = flagged)*
- Flagged value: **35:00**, deviation 16.0 h from other-years median (50.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Omaha, Nebraska → San Francisco, California (1892)
- Values by year: **1882: 97:05** | **1883: 97:06** | **1892: 92:15*** | **1902: 52:30** | **1908: 55:30**  *(asterisk = flagged)*
- Flagged value: **92:15**, deviation 16.0 h from other-years median (76.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Boston, Massachusetts (1892)
- Values by year: **1882: 173:10** | **1883: 173:10** | **1892: 128:09*** | **1902: 115:00** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **128:09**, deviation 15.9 h from other-years median (144.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Newport, Rhode Island → San Francisco, California (1892)
- Values by year: **1882: 166:35** | **1883: 166:35** | **1892: 119:15*** | **1902: 103:45** | **1908: 103:28**  *(asterisk = flagged)*
- Flagged value: **119:15**, deviation 15.9 h from other-years median (135.16 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Chicago, Illinois (1892)
- Values by year: **1882: 48:50** | **1883: 48:50** | **1892: 15:30*** | **1902: 14:00** | **1908: 14:00**  *(asterisk = flagged)*
- Flagged value: **15:30**, deviation 15.9 h from other-years median (31.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Philadelphia, Pennsylvania (1892)
- Values by year: **1882: 27:10** | **1883: 27:10** | **1892: 38:50*** | **1902: 18:50** | **1908: 18:50**  *(asterisk = flagged)*
- Flagged value: **38:50**, deviation 15.8 h from other-years median (23.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Boston, Massachusetts (1892)
- Values by year: **1882: 122:05** | **1883: 122:05** | **1892: 89:30*** | **1902: 88:30** | **1908: 88:30**  *(asterisk = flagged)*
- Flagged value: **89:30**, deviation 15.8 h from other-years median (105.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Boston, Massachusetts (1902)
- Values by year: **1882: 83:49** | **1883: 83:49** | **1892: 76:20** | **1902: 64:20*** | **1908: 64:20**  *(asterisk = flagged)*
- Flagged value: **64:20**, deviation 15.7 h from other-years median (80.07 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Boston, Massachusetts (1908)
- Values by year: **1882: 83:49** | **1883: 83:49** | **1892: 76:20** | **1902: 64:20** | **1908: 64:20***  *(asterisk = flagged)*
- Flagged value: **64:20**, deviation 15.7 h from other-years median (80.07 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → New York, New York (1902)
- Values by year: **1882: 60:15** | **1883: 60:15** | **1892: 48:50** | **1902: 38:50*** | **1908: 38:50**  *(asterisk = flagged)*
- Flagged value: **38:50**, deviation 15.7 h from other-years median (54.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → New York, New York (1908)
- Values by year: **1882: 60:15** | **1883: 60:15** | **1892: 48:50** | **1902: 38:50** | **1908: 38:50***  *(asterisk = flagged)*
- Flagged value: **38:50**, deviation 15.7 h from other-years median (54.54 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Omaha, Nebraska (1908)
- Values by year: **1882: 56:25** | **1883: 56:25** | **1892: 43:00** | **1902: 34:00** | **1908: 34:00***  *(asterisk = flagged)*
- Flagged value: **34:00**, deviation 15.7 h from other-years median (49.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Omaha, Nebraska (1902)
- Values by year: **1882: 56:25** | **1883: 56:25** | **1892: 43:00** | **1902: 34:00*** | **1908: 34:00**  *(asterisk = flagged)*
- Flagged value: **34:00**, deviation 15.7 h from other-years median (49.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → Baltimore, Maryland (1908)
- Values by year: **1882: 39:10** | **1883: 39:10** | **1892: 32:00** | **1902: 26:00** | **1908: 20:00***  *(asterisk = flagged)*
- Flagged value: **20:00**, deviation 15.6 h from other-years median (35.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Staunton, Virginia → Charleston, South Carolina (1908)
- Values by year: **1882: 31:35** | **1883: 31:35** | **1892: 44:00** | **1902: 16:00** | **1908: 16:00***  *(asterisk = flagged)*
- Flagged value: **16:00**, deviation 15.6 h from other-years median (31.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Staunton, Virginia → Charleston, South Carolina (1902)
- Values by year: **1882: 31:35** | **1883: 31:35** | **1892: 44:00** | **1902: 16:00*** | **1908: 16:00**  *(asterisk = flagged)*
- Flagged value: **16:00**, deviation 15.6 h from other-years median (31.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → Omaha, Nebraska (1908)
- Values by year: **1882: 67:10** | **1883: 67:10** | **1892: 48:51** | **1902: 48:35** | **1908: 42:35***  *(asterisk = flagged)*
- Flagged value: **42:35**, deviation 15.4 h from other-years median (58.01 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → Omaha, Nebraska (1902)
- Values by year: **1883: 53:20** | **1892: 38:00** | **1902: 38:00*** | **1908: 68:00**  *(asterisk = flagged)*
- Flagged value: **38:00**, deviation 15.3 h from other-years median (53.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → Omaha, Nebraska (1892)
- Values by year: **1883: 53:20** | **1892: 38:00*** | **1902: 38:00** | **1908: 68:00**  *(asterisk = flagged)*
- Flagged value: **38:00**, deviation 15.3 h from other-years median (53.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → Omaha, Nebraska (1892)
- Values by year: **1882: 106:35** | **1883: 106:35** | **1892: 73:00*** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **73:00**, deviation 15.3 h from other-years median (88.29 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → Washington, District of Columbia (1892)
- Values by year: **1882: 59:08** | **1883: 59:08** | **1892: 77:50*** | **1902: 66:00** | **1908: 66:00**  *(asterisk = flagged)*
- Flagged value: **77:50**, deviation 15.3 h from other-years median (62.57 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Pittsburgh, Pennsylvania (1892)
- Values by year: **1883: 137:27** | **1892: 97:00*** | **1902: 87:00**  *(asterisk = flagged)*
- Flagged value: **97:00**, deviation 15.2 h from other-years median (112.22 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Boston, Massachusetts (1908)
- Values by year: **1882: 54:55** | **1883: 54:55** | **1892: 50:30** | **1902: 38:30** | **1908: 37:30***  *(asterisk = flagged)*
- Flagged value: **37:30**, deviation 15.2 h from other-years median (52.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Philadelphia, Pennsylvania (1892)
- Values by year: **1882: 147:05** | **1883: 147:05** | **1892: 110:40*** | **1902: 104:40** | **1908: 104:40**  *(asterisk = flagged)*
- Flagged value: **110:40**, deviation 15.2 h from other-years median (125.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → Pittsburgh, Pennsylvania (1902)
- Values by year: **1882: 47:30** | **1883: 47:30** | **1892: 32:20** | **1902: 32:20***  *(asterisk = flagged)*
- Flagged value: **32:20**, deviation 15.2 h from other-years median (47.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → Pittsburgh, Pennsylvania (1892)
- Values by year: **1882: 47:30** | **1883: 47:30** | **1892: 32:20*** | **1902: 32:20**  *(asterisk = flagged)*
- Flagged value: **32:20**, deviation 15.2 h from other-years median (47.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Chicago, Illinois (1892)
- Values by year: **1882: 45:00** | **1883: 45:00** | **1892: 29:50*** | **1902: 35:50**  *(asterisk = flagged)*
- Flagged value: **29:50**, deviation 15.2 h from other-years median (45.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Baltimore, Maryland (1902)
- Values by year: **1882: 76:10** | **1883: 76:10** | **1892: 58:00** | **1902: 61:00***  *(asterisk = flagged)*
- Flagged value: **61:00**, deviation 15.2 h from other-years median (76.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Cincinnati, Ohio (1908)
- Values by year: **1882: 83:20** | **1883: 83:20** | **1892: 69:00** | **1902: 61:00** | **1908: 61:00***  *(asterisk = flagged)*
- Flagged value: **61:00**, deviation 15.2 h from other-years median (76.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Cincinnati, Ohio (1902)
- Values by year: **1882: 83:20** | **1883: 83:20** | **1892: 69:00** | **1902: 61:00*** | **1908: 61:00**  *(asterisk = flagged)*
- Flagged value: **61:00**, deviation 15.2 h from other-years median (76.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chicago, Illinois → San Francisco, California (1892)
- Values by year: **1882: 121:24** | **1883: 121:24** | **1892: 80:15*** | **1902: 69:25** | **1908: 65:15**  *(asterisk = flagged)*
- Flagged value: **80:15**, deviation 15.2 h from other-years median (95.41 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Cincinnati, Ohio (1902)
- Values by year: **1882: 47:15** | **1883: 47:15** | **1892: 37:30** | **1902: 57:30*** | **1908: 37:30**  *(asterisk = flagged)*
- Flagged value: **57:30**, deviation 15.1 h from other-years median (42.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Chicago, Illinois (1908)
- Values by year: **1882: 119:50** | **1883: 119:50** | **1892: 82:40** | **1902: 89:40** | **1908: 89:40***  *(asterisk = flagged)*
- Flagged value: **89:40**, deviation 15.1 h from other-years median (104.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Chicago, Illinois (1902)
- Values by year: **1882: 119:50** | **1883: 119:50** | **1892: 82:40** | **1902: 89:40*** | **1908: 89:40**  *(asterisk = flagged)*
- Flagged value: **89:40**, deviation 15.1 h from other-years median (104.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → Boston, Massachusetts (1902)
- Values by year: **1882: 70:37** | **1883: 70:37** | **1892: 52:30** | **1902: 46:30*** | **1908: 50:30**  *(asterisk = flagged)*
- Flagged value: **46:30**, deviation 15.1 h from other-years median (61.56 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Baltimore, Maryland (1892)
- Values by year: **1882: 62:04** | **1883: 62:04** | **1892: 35:00*** | **1902: 38:00** | **1908: 38:00**  *(asterisk = flagged)*
- Flagged value: **35:00**, deviation 15.0 h from other-years median (50.03 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tampa, Florida → San Francisco, California (1892)
- Values by year: **1892: 143:15*** | **1902: 129:45** | **1908: 126:45**  *(asterisk = flagged)*
- Flagged value: **143:15**, deviation 15.0 h from other-years median (128.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Ogden, Utah → Saint Louis, Missouri (1892)
- Values by year: **1892: 65:30*** | **1902: 50:30** | **1908: 50:30**  *(asterisk = flagged)*
- Flagged value: **65:30**, deviation 15.0 h from other-years median (50.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Washington, District of Columbia (1908)
- Values by year: **1882: 51:00** | **1883: 51:00** | **1892: 41:00** | **1902: 31:00** | **1908: 31:00***  *(asterisk = flagged)*
- Flagged value: **31:00**, deviation 15.0 h from other-years median (46.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Boston, Massachusetts (1908)
- Values by year: **1883: 183:20** | **1892: 133:00** | **1902: 120:00** | **1908: 118:00***  *(asterisk = flagged)*
- Flagged value: **118:00**, deviation 15.0 h from other-years median (133.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tacoma, Washington → Chicago, Illinois (1892)
- Values by year: **1892: 93:15*** | **1902: 78:15** | **1908: 78:15**  *(asterisk = flagged)*
- Flagged value: **93:15**, deviation 15.0 h from other-years median (78.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Washington, District of Columbia (1902)
- Values by year: **1882: 51:00** | **1883: 51:00** | **1892: 41:00** | **1902: 31:00*** | **1908: 31:00**  *(asterisk = flagged)*
- Flagged value: **31:00**, deviation 15.0 h from other-years median (46.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Boston, Massachusetts (1902)
- Values by year: **1882: 47:35** | **1883: 47:35** | **1892: 44:35** | **1902: 31:05*** | **1908: 31:35**  *(asterisk = flagged)*
- Flagged value: **31:05**, deviation 15.0 h from other-years median (46.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

## HISTORICAL (648 cases)
*1882 value is plausibly higher due to slower pre-transcontinental-railroad travel — likely not an error*

### Olympia, Washington → Boston, Massachusetts (1883)
- Values by year: **1883: 295:00*** | **1892: 129:00** | **1902: 116:00** | **1908: 116:00**  *(asterisk = flagged)*
- Flagged value: **295:00**, deviation 179.0 h from other-years median (116.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Charleston, South Carolina (1883)
- Values by year: **1883: 304:37*** | **1892: 149:10** | **1902: 133:10** | **1908: 133:10**  *(asterisk = flagged)*
- Flagged value: **304:37**, deviation 171.4 h from other-years median (133.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → New York, New York (1883)
- Values by year: **1883: 284:05*** | **1892: 123:55** | **1902: 112:00** | **1908: 112:55**  *(asterisk = flagged)*
- Flagged value: **284:05**, deviation 171.2 h from other-years median (112.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Baltimore, Maryland (1883)
- Values by year: **1883: 279:55*** | **1892: 127:35** | **1902: 110:35** | **1908: 110:35**  *(asterisk = flagged)*
- Flagged value: **279:55**, deviation 169.3 h from other-years median (110.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Philadelphia, Pennsylvania (1883)
- Values by year: **1883: 280:15*** | **1892: 125:10** | **1902: 112:10** | **1908: 112:10**  *(asterisk = flagged)*
- Flagged value: **280:15**, deviation 168.1 h from other-years median (112.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Washington, District of Columbia (1883)
- Values by year: **1883: 278:37*** | **1892: 128:25** | **1902: 112:25** | **1908: 112:25**  *(asterisk = flagged)*
- Flagged value: **278:37**, deviation 166.2 h from other-years median (112.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Chicago, Illinois (1883)
- Values by year: **1883: 252:30*** | **1892: 96:15** | **1902: 88:15** | **1908: 88:15**  *(asterisk = flagged)*
- Flagged value: **252:30**, deviation 164.2 h from other-years median (88.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Pittsburgh, Pennsylvania (1883)
- Values by year: **1883: 269:35*** | **1892: 114:15** | **1902: 101:15**  *(asterisk = flagged)*
- Flagged value: **269:35**, deviation 161.8 h from other-years median (107.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Charleston, South Carolina (1883)
- Values by year: **1883: 282:07*** | **1892: 132:45** | **1902: 125:40** | **1908: 125:40**  *(asterisk = flagged)*
- Flagged value: **282:07**, deviation 156.4 h from other-years median (125.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Boston, Massachusetts (1883)
- Values by year: **1883: 272:30*** | **1892: 126:20** | **1902: 117:20** | **1908: 117:20**  *(asterisk = flagged)*
- Flagged value: **272:30**, deviation 155.2 h from other-years median (117.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Charleston, South Carolina (1883)
- Values by year: **1883: 279:07*** | **1892: 134:45** | **1902: 127:45** | **1908: 127:45**  *(asterisk = flagged)*
- Flagged value: **279:07**, deviation 151.4 h from other-years median (127.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Cincinnati, Ohio (1883)
- Values by year: **1883: 255:35*** | **1892: 108:25** | **1902: 104:05** | **1908: 104:25**  *(asterisk = flagged)*
- Flagged value: **255:35**, deviation 151.2 h from other-years median (104.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Boston, Massachusetts (1883)
- Values by year: **1883: 269:30*** | **1892: 128:20** | **1902: 119:20** | **1908: 119:20**  *(asterisk = flagged)*
- Flagged value: **269:30**, deviation 150.2 h from other-years median (119.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Omaha, Nebraska (1883)
- Values by year: **1883: 229:10*** | **1892: 72:15** | **1902: 80:15** | **1908: 80:15**  *(asterisk = flagged)*
- Flagged value: **229:10**, deviation 148.9 h from other-years median (80.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → New York, New York (1883)
- Values by year: **1883: 261:35*** | **1892: 121:30** | **1902: 114:03** | **1908: 114:30**  *(asterisk = flagged)*
- Flagged value: **261:35**, deviation 147.1 h from other-years median (114.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Washington, District of Columbia (1883)
- Values by year: **1883: 259:07*** | **1892: 124:30** | **1902: 114:30** | **1908: 114:30**  *(asterisk = flagged)*
- Flagged value: **259:07**, deviation 144.6 h from other-years median (114.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Baltimore, Maryland (1883)
- Values by year: **1883: 257:25*** | **1892: 123:20** | **1902: 113:20** | **1908: 113:20**  *(asterisk = flagged)*
- Flagged value: **257:25**, deviation 144.1 h from other-years median (113.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → Saint Louis, Missouri (1883)
- Values by year: **1883: 244:45*** | **1892: 95:05** | **1902: 101:05** | **1908: 101:05**  *(asterisk = flagged)*
- Flagged value: **244:45**, deviation 143.7 h from other-years median (101.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Chicago, Illinois (1883)
- Values by year: **1883: 230:00*** | **1892: 92:50** | **1902: 87:50** | **1908: 87:50**  *(asterisk = flagged)*
- Flagged value: **230:00**, deviation 142.2 h from other-years median (87.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → New York, New York (1883)
- Values by year: **1883: 258:35*** | **1892: 123:30** | **1902: 116:30** | **1908: 116:30**  *(asterisk = flagged)*
- Flagged value: **258:35**, deviation 142.1 h from other-years median (116.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Philadelphia, Pennsylvania (1883)
- Values by year: **1883: 257:45*** | **1892: 121:30** | **1902: 116:30** | **1908: 116:30**  *(asterisk = flagged)*
- Flagged value: **257:45**, deviation 141.2 h from other-years median (116.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Washington, District of Columbia (1883)
- Values by year: **1883: 256:07*** | **1892: 126:30** | **1902: 116:30** | **1908: 116:30**  *(asterisk = flagged)*
- Flagged value: **256:07**, deviation 139.6 h from other-years median (116.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Baltimore, Maryland (1883)
- Values by year: **1883: 254:25*** | **1892: 125:20** | **1902: 115:20** | **1908: 115:20**  *(asterisk = flagged)*
- Flagged value: **254:25**, deviation 139.1 h from other-years median (115.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Pittsburgh, Pennsylvania (1883)
- Values by year: **1883: 247:05*** | **1892: 110:50** | **1902: 105:50**  *(asterisk = flagged)*
- Flagged value: **247:05**, deviation 138.8 h from other-years median (108.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Philadelphia, Pennsylvania (1883)
- Values by year: **1883: 254:45*** | **1892: 123:30** | **1902: 118:30** | **1908: 118:30**  *(asterisk = flagged)*
- Flagged value: **254:45**, deviation 136.2 h from other-years median (118.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Chicago, Illinois (1883)
- Values by year: **1883: 227:00*** | **1892: 94:54** | **1902: 90:50** | **1908: 90:50**  *(asterisk = flagged)*
- Flagged value: **227:00**, deviation 136.2 h from other-years median (90.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Pittsburgh, Pennsylvania (1883)
- Values by year: **1883: 243:05*** | **1892: 112:50** | **1902: 107:50**  *(asterisk = flagged)*
- Flagged value: **243:05**, deviation 132.8 h from other-years median (110.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Cincinnati, Ohio (1883)
- Values by year: **1883: 233:05*** | **1892: 100:20** | **1902: 100:20** | **1908: 100:20**  *(asterisk = flagged)*
- Flagged value: **233:05**, deviation 132.8 h from other-years median (100.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Omaha, Nebraska (1883)
- Values by year: **1883: 206:40*** | **1892: 74:00** | **1902: 74:00** | **1908: 74:00**  *(asterisk = flagged)*
- Flagged value: **206:40**, deviation 132.7 h from other-years median (74.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Cincinnati, Ohio (1883)
- Values by year: **1883: 230:05*** | **1892: 102:20** | **1902: 102:20** | **1908: 102:20**  *(asterisk = flagged)*
- Flagged value: **230:05**, deviation 127.8 h from other-years median (102.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Omaha, Nebraska (1883)
- Values by year: **1883: 203:40*** | **1892: 76:00** | **1902: 76:00** | **1908: 76:00**  *(asterisk = flagged)*
- Flagged value: **203:40**, deviation 127.7 h from other-years median (76.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → Saint Louis, Missouri (1883)
- Values by year: **1883: 222:15*** | **1892: 99:50** | **1902: 99:50** | **1908: 99:50**  *(asterisk = flagged)*
- Flagged value: **222:15**, deviation 122.4 h from other-years median (99.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → Saint Louis, Missouri (1883)
- Values by year: **1883: 219:15*** | **1892: 101:50** | **1902: 100:50** | **1908: 100:50**  *(asterisk = flagged)*
- Flagged value: **219:15**, deviation 118.4 h from other-years median (100.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mesilla, New Mexico → Charleston, South Carolina (1883)
- Values by year: **1882: 24:04** | **1883: 124:04***  *(asterisk = flagged)*
- Flagged value: **124:04**, deviation 100.0 h from other-years median (24.07 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Olympia, Washington → San Francisco, California (1883)
- Values by year: **1883: 141:40*** | **1892: 48:35** | **1902: 44:02** | **1908: 44:25**  *(asterisk = flagged)*
- Flagged value: **141:40**, deviation 97.2 h from other-years median (44.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → San Francisco, California (1883)
- Values by year: **1883: 127:52*** | **1892: 40:45** | **1902: 40:35** | **1908: 40:35**  *(asterisk = flagged)*
- Flagged value: **127:52**, deviation 87.3 h from other-years median (40.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → San Francisco, California (1882)
- Values by year: **1882: 169:34*** | **1883: 169:30** | **1892: 84:15** | **1902: 83:45** | **1908: 83:45**  *(asterisk = flagged)*
- Flagged value: **169:34**, deviation 85.6 h from other-years median (84.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → San Francisco, California (1883)
- Values by year: **1882: 169:34** | **1883: 169:30*** | **1892: 84:15** | **1902: 83:45** | **1908: 83:45**  *(asterisk = flagged)*
- Flagged value: **169:30**, deviation 85.5 h from other-years median (84.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Charleston, South Carolina (1883)
- Values by year: **1883: 189:45*** | **1892: 125:15** | **1902: 105:15** | **1908: 105:15**  *(asterisk = flagged)*
- Flagged value: **189:45**, deviation 84.5 h from other-years median (105.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Oregon → San Francisco, California (1883)
- Values by year: **1883: 119:10*** | **1892: 39:45** | **1902: 39:15** | **1908: 39:15**  *(asterisk = flagged)*
- Flagged value: **119:10**, deviation 79.9 h from other-years median (39.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salem, Oregon → San Francisco, California (1883)
- Values by year: **1883: 116:10*** | **1892: 37:45** | **1902: 37:45** | **1908: 37:45**  *(asterisk = flagged)*
- Flagged value: **116:10**, deviation 78.4 h from other-years median (37.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → San Francisco, California (1883)
- Values by year: **1882: 165:34** | **1883: 165:34*** | **1892: 88:15** | **1902: 88:15** | **1908: 88:15**  *(asterisk = flagged)*
- Flagged value: **165:34**, deviation 77.3 h from other-years median (88.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → San Francisco, California (1882)
- Values by year: **1882: 165:34*** | **1883: 165:34** | **1892: 88:15** | **1902: 88:15** | **1908: 88:15**  *(asterisk = flagged)*
- Flagged value: **165:34**, deviation 77.3 h from other-years median (88.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Boston, Massachusetts (1883)
- Values by year: **1883: 168:00*** | **1892: 85:30** | **1902: 91:30** | **1908: 91:30**  *(asterisk = flagged)*
- Flagged value: **168:00**, deviation 76.5 h from other-years median (91.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Charleston, South Carolina (1883)
- Values by year: **1883: 200:30*** | **1892: 120:45** | **1902: 125:00** | **1908: 125:00**  *(asterisk = flagged)*
- Flagged value: **200:30**, deviation 75.5 h from other-years median (125.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Charleston, South Carolina (1882)
- Values by year: **1882: 190:20*** | **1883: 190:20** | **1892: 115:45** | **1902: 115:00** | **1908: 115:00**  *(asterisk = flagged)*
- Flagged value: **190:20**, deviation 75.0 h from other-years median (115.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Charleston, South Carolina (1883)
- Values by year: **1882: 190:20** | **1883: 190:20*** | **1892: 115:45** | **1902: 115:00** | **1908: 115:00**  *(asterisk = flagged)*
- Flagged value: **190:20**, deviation 75.0 h from other-years median (115.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → San Francisco, California (1883)
- Values by year: **1882: 167:25** | **1883: 167:25*** | **1892: 101:15** | **1902: 83:45** | **1908: 82:28**  *(asterisk = flagged)*
- Flagged value: **167:25**, deviation 74.9 h from other-years median (92.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → San Francisco, California (1882)
- Values by year: **1882: 167:25*** | **1883: 167:25** | **1892: 101:15** | **1902: 83:45** | **1908: 82:28**  *(asterisk = flagged)*
- Flagged value: **167:25**, deviation 74.9 h from other-years median (92.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Philadelphia, Pennsylvania (1883)
- Values by year: **1883: 153:30*** | **1892: 82:00** | **1902: 80:00** | **1908: 80:00**  *(asterisk = flagged)*
- Flagged value: **153:30**, deviation 73.5 h from other-years median (80.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → San Francisco, California (1882)
- Values by year: **1882: 202:35*** | **1883: 202:35** | **1892: 139:15** | **1902: 122:45** | **1908: 122:28**  *(asterisk = flagged)*
- Flagged value: **202:35**, deviation 71.6 h from other-years median (131.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → San Francisco, California (1883)
- Values by year: **1882: 202:35** | **1883: 202:35*** | **1892: 139:15** | **1902: 122:45** | **1908: 122:28**  *(asterisk = flagged)*
- Flagged value: **202:35**, deviation 71.6 h from other-years median (131.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → San Francisco, California (1882)
- Values by year: **1882: 164:53*** | **1883: 164:53** | **1892: 102:15** | **1902: 84:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **164:53**, deviation 71.4 h from other-years median (93.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → San Francisco, California (1883)
- Values by year: **1882: 164:53** | **1883: 164:53*** | **1892: 102:15** | **1902: 84:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **164:53**, deviation 71.4 h from other-years median (93.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Charleston, South Carolina (1882)
- Values by year: **1882: 190:20*** | **1883: 190:20** | **1892: 115:45** | **1902: 119:30** | **1908: 119:30**  *(asterisk = flagged)*
- Flagged value: **190:20**, deviation 70.8 h from other-years median (119.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Charleston, South Carolina (1883)
- Values by year: **1882: 190:20** | **1883: 190:20*** | **1892: 115:45** | **1902: 119:30** | **1908: 119:30**  *(asterisk = flagged)*
- Flagged value: **190:20**, deviation 70.8 h from other-years median (119.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Washington, District of Columbia (1883)
- Values by year: **1883: 154:47*** | **1892: 85:00** | **1902: 87:00** | **1908: 85:00**  *(asterisk = flagged)*
- Flagged value: **154:47**, deviation 69.8 h from other-years median (85.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Pittsburgh, Pennsylvania (1883)
- Values by year: **1883: 140:25*** | **1892: 69:00** | **1902: 75:00**  *(asterisk = flagged)*
- Flagged value: **140:25**, deviation 68.4 h from other-years median (72.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Baltimore, Maryland (1883)
- Values by year: **1883: 153:15*** | **1892: 84:00** | **1902: 86:00** | **1908: 86:00**  *(asterisk = flagged)*
- Flagged value: **153:15**, deviation 67.2 h from other-years median (86.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → New York, New York (1883)
- Values by year: **1883: 152:55*** | **1892: 81:00** | **1902: 89:00** | **1908: 86:00**  *(asterisk = flagged)*
- Flagged value: **152:55**, deviation 66.9 h from other-years median (86.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → San Francisco, California (1882)
- Values by year: **1882: 165:39*** | **1883: 165:35** | **1892: 102:15** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **165:39**, deviation 66.7 h from other-years median (99.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → San Francisco, California (1883)
- Values by year: **1882: 165:39** | **1883: 165:35*** | **1892: 102:15** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **165:35**, deviation 66.6 h from other-years median (99.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → San Francisco, California (1882)
- Values by year: **1882: 196:50*** | **1883: 196:50** | **1892: 138:15** | **1902: 124:45** | **1908: 122:45**  *(asterisk = flagged)*
- Flagged value: **196:50**, deviation 65.3 h from other-years median (131.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → San Francisco, California (1883)
- Values by year: **1882: 196:50** | **1883: 196:50*** | **1892: 138:15** | **1902: 124:45** | **1908: 122:45**  *(asterisk = flagged)*
- Flagged value: **196:50**, deviation 65.3 h from other-years median (131.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → San Francisco, California (1883)
- Values by year: **1882: 197:00** | **1883: 197:00*** | **1892: 138:45** | **1902: 124:45** | **1908: 124:45**  *(asterisk = flagged)*
- Flagged value: **197:00**, deviation 65.2 h from other-years median (131.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → San Francisco, California (1882)
- Values by year: **1882: 197:00*** | **1883: 197:00** | **1892: 138:45** | **1902: 124:45** | **1908: 124:45**  *(asterisk = flagged)*
- Flagged value: **197:00**, deviation 65.2 h from other-years median (131.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Boston, Massachusetts (1883)
- Values by year: **1883: 183:20*** | **1892: 133:00** | **1902: 120:00** | **1908: 118:00**  *(asterisk = flagged)*
- Flagged value: **183:20**, deviation 63.3 h from other-years median (120.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → New York, New York (1883)
- Values by year: **1883: 179:15*** | **1892: 130:00** | **1902: 117:00** | **1908: 117:00**  *(asterisk = flagged)*
- Flagged value: **179:15**, deviation 62.2 h from other-years median (117.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Philadelphia, Pennsylvania (1883)
- Values by year: **1883: 176:15*** | **1892: 125:00** | **1902: 114:00** | **1908: 114:00**  *(asterisk = flagged)*
- Flagged value: **176:15**, deviation 62.2 h from other-years median (114.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Baltimore, Maryland (1883)
- Values by year: **1883: 176:10*** | **1892: 125:00** | **1902: 114:00** | **1908: 114:00**  *(asterisk = flagged)*
- Flagged value: **176:10**, deviation 62.2 h from other-years median (114.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Washington, District of Columbia (1883)
- Values by year: **1883: 177:30*** | **1892: 109:00** | **1902: 116:00** | **1908: 116:00**  *(asterisk = flagged)*
- Flagged value: **177:30**, deviation 61.5 h from other-years median (116.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Chicago, Illinois (1883)
- Values by year: **1883: 125:40*** | **1892: 57:20** | **1902: 64:20** | **1908: 64:20**  *(asterisk = flagged)*
- Flagged value: **125:40**, deviation 61.3 h from other-years median (64.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → San Francisco, California (1883)
- Values by year: **1882: 186:00** | **1883: 186:00*** | **1892: 131:45** | **1902: 117:45** | **1908: 115:45**  *(asterisk = flagged)*
- Flagged value: **186:00**, deviation 61.2 h from other-years median (124.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → San Francisco, California (1882)
- Values by year: **1882: 186:00*** | **1883: 186:00** | **1892: 131:45** | **1902: 117:45** | **1908: 115:45**  *(asterisk = flagged)*
- Flagged value: **186:00**, deviation 61.2 h from other-years median (124.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Chicago, Illinois (1883)
- Values by year: **1883: 151:35*** | **1892: 95:25** | **1902: 90:50** | **1908: 90:50**  *(asterisk = flagged)*
- Flagged value: **151:35**, deviation 60.8 h from other-years median (90.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Cincinnati, Ohio (1883)
- Values by year: **1883: 129:15*** | **1892: 61:00** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **129:15**, deviation 59.2 h from other-years median (70.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Pittsburgh, Pennsylvania (1883)
- Values by year: **1883: 164:15*** | **1892: 109:00** | **1902: 102:00**  *(asterisk = flagged)*
- Flagged value: **164:15**, deviation 58.8 h from other-years median (105.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → San Francisco, California (1882)
- Values by year: **1882: 162:29*** | **1883: 162:20** | **1892: 112:00** | **1902: 97:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **162:29**, deviation 57.6 h from other-years median (104.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Frankfort, Kentucky → San Francisco, California (1882)
- Values by year: **1882: 147:30*** | **1883: 147:30** | **1892: 96:15** | **1902: 83:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **147:30**, deviation 57.5 h from other-years median (90.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Frankfort, Kentucky → San Francisco, California (1883)
- Values by year: **1882: 147:30** | **1883: 147:30*** | **1892: 96:15** | **1902: 83:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **147:30**, deviation 57.5 h from other-years median (90.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → San Francisco, California (1883)
- Values by year: **1882: 162:29** | **1883: 162:20*** | **1892: 112:00** | **1902: 97:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **162:20**, deviation 57.5 h from other-years median (104.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → New York, New York (1883)
- Values by year: **1883: 151:11*** | **1892: 120:00** | **1902: 94:00** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **151:11**, deviation 57.2 h from other-years median (94.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → San Francisco, California (1883)
- Values by year: **1882: 163:10** | **1883: 163:10*** | **1892: 115:00** | **1902: 98:55** | **1908: 96:55**  *(asterisk = flagged)*
- Flagged value: **163:10**, deviation 56.2 h from other-years median (106.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → San Francisco, California (1882)
- Values by year: **1882: 163:10*** | **1883: 163:10** | **1892: 115:00** | **1902: 98:55** | **1908: 96:55**  *(asterisk = flagged)*
- Flagged value: **163:10**, deviation 56.2 h from other-years median (106.96 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rome, New York → San Francisco, California (1882)
- Values by year: **1882: 152:05*** | **1883: 152:05** | **1892: 103:15** | **1902: 88:45** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **152:05**, deviation 56.1 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rome, New York → San Francisco, California (1883)
- Values by year: **1882: 152:05** | **1883: 152:05*** | **1892: 103:15** | **1902: 88:45** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **152:05**, deviation 56.1 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albany, New York → San Francisco, California (1883)
- Values by year: **1882: 154:25** | **1883: 154:25*** | **1892: 107:45** | **1902: 89:15** | **1908: 87:28**  *(asterisk = flagged)*
- Flagged value: **154:25**, deviation 55.9 h from other-years median (98.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albany, New York → San Francisco, California (1882)
- Values by year: **1882: 154:25*** | **1883: 154:25** | **1892: 107:45** | **1902: 89:15** | **1908: 87:28**  *(asterisk = flagged)*
- Flagged value: **154:25**, deviation 55.9 h from other-years median (98.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Newport, Rhode Island → San Francisco, California (1882)
- Values by year: **1882: 166:35*** | **1883: 166:35** | **1892: 119:15** | **1902: 103:45** | **1908: 103:28**  *(asterisk = flagged)*
- Flagged value: **166:35**, deviation 55.1 h from other-years median (111.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Newport, Rhode Island → San Francisco, California (1883)
- Values by year: **1882: 166:35** | **1883: 166:35*** | **1892: 119:15** | **1902: 103:45** | **1908: 103:28**  *(asterisk = flagged)*
- Flagged value: **166:35**, deviation 55.1 h from other-years median (111.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Washington, District of Columbia (1882)
- Values by year: **1882: 167:20*** | **1883: 167:20** | **1892: 110:00** | **1902: 112:30** | **1908: 112:30**  *(asterisk = flagged)*
- Flagged value: **167:20**, deviation 54.8 h from other-years median (112.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Washington, District of Columbia (1883)
- Values by year: **1882: 167:20** | **1883: 167:20*** | **1892: 110:00** | **1902: 112:30** | **1908: 112:30**  *(asterisk = flagged)*
- Flagged value: **167:20**, deviation 54.8 h from other-years median (112.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New York, New York → San Francisco, California (1883)
- Values by year: **1882: 159:15** | **1883: 159:15*** | **1892: 111:15** | **1902: 97:45** | **1908: 92:28**  *(asterisk = flagged)*
- Flagged value: **159:15**, deviation 54.8 h from other-years median (104.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New York, New York → San Francisco, California (1882)
- Values by year: **1882: 159:15*** | **1883: 159:15** | **1892: 111:15** | **1902: 97:45** | **1908: 92:28**  *(asterisk = flagged)*
- Flagged value: **159:15**, deviation 54.8 h from other-years median (104.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Baltimore, Maryland (1883)
- Values by year: **1883: 149:08*** | **1892: 116:30** | **1902: 94:30** | **1908: 94:30**  *(asterisk = flagged)*
- Flagged value: **149:08**, deviation 54.6 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montpelier, Vermont → San Francisco, California (1882)
- Values by year: **1882: 170:05*** | **1883: 170:05** | **1892: 127:15** | **1902: 103:45** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **170:05**, deviation 54.6 h from other-years median (115.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montpelier, Vermont → San Francisco, California (1883)
- Values by year: **1882: 170:05** | **1883: 170:05*** | **1892: 127:15** | **1902: 103:45** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **170:05**, deviation 54.6 h from other-years median (115.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → San Francisco, California (1883)
- Values by year: **1883: 151:20*** | **1892: 103:45** | **1902: 96:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **151:20**, deviation 54.6 h from other-years median (96.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 154:05*** | **1883: 154:05** | **1892: 100:00** | **1902: 96:30**  *(asterisk = flagged)*
- Flagged value: **154:05**, deviation 54.1 h from other-years median (100.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → San Francisco, California (1882)
- Values by year: **1882: 148:20*** | **1883: 148:20** | **1892: 93:20** | **1902: 94:15** | **1908: 94:15**  *(asterisk = flagged)*
- Flagged value: **148:20**, deviation 54.1 h from other-years median (94.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 154:05** | **1883: 154:05*** | **1892: 100:00** | **1902: 96:30**  *(asterisk = flagged)*
- Flagged value: **154:05**, deviation 54.1 h from other-years median (100.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → San Francisco, California (1883)
- Values by year: **1882: 148:20** | **1883: 148:20*** | **1892: 93:20** | **1902: 94:15** | **1908: 94:15**  *(asterisk = flagged)*
- Flagged value: **148:20**, deviation 54.1 h from other-years median (94.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Concord, New Hampshire → San Francisco, California (1883)
- Values by year: **1882: 166:00** | **1883: 166:00*** | **1892: 118:15** | **1902: 105:45** | **1908: 105:45**  *(asterisk = flagged)*
- Flagged value: **166:00**, deviation 54.0 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Concord, New Hampshire → San Francisco, California (1882)
- Values by year: **1882: 166:00*** | **1883: 166:00** | **1892: 118:15** | **1902: 105:45** | **1908: 105:45**  *(asterisk = flagged)*
- Flagged value: **166:00**, deviation 54.0 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Chicago, Illinois (1883)
- Values by year: **1882: 141:25** | **1883: 141:25*** | **1892: 90:25** | **1902: 84:30** | **1908: 84:30**  *(asterisk = flagged)*
- Flagged value: **141:25**, deviation 54.0 h from other-years median (87.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Chicago, Illinois (1882)
- Values by year: **1882: 141:25*** | **1883: 141:25** | **1892: 90:25** | **1902: 84:30** | **1908: 84:30**  *(asterisk = flagged)*
- Flagged value: **141:25**, deviation 54.0 h from other-years median (87.46 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → San Francisco, California (1883)
- Values by year: **1882: 173:15** | **1883: 173:15*** | **1892: 126:15** | **1902: 112:45** | **1908: 108:28**  *(asterisk = flagged)*
- Flagged value: **173:15**, deviation 53.8 h from other-years median (119.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Providence, Rhode Island → San Francisco, California (1882)
- Values by year: **1882: 163:30*** | **1883: 163:30** | **1892: 118:45** | **1902: 100:45** | **1908: 100:28**  *(asterisk = flagged)*
- Flagged value: **163:30**, deviation 53.8 h from other-years median (109.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Providence, Rhode Island → San Francisco, California (1883)
- Values by year: **1882: 163:30** | **1883: 163:30*** | **1892: 118:45** | **1902: 100:45** | **1908: 100:28**  *(asterisk = flagged)*
- Flagged value: **163:30**, deviation 53.8 h from other-years median (109.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → San Francisco, California (1882)
- Values by year: **1882: 173:15*** | **1883: 173:15** | **1892: 126:15** | **1902: 112:45** | **1908: 108:28**  *(asterisk = flagged)*
- Flagged value: **173:15**, deviation 53.8 h from other-years median (119.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Charleston, South Carolina (1882)
- Values by year: **1882: 144:29*** | **1883: 144:29** | **1892: 90:45** | **1902: 90:45**  *(asterisk = flagged)*
- Flagged value: **144:29**, deviation 53.7 h from other-years median (90.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Charleston, South Carolina (1883)
- Values by year: **1882: 144:29** | **1883: 144:29*** | **1892: 90:45** | **1902: 90:45**  *(asterisk = flagged)*
- Flagged value: **144:29**, deviation 53.7 h from other-years median (90.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Washington, District of Columbia (1883)
- Values by year: **1883: 148:58*** | **1892: 115:20** | **1902: 95:20** | **1908: 95:20**  *(asterisk = flagged)*
- Flagged value: **148:58**, deviation 53.6 h from other-years median (95.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → San Francisco, California (1882)
- Values by year: **1882: 161:35*** | **1883: 161:35** | **1892: 116:15** | **1902: 99:45** | **1908: 99:45**  *(asterisk = flagged)*
- Flagged value: **161:35**, deviation 53.6 h from other-years median (108.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → San Francisco, California (1883)
- Values by year: **1882: 161:35** | **1883: 161:35*** | **1892: 116:15** | **1902: 99:45** | **1908: 99:45**  *(asterisk = flagged)*
- Flagged value: **161:35**, deviation 53.6 h from other-years median (108.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hartford, Connecticut → San Francisco, California (1883)
- Values by year: **1882: 160:27** | **1883: 160:27*** | **1892: 114:00** | **1902: 99:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **160:27**, deviation 53.6 h from other-years median (106.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hartford, Connecticut → San Francisco, California (1882)
- Values by year: **1882: 160:27*** | **1883: 160:27** | **1892: 114:00** | **1902: 99:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **160:27**, deviation 53.6 h from other-years median (106.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Boston, Massachusetts (1883)
- Values by year: **1883: 156:11*** | **1892: 127:50** | **1902: 102:50** | **1908: 102:50**  *(asterisk = flagged)*
- Flagged value: **156:11**, deviation 53.4 h from other-years median (102.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Cincinnati, Ohio (1882)
- Values by year: **1882: 99:45*** | **1883: 99:45** | **1892: 47:00** | **1902: 47:00**  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 52.8 h from other-years median (47.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Cincinnati, Ohio (1883)
- Values by year: **1882: 99:45** | **1883: 99:45*** | **1892: 47:00** | **1902: 47:00**  *(asterisk = flagged)*
- Flagged value: **99:45**, deviation 52.8 h from other-years median (47.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → San Francisco, California (1882)
- Values by year: **1882: 156:20*** | **1883: 156:20** | **1892: 90:20** | **1902: 103:45** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **156:20**, deviation 52.6 h from other-years median (103.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → San Francisco, California (1883)
- Values by year: **1882: 156:20** | **1883: 156:20*** | **1892: 90:20** | **1902: 103:45** | **1908: 103:45**  *(asterisk = flagged)*
- Flagged value: **156:20**, deviation 52.6 h from other-years median (103.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Philadelphia, Pennsylvania (1883)
- Values by year: **1883: 146:33*** | **1892: 118:00** | **1902: 94:00** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **146:33**, deviation 52.5 h from other-years median (94.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Madison, Wisconsin → San Francisco, California (1883)
- Values by year: **1882: 132:19** | **1883: 132:19*** | **1892: 86:15** | **1902: 73:45** | **1908: 73:45**  *(asterisk = flagged)*
- Flagged value: **132:19**, deviation 52.3 h from other-years median (80.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Madison, Wisconsin → San Francisco, California (1882)
- Values by year: **1882: 132:19*** | **1883: 132:19** | **1892: 86:15** | **1902: 73:45** | **1908: 73:45**  *(asterisk = flagged)*
- Flagged value: **132:19**, deviation 52.3 h from other-years median (80.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Buffalo, New York → San Francisco, California (1883)
- Values by year: **1882: 143:30** | **1883: 143:30*** | **1892: 99:45** | **1902: 83:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **143:30**, deviation 51.8 h from other-years median (91.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Buffalo, New York → San Francisco, California (1882)
- Values by year: **1882: 143:30*** | **1883: 143:30** | **1892: 99:45** | **1902: 83:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **143:30**, deviation 51.8 h from other-years median (91.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Boston, Massachusetts (1883)
- Values by year: **1882: 173:10** | **1883: 173:10*** | **1892: 128:09** | **1902: 115:00** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **173:10**, deviation 51.6 h from other-years median (121.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Boston, Massachusetts (1882)
- Values by year: **1882: 173:10*** | **1883: 173:10** | **1892: 128:09** | **1902: 115:00** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **173:10**, deviation 51.6 h from other-years median (121.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Massachusetts → San Francisco, California (1882)
- Values by year: **1882: 158:05*** | **1883: 158:05** | **1892: 112:15** | **1902: 100:45** | **1908: 97:45**  *(asterisk = flagged)*
- Flagged value: **158:05**, deviation 51.6 h from other-years median (106.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → New York, New York (1882)
- Values by year: **1882: 169:05*** | **1883: 169:05** | **1892: 121:00** | **1902: 114:00** | **1908: 114:00**  *(asterisk = flagged)*
- Flagged value: **169:05**, deviation 51.6 h from other-years median (117.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → New York, New York (1883)
- Values by year: **1882: 169:05** | **1883: 169:05*** | **1892: 121:00** | **1902: 114:00** | **1908: 114:00**  *(asterisk = flagged)*
- Flagged value: **169:05**, deviation 51.6 h from other-years median (117.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Massachusetts → San Francisco, California (1883)
- Values by year: **1882: 158:05** | **1883: 158:05*** | **1892: 112:15** | **1902: 100:45** | **1908: 97:45**  *(asterisk = flagged)*
- Flagged value: **158:05**, deviation 51.6 h from other-years median (106.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Harrisburg, Pennsylvania → San Francisco, California (1882)
- Values by year: **1882: 141:09*** | **1883: 141:00** | **1902: 89:45** | **1908: 89:28**  *(asterisk = flagged)*
- Flagged value: **141:09**, deviation 51.4 h from other-years median (89.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Harrisburg, Pennsylvania → San Francisco, California (1883)
- Values by year: **1882: 141:09** | **1883: 141:00*** | **1902: 89:45** | **1908: 89:28**  *(asterisk = flagged)*
- Flagged value: **141:00**, deviation 51.2 h from other-years median (89.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### White River Junction, Vermont → San Francisco, California (1883)
- Values by year: **1882: 166:45** | **1883: 166:45*** | **1892: 125:15** | **1902: 105:45** | **1908: 105:45**  *(asterisk = flagged)*
- Flagged value: **166:45**, deviation 51.2 h from other-years median (115.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### White River Junction, Vermont → San Francisco, California (1882)
- Values by year: **1882: 166:45*** | **1883: 166:45** | **1892: 125:15** | **1902: 105:45** | **1908: 105:45**  *(asterisk = flagged)*
- Flagged value: **166:45**, deviation 51.2 h from other-years median (115.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Boston, Massachusetts (1883)
- Values by year: **1882: 161:10** | **1883: 161:10*** | **1892: 111:30** | **1902: 108:30** | **1908: 107:30**  *(asterisk = flagged)*
- Flagged value: **161:10**, deviation 51.2 h from other-years median (110.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Boston, Massachusetts (1882)
- Values by year: **1882: 161:10*** | **1883: 161:10** | **1892: 111:30** | **1902: 108:30** | **1908: 107:30**  *(asterisk = flagged)*
- Flagged value: **161:10**, deviation 51.2 h from other-years median (110.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Charleston, South Carolina (1882)
- Values by year: **1882: 171:27*** | **1883: 171:27** | **1892: 120:45** | **1902: 120:00** | **1908: 120:00**  *(asterisk = flagged)*
- Flagged value: **171:27**, deviation 51.1 h from other-years median (120.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Charleston, South Carolina (1883)
- Values by year: **1882: 171:27** | **1883: 171:27*** | **1892: 120:45** | **1902: 120:00** | **1908: 120:00**  *(asterisk = flagged)*
- Flagged value: **171:27**, deviation 51.1 h from other-years median (120.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Memphis, Tennessee → San Francisco, California (1882)
- Values by year: **1882: 145:00*** | **1883: 145:00** | **1892: 99:15** | **1902: 88:45** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **145:00**, deviation 51.0 h from other-years median (94.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Memphis, Tennessee → San Francisco, California (1883)
- Values by year: **1882: 145:00** | **1883: 145:00*** | **1892: 99:15** | **1902: 88:45** | **1908: 88:28**  *(asterisk = flagged)*
- Flagged value: **145:00**, deviation 51.0 h from other-years median (94.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, South Carolina → San Francisco, California (1883)
- Values by year: **1882: 169:15** | **1883: 169:15*** | **1892: 126:15** | **1902: 110:45** | **1908: 108:28**  *(asterisk = flagged)*
- Flagged value: **169:15**, deviation 50.8 h from other-years median (118.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, South Carolina → San Francisco, California (1882)
- Values by year: **1882: 169:15*** | **1883: 169:15** | **1892: 126:15** | **1902: 110:45** | **1908: 108:28**  *(asterisk = flagged)*
- Flagged value: **169:15**, deviation 50.8 h from other-years median (118.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lynchburg, Virginia → San Francisco, California (1883)
- Values by year: **1882: 150:22** | **1883: 150:22*** | **1902: 99:45** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **150:22**, deviation 50.6 h from other-years median (99.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lynchburg, Virginia → San Francisco, California (1882)
- Values by year: **1882: 150:22*** | **1883: 150:22** | **1902: 99:45** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **150:22**, deviation 50.6 h from other-years median (99.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 166:05*** | **1883: 166:05** | **1892: 119:00** | **1902: 112:00** | **1908: 112:00**  *(asterisk = flagged)*
- Flagged value: **166:05**, deviation 50.6 h from other-years median (115.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 166:05** | **1883: 166:05*** | **1892: 119:00** | **1902: 112:00** | **1908: 112:00**  *(asterisk = flagged)*
- Flagged value: **166:05**, deviation 50.6 h from other-years median (115.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Boston, Massachusetts (1882)
- Values by year: **1882: 124:18*** | **1883: 124:13** | **1892: 73:50** | **1902: 68:50**  *(asterisk = flagged)*
- Flagged value: **124:18**, deviation 50.5 h from other-years median (73.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Boston, Massachusetts (1883)
- Values by year: **1882: 124:18** | **1883: 124:13*** | **1892: 73:50** | **1902: 68:50**  *(asterisk = flagged)*
- Flagged value: **124:13**, deviation 50.4 h from other-years median (73.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Baltimore, Maryland (1883)
- Values by year: **1882: 166:00** | **1883: 166:00*** | **1892: 121:00** | **1902: 111:00** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **166:00**, deviation 50.0 h from other-years median (116.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Baltimore, Maryland (1882)
- Values by year: **1882: 166:00*** | **1883: 166:00** | **1892: 121:00** | **1902: 111:00** | **1908: 111:00**  *(asterisk = flagged)*
- Flagged value: **166:00**, deviation 50.0 h from other-years median (116.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → San Francisco, California (1883)
- Values by year: **1882: 169:37** | **1883: 169:37*** | **1892: 133:15** | **1902: 106:45** | **1908: 106:28**  *(asterisk = flagged)*
- Flagged value: **169:37**, deviation 49.6 h from other-years median (120.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → San Francisco, California (1882)
- Values by year: **1882: 169:37*** | **1883: 169:37** | **1892: 133:15** | **1902: 106:45** | **1908: 106:28**  *(asterisk = flagged)*
- Flagged value: **169:37**, deviation 49.6 h from other-years median (120.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dubuque, Iowa → San Francisco, California (1883)
- Values by year: **1882: 124:54** | **1883: 124:54*** | **1892: 84:15** | **1902: 60:45** | **1908: 67:08**  *(asterisk = flagged)*
- Flagged value: **124:54**, deviation 49.2 h from other-years median (75.69 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dubuque, Iowa → San Francisco, California (1882)
- Values by year: **1882: 124:54*** | **1883: 124:54** | **1892: 84:15** | **1902: 60:45** | **1908: 67:08**  *(asterisk = flagged)*
- Flagged value: **124:54**, deviation 49.2 h from other-years median (75.69 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Nashville, Tennessee → San Francisco, California (1883)
- Values by year: **1882: 133:40** | **1883: 138:40*** | **1892: 96:15** | **1902: 82:45** | **1908: 82:28**  *(asterisk = flagged)*
- Flagged value: **138:40**, deviation 49.2 h from other-years median (89.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Saint Louis, Missouri (1883)
- Values by year: **1883: 138:32*** | **1892: 91:30** | **1902: 89:30** | **1908: 89:30**  *(asterisk = flagged)*
- Flagged value: **138:32**, deviation 49.0 h from other-years median (89.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Saint Louis, Missouri (1883)
- Values by year: **1882: 99:55** | **1883: 99:55*** | **1892: 51:00** | **1902: 40:00**  *(asterisk = flagged)*
- Flagged value: **99:55**, deviation 48.9 h from other-years median (51.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Saint Louis, Missouri (1882)
- Values by year: **1882: 99:55*** | **1883: 99:55** | **1892: 51:00** | **1902: 40:00**  *(asterisk = flagged)*
- Flagged value: **99:55**, deviation 48.9 h from other-years median (51.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Diego, California → Cincinnati, Ohio (1883)
- Values by year: **1883: 151:40*** | **1892: 120:50** | **1902: 103:00** | **1908: 103:00**  *(asterisk = flagged)*
- Flagged value: **151:40**, deviation 48.7 h from other-years median (103.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → San Francisco, California (1883)
- Values by year: **1882: 170:40** | **1883: 170:40*** | **1892: 139:15** | **1902: 105:45** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **170:40**, deviation 48.2 h from other-years median (122.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → San Francisco, California (1882)
- Values by year: **1882: 170:40*** | **1883: 170:40** | **1892: 139:15** | **1902: 105:45** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **170:40**, deviation 48.2 h from other-years median (122.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vicksburg, Mississippi → San Francisco, California (1883)
- Values by year: **1883: 144:25*** | **1892: 107:15** | **1902: 96:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **144:25**, deviation 47.7 h from other-years median (96.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Maine → San Francisco, California (1882)
- Values by year: **1882: 166:35*** | **1883: 166:35** | **1892: 130:15** | **1902: 107:45** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **166:35**, deviation 47.6 h from other-years median (119.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Portland, Maine → San Francisco, California (1883)
- Values by year: **1882: 166:35** | **1883: 166:35*** | **1892: 130:15** | **1902: 107:45** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **166:35**, deviation 47.6 h from other-years median (119.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Wayne, Indiana → San Francisco, California (1883)
- Values by year: **1882: 123:10** | **1883: 123:10*** | **1902: 75:45** | **1908: 73:45**  *(asterisk = flagged)*
- Flagged value: **123:10**, deviation 47.4 h from other-years median (75.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Wayne, Indiana → San Francisco, California (1882)
- Values by year: **1882: 123:10*** | **1883: 123:10** | **1902: 75:45** | **1908: 73:45**  *(asterisk = flagged)*
- Flagged value: **123:10**, deviation 47.4 h from other-years median (75.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Georgia → San Francisco, California (1882)
- Values by year: **1882: 162:05*** | **1883: 162:05** | **1892: 126:40** | **1902: 102:45** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **162:05**, deviation 47.4 h from other-years median (114.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Georgia → San Francisco, California (1883)
- Values by year: **1882: 162:05** | **1883: 162:05*** | **1892: 126:40** | **1902: 102:45** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **162:05**, deviation 47.4 h from other-years median (114.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → San Francisco, California (1883)
- Values by year: **1882: 127:37** | **1883: 127:37*** | **1892: 80:45** | **1902: 75:45**  *(asterisk = flagged)*
- Flagged value: **127:37**, deviation 46.9 h from other-years median (80.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → San Francisco, California (1882)
- Values by year: **1882: 127:37*** | **1883: 127:37** | **1892: 80:45** | **1902: 75:45**  *(asterisk = flagged)*
- Flagged value: **127:37**, deviation 46.9 h from other-years median (80.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Saint Louis, Missouri (1883)
- Values by year: **1883: 112:20*** | **1892: 85:30** | **1902: 65:30** | **1908: 65:30**  *(asterisk = flagged)*
- Flagged value: **112:20**, deviation 46.8 h from other-years median (65.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chicago, Illinois → San Francisco, California (1882)
- Values by year: **1882: 121:24*** | **1883: 121:24** | **1892: 80:15** | **1902: 69:25** | **1908: 65:15**  *(asterisk = flagged)*
- Flagged value: **121:24**, deviation 46.6 h from other-years median (74.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chicago, Illinois → San Francisco, California (1883)
- Values by year: **1882: 121:24** | **1883: 121:24*** | **1892: 80:15** | **1902: 69:25** | **1908: 65:15**  *(asterisk = flagged)*
- Flagged value: **121:24**, deviation 46.6 h from other-years median (74.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Charleston, South Carolina (1883)
- Values by year: **1883: 166:27*** | **1892: 120:45** | **1902: 120:45** | **1908: 120:45**  *(asterisk = flagged)*
- Flagged value: **166:27**, deviation 45.7 h from other-years median (120.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Boston, Massachusetts (1883)
- Values by year: **1882: 157:10** | **1883: 157:10*** | **1892: 117:30** | **1902: 105:30** | **1908: 103:30**  *(asterisk = flagged)*
- Flagged value: **157:10**, deviation 45.7 h from other-years median (111.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Boston, Massachusetts (1882)
- Values by year: **1882: 157:10*** | **1883: 157:10** | **1892: 117:30** | **1902: 105:30** | **1908: 103:30**  *(asterisk = flagged)*
- Flagged value: **157:10**, deviation 45.7 h from other-years median (111.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cleveland, Ohio → San Francisco, California (1883)
- Values by year: **1882: 132:42** | **1883: 132:42*** | **1892: 94:15** | **1902: 79:55** | **1908: 79:55**  *(asterisk = flagged)*
- Flagged value: **132:42**, deviation 45.6 h from other-years median (87.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cleveland, Ohio → San Francisco, California (1882)
- Values by year: **1882: 132:42*** | **1883: 132:42** | **1892: 94:15** | **1902: 79:55** | **1908: 79:55**  *(asterisk = flagged)*
- Flagged value: **132:42**, deviation 45.6 h from other-years median (87.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Pittsburgh, Pennsylvania (1883)
- Values by year: **1883: 137:27*** | **1892: 97:00** | **1902: 87:00**  *(asterisk = flagged)*
- Flagged value: **137:27**, deviation 45.5 h from other-years median (92.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbia, South Carolina → San Francisco, California (1883)
- Values by year: **1882: 162:45** | **1883: 162:45*** | **1892: 124:15** | **1902: 110:45** | **1908: 110:28**  *(asterisk = flagged)*
- Flagged value: **162:45**, deviation 45.2 h from other-years median (117.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbia, South Carolina → San Francisco, California (1882)
- Values by year: **1882: 162:45*** | **1883: 162:45** | **1892: 124:15** | **1902: 110:45** | **1908: 110:28**  *(asterisk = flagged)*
- Flagged value: **162:45**, deviation 45.2 h from other-years median (117.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jefferson City, Missouri → San Francisco, California (1883)
- Values by year: **1882: 119:42** | **1883: 119:42*** | **1892: 78:15** | **1902: 70:45** | **1908: 70:45**  *(asterisk = flagged)*
- Flagged value: **119:42**, deviation 45.2 h from other-years median (74.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jefferson City, Missouri → San Francisco, California (1882)
- Values by year: **1882: 119:42*** | **1883: 119:42** | **1892: 78:15** | **1902: 70:45** | **1908: 70:45**  *(asterisk = flagged)*
- Flagged value: **119:42**, deviation 45.2 h from other-years median (74.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → San Francisco, California (1882)
- Values by year: **1882: 147:54*** | **1883: 147:54** | **1892: 102:45** | **1902: 94:45**  *(asterisk = flagged)*
- Flagged value: **147:54**, deviation 45.1 h from other-years median (102.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → San Francisco, California (1883)
- Values by year: **1882: 147:54** | **1883: 147:54*** | **1892: 102:45** | **1902: 94:45**  *(asterisk = flagged)*
- Flagged value: **147:54**, deviation 45.1 h from other-years median (102.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Milwaukee, Wisconsin → San Francisco, California (1882)
- Values by year: **1882: 125:14*** | **1883: 125:14** | **1892: 89:15** | **1902: 71:45** | **1908: 71:45**  *(asterisk = flagged)*
- Flagged value: **125:14**, deviation 44.7 h from other-years median (80.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Milwaukee, Wisconsin → San Francisco, California (1883)
- Values by year: **1882: 125:14** | **1883: 125:14*** | **1892: 89:15** | **1902: 71:45** | **1908: 71:45**  *(asterisk = flagged)*
- Flagged value: **125:14**, deviation 44.7 h from other-years median (80.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hot Springs, Arkansas → San Francisco, California (1883)
- Values by year: **1883: 135:28*** | **1892: 108:15** | **1902: 90:45** | **1908: 90:45**  *(asterisk = flagged)*
- Flagged value: **135:28**, deviation 44.7 h from other-years median (90.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Shreveport, Louisiana → San Francisco, California (1883)
- Values by year: **1882: 147:46** | **1883: 147:46*** | **1892: 106:15** | **1902: 99:55** | **1908: 99:55**  *(asterisk = flagged)*
- Flagged value: **147:46**, deviation 44.7 h from other-years median (103.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Shreveport, Louisiana → San Francisco, California (1882)
- Values by year: **1882: 147:46*** | **1883: 147:46** | **1892: 106:15** | **1902: 99:55** | **1908: 99:55**  *(asterisk = flagged)*
- Flagged value: **147:46**, deviation 44.7 h from other-years median (103.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Toledo, Ohio → San Francisco, California (1883)
- Values by year: **1882: 129:16** | **1883: 129:16*** | **1892: 91:45** | **1902: 77:45** | **1908: 77:45**  *(asterisk = flagged)*
- Flagged value: **129:16**, deviation 44.5 h from other-years median (84.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Toledo, Ohio → San Francisco, California (1882)
- Values by year: **1882: 129:16*** | **1883: 129:16** | **1892: 91:45** | **1902: 77:45** | **1908: 77:45**  *(asterisk = flagged)*
- Flagged value: **129:16**, deviation 44.5 h from other-years median (84.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Saint Louis, Missouri (1883)
- Values by year: **1883: 118:25*** | **1892: 70:00** | **1902: 74:00** | **1908: 74:00**  *(asterisk = flagged)*
- Flagged value: **118:25**, deviation 44.4 h from other-years median (74.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Smith, Arkansas → San Francisco, California (1882)
- Values by year: **1882: 141:21*** | **1883: 141:21** | **1892: 105:15** | **1902: 88:45** | **1908: 88:35**  *(asterisk = flagged)*
- Flagged value: **141:21**, deviation 44.4 h from other-years median (97.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Smith, Arkansas → San Francisco, California (1883)
- Values by year: **1882: 141:21** | **1883: 141:21*** | **1892: 105:15** | **1902: 88:45** | **1908: 88:35**  *(asterisk = flagged)*
- Flagged value: **141:21**, deviation 44.4 h from other-years median (97.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Nashville, Tennessee → San Francisco, California (1882)
- Values by year: **1882: 133:40*** | **1883: 138:40** | **1892: 96:15** | **1902: 82:45** | **1908: 82:28**  *(asterisk = flagged)*
- Flagged value: **133:40**, deviation 44.2 h from other-years median (89.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Norfolk, Virginia → San Francisco, California (1882)
- Values by year: **1882: 152:35*** | **1883: 152:35** | **1892: 116:15** | **1902: 100:45** | **1908: 100:28**  *(asterisk = flagged)*
- Flagged value: **152:35**, deviation 44.1 h from other-years median (108.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Norfolk, Virginia → San Francisco, California (1883)
- Values by year: **1882: 152:35** | **1883: 152:35*** | **1892: 116:15** | **1902: 100:45** | **1908: 100:28**  *(asterisk = flagged)*
- Flagged value: **152:35**, deviation 44.1 h from other-years median (108.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prairie du Chien, Wisconsin → San Francisco, California (1882)
- Values by year: **1882: 128:06*** | **1883: 128:06** | **1892: 89:15** | **1902: 79:45** | **1908: 79:45**  *(asterisk = flagged)*
- Flagged value: **128:06**, deviation 43.6 h from other-years median (84.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prairie du Chien, Wisconsin → San Francisco, California (1883)
- Values by year: **1882: 128:06** | **1883: 128:06*** | **1892: 89:15** | **1902: 79:45** | **1908: 79:45**  *(asterisk = flagged)*
- Flagged value: **128:06**, deviation 43.6 h from other-years median (84.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Burlington, Iowa → San Francisco, California (1882)
- Values by year: **1882: 113:29*** | **1883: 113:29** | **1892: 75:15** | **1902: 64:45** | **1908: 64:45**  *(asterisk = flagged)*
- Flagged value: **113:29**, deviation 43.5 h from other-years median (70.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Burlington, Iowa → San Francisco, California (1883)
- Values by year: **1882: 113:29** | **1883: 113:29*** | **1892: 75:15** | **1902: 64:45** | **1908: 64:45**  *(asterisk = flagged)*
- Flagged value: **113:29**, deviation 43.5 h from other-years median (70.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Saint Louis, Missouri (1883)
- Values by year: **1882: 128:22** | **1883: 128:22*** | **1892: 86:30** | **1902: 83:30** | **1908: 83:30**  *(asterisk = flagged)*
- Flagged value: **128:22**, deviation 43.4 h from other-years median (85.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Saint Louis, Missouri (1882)
- Values by year: **1882: 128:22*** | **1883: 128:22** | **1892: 86:30** | **1902: 83:30** | **1908: 83:30**  *(asterisk = flagged)*
- Flagged value: **128:22**, deviation 43.4 h from other-years median (85.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → Omaha, Nebraska (1883)
- Values by year: **1883: 102:20*** | **1892: 59:00** | **1902: 59:00** | **1908: 59:00**  *(asterisk = flagged)*
- Flagged value: **102:20**, deviation 43.3 h from other-years median (59.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bay City, Michigan → San Francisco, California (1882)
- Values by year: **1882: 135:17*** | **1883: 135:17** | **1892: 101:15** | **1902: 82:45** | **1908: 81:45**  *(asterisk = flagged)*
- Flagged value: **135:17**, deviation 43.3 h from other-years median (92.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bay City, Michigan → San Francisco, California (1883)
- Values by year: **1882: 135:17** | **1883: 135:17*** | **1892: 101:15** | **1902: 82:45** | **1908: 81:45**  *(asterisk = flagged)*
- Flagged value: **135:17**, deviation 43.3 h from other-years median (92.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Charleston, South Carolina (1883)
- Values by year: **1882: 92:29** | **1883: 92:59*** | **1892: 50:00** | **1902: 50:00** | **1908: 50:00**  *(asterisk = flagged)*
- Flagged value: **92:59**, deviation 43.0 h from other-years median (50.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Knoxville, Tennessee → San Francisco, California (1883)
- Values by year: **1882: 150:28** | **1883: 150:28*** | **1892: 116:15** | **1902: 98:45** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **150:28**, deviation 43.0 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Knoxville, Tennessee → San Francisco, California (1882)
- Values by year: **1882: 150:28*** | **1883: 150:28** | **1892: 116:15** | **1902: 98:45** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **150:28**, deviation 43.0 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → San Francisco, California (1882)
- Values by year: **1882: 150:20*** | **1883: 150:20** | **1892: 108:15** | **1902: 95:45** | **1908: 106:45**  *(asterisk = flagged)*
- Flagged value: **150:20**, deviation 42.8 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → San Francisco, California (1883)
- Values by year: **1882: 150:20** | **1883: 150:20*** | **1892: 108:15** | **1902: 95:45** | **1908: 106:45**  *(asterisk = flagged)*
- Flagged value: **150:20**, deviation 42.8 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Baltimore, Maryland (1882)
- Values by year: **1882: 114:00*** | **1883: 114:00** | **1892: 71:30** | **1902: 65:30**  *(asterisk = flagged)*
- Flagged value: **114:00**, deviation 42.5 h from other-years median (71.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Baltimore, Maryland (1883)
- Values by year: **1882: 114:00** | **1883: 114:00*** | **1892: 71:30** | **1902: 65:30**  *(asterisk = flagged)*
- Flagged value: **114:00**, deviation 42.5 h from other-years median (71.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Charleston, South Carolina (1882)
- Values by year: **1882: 92:29*** | **1883: 92:59** | **1892: 50:00** | **1902: 50:00** | **1908: 50:00**  *(asterisk = flagged)*
- Flagged value: **92:29**, deviation 42.5 h from other-years median (50.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 96:55** | **1883: 96:55*** | **1892: 54:50** | **1902: 50:50**  *(asterisk = flagged)*
- Flagged value: **96:55**, deviation 42.1 h from other-years median (54.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 96:55*** | **1883: 96:55** | **1892: 54:50** | **1902: 50:50**  *(asterisk = flagged)*
- Flagged value: **96:55**, deviation 42.1 h from other-years median (54.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dover, Delaware → San Francisco, California (1883)
- Values by year: **1882: 149:14** | **1883: 149:18*** | **1892: 118:15** | **1902: 96:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **149:18**, deviation 41.8 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dover, Delaware → San Francisco, California (1882)
- Values by year: **1882: 149:14*** | **1883: 149:18** | **1892: 118:15** | **1902: 96:45** | **1908: 96:45**  *(asterisk = flagged)*
- Flagged value: **149:14**, deviation 41.7 h from other-years median (107.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Washington, District of Columbia → San Francisco, California (1883)
- Values by year: **1882: 145:15** | **1883: 145:15*** | **1892: 112:15** | **1902: 94:05** | **1908: 95:05**  *(asterisk = flagged)*
- Flagged value: **145:15**, deviation 41.6 h from other-years median (103.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Washington, District of Columbia → San Francisco, California (1882)
- Values by year: **1882: 145:15*** | **1883: 145:15** | **1892: 112:15** | **1902: 94:05** | **1908: 95:05**  *(asterisk = flagged)*
- Flagged value: **145:15**, deviation 41.6 h from other-years median (103.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Charleston, South Carolina (1882)
- Values by year: **1882: 143:50*** | **1883: 143:50** | **1892: 109:45** | **1902: 94:45** | **1908: 94:45**  *(asterisk = flagged)*
- Flagged value: **143:50**, deviation 41.6 h from other-years median (102.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Charleston, South Carolina (1883)
- Values by year: **1882: 143:50** | **1883: 143:50*** | **1892: 109:45** | **1902: 94:45** | **1908: 94:45**  *(asterisk = flagged)*
- Flagged value: **143:50**, deviation 41.6 h from other-years median (102.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Washington, District of Columbia (1882)
- Values by year: **1882: 145:45*** | **1883: 145:45** | **1892: 106:55** | **1902: 101:55** | **1908: 101:55**  *(asterisk = flagged)*
- Flagged value: **145:45**, deviation 41.3 h from other-years median (104.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Washington, District of Columbia (1883)
- Values by year: **1882: 145:45** | **1883: 145:45*** | **1892: 106:55** | **1902: 101:55** | **1908: 101:55**  *(asterisk = flagged)*
- Flagged value: **145:45**, deviation 41.3 h from other-years median (104.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cape May, New Jersey → San Francisco, California (1883)
- Values by year: **1882: 147:40** | **1883: 147:40*** | **1892: 116:45** | **1902: 96:00** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **147:40**, deviation 41.3 h from other-years median (106.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cape May, New Jersey → San Francisco, California (1882)
- Values by year: **1882: 147:40*** | **1883: 147:40** | **1892: 116:45** | **1902: 96:00** | **1908: 94:00**  *(asterisk = flagged)*
- Flagged value: **147:40**, deviation 41.3 h from other-years median (106.38 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kansas City, Missouri → San Francisco, California (1882)
- Values by year: **1882: 111:27*** | **1883: 111:27** | **1892: 75:15** | **1902: 65:15** | **1908: 65:15**  *(asterisk = flagged)*
- Flagged value: **111:27**, deviation 41.2 h from other-years median (70.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kansas City, Missouri → San Francisco, California (1883)
- Values by year: **1882: 111:27** | **1883: 111:27*** | **1892: 75:15** | **1902: 65:15** | **1908: 65:15**  *(asterisk = flagged)*
- Flagged value: **111:27**, deviation 41.2 h from other-years median (70.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → New York, New York (1883)
- Values by year: **1882: 147:30** | **1883: 147:30*** | **1892: 111:50** | **1902: 100:50** | **1908: 100:50**  *(asterisk = flagged)*
- Flagged value: **147:30**, deviation 41.2 h from other-years median (106.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → New York, New York (1882)
- Values by year: **1882: 147:30*** | **1883: 147:30** | **1892: 111:50** | **1902: 100:50** | **1908: 100:50**  *(asterisk = flagged)*
- Flagged value: **147:30**, deviation 41.2 h from other-years median (106.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wheeling, West Virginia → San Francisco, California (1882)
- Values by year: **1882: 134:35*** | **1883: 134:35** | **1892: 103:15** | **1902: 83:45** | **1908: 83:15**  *(asterisk = flagged)*
- Flagged value: **134:35**, deviation 41.1 h from other-years median (93.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wheeling, West Virginia → San Francisco, California (1883)
- Values by year: **1882: 134:35** | **1883: 134:35*** | **1892: 103:15** | **1902: 83:45** | **1908: 83:15**  *(asterisk = flagged)*
- Flagged value: **134:35**, deviation 41.1 h from other-years median (93.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Philadelphia, Pennsylvania → San Francisco, California (1883)
- Values by year: **1882: 143:55** | **1883: 143:55*** | **1892: 112:15** | **1902: 93:45** | **1908: 93:28**  *(asterisk = flagged)*
- Flagged value: **143:55**, deviation 40.9 h from other-years median (103.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Philadelphia, Pennsylvania → San Francisco, California (1882)
- Values by year: **1882: 143:55*** | **1883: 143:55** | **1892: 112:15** | **1902: 93:45** | **1908: 93:28**  *(asterisk = flagged)*
- Flagged value: **143:55**, deviation 40.9 h from other-years median (103.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → New York, New York (1883)
- Values by year: **1882: 150:55** | **1883: 150:55*** | **1892: 114:30** | **1902: 106:00** | **1908: 105:00**  *(asterisk = flagged)*
- Flagged value: **150:55**, deviation 40.7 h from other-years median (110.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → New York, New York (1882)
- Values by year: **1882: 150:55*** | **1883: 150:55** | **1892: 114:30** | **1902: 106:00** | **1908: 105:00**  *(asterisk = flagged)*
- Flagged value: **150:55**, deviation 40.7 h from other-years median (110.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Omaha, Nebraska (1882)
- Values by year: **1882: 71:50*** | **1883: 71:50** | **1892: 35:10** | **1902: 27:10** | **1908: 27:10**  *(asterisk = flagged)*
- Flagged value: **71:50**, deviation 40.7 h from other-years median (31.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Omaha, Nebraska (1883)
- Values by year: **1882: 71:50** | **1883: 71:50*** | **1892: 35:10** | **1902: 27:10** | **1908: 27:10**  *(asterisk = flagged)*
- Flagged value: **71:50**, deviation 40.7 h from other-years median (31.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Staunton, Virginia → San Francisco, California (1882)
- Values by year: **1882: 151:35*** | **1883: 151:35** | **1892: 119:15** | **1902: 102:45** | **1908: 99:28**  *(asterisk = flagged)*
- Flagged value: **151:35**, deviation 40.6 h from other-years median (111.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Staunton, Virginia → San Francisco, California (1883)
- Values by year: **1882: 151:35** | **1883: 151:35*** | **1892: 119:15** | **1902: 102:45** | **1908: 99:28**  *(asterisk = flagged)*
- Flagged value: **151:35**, deviation 40.6 h from other-years median (111.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charlotte, North Carolina → San Francisco, California (1883)
- Values by year: **1882: 158:10** | **1883: 158:10*** | **1892: 127:45** | **1902: 107:45** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **158:10**, deviation 40.4 h from other-years median (117.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charlotte, North Carolina → San Francisco, California (1882)
- Values by year: **1882: 158:10*** | **1883: 158:10** | **1892: 127:45** | **1902: 107:45** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **158:10**, deviation 40.4 h from other-years median (117.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lansing, Michigan → San Francisco, California (1883)
- Values by year: **1882: 129:22** | **1883: 129:22*** | **1892: 97:15** | **1902: 80:45** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **129:22**, deviation 40.4 h from other-years median (89.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lansing, Michigan → San Francisco, California (1882)
- Values by year: **1882: 129:22*** | **1883: 129:22** | **1892: 97:15** | **1902: 80:45** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **129:22**, deviation 40.4 h from other-years median (89.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Cincinnati, Ohio (1883)
- Values by year: **1883: 125:05*** | **1892: 102:50** | **1902: 84:50** | **1908: 84:50**  *(asterisk = flagged)*
- Flagged value: **125:05**, deviation 40.2 h from other-years median (84.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cumberland, Maryland → San Francisco, California (1883)
- Values by year: **1882: 136:45** | **1883: 136:45*** | **1892: 105:15** | **1902: 87:45** | **1908: 87:45**  *(asterisk = flagged)*
- Flagged value: **136:45**, deviation 40.2 h from other-years median (96.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cumberland, Maryland → San Francisco, California (1882)
- Values by year: **1882: 136:45*** | **1883: 136:45** | **1892: 105:15** | **1902: 87:45** | **1908: 87:45**  *(asterisk = flagged)*
- Flagged value: **136:45**, deviation 40.2 h from other-years median (96.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Chicago, Illinois (1883)
- Values by year: **1883: 126:08*** | **1892: 98:55** | **1902: 85:55** | **1908: 85:55**  *(asterisk = flagged)*
- Flagged value: **126:08**, deviation 40.2 h from other-years median (85.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Trenton, New Jersey → San Francisco, California (1883)
- Values by year: **1882: 141:45** | **1883: 141:45*** | **1892: 110:22** | **1902: 92:45** | **1908: 91:45**  *(asterisk = flagged)*
- Flagged value: **141:45**, deviation 40.2 h from other-years median (101.56 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Trenton, New Jersey → San Francisco, California (1882)
- Values by year: **1882: 141:45*** | **1883: 141:45** | **1892: 110:22** | **1902: 92:45** | **1908: 91:45**  *(asterisk = flagged)*
- Flagged value: **141:45**, deviation 40.2 h from other-years median (101.56 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → New York, New York (1883)
- Values by year: **1882: 109:40** | **1883: 109:40*** | **1892: 69:30** | **1902: 65:30**  *(asterisk = flagged)*
- Flagged value: **109:40**, deviation 40.2 h from other-years median (69.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → New York, New York (1882)
- Values by year: **1882: 109:40*** | **1883: 109:40** | **1892: 69:30** | **1902: 65:30**  *(asterisk = flagged)*
- Flagged value: **109:40**, deviation 40.2 h from other-years median (69.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Winona, Minnesota → San Francisco, California (1882)
- Values by year: **1882: 124:51*** | **1892: 88:15** | **1902: 84:45** | **1908: 84:28**  *(asterisk = flagged)*
- Flagged value: **124:51**, deviation 40.1 h from other-years median (84.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Washington, District of Columbia (1882)
- Values by year: **1882: 112:50*** | **1883: 112:50** | **1892: 72:48** | **1902: 66:30**  *(asterisk = flagged)*
- Flagged value: **112:50**, deviation 40.0 h from other-years median (72.80 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Washington, District of Columbia (1883)
- Values by year: **1882: 112:50** | **1883: 112:50*** | **1892: 72:48** | **1902: 66:30**  *(asterisk = flagged)*
- Flagged value: **112:50**, deviation 40.0 h from other-years median (72.80 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Baltimore, Maryland (1883)
- Values by year: **1882: 144:25** | **1883: 144:25*** | **1892: 107:55** | **1902: 100:55** | **1908: 100:55**  *(asterisk = flagged)*
- Flagged value: **144:25**, deviation 40.0 h from other-years median (104.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Baltimore, Maryland (1882)
- Values by year: **1882: 144:25*** | **1883: 144:25** | **1892: 107:55** | **1902: 100:55** | **1908: 100:55**  *(asterisk = flagged)*
- Flagged value: **144:25**, deviation 40.0 h from other-years median (104.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, North Carolina → San Francisco, California (1883)
- Values by year: **1882: 160:13** | **1883: 160:13*** | **1892: 134:45** | **1902: 105:45** | **1908: 105:28**  *(asterisk = flagged)*
- Flagged value: **160:13**, deviation 40.0 h from other-years median (120.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, North Carolina → San Francisco, California (1882)
- Values by year: **1882: 160:13*** | **1883: 160:13** | **1892: 134:45** | **1902: 105:45** | **1908: 105:28**  *(asterisk = flagged)*
- Flagged value: **160:13**, deviation 40.0 h from other-years median (120.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 144:30*** | **1883: 144:30** | **1892: 108:40** | **1902: 100:40** | **1908: 100:40**  *(asterisk = flagged)*
- Flagged value: **144:30**, deviation 39.8 h from other-years median (104.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 144:30** | **1883: 144:30*** | **1892: 108:40** | **1902: 100:40** | **1908: 100:40**  *(asterisk = flagged)*
- Flagged value: **144:30**, deviation 39.8 h from other-years median (104.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Annapolis, Maryland → San Francisco, California (1883)
- Values by year: **1882: 144:49** | **1883: 144:49*** | **1892: 114:15** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **144:49**, deviation 39.8 h from other-years median (105.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Annapolis, Maryland → San Francisco, California (1882)
- Values by year: **1882: 144:49*** | **1883: 144:49** | **1892: 114:15** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **144:49**, deviation 39.8 h from other-years median (105.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Grafton, West Virginia → San Francisco, California (1882)
- Values by year: **1882: 135:47*** | **1883: 135:47** | **1892: 106:15** | **1902: 85:45** | **1908: 84:28**  *(asterisk = flagged)*
- Flagged value: **135:47**, deviation 39.8 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Grafton, West Virginia → San Francisco, California (1883)
- Values by year: **1882: 135:47** | **1883: 135:47*** | **1892: 106:15** | **1902: 85:45** | **1908: 84:28**  *(asterisk = flagged)*
- Flagged value: **135:47**, deviation 39.8 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jackson, Mississippi → San Francisco, California (1883)
- Values by year: **1882: 139:40** | **1883: 139:40*** | **1892: 104:15** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **139:40**, deviation 39.7 h from other-years median (100.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jackson, Mississippi → San Francisco, California (1882)
- Values by year: **1882: 139:40*** | **1883: 139:40** | **1892: 104:15** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **139:40**, deviation 39.7 h from other-years median (100.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Richmond, Virginia → San Francisco, California (1882)
- Values by year: **1882: 149:08*** | **1883: 149:08** | **1892: 119:15** | **1902: 99:45** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **149:08**, deviation 39.6 h from other-years median (109.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Richmond, Virginia → San Francisco, California (1883)
- Values by year: **1882: 149:08** | **1883: 149:08*** | **1892: 119:15** | **1902: 99:45** | **1908: 98:28**  *(asterisk = flagged)*
- Flagged value: **149:08**, deviation 39.6 h from other-years median (109.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hannibal, Missouri → San Francisco, California (1883)
- Values by year: **1882: 121:34** | **1883: 121:34*** | **1892: 84:15** | **1902: 79:45** | **1908: 79:45**  *(asterisk = flagged)*
- Flagged value: **121:34**, deviation 39.6 h from other-years median (82.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hannibal, Missouri → San Francisco, California (1882)
- Values by year: **1882: 121:34*** | **1883: 121:34** | **1892: 84:15** | **1902: 79:45** | **1908: 79:45**  *(asterisk = flagged)*
- Flagged value: **121:34**, deviation 39.6 h from other-years median (82.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → New York, New York (1883)
- Values by year: **1882: 146:25** | **1883: 146:25*** | **1892: 110:30** | **1902: 103:30** | **1908: 102:30**  *(asterisk = flagged)*
- Flagged value: **146:25**, deviation 39.4 h from other-years median (107.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → New York, New York (1882)
- Values by year: **1882: 146:25*** | **1883: 146:25** | **1892: 110:30** | **1902: 103:30** | **1908: 102:30**  *(asterisk = flagged)*
- Flagged value: **146:25**, deviation 39.4 h from other-years median (107.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 147:05*** | **1883: 147:05** | **1892: 110:40** | **1902: 104:40** | **1908: 104:40**  *(asterisk = flagged)*
- Flagged value: **147:05**, deviation 39.4 h from other-years median (107.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 147:05** | **1883: 147:05*** | **1892: 110:40** | **1902: 104:40** | **1908: 104:40**  *(asterisk = flagged)*
- Flagged value: **147:05**, deviation 39.4 h from other-years median (107.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prescott, Arizona → Omaha, Nebraska (1883)
- Values by year: **1883: 109:00*** | **1892: 89:00** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **109:00**, deviation 39.0 h from other-years median (70.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Baltimore, Maryland → San Francisco, California (1883)
- Values by year: **1882: 142:55** | **1883: 142:55*** | **1892: 113:15** | **1902: 94:45** | **1908: 94:45**  *(asterisk = flagged)*
- Flagged value: **142:55**, deviation 38.9 h from other-years median (104.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Baltimore, Maryland → San Francisco, California (1882)
- Values by year: **1882: 142:55*** | **1883: 142:55** | **1892: 113:15** | **1902: 94:45** | **1908: 94:45**  *(asterisk = flagged)*
- Flagged value: **142:55**, deviation 38.9 h from other-years median (104.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Decatur, Alabama → San Francisco, California (1882)
- Values by year: **1882: 142:00*** | **1883: 142:00** | **1892: 108:45** | **1902: 91:35** | **1908: 97:25**  *(asterisk = flagged)*
- Flagged value: **142:00**, deviation 38.9 h from other-years median (103.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Decatur, Alabama → San Francisco, California (1883)
- Values by year: **1882: 142:00** | **1883: 142:00*** | **1892: 108:45** | **1902: 91:35** | **1908: 97:25**  *(asterisk = flagged)*
- Flagged value: **142:00**, deviation 38.9 h from other-years median (103.08 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Omaha, Nebraska (1882)
- Values by year: **1882: 69:18*** | **1883: 69:18** | **1892: 26:30** | **1902: 30:30** | **1908: 30:30**  *(asterisk = flagged)*
- Flagged value: **69:18**, deviation 38.8 h from other-years median (30.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Omaha, Nebraska (1883)
- Values by year: **1882: 69:18** | **1883: 69:18*** | **1892: 26:30** | **1902: 30:30** | **1908: 30:30**  *(asterisk = flagged)*
- Flagged value: **69:18**, deviation 38.8 h from other-years median (30.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atlanta, Georgia → San Francisco, California (1882)
- Values by year: **1882: 150:30*** | **1883: 150:30** | **1892: 120:40** | **1902: 102:45** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **150:30**, deviation 38.8 h from other-years median (111.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atlanta, Georgia → San Francisco, California (1883)
- Values by year: **1882: 150:30** | **1883: 150:30*** | **1892: 120:40** | **1902: 102:45** | **1908: 102:45**  *(asterisk = flagged)*
- Flagged value: **150:30**, deviation 38.8 h from other-years median (111.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kalamazoo, Michigan → San Francisco, California (1882)
- Values by year: **1882: 126:12*** | **1883: 126:12** | **1892: 100:15** | **1902: 74:45** | **1908: 74:45**  *(asterisk = flagged)*
- Flagged value: **126:12**, deviation 38.7 h from other-years median (87.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Kalamazoo, Michigan → San Francisco, California (1883)
- Values by year: **1882: 126:12** | **1883: 126:12*** | **1892: 100:15** | **1902: 74:45** | **1908: 74:45**  *(asterisk = flagged)*
- Flagged value: **126:12**, deviation 38.7 h from other-years median (87.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sioux City, Iowa → San Francisco, California (1882)
- Values by year: **1882: 105:36*** | **1883: 105:36** | **1892: 71:15** | **1902: 62:45** | **1908: 62:45**  *(asterisk = flagged)*
- Flagged value: **105:36**, deviation 38.6 h from other-years median (67.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sioux City, Iowa → San Francisco, California (1883)
- Values by year: **1882: 105:36** | **1883: 105:36*** | **1892: 71:15** | **1902: 62:45** | **1908: 62:45**  *(asterisk = flagged)*
- Flagged value: **105:36**, deviation 38.6 h from other-years median (67.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → San Francisco, California (1883)
- Values by year: **1882: 125:34** | **1883: 125:34*** | **1892: 88:15** | **1902: 85:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **125:34**, deviation 38.6 h from other-years median (87.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → San Francisco, California (1882)
- Values by year: **1882: 125:34*** | **1883: 125:34** | **1892: 88:15** | **1902: 85:45** | **1908: 83:28**  *(asterisk = flagged)*
- Flagged value: **125:34**, deviation 38.6 h from other-years median (87.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Detroit, Michigan → San Francisco, California (1882)
- Values by year: **1882: 131:02*** | **1883: 131:02** | **1892: 104:15** | **1902: 80:45** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **131:02**, deviation 38.5 h from other-years median (92.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Detroit, Michigan → San Francisco, California (1883)
- Values by year: **1882: 131:02** | **1883: 131:02*** | **1892: 104:15** | **1902: 80:45** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **131:02**, deviation 38.5 h from other-years median (92.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Boston, Massachusetts (1883)
- Values by year: **1882: 134:25** | **1883: 134:25*** | **1892: 100:30** | **1902: 91:30** | **1908: 91:30**  *(asterisk = flagged)*
- Flagged value: **134:25**, deviation 38.4 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Boston, Massachusetts (1882)
- Values by year: **1882: 134:25*** | **1883: 134:25** | **1892: 100:30** | **1902: 91:30** | **1908: 91:30**  *(asterisk = flagged)*
- Flagged value: **134:25**, deviation 38.4 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Des Moines, Iowa → San Francisco, California (1882)
- Values by year: **1882: 106:44*** | **1883: 106:44** | **1892: 72:15** | **1902: 60:45** | **1908: 64:53**  *(asterisk = flagged)*
- Flagged value: **106:44**, deviation 38.2 h from other-years median (68.56 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Des Moines, Iowa → San Francisco, California (1883)
- Values by year: **1882: 106:44** | **1883: 106:44*** | **1892: 72:15** | **1902: 60:45** | **1908: 64:53**  *(asterisk = flagged)*
- Flagged value: **106:44**, deviation 38.2 h from other-years median (68.56 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Leavenworth, Kansas → San Francisco, California (1883)
- Values by year: **1882: 109:09** | **1883: 109:09*** | **1892: 80:15** | **1902: 61:45** | **1908: 61:28**  *(asterisk = flagged)*
- Flagged value: **109:09**, deviation 38.1 h from other-years median (71.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Leavenworth, Kansas → San Francisco, California (1882)
- Values by year: **1882: 109:09*** | **1883: 109:09** | **1892: 80:15** | **1902: 61:45** | **1908: 61:28**  *(asterisk = flagged)*
- Flagged value: **109:09**, deviation 38.1 h from other-years median (71.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cairo, Illinois → San Francisco, California (1883)
- Values by year: **1882: 130:31** | **1883: 130:31*** | **1892: 106:15** | **1902: 79:00** | **1908: 75:00**  *(asterisk = flagged)*
- Flagged value: **130:31**, deviation 37.9 h from other-years median (92.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cairo, Illinois → San Francisco, California (1882)
- Values by year: **1882: 130:31*** | **1883: 130:31** | **1892: 106:15** | **1902: 79:00** | **1908: 75:00**  *(asterisk = flagged)*
- Flagged value: **130:31**, deviation 37.9 h from other-years median (92.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 107:20*** | **1883: 107:20** | **1892: 69:40** | **1902: 67:40**  *(asterisk = flagged)*
- Flagged value: **107:20**, deviation 37.7 h from other-years median (69.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 107:20** | **1883: 107:20*** | **1892: 69:40** | **1902: 67:40**  *(asterisk = flagged)*
- Flagged value: **107:20**, deviation 37.7 h from other-years median (69.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Williamsport, Pennsylvania → San Francisco, California (1883)
- Values by year: **1882: 135:50** | **1883: 136:50*** | **1892: 109:15** | **1902: 90:00** | **1908: 90:00**  *(asterisk = flagged)*
- Flagged value: **136:50**, deviation 37.2 h from other-years median (99.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, Delaware → San Francisco, California (1882)
- Values by year: **1882: 147:16*** | **1883: 147:10** | **1892: 126:15** | **1902: 94:25** | **1908: 94:25**  *(asterisk = flagged)*
- Flagged value: **147:16**, deviation 36.9 h from other-years median (110.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Baltimore, Maryland (1883)
- Values by year: **1882: 142:25** | **1883: 142:25*** | **1892: 111:00** | **1902: 100:00** | **1908: 100:00**  *(asterisk = flagged)*
- Flagged value: **142:25**, deviation 36.9 h from other-years median (105.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Baltimore, Maryland (1882)
- Values by year: **1882: 142:25*** | **1883: 142:25** | **1892: 111:00** | **1902: 100:00** | **1908: 100:00**  *(asterisk = flagged)*
- Flagged value: **142:25**, deviation 36.9 h from other-years median (105.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Saint Louis, Missouri (1883)
- Values by year: **1882: 53:10** | **1883: 53:10*** | **1892: 16:20** | **1902: 16:20** | **1908: 16:20**  *(asterisk = flagged)*
- Flagged value: **53:10**, deviation 36.8 h from other-years median (16.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Saint Louis, Missouri (1882)
- Values by year: **1882: 53:10*** | **1883: 53:10** | **1892: 16:20** | **1902: 16:20** | **1908: 16:20**  *(asterisk = flagged)*
- Flagged value: **53:10**, deviation 36.8 h from other-years median (16.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Wilmington, Delaware → San Francisco, California (1883)
- Values by year: **1882: 147:16** | **1883: 147:10*** | **1892: 126:15** | **1902: 94:25** | **1908: 94:25**  *(asterisk = flagged)*
- Flagged value: **147:10**, deviation 36.8 h from other-years median (110.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rock Island, Illinois → San Francisco, California (1882)
- Values by year: **1882: 116:39*** | **1883: 116:39** | **1892: 80:15** | **1902: 76:25** | **1908: 79:25**  *(asterisk = flagged)*
- Flagged value: **116:39**, deviation 36.8 h from other-years median (79.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rock Island, Illinois → San Francisco, California (1883)
- Values by year: **1882: 116:39** | **1883: 116:39*** | **1892: 80:15** | **1902: 76:25** | **1908: 79:25**  *(asterisk = flagged)*
- Flagged value: **116:39**, deviation 36.8 h from other-years median (79.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Boston, Massachusetts (1882)
- Values by year: **1882: 151:35*** | **1883: 151:35** | **1892: 120:50** | **1902: 108:50** | **1908: 108:50**  *(asterisk = flagged)*
- Flagged value: **151:35**, deviation 36.8 h from other-years median (114.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Boston, Massachusetts (1883)
- Values by year: **1882: 151:35** | **1883: 151:35*** | **1892: 120:50** | **1902: 108:50** | **1908: 108:50**  *(asterisk = flagged)*
- Flagged value: **151:35**, deviation 36.8 h from other-years median (114.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atchison, Kansas → San Francisco, California (1883)
- Values by year: **1882: 108:07** | **1883: 108:07*** | **1892: 79:15** | **1902: 63:45** | **1908: 63:28**  *(asterisk = flagged)*
- Flagged value: **108:07**, deviation 36.6 h from other-years median (71.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Atchison, Kansas → San Francisco, California (1882)
- Values by year: **1882: 108:07*** | **1883: 108:07** | **1892: 79:15** | **1902: 63:45** | **1908: 63:28**  *(asterisk = flagged)*
- Flagged value: **108:07**, deviation 36.6 h from other-years median (71.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → San Francisco, California (1882)
- Values by year: **1882: 156:45*** | **1883: 156:45** | **1892: 128:15** | **1902: 105:45** | **1908: 112:15**  *(asterisk = flagged)*
- Flagged value: **156:45**, deviation 36.5 h from other-years median (120.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → San Francisco, California (1883)
- Values by year: **1882: 156:45** | **1883: 156:45*** | **1892: 128:15** | **1902: 105:45** | **1908: 112:15**  *(asterisk = flagged)*
- Flagged value: **156:45**, deviation 36.5 h from other-years median (120.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Washington, District of Columbia (1882)
- Values by year: **1882: 148:27*** | **1883: 148:27** | **1892: 120:00** | **1902: 104:00** | **1908: 104:00**  *(asterisk = flagged)*
- Flagged value: **148:27**, deviation 36.5 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Washington, District of Columbia (1883)
- Values by year: **1882: 148:27** | **1883: 148:27*** | **1892: 120:00** | **1902: 104:00** | **1908: 104:00**  *(asterisk = flagged)*
- Flagged value: **148:27**, deviation 36.5 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Evansville, Indiana → San Francisco, California (1883)
- Values by year: **1882: 120:40** | **1883: 120:40*** | **1892: 90:45** | **1902: 77:45** | **1908: 76:15**  *(asterisk = flagged)*
- Flagged value: **120:40**, deviation 36.4 h from other-years median (84.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Evansville, Indiana → San Francisco, California (1882)
- Values by year: **1882: 120:40*** | **1883: 120:40** | **1892: 90:45** | **1902: 77:45** | **1908: 76:15**  *(asterisk = flagged)*
- Flagged value: **120:40**, deviation 36.4 h from other-years median (84.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Cincinnati, Ohio (1882)
- Values by year: **1882: 41:20*** | **1883: 41:20** | **1892: 5:00** | **1902: 5:00** | **1908: 5:00**  *(asterisk = flagged)*
- Flagged value: **41:20**, deviation 36.3 h from other-years median (5.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Cincinnati, Ohio (1883)
- Values by year: **1882: 41:20** | **1883: 41:20*** | **1892: 5:00** | **1902: 5:00** | **1908: 5:00**  *(asterisk = flagged)*
- Flagged value: **41:20**, deviation 36.3 h from other-years median (5.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Williamsport, Pennsylvania → San Francisco, California (1882)
- Values by year: **1882: 135:50*** | **1883: 136:50** | **1892: 109:15** | **1902: 90:00** | **1908: 90:00**  *(asterisk = flagged)*
- Flagged value: **135:50**, deviation 36.2 h from other-years median (99.62 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sherman, Texas → San Francisco, California (1883)
- Values by year: **1882: 143:40** | **1883: 145:40*** | **1892: 123:13** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **145:40**, deviation 36.2 h from other-years median (109.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chattanooga, Tennessee → San Francisco, California (1882)
- Values by year: **1882: 137:05*** | **1883: 137:05** | **1892: 109:15** | **1902: 92:45** | **1908: 92:28**  *(asterisk = flagged)*
- Flagged value: **137:05**, deviation 36.1 h from other-years median (101.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Montana → San Francisco, California (1883)
- Values by year: **1883: 90:50*** | **1892: 68:00** | **1902: 54:45** | **1908: 54:45**  *(asterisk = flagged)*
- Flagged value: **90:50**, deviation 36.1 h from other-years median (54.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Chattanooga, Tennessee → San Francisco, California (1883)
- Values by year: **1882: 137:05** | **1883: 137:05*** | **1892: 109:15** | **1902: 92:45** | **1908: 92:28**  *(asterisk = flagged)*
- Flagged value: **137:05**, deviation 36.1 h from other-years median (101.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Charleston, South Carolina (1882)
- Values by year: **1882: 166:57*** | **1883: 166:57** | **1892: 141:45** | **1902: 120:00** | **1908: 120:00**  *(asterisk = flagged)*
- Flagged value: **166:57**, deviation 36.1 h from other-years median (130.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Charleston, South Carolina (1883)
- Values by year: **1882: 166:57** | **1883: 166:57*** | **1892: 141:45** | **1902: 120:00** | **1908: 120:00**  *(asterisk = flagged)*
- Flagged value: **166:57**, deviation 36.1 h from other-years median (130.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Illinois → San Francisco, California (1883)
- Values by year: **1882: 117:25** | **1883: 117:25*** | **1892: 85:15** | **1902: 76:35** | **1908: 77:35**  *(asterisk = flagged)*
- Flagged value: **117:25**, deviation 36.0 h from other-years median (81.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Illinois → San Francisco, California (1882)
- Values by year: **1882: 117:25*** | **1883: 117:25** | **1892: 85:15** | **1902: 76:35** | **1908: 77:35**  *(asterisk = flagged)*
- Flagged value: **117:25**, deviation 36.0 h from other-years median (81.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Louisville, Kentucky → San Francisco, California (1883)
- Values by year: **1882: 122:45** | **1883: 122:45*** | **1892: 93:15** | **1902: 80:45** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **122:45**, deviation 35.8 h from other-years median (87.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Louisville, Kentucky → San Francisco, California (1882)
- Values by year: **1882: 122:45*** | **1883: 122:45** | **1892: 93:15** | **1902: 80:45** | **1908: 80:45**  *(asterisk = flagged)*
- Flagged value: **122:45**, deviation 35.8 h from other-years median (87.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Cincinnati, Ohio (1883)
- Values by year: **1882: 141:30** | **1883: 141:30*** | **1892: 115:50** | **1902: 95:50** | **1908: 95:50**  *(asterisk = flagged)*
- Flagged value: **141:30**, deviation 35.7 h from other-years median (105.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Los Angeles, California → Cincinnati, Ohio (1882)
- Values by year: **1882: 141:30*** | **1883: 141:30** | **1892: 115:50** | **1902: 95:50** | **1908: 95:50**  *(asterisk = flagged)*
- Flagged value: **141:30**, deviation 35.7 h from other-years median (105.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Indianapolis, Indiana → San Francisco, California (1882)
- Values by year: **1882: 118:03*** | **1883: 118:03** | **1892: 89:45** | **1902: 75:15** | **1908: 75:15**  *(asterisk = flagged)*
- Flagged value: **118:03**, deviation 35.5 h from other-years median (82.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Indianapolis, Indiana → San Francisco, California (1883)
- Values by year: **1882: 118:03** | **1883: 118:03*** | **1892: 89:45** | **1902: 75:15** | **1908: 75:15**  *(asterisk = flagged)*
- Flagged value: **118:03**, deviation 35.5 h from other-years median (82.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Winona, Minnesota → Charleston, South Carolina (1882)
- Values by year: **1882: 78:13*** | **1892: 43:00** | **1902: 43:00** | **1908: 43:00**  *(asterisk = flagged)*
- Flagged value: **78:13**, deviation 35.2 h from other-years median (43.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Raleigh, North Carolina → San Francisco, California (1883)
- Values by year: **1882: 158:52** | **1883: 158:52*** | **1892: 139:45** | **1902: 107:45** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **158:52**, deviation 35.1 h from other-years median (123.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Raleigh, North Carolina → San Francisco, California (1882)
- Values by year: **1882: 158:52*** | **1883: 158:52** | **1892: 139:45** | **1902: 107:45** | **1908: 107:28**  *(asterisk = flagged)*
- Flagged value: **158:52**, deviation 35.1 h from other-years median (123.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → Omaha, Nebraska (1882)
- Values by year: **1882: 106:35*** | **1883: 106:35** | **1892: 73:00** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **106:35**, deviation 35.1 h from other-years median (71.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → Omaha, Nebraska (1883)
- Values by year: **1882: 106:35** | **1883: 106:35*** | **1892: 73:00** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **106:35**, deviation 35.1 h from other-years median (71.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Santa Fe, New Mexico → San Francisco, California (1882)
- Values by year: **1882: 71:41*** | **1892: 77:15** | **1902: 34:05** | **1908: 36:45**  *(asterisk = flagged)*
- Flagged value: **71:41**, deviation 34.9 h from other-years median (36.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Baltimore, Maryland (1883)
- Values by year: **1882: 146:55** | **1883: 146:55*** | **1892: 121:00** | **1902: 103:00** | **1908: 103:00**  *(asterisk = flagged)*
- Flagged value: **146:55**, deviation 34.9 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Baltimore, Maryland (1882)
- Values by year: **1882: 146:55*** | **1883: 146:55** | **1892: 121:00** | **1902: 103:00** | **1908: 103:00**  *(asterisk = flagged)*
- Flagged value: **146:55**, deviation 34.9 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → San Francisco, California (1883)
- Values by year: **1882: 148:00** | **1883: 148:00*** | **1892: 124:40** | **1902: 102:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **148:00**, deviation 34.3 h from other-years median (113.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → San Francisco, California (1882)
- Values by year: **1882: 148:00*** | **1883: 148:00** | **1892: 124:40** | **1902: 102:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **148:00**, deviation 34.3 h from other-years median (113.71 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sherman, Texas → San Francisco, California (1882)
- Values by year: **1882: 143:40*** | **1883: 145:40** | **1892: 123:13** | **1902: 95:45** | **1908: 95:45**  *(asterisk = flagged)*
- Flagged value: **143:40**, deviation 34.2 h from other-years median (109.48 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Chicago, Illinois (1882)
- Values by year: **1882: 119:30*** | **1883: 119:30** | **1892: 90:50** | **1902: 80:00** | **1908: 80:00**  *(asterisk = flagged)*
- Flagged value: **119:30**, deviation 34.1 h from other-years median (85.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Chicago, Illinois (1883)
- Values by year: **1882: 119:30** | **1883: 119:30*** | **1892: 90:50** | **1902: 80:00** | **1908: 80:00**  *(asterisk = flagged)*
- Flagged value: **119:30**, deviation 34.1 h from other-years median (85.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Chicago, Illinois (1882)
- Values by year: **1882: 48:50*** | **1883: 48:50** | **1892: 15:30** | **1902: 14:00** | **1908: 14:00**  *(asterisk = flagged)*
- Flagged value: **48:50**, deviation 34.1 h from other-years median (14.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Chicago, Illinois (1883)
- Values by year: **1882: 48:50** | **1883: 48:50*** | **1892: 15:30** | **1902: 14:00** | **1908: 14:00**  *(asterisk = flagged)*
- Flagged value: **48:50**, deviation 34.1 h from other-years median (14.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Henderson, Kentucky → San Francisco, California (1882)
- Values by year: **1882: 124:00*** | **1883: 124:00** | **1892: 90:15** | **1902: 89:45** | **1908: 89:20**  *(asterisk = flagged)*
- Flagged value: **124:00**, deviation 34.0 h from other-years median (90.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Henderson, Kentucky → San Francisco, California (1883)
- Values by year: **1882: 124:00** | **1883: 124:00*** | **1892: 90:15** | **1902: 89:45** | **1908: 89:20**  *(asterisk = flagged)*
- Flagged value: **124:00**, deviation 34.0 h from other-years median (90.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Washington, District of Columbia (1882)
- Values by year: **1882: 143:57*** | **1883: 143:57** | **1892: 119:00** | **1902: 101:00** | **1908: 101:00**  *(asterisk = flagged)*
- Flagged value: **143:57**, deviation 34.0 h from other-years median (110.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Washington, District of Columbia (1883)
- Values by year: **1882: 143:57** | **1883: 143:57*** | **1892: 119:00** | **1902: 101:00** | **1908: 101:00**  *(asterisk = flagged)*
- Flagged value: **143:57**, deviation 34.0 h from other-years median (110.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 142:35*** | **1883: 142:35** | **1892: 115:40** | **1902: 101:40** | **1908: 101:40**  *(asterisk = flagged)*
- Flagged value: **142:35**, deviation 33.9 h from other-years median (108.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 142:35** | **1883: 142:35*** | **1892: 115:40** | **1902: 101:40** | **1908: 101:40**  *(asterisk = flagged)*
- Flagged value: **142:35**, deviation 33.9 h from other-years median (108.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Charleston, South Carolina (1882)
- Values by year: **1882: 99:02*** | **1883: 99:02** | **1892: 65:15** | **1902: 65:00** | **1908: 65:00**  *(asterisk = flagged)*
- Flagged value: **99:02**, deviation 33.9 h from other-years median (65.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Charleston, South Carolina (1883)
- Values by year: **1882: 99:02** | **1883: 99:02*** | **1892: 65:15** | **1902: 65:00** | **1908: 65:00**  *(asterisk = flagged)*
- Flagged value: **99:02**, deviation 33.9 h from other-years median (65.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cincinnati, Ohio → San Francisco, California (1883)
- Values by year: **1882: 123:45** | **1883: 123:45*** | **1892: 97:15** | **1902: 82:45** | **1908: 82:45**  *(asterisk = flagged)*
- Flagged value: **123:45**, deviation 33.8 h from other-years median (90.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cincinnati, Ohio → San Francisco, California (1882)
- Values by year: **1882: 123:45*** | **1883: 123:45** | **1892: 97:15** | **1902: 82:45** | **1908: 82:45**  *(asterisk = flagged)*
- Flagged value: **123:45**, deviation 33.8 h from other-years median (90.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Boston, Massachusetts (1882)
- Values by year: **1882: 122:05*** | **1883: 122:05** | **1892: 89:30** | **1902: 88:30** | **1908: 88:30**  *(asterisk = flagged)*
- Flagged value: **122:05**, deviation 33.1 h from other-years median (89.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Boston, Massachusetts (1883)
- Values by year: **1882: 122:05** | **1883: 122:05*** | **1892: 89:30** | **1902: 88:30** | **1908: 88:30**  *(asterisk = flagged)*
- Flagged value: **122:05**, deviation 33.1 h from other-years median (89.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Little Rock, Arkansas → San Francisco, California (1883)
- Values by year: **1882: 131:26** | **1883: 131:28*** | **1892: 102:15** | **1902: 94:35** | **1908: 94:35**  *(asterisk = flagged)*
- Flagged value: **131:28**, deviation 33.1 h from other-years median (98.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Little Rock, Arkansas → San Francisco, California (1882)
- Values by year: **1882: 131:26*** | **1883: 131:28** | **1892: 102:15** | **1902: 94:35** | **1908: 94:35**  *(asterisk = flagged)*
- Flagged value: **131:26**, deviation 33.0 h from other-years median (98.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Saint Louis, Missouri (1882)
- Values by year: **1882: 50:38*** | **1883: 50:38** | **1892: 17:40** | **1902: 17:40** | **1908: 17:40**  *(asterisk = flagged)*
- Flagged value: **50:38**, deviation 33.0 h from other-years median (17.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Saint Louis, Missouri (1883)
- Values by year: **1882: 50:38** | **1883: 50:38*** | **1892: 17:40** | **1902: 17:40** | **1908: 17:40**  *(asterisk = flagged)*
- Flagged value: **50:38**, deviation 33.0 h from other-years median (17.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Washington, District of Columbia (1883)
- Values by year: **1882: 108:52** | **1883: 108:52*** | **1892: 71:00** | **1902: 76:00** | **1908: 76:00**  *(asterisk = flagged)*
- Flagged value: **108:52**, deviation 32.9 h from other-years median (76.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Washington, District of Columbia (1882)
- Values by year: **1882: 108:52*** | **1883: 108:52** | **1892: 71:00** | **1902: 76:00** | **1908: 76:00**  *(asterisk = flagged)*
- Flagged value: **108:52**, deviation 32.9 h from other-years median (76.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Cincinnati, Ohio (1883)
- Values by year: **1882: 38:48** | **1883: 38:48*** | **1892: 6:00** | **1902: 6:00** | **1908: 6:00**  *(asterisk = flagged)*
- Flagged value: **38:48**, deviation 32.8 h from other-years median (6.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Cincinnati, Ohio (1882)
- Values by year: **1882: 38:48*** | **1883: 38:48** | **1892: 6:00** | **1902: 6:00** | **1908: 6:00**  *(asterisk = flagged)*
- Flagged value: **38:48**, deviation 32.8 h from other-years median (6.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → San Francisco, California (1883)
- Values by year: **1882: 97:01** | **1883: 97:01*** | **1892: 68:15** | **1902: 60:45** | **1908: 59:45**  *(asterisk = flagged)*
- Flagged value: **97:01**, deviation 32.5 h from other-years median (64.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → San Francisco, California (1882)
- Values by year: **1882: 97:01*** | **1883: 97:01** | **1892: 68:15** | **1902: 60:45** | **1908: 59:45**  *(asterisk = flagged)*
- Flagged value: **97:01**, deviation 32.5 h from other-years median (64.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Topeka, Kansas → San Francisco, California (1882)
- Values by year: **1882: 107:50*** | **1883: 107:50** | **1892: 82:15** | **1902: 68:45** | **1908: 68:28**  *(asterisk = flagged)*
- Flagged value: **107:50**, deviation 32.3 h from other-years median (75.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Topeka, Kansas → San Francisco, California (1883)
- Values by year: **1882: 107:50** | **1883: 107:50*** | **1892: 82:15** | **1902: 68:45** | **1908: 68:28**  *(asterisk = flagged)*
- Flagged value: **107:50**, deviation 32.3 h from other-years median (75.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Charleston, South Carolina (1882)
- Values by year: **1882: 143:02*** | **1883: 143:02** | **1892: 115:00** | **1902: 107:00** | **1908: 107:00**  *(asterisk = flagged)*
- Flagged value: **143:02**, deviation 32.0 h from other-years median (111.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Charleston, South Carolina (1883)
- Values by year: **1882: 143:02** | **1883: 143:02*** | **1892: 115:00** | **1902: 107:00** | **1908: 107:00**  *(asterisk = flagged)*
- Flagged value: **143:02**, deviation 32.0 h from other-years median (111.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbus, Ohio → San Francisco, California (1882)
- Values by year: **1882: 124:00*** | **1883: 124:00** | **1892: 102:15** | **1902: 82:15** | **1908: 82:15**  *(asterisk = flagged)*
- Flagged value: **124:00**, deviation 31.8 h from other-years median (92.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Columbus, Ohio → San Francisco, California (1883)
- Values by year: **1882: 124:00** | **1883: 124:00*** | **1892: 102:15** | **1902: 82:15** | **1908: 82:15**  *(asterisk = flagged)*
- Flagged value: **124:00**, deviation 31.8 h from other-years median (92.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Chicago, Illinois (1882)
- Values by year: **1882: 114:50*** | **1883: 114:50** | **1892: 90:50** | **1902: 77:00** | **1908: 77:00**  *(asterisk = flagged)*
- Flagged value: **114:50**, deviation 30.9 h from other-years median (83.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Chicago, Illinois (1883)
- Values by year: **1882: 114:50** | **1883: 114:50*** | **1892: 90:50** | **1902: 77:00** | **1908: 77:00**  *(asterisk = flagged)*
- Flagged value: **114:50**, deviation 30.9 h from other-years median (83.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Chicago, Illinois (1882)
- Values by year: **1882: 119:50*** | **1883: 119:50** | **1892: 82:40** | **1902: 89:40** | **1908: 89:40**  *(asterisk = flagged)*
- Flagged value: **119:50**, deviation 30.2 h from other-years median (89.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Chicago, Illinois (1883)
- Values by year: **1882: 119:50** | **1883: 119:50*** | **1892: 82:40** | **1902: 89:40** | **1908: 89:40**  *(asterisk = flagged)*
- Flagged value: **119:50**, deviation 30.2 h from other-years median (89.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Chicago, Illinois (1882)
- Values by year: **1882: 46:18*** | **1883: 46:18** | **1892: 16:50** | **1902: 15:34** | **1908: 15:00**  *(asterisk = flagged)*
- Flagged value: **46:18**, deviation 30.1 h from other-years median (16.20 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Chicago, Illinois (1883)
- Values by year: **1882: 46:18** | **1883: 46:18*** | **1892: 16:50** | **1902: 15:34** | **1908: 15:00**  *(asterisk = flagged)*
- Flagged value: **46:18**, deviation 30.1 h from other-years median (16.20 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Baltimore, Maryland (1882)
- Values by year: **1882: 107:20*** | **1883: 107:20** | **1892: 80:00** | **1902: 75:00** | **1908: 75:00**  *(asterisk = flagged)*
- Flagged value: **107:20**, deviation 29.8 h from other-years median (77.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Baltimore, Maryland (1883)
- Values by year: **1882: 107:20** | **1883: 107:20*** | **1892: 80:00** | **1902: 75:00** | **1908: 75:00**  *(asterisk = flagged)*
- Flagged value: **107:20**, deviation 29.8 h from other-years median (77.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Boston, Massachusetts (1882)
- Values by year: **1882: 146:15*** | **1883: 146:15** | **1892: 119:35** | **1902: 113:35** | **1908: 113:35**  *(asterisk = flagged)*
- Flagged value: **146:15**, deviation 29.7 h from other-years median (116.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Boston, Massachusetts (1883)
- Values by year: **1882: 146:15** | **1883: 146:15*** | **1892: 119:35** | **1902: 113:35** | **1908: 113:35**  *(asterisk = flagged)*
- Flagged value: **146:15**, deviation 29.7 h from other-years median (116.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Chicago, Illinois (1882)
- Values by year: **1882: 88:00*** | **1883: 83:00** | **1892: 60:30** | **1902: 57:30** | **1908: 57:30**  *(asterisk = flagged)*
- Flagged value: **88:00**, deviation 29.0 h from other-years median (59.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Charleston, South Carolina (1883)
- Values by year: **1882: 84:12** | **1883: 84:12*** | **1892: 55:25** | **1902: 55:25** | **1908: 55:25**  *(asterisk = flagged)*
- Flagged value: **84:12**, deviation 28.8 h from other-years median (55.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Charleston, South Carolina (1882)
- Values by year: **1882: 84:12*** | **1883: 84:12** | **1892: 55:25** | **1902: 55:25** | **1908: 55:25**  *(asterisk = flagged)*
- Flagged value: **84:12**, deviation 28.8 h from other-years median (55.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Chicago, Illinois (1882)
- Values by year: **1882: 79:45*** | **1883: 79:45** | **1892: 58:48** | **1902: 45:30** | **1908: 45:30**  *(asterisk = flagged)*
- Flagged value: **79:45**, deviation 27.6 h from other-years median (52.15 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Chicago, Illinois (1883)
- Values by year: **1882: 79:45** | **1883: 79:45*** | **1892: 58:48** | **1902: 45:30** | **1908: 45:30**  *(asterisk = flagged)*
- Flagged value: **79:45**, deviation 27.6 h from other-years median (52.15 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 136:25** | **1883: 136:25*** | **1892: 108:50** | **1902: 107:50**  *(asterisk = flagged)*
- Flagged value: **136:25**, deviation 27.6 h from other-years median (108.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 136:25*** | **1883: 136:25** | **1892: 108:50** | **1902: 107:50**  *(asterisk = flagged)*
- Flagged value: **136:25**, deviation 27.6 h from other-years median (108.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → San Francisco, California (1882)
- Values by year: **1882: 127:06*** | **1883: 127:06** | **1892: 99:45** | **1902: 89:45**  *(asterisk = flagged)*
- Flagged value: **127:06**, deviation 27.4 h from other-years median (99.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Deadwood, Dakota → San Francisco, California (1883)
- Values by year: **1882: 127:06** | **1883: 127:06*** | **1892: 99:45** | **1902: 89:45**  *(asterisk = flagged)*
- Flagged value: **127:06**, deviation 27.4 h from other-years median (99.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 131:55** | **1883: 131:55*** | **1892: 104:50** | **1902: 104:50**  *(asterisk = flagged)*
- Flagged value: **131:55**, deviation 27.1 h from other-years median (104.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 131:55*** | **1883: 131:55** | **1892: 104:50** | **1902: 104:50**  *(asterisk = flagged)*
- Flagged value: **131:55**, deviation 27.1 h from other-years median (104.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Omaha, Nebraska (1883)
- Values by year: **1882: 99:30** | **1883: 99:30*** | **1892: 72:30** | **1902: 72:30** | **1908: 72:30**  *(asterisk = flagged)*
- Flagged value: **99:30**, deviation 27.0 h from other-years median (72.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Omaha, Nebraska (1882)
- Values by year: **1882: 99:30*** | **1883: 99:30** | **1892: 72:30** | **1902: 72:30** | **1908: 72:30**  *(asterisk = flagged)*
- Flagged value: **99:30**, deviation 27.0 h from other-years median (72.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Omaha, Nebraska (1882)
- Values by year: **1882: 99:20*** | **1883: 99:20** | **1892: 72:30** | **1902: 72:30** | **1908: 72:30**  *(asterisk = flagged)*
- Flagged value: **99:20**, deviation 26.8 h from other-years median (72.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Omaha, Nebraska (1883)
- Values by year: **1882: 99:20** | **1883: 99:20*** | **1892: 72:30** | **1902: 72:30** | **1908: 72:30**  *(asterisk = flagged)*
- Flagged value: **99:20**, deviation 26.8 h from other-years median (72.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Boston, Massachusetts (1883)
- Values by year: **1882: 72:13** | **1883: 72:13*** | **1892: 36:30** | **1902: 48:00** | **1908: 43:00**  *(asterisk = flagged)*
- Flagged value: **72:13**, deviation 26.7 h from other-years median (45.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Boston, Massachusetts (1882)
- Values by year: **1882: 72:13*** | **1883: 72:13** | **1892: 36:30** | **1902: 48:00** | **1908: 43:00**  *(asterisk = flagged)*
- Flagged value: **72:13**, deviation 26.7 h from other-years median (45.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → New York, New York (1883)
- Values by year: **1882: 107:00** | **1883: 107:00*** | **1892: 89:30** | **1902: 71:30** | **1908: 71:30**  *(asterisk = flagged)*
- Flagged value: **107:00**, deviation 26.5 h from other-years median (80.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → New York, New York (1882)
- Values by year: **1882: 107:00*** | **1883: 107:00** | **1892: 89:30** | **1902: 71:30** | **1908: 71:30**  *(asterisk = flagged)*
- Flagged value: **107:00**, deviation 26.5 h from other-years median (80.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### West Point, New York → San Francisco, California (1882)
- Values by year: **1882: 162:32*** | **1883: 162:32** | **1892: 110:15**  *(asterisk = flagged)*
- Flagged value: **162:32**, deviation 26.1 h from other-years median (136.39 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### West Point, New York → San Francisco, California (1883)
- Values by year: **1882: 162:32** | **1883: 162:32*** | **1892: 110:15**  *(asterisk = flagged)*
- Flagged value: **162:32**, deviation 26.1 h from other-years median (136.39 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Saint Louis, Missouri (1882)
- Values by year: **1882: 106:47*** | **1883: 106:47** | **1892: 90:40** | **1902: 70:40** | **1908: 70:40**  *(asterisk = flagged)*
- Flagged value: **106:47**, deviation 26.1 h from other-years median (80.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Saint Louis, Missouri (1883)
- Values by year: **1882: 106:47** | **1883: 106:47*** | **1892: 90:40** | **1902: 70:40** | **1908: 70:40**  *(asterisk = flagged)*
- Flagged value: **106:47**, deviation 26.1 h from other-years median (80.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Chicago, Illinois (1882)
- Values by year: **1882: 90:50*** | **1883: 90:50** | **1892: 67:50** | **1902: 61:50** | **1908: 61:50**  *(asterisk = flagged)*
- Flagged value: **90:50**, deviation 26.0 h from other-years median (64.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Chicago, Illinois (1883)
- Values by year: **1882: 90:50** | **1883: 90:50*** | **1892: 67:50** | **1902: 61:50** | **1908: 61:50**  *(asterisk = flagged)*
- Flagged value: **90:50**, deviation 26.0 h from other-years median (64.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 107:35*** | **1883: 107:35** | **1892: 86:40** | **1902: 76:40** | **1908: 76:40**  *(asterisk = flagged)*
- Flagged value: **107:35**, deviation 25.9 h from other-years median (81.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 107:35** | **1883: 107:35*** | **1892: 86:40** | **1902: 76:40** | **1908: 76:40**  *(asterisk = flagged)*
- Flagged value: **107:35**, deviation 25.9 h from other-years median (81.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Charleston, South Carolina (1883)
- Values by year: **1882: 88:07** | **1883: 88:07*** | **1892: 62:25** | **1902: 62:25** | **1908: 62:25**  *(asterisk = flagged)*
- Flagged value: **88:07**, deviation 25.7 h from other-years median (62.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Charleston, South Carolina (1882)
- Values by year: **1882: 88:07*** | **1883: 88:07** | **1892: 62:25** | **1902: 62:25** | **1908: 62:25**  *(asterisk = flagged)*
- Flagged value: **88:07**, deviation 25.7 h from other-years median (62.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 118:35*** | **1883: 118:35** | **1892: 96:25** | **1902: 89:25** | **1908: 89:25**  *(asterisk = flagged)*
- Flagged value: **118:35**, deviation 25.7 h from other-years median (92.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 118:35** | **1883: 118:35*** | **1892: 96:25** | **1902: 89:25** | **1908: 89:25**  *(asterisk = flagged)*
- Flagged value: **118:35**, deviation 25.7 h from other-years median (92.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Washington, District of Columbia (1882)
- Values by year: **1882: 120:02*** | **1883: 120:02** | **1892: 100:00** | **1902: 89:00** | **1908: 89:00**  *(asterisk = flagged)*
- Flagged value: **120:02**, deviation 25.5 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Washington, District of Columbia (1883)
- Values by year: **1882: 120:02** | **1883: 120:02*** | **1892: 100:00** | **1902: 89:00** | **1908: 89:00**  *(asterisk = flagged)*
- Flagged value: **120:02**, deviation 25.5 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → New York, New York (1882)
- Values by year: **1882: 117:35*** | **1883: 117:35** | **1892: 96:30** | **1902: 88:30** | **1908: 88:30**  *(asterisk = flagged)*
- Flagged value: **117:35**, deviation 25.1 h from other-years median (92.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → New York, New York (1883)
- Values by year: **1882: 117:35** | **1883: 117:35*** | **1892: 96:30** | **1902: 88:30** | **1908: 88:30**  *(asterisk = flagged)*
- Flagged value: **117:35**, deviation 25.1 h from other-years median (92.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Omaha, Nebraska (1883)
- Values by year: **1882: 96:00** | **1883: 96:00*** | **1892: 71:40** | **1902: 70:40** | **1908: 70:40**  *(asterisk = flagged)*
- Flagged value: **96:00**, deviation 24.8 h from other-years median (71.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Francisco, California → Omaha, Nebraska (1882)
- Values by year: **1882: 96:00*** | **1883: 96:00** | **1892: 71:40** | **1902: 70:40** | **1908: 70:40**  *(asterisk = flagged)*
- Flagged value: **96:00**, deviation 24.8 h from other-years median (71.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 94:30*** | **1883: 94:30** | **1892: 69:50** | **1902: 61:50**  *(asterisk = flagged)*
- Flagged value: **94:30**, deviation 24.7 h from other-years median (69.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 94:30** | **1883: 94:30*** | **1892: 69:50** | **1902: 61:50**  *(asterisk = flagged)*
- Flagged value: **94:30**, deviation 24.7 h from other-years median (69.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Charleston, South Carolina (1883)
- Values by year: **1882: 154:52** | **1883: 154:52*** | **1892: 133:45** | **1902: 127:45** | **1908: 127:45**  *(asterisk = flagged)*
- Flagged value: **154:52**, deviation 24.1 h from other-years median (130.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Charleston, South Carolina (1882)
- Values by year: **1882: 154:52*** | **1883: 154:52** | **1892: 133:45** | **1902: 127:45** | **1908: 127:45**  *(asterisk = flagged)*
- Flagged value: **154:52**, deviation 24.1 h from other-years median (130.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pueblo, Colorado → Charleston, South Carolina (1882)
- Values by year: **1882: 94:14*** | **1883: 94:14** | **1892: 70:15** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **94:14**, deviation 24.1 h from other-years median (70.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pueblo, Colorado → Charleston, South Carolina (1883)
- Values by year: **1882: 94:14** | **1883: 94:14*** | **1892: 70:15** | **1902: 70:00** | **1908: 70:00**  *(asterisk = flagged)*
- Flagged value: **94:14**, deviation 24.1 h from other-years median (70.12 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Baltimore, Maryland (1883)
- Values by year: **1882: 62:04** | **1883: 62:04*** | **1892: 35:00** | **1902: 38:00** | **1908: 38:00**  *(asterisk = flagged)*
- Flagged value: **62:04**, deviation 24.1 h from other-years median (38.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Baltimore, Maryland (1882)
- Values by year: **1882: 62:04*** | **1883: 62:04** | **1892: 35:00** | **1902: 38:00** | **1908: 38:00**  *(asterisk = flagged)*
- Flagged value: **62:04**, deviation 24.1 h from other-years median (38.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 132:30*** | **1883: 132:30** | **1892: 108:30** | **1902: 90:39**  *(asterisk = flagged)*
- Flagged value: **132:30**, deviation 24.0 h from other-years median (108.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Baltimore, Maryland (1882)
- Values by year: **1882: 118:30*** | **1883: 118:30** | **1892: 99:00** | **1902: 90:00** | **1908: 90:00**  *(asterisk = flagged)*
- Flagged value: **118:30**, deviation 24.0 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Chicago, Illinois (1883)
- Values by year: **1882: 88:00** | **1883: 83:00*** | **1892: 60:30** | **1902: 57:30** | **1908: 57:30**  *(asterisk = flagged)*
- Flagged value: **83:00**, deviation 24.0 h from other-years median (59.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Baltimore, Maryland (1883)
- Values by year: **1882: 118:30** | **1883: 118:30*** | **1892: 99:00** | **1902: 90:00** | **1908: 90:00**  *(asterisk = flagged)*
- Flagged value: **118:30**, deviation 24.0 h from other-years median (94.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 132:30** | **1883: 132:30*** | **1892: 108:30** | **1902: 90:39**  *(asterisk = flagged)*
- Flagged value: **132:30**, deviation 24.0 h from other-years median (108.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Cincinnati, Ohio (1883)
- Values by year: **1882: 119:55** | **1883: 119:55*** | **1892: 101:30** | **1902: 90:30** | **1908: 90:30**  *(asterisk = flagged)*
- Flagged value: **119:55**, deviation 23.9 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tucson, Arizona → Cincinnati, Ohio (1882)
- Values by year: **1882: 119:55*** | **1883: 119:55** | **1892: 101:30** | **1902: 90:30** | **1908: 90:30**  *(asterisk = flagged)*
- Flagged value: **119:55**, deviation 23.9 h from other-years median (96.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 88:25** | **1883: 88:25*** | **1892: 69:40** | **1902: 59:40** | **1908: 59:40**  *(asterisk = flagged)*
- Flagged value: **88:25**, deviation 23.8 h from other-years median (64.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Saint Louis, Missouri (1883)
- Values by year: **1882: 83:10** | **1883: 83:10*** | **1892: 59:25** | **1902: 59:25** | **1908: 59:25**  *(asterisk = flagged)*
- Flagged value: **83:10**, deviation 23.8 h from other-years median (59.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Saint Louis, Missouri (1883)
- Values by year: **1882: 83:10** | **1883: 83:10*** | **1892: 49:25** | **1902: 59:25** | **1908: 59:25**  *(asterisk = flagged)*
- Flagged value: **83:10**, deviation 23.8 h from other-years median (59.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Saint Louis, Missouri (1882)
- Values by year: **1882: 83:10*** | **1883: 83:10** | **1892: 59:25** | **1902: 59:25** | **1908: 59:25**  *(asterisk = flagged)*
- Flagged value: **83:10**, deviation 23.7 h from other-years median (59.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Saint Louis, Missouri (1882)
- Values by year: **1882: 83:10*** | **1883: 83:10** | **1892: 49:25** | **1902: 59:25** | **1908: 59:25**  *(asterisk = flagged)*
- Flagged value: **83:10**, deviation 23.7 h from other-years median (59.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 88:25*** | **1883: 88:25** | **1892: 69:40** | **1902: 59:40** | **1908: 59:40**  *(asterisk = flagged)*
- Flagged value: **88:25**, deviation 23.7 h from other-years median (64.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Chicago, Illinois (1882)
- Values by year: **1882: 83:50*** | **1883: 83:50** | **1892: 60:30** | **1902: 60:30** | **1908: 60:30**  *(asterisk = flagged)*
- Flagged value: **83:50**, deviation 23.3 h from other-years median (60.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Chicago, Illinois (1883)
- Values by year: **1882: 83:50** | **1883: 83:50*** | **1892: 60:30** | **1902: 60:30** | **1908: 60:30**  *(asterisk = flagged)*
- Flagged value: **83:50**, deviation 23.3 h from other-years median (60.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Omaha, Nebraska → San Francisco, California (1883)
- Values by year: **1882: 97:05** | **1883: 97:06*** | **1892: 92:15** | **1902: 52:30** | **1908: 55:30**  *(asterisk = flagged)*
- Flagged value: **97:06**, deviation 23.2 h from other-years median (73.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Omaha, Nebraska → San Francisco, California (1882)
- Values by year: **1882: 97:05*** | **1883: 97:06** | **1892: 92:15** | **1902: 52:30** | **1908: 55:30**  *(asterisk = flagged)*
- Flagged value: **97:05**, deviation 23.2 h from other-years median (73.88 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Washington, District of Columbia (1883)
- Values by year: **1882: 63:08** | **1883: 83:08*** | **1892: 73:00** | **1902: 57:00** | **1908: 57:00**  *(asterisk = flagged)*
- Flagged value: **83:08**, deviation 23.1 h from other-years median (60.07 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Omaha, Nebraska (1883)
- Values by year: **1882: 88:30** | **1883: 88:30*** | **1892: 65:30** | **1902: 65:30** | **1908: 65:30**  *(asterisk = flagged)*
- Flagged value: **88:30**, deviation 23.0 h from other-years median (65.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Omaha, Nebraska (1882)
- Values by year: **1882: 88:30*** | **1883: 88:30** | **1892: 65:30** | **1902: 65:30** | **1908: 65:30**  *(asterisk = flagged)*
- Flagged value: **88:30**, deviation 23.0 h from other-years median (65.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → Charleston, South Carolina (1883)
- Values by year: **1882: 84:07** | **1883: 84:07*** | **1892: 61:30** | **1902: 61:30** | **1908: 61:30**  *(asterisk = flagged)*
- Flagged value: **84:07**, deviation 22.6 h from other-years median (61.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Austin, Texas → Charleston, South Carolina (1882)
- Values by year: **1882: 84:07*** | **1883: 84:07** | **1892: 61:30** | **1902: 61:30** | **1908: 61:30**  *(asterisk = flagged)*
- Flagged value: **84:07**, deviation 22.6 h from other-years median (61.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → New York, New York (1882)
- Values by year: **1882: 90:35*** | **1883: 90:35** | **1892: 73:00** | **1902: 63:00** | **1908: 63:00**  *(asterisk = flagged)*
- Flagged value: **90:35**, deviation 22.6 h from other-years median (68.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → New York, New York (1883)
- Values by year: **1882: 90:35** | **1883: 90:35*** | **1892: 73:00** | **1902: 63:00** | **1908: 63:00**  *(asterisk = flagged)*
- Flagged value: **90:35**, deviation 22.6 h from other-years median (68.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Cincinnati, Ohio (1883)
- Values by year: **1882: 71:00** | **1883: 71:00*** | **1892: 48:00** | **1902: 48:40** | **1908: 48:40**  *(asterisk = flagged)*
- Flagged value: **71:00**, deviation 22.3 h from other-years median (48.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Cincinnati, Ohio (1882)
- Values by year: **1882: 71:00*** | **1883: 71:00** | **1892: 48:00** | **1902: 48:40** | **1908: 48:40**  *(asterisk = flagged)*
- Flagged value: **71:00**, deviation 22.3 h from other-years median (48.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Cincinnati, Ohio (1883)
- Values by year: **1882: 71:00** | **1883: 71:00*** | **1892: 48:40** | **1902: 48:40** | **1908: 48:40**  *(asterisk = flagged)*
- Flagged value: **71:00**, deviation 22.3 h from other-years median (48.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Cincinnati, Ohio (1882)
- Values by year: **1882: 71:00*** | **1883: 71:00** | **1892: 48:40** | **1902: 48:40** | **1908: 48:40**  *(asterisk = flagged)*
- Flagged value: **71:00**, deviation 22.3 h from other-years median (48.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Boston, Massachusetts (1882)
- Values by year: **1882: 97:08*** | **1883: 97:08** | **1892: 79:50** | **1902: 69:05** | **1908: 69:50**  *(asterisk = flagged)*
- Flagged value: **97:08**, deviation 22.3 h from other-years median (74.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Boston, Massachusetts (1883)
- Values by year: **1882: 97:08** | **1883: 97:08*** | **1892: 79:50** | **1902: 69:05** | **1908: 69:50**  *(asterisk = flagged)*
- Flagged value: **97:08**, deviation 22.3 h from other-years median (74.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → Saint Louis, Missouri (1882)
- Values by year: **1882: 56:50*** | **1883: 56:50** | **1892: 35:05** | **1902: 34:05** | **1908: 34:05**  *(asterisk = flagged)*
- Flagged value: **56:50**, deviation 22.3 h from other-years median (34.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → Saint Louis, Missouri (1883)
- Values by year: **1882: 56:50** | **1883: 56:50*** | **1892: 35:05** | **1902: 34:05** | **1908: 34:05**  *(asterisk = flagged)*
- Flagged value: **56:50**, deviation 22.2 h from other-years median (34.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Washington, District of Columbia (1883)
- Values by year: **1882: 60:49** | **1883: 60:49*** | **1892: 36:00** | **1902: 39:00** | **1908: 39:00**  *(asterisk = flagged)*
- Flagged value: **60:49**, deviation 21.8 h from other-years median (39.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Washington, District of Columbia (1882)
- Values by year: **1882: 60:49*** | **1883: 60:49** | **1892: 36:00** | **1902: 39:00** | **1908: 39:00**  *(asterisk = flagged)*
- Flagged value: **60:49**, deviation 21.8 h from other-years median (39.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Saint Louis, Missouri (1883)
- Values by year: **1882: 72:10** | **1883: 72:10*** | **1892: 50:25** | **1902: 50:25** | **1908: 50:25**  *(asterisk = flagged)*
- Flagged value: **72:10**, deviation 21.8 h from other-years median (50.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Saint Louis, Missouri (1882)
- Values by year: **1882: 72:10*** | **1883: 72:10** | **1892: 50:25** | **1902: 50:25** | **1908: 50:25**  *(asterisk = flagged)*
- Flagged value: **72:10**, deviation 21.7 h from other-years median (50.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → Charleston, South Carolina (1883)
- Values by year: **1882: 72:06** | **1883: 72:08*** | **1892: 50:45** | **1902: 50:45**  *(asterisk = flagged)*
- Flagged value: **72:08**, deviation 21.4 h from other-years median (50.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → Charleston, South Carolina (1882)
- Values by year: **1882: 72:06*** | **1883: 72:08** | **1892: 50:45** | **1902: 50:45**  *(asterisk = flagged)*
- Flagged value: **72:06**, deviation 21.4 h from other-years median (50.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Charleston, South Carolina (1882)
- Values by year: **1882: 98:59*** | **1883: 98:59** | **1892: 77:45** | **1902: 77:45**  *(asterisk = flagged)*
- Flagged value: **98:59**, deviation 21.2 h from other-years median (77.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Charleston, South Carolina (1883)
- Values by year: **1882: 98:59** | **1883: 98:59*** | **1892: 77:45** | **1902: 77:45**  *(asterisk = flagged)*
- Flagged value: **98:59**, deviation 21.2 h from other-years median (77.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Winona, Minnesota → Boston, Massachusetts (1882)
- Values by year: **1882: 56:13*** | **1892: 29:20** | **1902: 38:00** | **1908: 35:00**  *(asterisk = flagged)*
- Flagged value: **56:13**, deviation 21.2 h from other-years median (35.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Baltimore, Maryland (1882)
- Values by year: **1882: 53:05*** | **1883: 53:05** | **1892: 42:00** | **1902: 22:00** | **1908: 22:00**  *(asterisk = flagged)*
- Flagged value: **53:05**, deviation 21.1 h from other-years median (32.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Baltimore, Maryland (1883)
- Values by year: **1882: 53:05** | **1883: 53:05*** | **1892: 42:00** | **1902: 22:00** | **1908: 22:00**  *(asterisk = flagged)*
- Flagged value: **53:05**, deviation 21.1 h from other-years median (32.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### St. Louis, Missouri → San Francisco, California (1882)
- Values by year: **1882: 118:24*** | **1883: 113:24** | **1892: 81:15**  *(asterisk = flagged)*
- Flagged value: **118:24**, deviation 21.1 h from other-years median (97.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → Charleston, South Carolina (1882)
- Values by year: **1882: 80:54*** | **1883: 80:54** | **1892: 60:00** | **1902: 60:00** | **1908: 60:00**  *(asterisk = flagged)*
- Flagged value: **80:54**, deviation 20.9 h from other-years median (60.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → Charleston, South Carolina (1883)
- Values by year: **1882: 80:54** | **1883: 80:54*** | **1892: 60:00** | **1902: 60:00** | **1908: 60:00**  *(asterisk = flagged)*
- Flagged value: **80:54**, deviation 20.9 h from other-years median (60.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 84:30*** | **1883: 84:30** | **1892: 73:10** | **1902: 54:10** | **1908: 54:10**  *(asterisk = flagged)*
- Flagged value: **84:30**, deviation 20.8 h from other-years median (63.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 84:30** | **1883: 84:30*** | **1892: 73:10** | **1902: 54:10** | **1908: 54:10**  *(asterisk = flagged)*
- Flagged value: **84:30**, deviation 20.8 h from other-years median (63.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → Omaha, Nebraska (1882)
- Values by year: **1882: 66:20*** | **1883: 66:20** | **1892: 45:35** | **1902: 45:35** | **1908: 42:35**  *(asterisk = flagged)*
- Flagged value: **66:20**, deviation 20.8 h from other-years median (45.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Haven, Connecticut → Omaha, Nebraska (1883)
- Values by year: **1882: 66:20** | **1883: 66:20*** | **1892: 45:35** | **1902: 45:35** | **1908: 42:35**  *(asterisk = flagged)*
- Flagged value: **66:20**, deviation 20.8 h from other-years median (45.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → Omaha, Nebraska (1882)
- Values by year: **1882: 65:35*** | **1883: 65:35** | **1892: 50:00** | **1902: 40:00** | **1908: 40:00**  *(asterisk = flagged)*
- Flagged value: **65:35**, deviation 20.6 h from other-years median (45.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Boston, Massachusetts → Omaha, Nebraska (1883)
- Values by year: **1882: 65:35** | **1883: 65:35*** | **1892: 50:00** | **1902: 40:00** | **1908: 40:00**  *(asterisk = flagged)*
- Flagged value: **65:35**, deviation 20.6 h from other-years median (45.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Saint Louis, Missouri (1883)
- Values by year: **1882: 59:25** | **1883: 59:25*** | **1892: 39:10** | **1902: 39:10** | **1908: 39:10**  *(asterisk = flagged)*
- Flagged value: **59:25**, deviation 20.2 h from other-years median (39.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Chicago, Illinois (1883)
- Values by year: **1882: 60:45** | **1883: 60:45*** | **1892: 40:30** | **1902: 40:30** | **1908: 40:30**  *(asterisk = flagged)*
- Flagged value: **60:45**, deviation 20.2 h from other-years median (40.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Chicago, Illinois (1882)
- Values by year: **1882: 60:45*** | **1883: 60:45** | **1892: 40:30** | **1902: 40:30** | **1908: 40:30**  *(asterisk = flagged)*
- Flagged value: **60:45**, deviation 20.2 h from other-years median (40.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Saint Louis, Missouri (1882)
- Values by year: **1882: 59:25*** | **1883: 59:25** | **1892: 39:10** | **1902: 39:10** | **1908: 39:10**  *(asterisk = flagged)*
- Flagged value: **59:25**, deviation 20.2 h from other-years median (39.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → San Francisco, California (1883)
- Values by year: **1882: 116:27** | **1883: 116:27*** | **1892: 92:45** | **1902: 96:15**  *(asterisk = flagged)*
- Flagged value: **116:27**, deviation 20.2 h from other-years median (96.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vinita, Indian Territory → San Francisco, California (1882)
- Values by year: **1882: 116:27*** | **1883: 116:27** | **1892: 92:45** | **1902: 96:15**  *(asterisk = flagged)*
- Flagged value: **116:27**, deviation 20.2 h from other-years median (96.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → New York, New York (1883)
- Values by year: **1882: 86:40** | **1883: 86:40*** | **1892: 76:30** | **1902: 56:03** | **1908: 56:30**  *(asterisk = flagged)*
- Flagged value: **86:40**, deviation 20.2 h from other-years median (66.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → New York, New York (1882)
- Values by year: **1882: 86:40*** | **1883: 86:40** | **1892: 76:30** | **1902: 56:03** | **1908: 56:30**  *(asterisk = flagged)*
- Flagged value: **86:40**, deviation 20.2 h from other-years median (66.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 130:25** | **1883: 130:25*** | **1892: 112:00** | **1902: 109:00** | **1908: 109:00**  *(asterisk = flagged)*
- Flagged value: **130:25**, deviation 19.9 h from other-years median (110.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 130:25*** | **1883: 130:25** | **1892: 112:00** | **1902: 109:00** | **1908: 109:00**  *(asterisk = flagged)*
- Flagged value: **130:25**, deviation 19.9 h from other-years median (110.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Boston, Massachusetts (1883)
- Values by year: **1882: 93:13** | **1883: 93:13*** | **1892: 83:20** | **1902: 63:20** | **1908: 63:20**  *(asterisk = flagged)*
- Flagged value: **93:13**, deviation 19.9 h from other-years median (73.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Boston, Massachusetts (1882)
- Values by year: **1882: 93:13*** | **1883: 93:13** | **1892: 83:20** | **1902: 63:20** | **1908: 63:20**  *(asterisk = flagged)*
- Flagged value: **93:13**, deviation 19.9 h from other-years median (73.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Washington, District of Columbia (1883)
- Values by year: **1882: 131:52** | **1883: 131:52*** | **1892: 115:00** | **1902: 109:00** | **1908: 109:00**  *(asterisk = flagged)*
- Flagged value: **131:52**, deviation 19.9 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Washington, District of Columbia (1882)
- Values by year: **1882: 131:52*** | **1883: 131:52** | **1892: 115:00** | **1902: 109:00** | **1908: 109:00**  *(asterisk = flagged)*
- Flagged value: **131:52**, deviation 19.9 h from other-years median (112.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 105:35*** | **1883: 105:35** | **1892: 85:50** | **1902: 75:50**  *(asterisk = flagged)*
- Flagged value: **105:35**, deviation 19.8 h from other-years median (85.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 105:35** | **1883: 105:35*** | **1892: 85:50** | **1902: 75:50**  *(asterisk = flagged)*
- Flagged value: **105:35**, deviation 19.8 h from other-years median (85.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Baltimore, Maryland (1882)
- Values by year: **1882: 130:20*** | **1883: 130:20** | **1892: 114:00** | **1902: 108:00** | **1908: 108:00**  *(asterisk = flagged)*
- Flagged value: **130:20**, deviation 19.3 h from other-years median (111.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Baltimore, Maryland (1883)
- Values by year: **1882: 130:20** | **1883: 130:20*** | **1892: 114:00** | **1902: 108:00** | **1908: 108:00**  *(asterisk = flagged)*
- Flagged value: **130:20**, deviation 19.3 h from other-years median (111.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vicksburg, Mississippi → Pittsburgh, Pennsylvania (1883)
- Values by year: **1883: 62:18*** | **1892: 44:00** | **1902: 42:00**  *(asterisk = flagged)*
- Flagged value: **62:18**, deviation 19.3 h from other-years median (43.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 67:05*** | **1883: 67:05** | **1892: 47:50** | **1902: 47:50**  *(asterisk = flagged)*
- Flagged value: **67:05**, deviation 19.3 h from other-years median (47.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, South Carolina → Saint Louis, Missouri (1883)
- Values by year: **1882: 55:25** | **1883: 55:25*** | **1892: 36:10** | **1902: 36:10** | **1908: 36:10**  *(asterisk = flagged)*
- Flagged value: **55:25**, deviation 19.2 h from other-years median (36.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 67:05** | **1883: 67:05*** | **1892: 47:50** | **1902: 47:50**  *(asterisk = flagged)*
- Flagged value: **67:05**, deviation 19.2 h from other-years median (47.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, South Carolina → Saint Louis, Missouri (1882)
- Values by year: **1882: 55:25*** | **1883: 55:25** | **1892: 36:10** | **1902: 36:10** | **1908: 36:10**  *(asterisk = flagged)*
- Flagged value: **55:25**, deviation 19.2 h from other-years median (36.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Fort Smith, Arkansas → Omaha, Nebraska (1882)
- Values by year: **1882: 48:40*** | **1883: 43:40** | **1892: 29:30** | **1902: 29:30** | **1908: 29:30**  *(asterisk = flagged)*
- Flagged value: **48:40**, deviation 19.2 h from other-years median (29.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → Boston, Massachusetts (1883)
- Values by year: **1882: 70:37** | **1883: 70:37*** | **1892: 52:30** | **1902: 46:30** | **1908: 50:30**  *(asterisk = flagged)*
- Flagged value: **70:37**, deviation 19.1 h from other-years median (51.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → Boston, Massachusetts (1882)
- Values by year: **1882: 70:37*** | **1883: 70:37** | **1892: 52:30** | **1902: 46:30** | **1908: 50:30**  *(asterisk = flagged)*
- Flagged value: **70:37**, deviation 19.1 h from other-years median (51.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Massachusetts → Omaha, Nebraska (1882)
- Values by year: **1882: 62:05*** | **1883: 62:05** | **1892: 46:00** | **1902: 40:00** | **1908: 40:00**  *(asterisk = flagged)*
- Flagged value: **62:05**, deviation 19.1 h from other-years median (43.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Springfield, Massachusetts → Omaha, Nebraska (1883)
- Values by year: **1882: 62:05** | **1883: 62:05*** | **1892: 46:00** | **1902: 40:00** | **1908: 40:00**  *(asterisk = flagged)*
- Flagged value: **62:05**, deviation 19.1 h from other-years median (43.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → New York, New York (1883)
- Values by year: **1882: 79:25** | **1883: 79:25*** | **1892: 54:30** | **1902: 60:30**  *(asterisk = flagged)*
- Flagged value: **79:25**, deviation 18.9 h from other-years median (60.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → New York, New York (1882)
- Values by year: **1882: 79:25*** | **1883: 79:25** | **1892: 54:30** | **1902: 60:30**  *(asterisk = flagged)*
- Flagged value: **79:25**, deviation 18.9 h from other-years median (60.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Vicksburg, Mississippi → Cincinnati, Ohio (1883)
- Values by year: **1883: 48:53*** | **1892: 36:00** | **1902: 30:00** | **1908: 30:00**  *(asterisk = flagged)*
- Flagged value: **48:53**, deviation 18.9 h from other-years median (30.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → Charleston, South Carolina (1882)
- Values by year: **1882: 78:59*** | **1883: 78:50** | **1892: 60:15** | **1902: 60:15**  *(asterisk = flagged)*
- Flagged value: **78:59**, deviation 18.7 h from other-years median (60.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Cincinnati, Ohio (1883)
- Values by year: **1882: 47:43** | **1883: 47:43*** | **1892: 32:06** | **1902: 26:00** | **1908: 26:00**  *(asterisk = flagged)*
- Flagged value: **47:43**, deviation 18.7 h from other-years median (29.05 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Cincinnati, Ohio (1882)
- Values by year: **1882: 47:43*** | **1883: 47:43** | **1892: 32:06** | **1902: 26:00** | **1908: 26:00**  *(asterisk = flagged)*
- Flagged value: **47:43**, deviation 18.7 h from other-years median (29.05 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Saint Louis, Missouri (1882)
- Values by year: **1882: 47:38*** | **1883: 47:38** | **1892: 31:00** | **1902: 27:00** | **1908: 27:00**  *(asterisk = flagged)*
- Flagged value: **47:38**, deviation 18.6 h from other-years median (29.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Saint Louis, Missouri (1883)
- Values by year: **1882: 47:38** | **1883: 47:38*** | **1892: 31:00** | **1902: 27:00** | **1908: 27:00**  *(asterisk = flagged)*
- Flagged value: **47:38**, deviation 18.6 h from other-years median (29.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 79:55** | **1883: 79:55*** | **1892: 61:40** | **1902: 61:00** | **1908: 61:00**  *(asterisk = flagged)*
- Flagged value: **79:55**, deviation 18.6 h from other-years median (61.34 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → Boston, Massachusetts (1882)
- Values by year: **1882: 74:35*** | **1883: 74:35** | **1892: 56:00** | **1902: 56:00** | **1908: 53:00**  *(asterisk = flagged)*
- Flagged value: **74:35**, deviation 18.6 h from other-years median (56.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 79:55*** | **1883: 79:55** | **1892: 61:40** | **1902: 61:00** | **1908: 61:00**  *(asterisk = flagged)*
- Flagged value: **79:55**, deviation 18.6 h from other-years median (61.34 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Yankton, Dakota → Charleston, South Carolina (1883)
- Values by year: **1882: 78:59** | **1883: 78:50*** | **1892: 60:15** | **1902: 60:15**  *(asterisk = flagged)*
- Flagged value: **78:50**, deviation 18.6 h from other-years median (60.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → Boston, Massachusetts (1883)
- Values by year: **1882: 74:35** | **1883: 74:35*** | **1892: 56:00** | **1902: 56:00** | **1908: 53:00**  *(asterisk = flagged)*
- Flagged value: **74:35**, deviation 18.6 h from other-years median (56.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 77:19** | **1883: 77:19*** | **1892: 58:50** | **1902: 58:50**  *(asterisk = flagged)*
- Flagged value: **77:19**, deviation 18.5 h from other-years median (58.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 77:19*** | **1883: 77:19** | **1892: 58:50** | **1902: 58:50**  *(asterisk = flagged)*
- Flagged value: **77:19**, deviation 18.5 h from other-years median (58.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → Omaha, Nebraska (1883)
- Values by year: **1882: 67:10** | **1883: 67:10*** | **1892: 48:51** | **1902: 48:35** | **1908: 42:35**  *(asterisk = flagged)*
- Flagged value: **67:10**, deviation 18.5 h from other-years median (48.72 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Willimantic, Connecticut → Omaha, Nebraska (1882)
- Values by year: **1882: 67:10*** | **1883: 67:10** | **1892: 48:51** | **1902: 48:35** | **1908: 42:35**  *(asterisk = flagged)*
- Flagged value: **67:10**, deviation 18.5 h from other-years median (48.72 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Cincinnati, Ohio (1882)
- Values by year: **1882: 83:20*** | **1883: 83:20** | **1892: 69:00** | **1902: 61:00** | **1908: 61:00**  *(asterisk = flagged)*
- Flagged value: **83:20**, deviation 18.3 h from other-years median (65.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Chicago, Illinois (1882)
- Values by year: **1882: 69:50*** | **1883: 69:50** | **1892: 52:30** | **1902: 50:30** | **1908: 50:30**  *(asterisk = flagged)*
- Flagged value: **69:50**, deviation 18.3 h from other-years median (51.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Cincinnati, Ohio (1883)
- Values by year: **1882: 83:20** | **1883: 83:20*** | **1892: 69:00** | **1902: 61:00** | **1908: 61:00**  *(asterisk = flagged)*
- Flagged value: **83:20**, deviation 18.3 h from other-years median (65.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Cincinnati, Ohio (1883)
- Values by year: **1882: 60:00** | **1883: 60:00*** | **1892: 41:40** | **1902: 41:40** | **1908: 41:40**  *(asterisk = flagged)*
- Flagged value: **60:00**, deviation 18.3 h from other-years median (41.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Chicago, Illinois (1883)
- Values by year: **1882: 69:50** | **1883: 69:50*** | **1892: 52:30** | **1902: 50:30** | **1908: 50:30**  *(asterisk = flagged)*
- Flagged value: **69:50**, deviation 18.3 h from other-years median (51.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Jacksonville, Florida → Cincinnati, Ohio (1882)
- Values by year: **1882: 60:00*** | **1883: 60:00** | **1892: 41:40** | **1902: 41:40** | **1908: 41:40**  *(asterisk = flagged)*
- Flagged value: **60:00**, deviation 18.3 h from other-years median (41.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Baltimore, Maryland (1883)
- Values by year: **1882: 84:10** | **1883: 84:10*** | **1892: 72:00** | **1902: 60:00** | **1908: 60:00**  *(asterisk = flagged)*
- Flagged value: **84:10**, deviation 18.2 h from other-years median (66.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### San Antonio, Texas → Baltimore, Maryland (1882)
- Values by year: **1882: 84:10*** | **1883: 84:10** | **1892: 72:00** | **1902: 60:00** | **1908: 60:00**  *(asterisk = flagged)*
- Flagged value: **84:10**, deviation 18.2 h from other-years median (66.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 33:50*** | **1883: 33:50** | **1892: 15:40** | **1902: 15:40**  *(asterisk = flagged)*
- Flagged value: **33:50**, deviation 18.2 h from other-years median (15.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 33:50** | **1883: 33:50*** | **1892: 15:40** | **1902: 15:40**  *(asterisk = flagged)*
- Flagged value: **33:50**, deviation 18.2 h from other-years median (15.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Omaha, Nebraska (1883)
- Values by year: **1882: 56:25** | **1883: 56:25*** | **1892: 43:00** | **1902: 34:00** | **1908: 34:00**  *(asterisk = flagged)*
- Flagged value: **56:25**, deviation 17.9 h from other-years median (38.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Salt Lake City, Utah → Omaha, Nebraska (1882)
- Values by year: **1882: 56:25*** | **1883: 56:25** | **1892: 43:00** | **1902: 34:00** | **1908: 34:00**  *(asterisk = flagged)*
- Flagged value: **56:25**, deviation 17.9 h from other-years median (38.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → Boston, Massachusetts (1882)
- Values by year: **1882: 57:20*** | **1883: 57:20** | **1892: 40:00** | **1902: 39:00** | **1908: 34:00**  *(asterisk = flagged)*
- Flagged value: **57:20**, deviation 17.8 h from other-years median (39.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Montgomery, Alabama → Boston, Massachusetts (1883)
- Values by year: **1882: 57:20** | **1883: 57:20*** | **1892: 40:00** | **1902: 39:00** | **1908: 34:00**  *(asterisk = flagged)*
- Flagged value: **57:20**, deviation 17.8 h from other-years median (39.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 34:46** | **1883: 34:46*** | **1892: 17:00** | **1902: 17:00**  *(asterisk = flagged)*
- Flagged value: **34:46**, deviation 17.8 h from other-years median (17.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 34:46*** | **1883: 34:46** | **1892: 17:00** | **1902: 17:00**  *(asterisk = flagged)*
- Flagged value: **34:46**, deviation 17.8 h from other-years median (17.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 68:30*** | **1883: 68:30** | **1892: 41:50** | **1902: 50:50**  *(asterisk = flagged)*
- Flagged value: **68:30**, deviation 17.7 h from other-years median (50.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albany, New York → Omaha, Nebraska (1883)
- Values by year: **1882: 56:40** | **1883: 56:40*** | **1892: 41:00** | **1902: 37:00** | **1908: 37:00**  *(asterisk = flagged)*
- Flagged value: **56:40**, deviation 17.7 h from other-years median (39.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 68:30** | **1883: 68:30*** | **1892: 41:50** | **1902: 50:50**  *(asterisk = flagged)*
- Flagged value: **68:30**, deviation 17.7 h from other-years median (50.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Albany, New York → Omaha, Nebraska (1882)
- Values by year: **1882: 56:40*** | **1883: 56:40** | **1892: 41:00** | **1902: 37:00** | **1908: 37:00**  *(asterisk = flagged)*
- Flagged value: **56:40**, deviation 17.7 h from other-years median (39.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → Chicago, Illinois (1883)
- Values by year: **1882: 58:10** | **1883: 58:10*** | **1892: 44:10** | **1902: 37:10** | **1908: 37:10**  *(asterisk = flagged)*
- Flagged value: **58:10**, deviation 17.5 h from other-years median (40.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Baltimore, Maryland (1882)
- Values by year: **1882: 76:00*** | **1883: 76:00** | **1892: 58:30** | **1902: 58:30** | **1908: 58:30**  *(asterisk = flagged)*
- Flagged value: **76:00**, deviation 17.5 h from other-years median (58.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Baltimore, Maryland (1883)
- Values by year: **1882: 76:00** | **1883: 76:00*** | **1892: 58:30** | **1902: 58:30** | **1908: 58:30**  *(asterisk = flagged)*
- Flagged value: **76:00**, deviation 17.5 h from other-years median (58.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Savannah, Georgia → Chicago, Illinois (1882)
- Values by year: **1882: 58:10*** | **1883: 58:10** | **1892: 44:10** | **1902: 37:10** | **1908: 37:10**  *(asterisk = flagged)*
- Flagged value: **58:10**, deviation 17.5 h from other-years median (40.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → New York, New York (1882)
- Values by year: **1882: 61:27*** | **1883: 61:27** | **1892: 46:00** | **1902: 40:00** | **1908: 42:00**  *(asterisk = flagged)*
- Flagged value: **61:27**, deviation 17.4 h from other-years median (44.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → New York, New York (1883)
- Values by year: **1882: 61:27** | **1883: 61:27*** | **1892: 46:00** | **1902: 40:00** | **1908: 42:00**  *(asterisk = flagged)*
- Flagged value: **61:27**, deviation 17.4 h from other-years median (44.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Concord, New Hampshire → Omaha, Nebraska (1882)
- Values by year: **1882: 68:00*** | **1883: 68:00** | **1892: 52:30** | **1902: 48:39** | **1908: 48:39**  *(asterisk = flagged)*
- Flagged value: **68:00**, deviation 17.4 h from other-years median (50.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Concord, New Hampshire → Omaha, Nebraska (1883)
- Values by year: **1882: 68:00** | **1883: 68:00*** | **1892: 52:30** | **1902: 48:39** | **1908: 48:39**  *(asterisk = flagged)*
- Flagged value: **68:00**, deviation 17.4 h from other-years median (50.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rome, New York → Omaha, Nebraska (1882)
- Values by year: **1882: 54:20*** | **1883: 54:20** | **1892: 37:30** | **1902: 36:30** | **1908: 36:30**  *(asterisk = flagged)*
- Flagged value: **54:20**, deviation 17.3 h from other-years median (37.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Rome, New York → Omaha, Nebraska (1883)
- Values by year: **1882: 54:20** | **1883: 54:20*** | **1892: 37:30** | **1902: 36:30** | **1908: 36:30**  *(asterisk = flagged)*
- Flagged value: **54:20**, deviation 17.3 h from other-years median (37.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Chicago, Illinois (1883)
- Values by year: **1882: 102:40** | **1883: 102:40*** | **1892: 86:25** | **1902: 84:25** | **1908: 84:25**  *(asterisk = flagged)*
- Flagged value: **102:40**, deviation 17.2 h from other-years median (85.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → Chicago, Illinois (1882)
- Values by year: **1882: 102:40*** | **1883: 102:40** | **1892: 86:25** | **1902: 84:25** | **1908: 84:25**  *(asterisk = flagged)*
- Flagged value: **102:40**, deviation 17.2 h from other-years median (85.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → New York, New York (1883)
- Values by year: **1882: 129:25** | **1883: 129:25*** | **1892: 115:15** | **1902: 109:15** | **1908: 109:15**  *(asterisk = flagged)*
- Flagged value: **129:25**, deviation 17.2 h from other-years median (112.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Carson City, Nevada → New York, New York (1882)
- Values by year: **1882: 129:25*** | **1883: 129:25** | **1892: 115:15** | **1902: 109:15** | **1908: 109:15**  *(asterisk = flagged)*
- Flagged value: **129:25**, deviation 17.2 h from other-years median (112.25 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Boston, Massachusetts (1882)
- Values by year: **1882: 81:56*** | **1883: 81:56** | **1892: 64:50** | **1902: 64:50**  *(asterisk = flagged)*
- Flagged value: **81:56**, deviation 17.1 h from other-years median (64.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Boston, Massachusetts (1883)
- Values by year: **1882: 81:56** | **1883: 81:56*** | **1892: 64:50** | **1902: 64:50**  *(asterisk = flagged)*
- Flagged value: **81:56**, deviation 17.1 h from other-years median (64.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Newport, Rhode Island → Omaha, Nebraska (1882)
- Values by year: **1882: 70:35*** | **1883: 70:35** | **1892: 53:30** | **1902: 53:30** | **1908: 53:30**  *(asterisk = flagged)*
- Flagged value: **70:35**, deviation 17.1 h from other-years median (53.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Newport, Rhode Island → Omaha, Nebraska (1883)
- Values by year: **1882: 70:35** | **1883: 70:35*** | **1892: 53:30** | **1902: 53:30** | **1908: 53:30**  *(asterisk = flagged)*
- Flagged value: **70:35**, deviation 17.1 h from other-years median (53.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Omaha, Nebraska (1883)
- Values by year: **1882: 43:00** | **1883: 48:00*** | **1892: 30:55** | **1902: 30:55**  *(asterisk = flagged)*
- Flagged value: **48:00**, deviation 17.1 h from other-years median (30.92 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Boston, Massachusetts (1883)
- Values by year: **1882: 65:31** | **1883: 65:31*** | **1892: 48:00** | **1902: 49:00** | **1908: 37:00**  *(asterisk = flagged)*
- Flagged value: **65:31**, deviation 17.0 h from other-years median (48.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Boston, Massachusetts (1882)
- Values by year: **1882: 65:31*** | **1883: 65:31** | **1892: 48:00** | **1902: 49:00** | **1908: 37:00**  *(asterisk = flagged)*
- Flagged value: **65:31**, deviation 17.0 h from other-years median (48.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Omaha, Nebraska (1882)
- Values by year: **1882: 67:30*** | **1883: 67:30** | **1892: 53:00** | **1902: 48:00** | **1908: 48:00**  *(asterisk = flagged)*
- Flagged value: **67:30**, deviation 17.0 h from other-years median (50.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Omaha, Nebraska (1883)
- Values by year: **1882: 67:30** | **1883: 67:30*** | **1892: 53:00** | **1902: 48:00** | **1908: 48:00**  *(asterisk = flagged)*
- Flagged value: **67:30**, deviation 17.0 h from other-years median (50.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Omaha, Nebraska → Boston, Massachusetts (1883)
- Values by year: **1882: 62:58** | **1883: 62:58*** | **1892: 47:00** | **1902: 45:00** | **1908: 45:00**  *(asterisk = flagged)*
- Flagged value: **62:58**, deviation 17.0 h from other-years median (46.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Omaha, Nebraska → Boston, Massachusetts (1882)
- Values by year: **1882: 62:58*** | **1883: 62:58** | **1892: 47:00** | **1902: 45:00** | **1908: 45:00**  *(asterisk = flagged)*
- Flagged value: **62:58**, deviation 17.0 h from other-years median (46.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 56:55** | **1883: 56:55*** | **1892: 45:00** | **1902: 35:00** | **1908: 35:00**  *(asterisk = flagged)*
- Flagged value: **56:55**, deviation 16.9 h from other-years median (40.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Boston, Massachusetts (1883)
- Values by year: **1882: 69:25** | **1883: 69:25*** | **1892: 57:30** | **1902: 47:30** | **1908: 47:30**  *(asterisk = flagged)*
- Flagged value: **69:25**, deviation 16.9 h from other-years median (52.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 56:55*** | **1883: 56:55** | **1892: 45:00** | **1902: 35:00** | **1908: 35:00**  *(asterisk = flagged)*
- Flagged value: **56:55**, deviation 16.9 h from other-years median (40.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Boston, Massachusetts (1882)
- Values by year: **1882: 69:25*** | **1883: 69:25** | **1892: 57:30** | **1902: 47:30** | **1908: 47:30**  *(asterisk = flagged)*
- Flagged value: **69:25**, deviation 16.9 h from other-years median (52.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dover, Delaware → Charleston, South Carolina (1883)
- Values by year: **1882: 38:52** | **1883: 38:52*** | **1892: 22:00** | **1902: 22:00** | **1908: 22:00**  *(asterisk = flagged)*
- Flagged value: **38:52**, deviation 16.9 h from other-years median (22.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Hartford, Connecticut → Omaha, Nebraska (1883)
- Values by year: **1882: 61:27** | **1883: 64:27*** | **1892: 47:35** | **1902: 47:35** | **1908: 42:35**  *(asterisk = flagged)*
- Flagged value: **64:27**, deviation 16.9 h from other-years median (47.58 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Dover, Delaware → Charleston, South Carolina (1882)
- Values by year: **1882: 38:52*** | **1883: 38:52** | **1892: 22:00** | **1902: 22:00** | **1908: 22:00**  *(asterisk = flagged)*
- Flagged value: **38:52**, deviation 16.9 h from other-years median (22.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Boston, Massachusetts (1882)
- Values by year: **1882: 44:30*** | **1883: 44:30** | **1892: 28:40** | **1902: 26:40** | **1908: 26:40**  *(asterisk = flagged)*
- Flagged value: **44:30**, deviation 16.8 h from other-years median (27.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Huntington, West Virginia → Boston, Massachusetts (1883)
- Values by year: **1882: 44:30** | **1883: 44:30*** | **1892: 28:40** | **1902: 26:40** | **1908: 26:40**  *(asterisk = flagged)*
- Flagged value: **44:30**, deviation 16.8 h from other-years median (27.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → Boston, Massachusetts (1882)
- Values by year: **1882: 64:18*** | **1883: 64:13** | **1892: 48:30** | **1902: 46:30** | **1908: 46:30**  *(asterisk = flagged)*
- Flagged value: **64:18**, deviation 16.8 h from other-years median (47.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Lincoln, Nebraska → Boston, Massachusetts (1883)
- Values by year: **1882: 64:18** | **1883: 64:13*** | **1892: 48:30** | **1902: 46:30** | **1908: 46:30**  *(asterisk = flagged)*
- Flagged value: **64:13**, deviation 16.7 h from other-years median (47.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → New York, New York (1883)
- Values by year: **1882: 57:40** | **1883: 57:40*** | **1892: 32:00** | **1902: 41:00** | **1908: 41:00**  *(asterisk = flagged)*
- Flagged value: **57:40**, deviation 16.7 h from other-years median (41.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → New York, New York (1882)
- Values by year: **1882: 57:40*** | **1883: 57:40** | **1892: 32:00** | **1902: 41:00** | **1908: 41:00**  *(asterisk = flagged)*
- Flagged value: **57:40**, deviation 16.7 h from other-years median (41.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → Omaha, Nebraska (1883)
- Values by year: **1882: 73:37** | **1883: 73:37*** | **1892: 67:00** | **1902: 47:00** | **1908: 47:00**  *(asterisk = flagged)*
- Flagged value: **73:37**, deviation 16.6 h from other-years median (57.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Augusta, Maine → Omaha, Nebraska (1882)
- Values by year: **1882: 73:37*** | **1883: 73:37** | **1892: 67:00** | **1902: 47:00** | **1908: 47:00**  *(asterisk = flagged)*
- Flagged value: **73:37**, deviation 16.6 h from other-years median (57.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pittsburgh, Pennsylvania → San Francisco, California (1882)
- Values by year: **1882: 132:15*** | **1883: 132:15** | **1892: 99:15**  *(asterisk = flagged)*
- Flagged value: **132:15**, deviation 16.5 h from other-years median (115.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Providence, Rhode Island → Omaha, Nebraska (1883)
- Values by year: **1882: 67:30** | **1883: 67:30*** | **1892: 52:00** | **1902: 50:00** | **1908: 50:00**  *(asterisk = flagged)*
- Flagged value: **67:30**, deviation 16.5 h from other-years median (51.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Pittsburgh, Pennsylvania → San Francisco, California (1883)
- Values by year: **1882: 132:15** | **1883: 132:15*** | **1892: 99:15**  *(asterisk = flagged)*
- Flagged value: **132:15**, deviation 16.5 h from other-years median (115.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Providence, Rhode Island → Omaha, Nebraska (1882)
- Values by year: **1882: 67:30*** | **1883: 67:30** | **1892: 52:00** | **1902: 50:00** | **1908: 50:00**  *(asterisk = flagged)*
- Flagged value: **67:30**, deviation 16.5 h from other-years median (51.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 58:07** | **1883: 58:07*** | **1892: 43:17** | **1902: 37:00** | **1908: 40:00**  *(asterisk = flagged)*
- Flagged value: **58:07**, deviation 16.5 h from other-years median (41.64 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New Orleans, Louisiana → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 58:07*** | **1883: 58:07** | **1892: 43:17** | **1902: 37:00** | **1908: 40:00**  *(asterisk = flagged)*
- Flagged value: **58:07**, deviation 16.5 h from other-years median (41.64 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → New York, New York (1883)
- Values by year: **1882: 60:15** | **1883: 60:15*** | **1892: 48:50** | **1902: 38:50** | **1908: 38:50**  *(asterisk = flagged)*
- Flagged value: **60:15**, deviation 16.4 h from other-years median (43.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → New York, New York (1882)
- Values by year: **1882: 60:15*** | **1883: 60:15** | **1892: 48:50** | **1902: 38:50** | **1908: 38:50**  *(asterisk = flagged)*
- Flagged value: **60:15**, deviation 16.4 h from other-years median (43.83 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Cincinnati, Ohio (1883)
- Values by year: **1882: 117:55** | **1883: 117:55*** | **1892: 101:30** | **1902: 101:30** | **1908: 101:30**  *(asterisk = flagged)*
- Flagged value: **117:55**, deviation 16.4 h from other-years median (101.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Cincinnati, Ohio (1882)
- Values by year: **1882: 117:55*** | **1883: 117:55** | **1892: 101:30** | **1902: 101:30** | **1908: 101:30**  *(asterisk = flagged)*
- Flagged value: **117:55**, deviation 16.4 h from other-years median (101.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Baltimore, Maryland (1882)
- Values by year: **1882: 80:15*** | **1883: 80:15** | **1892: 75:30** | **1902: 52:30** | **1908: 52:30**  *(asterisk = flagged)*
- Flagged value: **80:15**, deviation 16.2 h from other-years median (64.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Galveston, Texas → Baltimore, Maryland (1883)
- Values by year: **1882: 80:15** | **1883: 80:15*** | **1892: 75:30** | **1902: 52:30** | **1908: 52:30**  *(asterisk = flagged)*
- Flagged value: **80:15**, deviation 16.2 h from other-years median (64.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Saint Louis, Missouri (1883)
- Values by year: **1882: 58:10** | **1883: 58:10*** | **1892: 42:00** | **1902: 42:00**  *(asterisk = flagged)*
- Flagged value: **58:10**, deviation 16.2 h from other-years median (42.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Saint Louis, Missouri (1882)
- Values by year: **1882: 58:10*** | **1883: 58:10** | **1892: 42:00** | **1902: 42:00**  *(asterisk = flagged)*
- Flagged value: **58:10**, deviation 16.2 h from other-years median (42.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 55:20*** | **1883: 55:20** | **1892: 33:40** | **1902: 39:40** | **1908: 38:40**  *(asterisk = flagged)*
- Flagged value: **55:20**, deviation 16.2 h from other-years median (39.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Duluth, Minnesota → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 55:20** | **1883: 55:20*** | **1892: 33:40** | **1902: 39:40** | **1908: 38:40**  *(asterisk = flagged)*
- Flagged value: **55:20**, deviation 16.2 h from other-years median (39.17 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → New York, New York (1883)
- Values by year: **1882: 65:25** | **1883: 65:25*** | **1892: 49:30** | **1902: 49:30** | **1908: 45:30**  *(asterisk = flagged)*
- Flagged value: **65:25**, deviation 15.9 h from other-years median (49.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → New York, New York (1882)
- Values by year: **1882: 65:25*** | **1883: 65:25** | **1892: 49:30** | **1902: 49:30** | **1908: 45:30**  *(asterisk = flagged)*
- Flagged value: **65:25**, deviation 15.9 h from other-years median (49.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Saint Louis, Missouri (1882)
- Values by year: **1882: 45:15*** | **1883: 45:15** | **1892: 24:25** | **1902: 29:25** | **1908: 29:25**  *(asterisk = flagged)*
- Flagged value: **45:15**, deviation 15.8 h from other-years median (29.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Mobile, Alabama → Saint Louis, Missouri (1883)
- Values by year: **1882: 45:15** | **1883: 45:15*** | **1892: 24:25** | **1902: 29:25** | **1908: 29:25**  *(asterisk = flagged)*
- Flagged value: **45:15**, deviation 15.8 h from other-years median (29.42 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Omaha, Nebraska (1882)
- Values by year: **1882: 91:30*** | **1883: 91:30** | **1892: 75:40** | **1902: 75:40** | **1908: 75:40**  *(asterisk = flagged)*
- Flagged value: **91:30**, deviation 15.8 h from other-years median (75.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Sacramento, California → Omaha, Nebraska (1883)
- Values by year: **1882: 91:30** | **1883: 91:30*** | **1892: 75:40** | **1902: 75:40** | **1908: 75:40**  *(asterisk = flagged)*
- Flagged value: **91:30**, deviation 15.8 h from other-years median (75.67 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New York, New York → Omaha, Nebraska (1883)
- Values by year: **1882: 61:30** | **1883: 61:30*** | **1892: 45:45** | **1902: 45:45** | **1908: 45:45**  *(asterisk = flagged)*
- Flagged value: **61:30**, deviation 15.8 h from other-years median (45.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### New York, New York → Omaha, Nebraska (1882)
- Values by year: **1882: 61:30*** | **1883: 61:30** | **1892: 45:45** | **1902: 45:45** | **1908: 45:45**  *(asterisk = flagged)*
- Flagged value: **61:30**, deviation 15.8 h from other-years median (45.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Washington, District of Columbia (1882)
- Values by year: **1882: 74:08*** | **1883: 74:08** | **1892: 59:30** | **1902: 57:30** | **1908: 57:30**  *(asterisk = flagged)*
- Flagged value: **74:08**, deviation 15.6 h from other-years median (58.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → Washington, District of Columbia (1883)
- Values by year: **1882: 74:08** | **1883: 74:08*** | **1892: 59:30** | **1902: 57:30** | **1908: 57:30**  *(asterisk = flagged)*
- Flagged value: **74:08**, deviation 15.6 h from other-years median (58.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → Philadelphia, Pennsylvania (1882)
- Values by year: **1882: 62:05*** | **1883: 62:05** | **1892: 46:47** | **1902: 46:30** | **1908: 43:30**  *(asterisk = flagged)*
- Flagged value: **62:05**, deviation 15.4 h from other-years median (46.64 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Morgan City, Louisiana → Philadelphia, Pennsylvania (1883)
- Values by year: **1882: 62:05** | **1883: 62:05*** | **1892: 46:47** | **1902: 46:30** | **1908: 43:30**  *(asterisk = flagged)*
- Flagged value: **62:05**, deviation 15.4 h from other-years median (46.64 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Cincinnati, Ohio (1883)
- Values by year: **1882: 94:25** | **1883: 94:25*** | **1892: 80:00** | **1902: 78:00** | **1908: 78:00**  *(asterisk = flagged)*
- Flagged value: **94:25**, deviation 15.4 h from other-years median (79.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Elko, Nevada → Cincinnati, Ohio (1882)
- Values by year: **1882: 94:25*** | **1883: 94:25** | **1892: 80:00** | **1902: 78:00** | **1908: 78:00**  *(asterisk = flagged)*
- Flagged value: **94:25**, deviation 15.4 h from other-years median (79.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cairo, Illinois → Charleston, South Carolina (1883)
- Values by year: **1882: 58:09** | **1883: 58:09*** | **1892: 42:45** | **1902: 42:45** | **1908: 42:45**  *(asterisk = flagged)*
- Flagged value: **58:09**, deviation 15.4 h from other-years median (42.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cairo, Illinois → Charleston, South Carolina (1882)
- Values by year: **1882: 58:09*** | **1883: 58:09** | **1892: 42:45** | **1902: 42:45** | **1908: 42:45**  *(asterisk = flagged)*
- Flagged value: **58:09**, deviation 15.4 h from other-years median (42.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Boston, Massachusetts (1883)
- Values by year: **1882: 71:21** | **1883: 71:21*** | **1892: 56:30** | **1902: 55:30** | **1908: 55:30**  *(asterisk = flagged)*
- Flagged value: **71:21**, deviation 15.3 h from other-years median (56.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Cedar Keys, Florida → Boston, Massachusetts (1882)
- Values by year: **1882: 71:21*** | **1883: 71:21** | **1892: 56:30** | **1902: 55:30** | **1908: 55:30**  *(asterisk = flagged)*
- Flagged value: **71:21**, deviation 15.3 h from other-years median (56.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Helena, Arkansas → Omaha, Nebraska (1883)
- Values by year: **1883: 53:20*** | **1892: 38:00** | **1902: 38:00** | **1908: 68:00**  *(asterisk = flagged)*
- Flagged value: **53:20**, deviation 15.3 h from other-years median (38.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → Charleston, South Carolina (1883)
- Values by year: **1882: 76:45** | **1883: 76:45*** | **1892: 63:30** | **1902: 59:30** | **1908: 59:30**  *(asterisk = flagged)*
- Flagged value: **76:45**, deviation 15.2 h from other-years median (61.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Eastport, Maine → Charleston, South Carolina (1882)
- Values by year: **1882: 76:45*** | **1883: 76:45** | **1892: 63:30** | **1902: 59:30** | **1908: 59:30**  *(asterisk = flagged)*
- Flagged value: **76:45**, deviation 15.2 h from other-years median (61.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Baltimore, Maryland (1883)
- Values by year: **1882: 76:10** | **1883: 76:10*** | **1892: 58:00** | **1902: 61:00**  *(asterisk = flagged)*
- Flagged value: **76:10**, deviation 15.2 h from other-years median (61.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → Pittsburgh, Pennsylvania (1883)
- Values by year: **1882: 47:30** | **1883: 47:30*** | **1892: 32:20** | **1902: 32:20**  *(asterisk = flagged)*
- Flagged value: **47:30**, deviation 15.2 h from other-years median (32.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Macon, Georgia → Pittsburgh, Pennsylvania (1882)
- Values by year: **1882: 47:30*** | **1883: 47:30** | **1892: 32:20** | **1902: 32:20**  *(asterisk = flagged)*
- Flagged value: **47:30**, deviation 15.2 h from other-years median (32.33 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Bismarck, Dakota → Baltimore, Maryland (1882)
- Values by year: **1882: 76:10*** | **1883: 76:10** | **1892: 58:00** | **1902: 61:00**  *(asterisk = flagged)*
- Flagged value: **76:10**, deviation 15.2 h from other-years median (61.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Boston, Massachusetts (1882)
- Values by year: **1882: 42:00*** | **1883: 42:00** | **1892: 27:00** | **1902: 26:50** | **1908: 26:00**  *(asterisk = flagged)*
- Flagged value: **42:00**, deviation 15.1 h from other-years median (26.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Charleston, West Virginia → Boston, Massachusetts (1883)
- Values by year: **1882: 42:00** | **1883: 42:00*** | **1892: 27:00** | **1902: 26:50** | **1908: 26:00**  *(asterisk = flagged)*
- Flagged value: **42:00**, deviation 15.1 h from other-years median (26.91 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → New York, New York (1883)
- Values by year: **1882: 81:04** | **1883: 81:04*** | **1892: 70:30** | **1902: 61:30** | **1908: 61:30**  *(asterisk = flagged)*
- Flagged value: **81:04**, deviation 15.1 h from other-years median (66.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Denver, Colorado → New York, New York (1882)
- Values by year: **1882: 81:04*** | **1883: 81:04** | **1892: 70:30** | **1902: 61:30** | **1908: 61:30**  *(asterisk = flagged)*
- Flagged value: **81:04**, deviation 15.1 h from other-years median (66.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prairie du Chien, Wisconsin → Boston, Massachusetts (1882)
- Values by year: **1882: 53:32*** | **1883: 53:32** | **1892: 38:30** | **1902: 38:30** | **1908: 38:30**  *(asterisk = flagged)*
- Flagged value: **53:32**, deviation 15.0 h from other-years median (38.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Prairie du Chien, Wisconsin → Boston, Massachusetts (1883)
- Values by year: **1882: 53:32** | **1883: 53:32*** | **1892: 38:30** | **1902: 38:30** | **1908: 38:30**  *(asterisk = flagged)*
- Flagged value: **53:32**, deviation 15.0 h from other-years median (38.50 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Omaha, Nebraska (1883)
- Values by year: **1882: 75:45** | **1883: 75:45*** | **1892: 60:45** | **1902: 60:45** | **1908: 60:45**  *(asterisk = flagged)*
- Flagged value: **75:45**, deviation 15.0 h from other-years median (60.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Washington, District of Columbia (1882)
- Values by year: **1882: 51:00*** | **1883: 51:00** | **1892: 41:00** | **1902: 31:00** | **1908: 31:00**  *(asterisk = flagged)*
- Flagged value: **51:00**, deviation 15.0 h from other-years median (36.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Tallahassee, Florida → Washington, District of Columbia (1883)
- Values by year: **1882: 51:00** | **1883: 51:00*** | **1892: 41:00** | **1902: 31:00** | **1908: 31:00**  *(asterisk = flagged)*
- Flagged value: **51:00**, deviation 15.0 h from other-years median (36.00 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`

### Port Royal, South Carolina → Omaha, Nebraska (1882)
- Values by year: **1882: 75:45*** | **1883: 75:45** | **1892: 60:45** | **1902: 60:45** | **1908: 60:45**  *(asterisk = flagged)*
- Flagged value: **75:45**, deviation 15.0 h from other-years median (60.75 h)
- No 3↔8 substitution found — manual review needed
- Error type: `unknown`
