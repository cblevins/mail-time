# Data Outliers in 1882 Transit Times CSV

Systematic review of `1882_TransitTimes.csv` against geographic expectations and neighboring city values. Organized by state for easy manual correction.

## Pattern Note

The overwhelming pattern is **8 appearing where 3 is expected** (e.g., `88:xx` instead of `38:xx`, `82:xx` instead of `32:xx`). This is a classic OCR error — in many 19th-century typefaces, the digits 3 and 8 are easily confused. The transcription likely used OCR on the original 1882 document.

Values marked with **[min>59]** have minutes exceeding 59, which is always invalid regardless of the intended value.

---

## Alabama

### Decatur
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| New York | `89:53:00` | `39:53:00` | Other AL cities: Mobile 52:25, Montgomery 44:15. 89 hrs is wildly out of range. |
| Baltimore | `82:53:00` | `32:53:00` | Other AL cities: Mobile 47:20, Montgomery 39:10. |

### Montgomery
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Pittsburgh | `87:05:00` | `37:05:00` | Decatur 29:55, Mobile 45:20. |
| Charleston | `82:00:00` | `32:00:00` | Atlanta→Charleston is 17:25, Mobile→Charleston is 38:55. |

---

## Arkansas

### Fort Smith
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Cincinnati | `88:24:00` | `38:24:00` | Little Rock→Cincinnati is 28:29. Fort Smith is farther but 88 hrs is extreme. |

### Little Rock
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `88:00:00` | `38:00:00` | Fort Smith→Omaha is 48:40, so Little Rock (closer to the east) should be less. |

---

## Colorado

### Pueblo
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `89:14:00` | `39:14:00` | Denver→St. Louis is 44:10. Pueblo is nearby and should be similar. |

---

## Connecticut

### New Haven
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Charleston | `86:20:00` | `36:20:00` | Hartford→Charleston is 37:39. New Haven is nearby. |

### Willimantic
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Chicago | `162:42:15` | `36:42` (garbled) | Hartford is 35:02, New Haven is 36:55. The value 162:42:15 is completely garbled — likely a transcription error spanning multiple columns. |
| Charleston | `89:30:00` | `39:30:00` | Hartford is 37:39. |

---

## Delaware

### Dover
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Chicago | `88:40:00` | `38:40:00` or `28:40:00` | Trenton NJ→Chicago is 32:50. Dover is close by. |
| Charleston | `88:52:00` | `28:52:00` | Wilmington DE→Charleston is 28:42. Dover is nearby. |

### Wilmington
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Chicago | `87:03:00` | `27:03:00` | Trenton NJ is 32:50, Philadelphia is 23:25. |
| St. Louis | `85:10:00` | `35:10:00` | Philadelphia→St. Louis is 32:00, Dover→St. Louis is 37:18. |

---

## Florida

### Jacksonville
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Baltimore | `88:35:00` | `38:35:00` | Cedar Keys→Baltimore is 53:10, Key West is 53:05. Jacksonville (northernmost FL city) should be shorter. |

---

## Georgia

### Augusta
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| New York | `88:55:00` | `38:55:00` | Atlanta→NY is 37:15, Savannah is 39:10. |

### Macon
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `84:10:00` | `34:10:00` | Atlanta→St. Louis is 30:55, Augusta is 48:15. |

---

## Illinois

### Cairo
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `81:25:00` | `31:25:00` | Springfield IL→Omaha is 18:26, Rock Island is 15:20. Cairo is in southern IL, farther from Omaha, but 81 hrs is extreme. |

---

## Iowa

### Burlington
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `12:80` | Unknown | **[min>59]** Minutes exceed 59. Likely `12:30` or `12:50` based on nearby Dubuque (25:10) and Des Moines (6:50). |

### Sioux City
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Cincinnati | `85:08:00` | `35:08:00` | Des Moines→Cincinnati is 27:10, Dubuque is 20:20. |

---

## Kansas

### Atchison
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `6:88` | Unknown | **[min>59]** Minutes exceed 59. Leavenworth→Omaha is 7:40, Topeka is 7:05. Likely `6:48` or similar. |

---

## Kentucky

### Henderson
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `26:80` | Unknown | **[min>59]** Minutes exceed 59. Louisville→Omaha is 26:45. Likely `26:30` or `26:50`. |

---

## Louisiana

### Morgan City
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Cincinnati | `88:35:00` | `38:35:00` | New Orleans→Cincinnati is 84:55 (also suspect — see below). |
| St. Louis | `88:20:00` | `38:20:00` | New Orleans→St. Louis is 29:40. |

### New Orleans
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Cincinnati | `84:55:00` | `34:55:00` | Jackson MS→Cincinnati is 17:58. New Orleans is farther but 84 hrs is ~3.5 days for a well-connected city. |

### Shreveport
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `88:02:00` | `38:02:00` | New Orleans→St. Louis is 29:40. |

---

## Maine

### Augusta
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `78:87` | Unknown | **[min>59]** Minutes exceed 59. Portland ME→Omaha is 70:35. Likely `78:37` or `78:57`. |

---

## Maryland

### Annapolis
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `88:09:00` | `33:09:00` | Baltimore→St. Louis is 31:15. Annapolis is right next to Baltimore. |

---

## Massachusetts

### Boston
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `5:35` | `65:35` | 5 hours 35 minutes from Boston to Omaha is impossible by 1882 rail. Boston→St. Louis is 42:35, Boston→Chicago is 36:10. Missing leading digit. |

---

## Michigan

### Lansing
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `80:82` | Unknown | **[min>59]** Minutes exceed 59. Bay City→Omaha is 88:10 (also likely suspect). Likely `30:32` or `30:52`. |

---

## Minnesota

### St. Paul
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `25:85` | Unknown | **[min>59]** Minutes exceed 59. Winona→St. Louis is 21:84 (also invalid). Likely `25:35` or `25:55`. |
| Omaha | `17:88` | Unknown | **[min>59]** Minutes exceed 59. Duluth→Omaha is 25:28. Likely `17:38` or `17:48`. |

### Winona
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `21:84` | Unknown | **[min>59]** Minutes exceed 59. Likely `21:34` or `21:54`. |

---

## Mississippi

### Vicksburg
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Cincinnati | `00:58` | `30:58` or `40:58` | 58 minutes from Mississippi to Ohio is impossible. Jackson MS→Cincinnati is 17:58. Missing leading digits — likely `30:58`. |

---

## Nebraska

### Lincoln
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `22:87` | Unknown | **[min>59]** Minutes exceed 59. Omaha→St. Louis is 15:10. Likely `22:37` or `22:47`. |
| Cincinnati | `84:45:00` | `34:45:00` | Omaha→Cincinnati is 27:18. |

---

## Nevada

### Carson City
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Washington, D.C. | `181:52:00` | `131:52:00` | All other values in this row are 95-154 hrs. 181 is a massive outlier. |

### Elko
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `88:85` | Unknown | **[min>59]** Minutes exceed 59. Carson City→St. Louis is 95:25. Likely `88:35` or `88:55`. |

---

## New Hampshire

### Concord
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Cincinnati | `88:30:00` | `38:30:00` | Portland ME→Cincinnati is 42:00, Boston is 31:00. |

---

## New Jersey

### Trenton
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `81:25` | `31:25` | Philadelphia→St. Louis is 32:00, Cape May is 37:20. |

---

## New Mexico

### Mesilla
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Charleston | `24:04:00` | `124:04:00` | Santa Fe→Charleston is 110:19. From southern NM to SC in 24 hours is impossible. Missing leading digit `1`. |
| St. Louis | `26:54` | `76:54` or `126:54` | Santa Fe→St. Louis is 56:09. From NM in 26 hrs is too fast. Missing leading digit. |

---

## Ohio

### Columbus
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `13:85` | Unknown | **[min>59]** Minutes exceed 59. Cincinnati→St. Louis is 10:00, Cleveland is 18:10. Likely `13:35` or `13:55`. |

---

## Tennessee

### Nashville
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Philadelphia | `85:05:00` | `35:05:00` | Chattanooga→Philadelphia is 31:45, Memphis is 43:40. |

---

## West Virginia

### Charleston
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| St. Louis | `50:88` | Unknown | **[min>59]** Minutes exceed 59. Grafton→St. Louis is 22:48. Likely `50:38` or `50:48`. |

---

## Wisconsin

### Milwaukee
| Destination | Raw Value | Likely Correct | Reasoning |
|------------|-----------|----------------|-----------|
| Omaha | `26:80` | Unknown | **[min>59]** Minutes exceed 59. Madison→Omaha is 82:25 (also possibly suspect). Likely `26:30` or `26:50`. |

---

## Additional Notes

### Values that may be correct but worth double-checking
These are not necessarily errors, but are worth verifying against the original PDF:

- **Grafton, WV → San Francisco: `185:47`** and **Wheeling, WV → San Francisco: `184:35`** — unusually high for cities near Pittsburgh (132:15 to SF). Could reflect indirect routing.
- **Memphis, TN → Chicago: `44:20:00`** — same value as Memphis → Charleston (`44:20:00`). Possibly a column-shift copy error during transcription.
- **Bay City, MI → Omaha: `88:10`** and **Detroit, MI → Omaha: `82:17`** — both possibly should start with 3 (38:10, 32:17) based on Kalamazoo (27:22).
- **Duluth, MN → Cincinnati: `23:43`** — seems fast for that distance. Nearby St. Paul is 29:28. May be correct given Duluth's rail connections.
