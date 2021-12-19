SI 507 Final Project README
May Chang


The program uses Ann Arbor’s businesses data from the Yelp Fusion and Open Table, provides an interactive command-line prompt for users to choose data/visualization options, and provides restaurant recommendations that meet their needs. To run the program, please install all required python packages, change into the directory where you store the python and data file, and run the python file. The interactive command-line prompt will inform and ask users’ options for visualization and recommendation preferences.


The Yelp Fusion API provides access to Yelp content and data, which is ideal for the restaurant recommendation application project. I created an app on Yelp Fusion and received a private API key authentication to access all endpoints’ information. Please see detailed instructions to create your private API Key (https://www.yelp.com/developers/documentation/v3/authentication). I used my private API Key to access Ann Arbor’s restaurant data for this project and saved it as a non-dynamic JSON file (yelp.json). I will also scrape data from OpenTable for restaurants in Ann Arbor (https://www.opentable.com/ann-arbor-restaurant-listings). The data include information about names, ratings, reviews, price, cuisine, and location and will be stored as a CSV file (opentable.csv).


Required Python packages for my project to work:  JSON, random, requests, webbrowser, pandas, plotly.express, selenium webdriver, and bs4 BeautifulSoup.




Two tree data structures:


Tree by price level
The class Business is an object that stores all the information about a specific restaurant. Function tree_price(json_str) constructs a tree data structure, organized in the format of the dictionary, storing businesses by price levels. The Attribute (internal) nodes of tree_price includes $, $$, $$$, $$$$, NA. Restaurant (leaf) nodes are Business objects. 


Tree by price level and rating
Function tree_price_rating constructs another tree data structure, storing business by price levels and rating. Attribute (internal) nodes are $, $$, $$$, $$$$, NA, and different ratings (e.g. 4.0, 4.5, 5.0). Restaurant (leaf) nodes are Business objects. 




Interaction and Presentation Options:


The program provides three different data visualizations of Ann Arbor’s restaurants, created using Plotly, with an interactive command-line prompt.
1. A scatter plot showing Ann Arbor's restaurants' locations
2. A pie chart showing Ann Arbor's restaurants' price level distribution
3. A histogram showing Ann Arbor's restaurants' rating distribution


The program will provide an interactive command-line prompt for users to choose their price level and rating preferences. The recommendation and detailed information of restaurants from Yelp and OpenTable will be provided via text. 


In addition to command-line prompts and different Plotly visualizations, the program will also ask if the user would like to open the yelp site of a specific restaurant. If the user says yes, the program will open the site in a web browser.




Files:
finalproj.py: a python file to run the Ann Arbor Restaurant Picker
store.py: a python file to scrape data from Yelp Fusion API and OpenTable page and store data as JSON and CSV file
tree.py: a python file that constructs trees from stored data using classes and methods
read_tree.py: a stand-alone python file that reads the JSON of trees


Data:
yelp.json
opentable.csv


JSON file of tree data structures:
tree_price.json 
tree_price_rating.json