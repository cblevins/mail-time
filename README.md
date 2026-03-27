# How Fast Was the Mail?

An interactive data visualization exploring how long it took mail to travel by railroad between major American cities during the late nineteenth and early twentieth centuries (1882–1908).

🗺️ **[View the live visualization here](https://cblevins.github.io/mail-time/)**

✏️ Read more about this visualization at: Cameron Blevins, ["Bottlenecks, Side Quests, and the Calculus of Historical Research"](cblevins.github.io/posts/bottleneck-side-quests/) (March 27, 2026)

_This visualization was created by [Cameron Blevins](https://cblevins.github.io/) using Claude Code_

---

## Data

- The core mail transit dataset is [`transit-times-merged.csv`](data/transit-times-merged.csv) — a combined table of mail transit times across all five years (1882, 1883, 1892, 1902, 1908), with origin city, destination city, state, and transit time in hours.
- The `data` folder also contains individual transit tables that were transcribed using Google's Gemini 3.1 Pro
- Railroad data is from: Jeremy Atack, ["Historical Geographic Information Systems (GIS) database of U.S. Railroads for 1826-1911"](https://my.vanderbilt.edu/jeremyatack/data-downloads/) (May 2016; revised Oct 31, 2023).
- The original source documents — U.S. Official Postal Guide tables listing scheduled railroad mail transit times — are in `source-docs/` as PDFs. These came from:
  - [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=mdp.39015063600780&seq=609) (January 1882), p. 579-582.
  - [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=njp.32101068314788&seq=654) (January 1883), p. 612-615.
  - [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=uc1.b2919442&seq=737) (January 1892), p. 735-738.
  - [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=hvd.hn4jgx&seq=859) (January 1902), p. 845-848.
  - [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=njp.32101068315199&seq=1061) (January 1908), p. 845-848.

---

## Repository Structure

```
mail-time/
├── index.html                  # Built visualization (output of build_transit.py)
├── transit-times.html          # Source template for the visualization
├── build_transit.py            # Build script: embeds data into index.html
├── about.md                    # About page content (rendered inside the visualization)
├── data/
│   ├── transit-times-merged.csv        # Full dataset — all years combined
│   ├── 1882-transit-times-google.csv   # Transcribed data for individual years
│   ├── 1883-transit-times-google.csv
│   ├── 1892-transt-times-google.csv
│   ├── 1902-transit-times-google.csv
│   ├── 1908-transit-times-google.csv
│   ├── city-typologies.csv
│   └── rr_lines.geojson                # Railroad data (from Jeremy Atack)
├── source-docs/                        # PDFs of original U.S. Official Postal Guide transit tables
│   ├── 1882-transit-times.pdf
│   ├── 1883-transit-times.pdf
│   ├── 1892-transit-times.pdf
│   ├── 1902-transit-times.pdf
│   └── 1908-transit-times.pdf
├── images/                     # Screenshots and plots for analysis
└── docs/                       # Outlier analysis docs
```

---

## Citation

Cameron Blevins, "How Fast Was the Mail?" interactive data visualization, 2026, https://cblevins.github.io/mail-time/.
