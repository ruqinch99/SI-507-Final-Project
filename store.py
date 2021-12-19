#################################
##### Name: May Chang       #####
##### Uniqname: ruqinch     #####
##### SI507 Final Project   #####
##### Fall 2021             #####
#################################

import json
import pandas as pd
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


def main():
    """ Main program to scrape data from Yelp Fusion API and OpenTable page and store data as JSON and CSV file
    """
    get_yelp()
    get_opentable()


def get_yelp():
    """ Send GET requests to the Yelp API, return a dictionary with information about the business in Ann Arbor.
    Parameters:
        NA
    Returns:
        dict: The JSON response from the request.
    """
    bearer_token = 'b1lyq9fawgtATzySu0PGu0PUev2MyW5S3Im7_D_-IFZMklhWhicEJ4spi-mQfAGg1drBgcZm3-mbkmTr8qy3WItd98nV0eAY8FA50lJXyfQGQEOJB0HjsEe6qIexYXYx'
    yelp_header = {'Authorization': 'Bearer ' + bearer_token}
    yelp_url_1 = 'https://api.yelp.com/v3/businesses/search?location=Ann Arbor&term=restaurants&limit=50'
    yelp_url_2 = 'https://api.yelp.com/v3/businesses/search?location=Ann Arbor&term=restaurants&limit=50&offset=50'
    yelp_url_3 = 'https://api.yelp.com/v3/businesses/search?location=Ann Arbor&term=restaurants&limit=50&offset=100'
    yelp_url_4 = 'https://api.yelp.com/v3/businesses/search?location=Ann Arbor&term=restaurants&limit=50&offset=150'
    yelp_url_5 = 'https://api.yelp.com/v3/businesses/search?location=Ann Arbor&term=restaurants&limit=40&offset=200'
    json_str = []
    for url in (yelp_url_1, yelp_url_2, yelp_url_3, yelp_url_4, yelp_url_5):
        response = requests.get(url, headers=yelp_header)
        json_dict = json.loads(response.text)
        json_str.extend(json_dict['businesses'])
    # Save data to local computer as a JSON file
    with open('yelp.json', 'w') as fp:
        json.dump(json_str, fp)
    return json_str


def parse_html(html):
    """ Parse content from url
    Parameters:
        html
    Returns:
        Pandas Data Frame
    Reference:
        furas (2020). https://stackoverflow.com/questions/65501642/scraping-opentable-website-using-python-beautifulsoup
    """
    data, item = pd.DataFrame(), {}
    soup = BeautifulSoup(html, 'lxml')
    for i, resto in enumerate(soup.find_all('div', class_='rest-row-info')):
        item['Name'] = resto.find('span', class_='rest-row-name-text').text
        rating = resto.select('.star-rating .star-rating-score')
        item['Rating'] = rating[0]['aria-label'] if rating else 'NA'
        reviews = resto.find('span', class_='star-rating-text--review-text')
        reviews = resto.select('div.review-rating-text span')
        item['Reviews'] = reviews[0].text if reviews else 'NA'
        item['Price'] = int(resto.find(
            'div', class_='rest-row-pricing').find('i').text.count('$'))
        item['Cuisine'] = resto.find_all(
            'span', class_='rest-row-meta--cuisine')[-1].text
        item['Location'] = resto.find(
            'span', class_='rest-row-meta--location').text
        data[i] = pd.Series(item)
    return data.T


def get_opentable():
    """ Scrape the Open Table site about Ann Arbor restaurants with the use of 
            Beautiful Soup and save the data frame as a csv file.
    Parameters:
        NA
    Returns:
        Pandas Data Frame
    """
    driver = webdriver.Chrome('/Applications/chromedriver')
    url = "https://www.opentable.com/ann-arbor-restaurant-listings"
    driver.get(url)
    data = parse_html(driver.page_source)
    data.to_csv('opentable.csv', index=False)
    return data


if __name__ == '__main__':
    main()
