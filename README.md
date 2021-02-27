# RadFinder
This project aims to locate radiology practices within the web.

# Requirements :construction_worker:
Necessary requirements for the project are:

* [Python 3.9](https://www.python.org/downloads/release/python-390/) 
* [PipEnv](https://pypi.org/project/pipenv/)
* IDE like ([PyCharm](https://www.jetbrains.com/de-de/pycharm/) or [VSCode](https://code.visualstudio.com/))

# Run the Code :rocket:
Make sure you have set up an environment with PipEnv.
To install the requirements use:

    $ pipenv install --dev

After installation you can run the code with:

    $ python YellowPages/main.py

The code return an `.csv` file of all radiologists available at `www.gelbeseiten.de`.

# Future Work :alien:
There are various possibilities to generate further data.
In the following, I will explain the options available for identifying radiology practices on the web.

## Preliminary work
It must be highlighted how the data will be generated.
It must be made clear what the differences are between [crawlers](https://www.ionos.de/digitalguide/online-marketing/suchmaschinenmarketing/was-ist-ein-crawler/) and [scapers](https://www.ionos.de/digitalguide/websites/web-entwicklung/was-ist-web-scraping/).
The decision of data acquisition must be based on this. The following questions must be asked:

* Are there sufficient data sources, which simply have to be skimmed?

* Should additional data sources be found and processed?

* How deep should the data acquisition progress?

    * What if the data source refers to an other web page, should this be crawled as well?

* How can the data be merged or sanitized?

* How should the infrastructure of the project be set up


## The easy way :moneybag:
The easiest way is to use production ready software like:
* https://webscraper.io/
* https://www.zyte.com/
* https://www.scrapestorm.com/
* https://www.parsehub.com/ (**recommended**)

# The nerdy way :nerd_face:
There are various free options for systematically obtaining data.
The programming languages `JavaScript` and `Python` are required.
These languages are beginner-friendly and easy to learn.
In addition, a basic understanding of the structure of websites must be given.
Accordingly, basic knowledge of `Python`, `JavaScript` and `HTML` needs to be existent.

Below you will find an overview of the different options.
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Easy to use but headless 
* [Scrapy](https://scrapy.org/): Advanced system with expert knowledge necessary (**recommended**)
* [Selenium](https://selenium-python.readthedocs.io/): Of-Label-Use (normally for frontend testing) but easy to use

# Beginner Setup :baby:
* Using [Anaconda](https://anaconda.org/) as a ready-to-use development environment 
* Setting up [Scrapy](https://docs.scrapy.org/en/latest/) with Anaconda and do the [tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)