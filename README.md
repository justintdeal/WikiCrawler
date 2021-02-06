# WikiCrawler

Dependencies
---

To this crawler, you must install two libraries
`pip install scrapy`
`pip install extruct`

Additionally, if you want to view the output of graph.py, you must install Matplotlib.
`pip install matplotlib`

Change directories into the wikicrawler folder.

Now the crawler should run with the following command.

`scrapy crawl wiki --logfile wikiCrawl.log -o wikiData.json -s CLOSESPIDER_PAGECOUNT=1000`

If you wish to see visual statisitcs, run 
`python graph.py`
