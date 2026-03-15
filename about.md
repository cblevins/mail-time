## About This Project

In January of 1882, a letter mailed from New York City to San Francisco would take nearly **a full week** to travel across the country. By 1902, that same journey had been cut to a little more than **four days**. This map uses a series of tables published by the U.S. Post Office Department recording how many hours it took for mail to travel via railway between **12 major railroad depots** and roughly **120-130 cities** across the country in the late 1800s and early 1900s. Mapping these transit time tables shows the distances separating Americans in different parts of the country and how the US Post and an expanding national railway system connected them.

### What is this showing?

Mail transit times were computed by the U.S. Post Office Department using railroad schedules, and reflect **ideal conditions** - ie. no delays or missed connections. They also capture only one leg of the journey: the time spent moving between railroad stations, not the additional time required to get a piece of mail to and from a depot on either end. The actual time between dropping off a letter at a post office and arriving in the hands of its recipient would therefore be

### How was this made?

This project was completed in early 2026 by [Cameron Blevins](https://cblevins.github.io/) over several steps. First, mail transit time tables were located in a selection of [United States Postal Guides found on HathiTrust](https://catalog.hathitrust.org/Record/002137107) and then downloaded as separate PDF files.

![Example page from an 1883 U.S. Official Postal Guide showing mail transit times](https://raw.githubusercontent.com/cblevins/mail-time/main/images/1883-table-example.png)

<p class="img-caption">Excerpt of transit time table from <a href="https://babel.hathitrust.org/cgi/pt?id=njp.32101068314788&seq=657">1883 U.S. Official Postal Guide</a></p>

The remaining steps relied extensively on Generative AI tools: Google's Gemini 3.1 Pro was used to extract data from each transit table PDF and process it into a CSV file. Claude Code (Sonnet 4.6) was used to combine yearly data into a single dataset, then identify and fix potential transcription errors (ex. a value of `33:15` recorded as `83:15`). Finally, Claude Code (Opus 4.6 and Sonnet 4.6) was used to build, design, and deploy the visualization.

### About the Data

#### Mail Transit Time Data

This data was transcribed from the following sources:

- [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=mdp.39015063600780&seq=609) (January 1882), p. 579-582.
- [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=njp.32101068314788&seq=654) (January 1883), p. 612-615.
- [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=uc1.b2919442&seq=737) (January 1892), p. 735-738.
- [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=hvd.hn4jgx&seq=859) (January 1902), p. 845-848.
- [United States Official Postal Guide](https://babel.hathitrust.org/cgi/pt?id=njp.32101068315199&seq=1061) (January 1908), p. 845-848.

The full dataset of mail transit times can [be downloaded as a CSV file](https://github.com/cblevins/mail-time/blob/main/data/transit-times-merged.csv).

#### Railroad Data

All railroad data comes from: Jeremy Atack, ["Historical Geographic Information Systems (GIS) database of U.S. Railroads for 1826-1911"](https://my.vanderbilt.edu/jeremyatack/data-downloads/) (May 2016; revised Oct 31, 2023).

### Historical Background

Mail had been traveling by railroad in the United States since the 1830s, but the real breakthrough came with the creation of [the Railway Mail Service](https://www.archives.gov/publications/prologue/2005/fall/fast-mail-1.html) in 1864, when the Post Office Department began sorting letters aboard moving trains. By the 1880s and 1890s, these railroad postal routes had become the backbone of [the world's most expansive postal system](https://cblevins.github.io/paper-trails/).

### How to Cite This

<div class="citation-box">
  <p class="citation-text">Cameron Blevins, &#x201C;How Fast Was the Mail?&#x201D; 2026, <a href="https://cblevins.github.io/mail-time/">https://cblevins.github.io/mail-time/</a>.</p>
  <button class="citation-copy-btn" data-cite='Cameron Blevins, \u201cHow Fast Was the Mail?\u201d interactive data visualization, 2026, https://cblevins.github.io/mail-time/.' onclick="(function(btn){navigator.clipboard.writeText('Cameron Blevins, \u201cHow Fast Was the Mail?\u201d 2026, https://cblevins.github.io/mail-time/.').then(function(){btn.textContent='Copied \u2713';setTimeout(function(){btn.textContent='Copy'},2000);})})(this)" aria-label="Copy citation to clipboard">Copy</button>
</div>
