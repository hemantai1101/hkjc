# hkjc
## Objective
The project aims at providing a set of utilities for match result analysis and prediction.

The components includes
1. Crawler  
Cralwer crawls and gathers historical data from different source to produce interface file in prdefined format. i.e. csv file

Crawl can crawl from different sources and produce different kind of output file:
- Crawler to crawl odds from famous bet websites => Odd file
- Crawler to crawl past match results from famous sports websites
- ... 

2. Data Repository
A database and an server app to ingest the interface data produced by Crawler. 

(TBC) Data model design
- Team
- Player
- Source System

3. UI
The requiremnt is yet to known for this part. But the UI uses data from Data Respository and display processed data in onecv on the following mean.

- Web application
- Android / IOS Native application 
- Report
- Message notification 

(TBC) Requirment spec