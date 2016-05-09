# KRYPTON Richlist Tracker
Tracking activity on top 100 highest $Krypton wallet by regularly scrapping (kinda manually...) the richlist (http://gaiaplatform.com/kr/richlist.php)

More information about Krypton at: 
* official website: http://krypton.rocks
* annoncement: https://bitcointalk.org/index.php?topic=1368118.0
* Krypton market informations: http://coinmarketcap.com/currencies/krypton/

## Prerequisites
* python lib `lxml`
lxml prerequisites (maybe too much) (src: http://stackoverflow.com/a/23239568/5903959)

`sudo apt-get install libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev`

* then`pip3 install libxml`


## Getting started
First, clone this repo:

`git clone https://github.com/pltrdy/krich_tracker.git`

then you may want to edit `conf.py` to fit your needs 
e.g. `vi conf.py`

finally run the tracker using the configuration module:
`./tracker conf`

(note that you may not type the extension .py, as it will be loaded as a module i.e. `import conf`)

## Output
The tracker generate a new record every `refresh` seconds (in conf module). 

It updates the data file at each iteration. (the path on that file is specified in the configuration module).

Currently, the output datasctructure is a json dictionnary

```
{
  "<kr_address>":
    {
      "records": 
        [
          {
            "time": YYYY-MM-DD HH:MM:SS string formatted date
            "address": kr wallet address (redundant with the key, i know, i may remove it)
            "rank": rank in the top 100. 1 is the best.
            "last_transaction": MM/DD/YYYY HH:MM:SS TZ string formatted date (date format from the original page)
            "label": will be None most of time, not really relevant.
          }
        ],[
        ...
        ]
    },
  "<another_kr_address>":
      ...
      ...
}

```
