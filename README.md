# SoccerBetAnalyser
It is a python and Qlik Sense project.  

Trough webscrapping using libs: requests, beautiful soup and xlsxwriter, I extract ifnromation about brazilian soccer games (Brasileirão Championship). And using Qlik Sense I transform and load this data into a dashboard to analyse if it is profitable to bet in how many goals a brazilian soccer team will make in a game.

In this project you will need to have installed:

pip install requests
pip install beautifulSoup
pip install xlsxwriter

You will also need Qlik Sense.


IMPORTANT!

On Qlik Sense, before you load the app, you will need to create a connection betwen your machine and the excel document generated from python.
For this, you will have to change in the script editor of Qlik Sense app the "Load ...  FROM [lib://Web Scrapping/Jogos 2013 - 2021.xlsx]" to your new connection to your excel file.
