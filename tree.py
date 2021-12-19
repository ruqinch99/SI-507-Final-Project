#################################
##### Name: May Chang       #####
##### Uniqname: ruqinch     #####
##### SI507 Final Project   #####
##### Fall 2021             #####
#################################

# A python file that constructs trees from stored data using classes and methods

import json


def main():
    """ Program constructs trees from stored data using classes and methods
    """

    yelp_file = open('yelp.json')
    yelp_json = json.load(yelp_file)
    price_tree = tree_price(yelp_json)
    save_tree_price(yelp_json)
    price_rating = tree_price_rating(yelp_json)
    save_tree_price_rating(yelp_json)


class Business:
    """ class Business
    """

    def __init__(self, name="NA", url="NA", image_url="NA", review_count="NA", categories="NA", rating="NA",
                 coordinates="NA", transactions="NA", price="NA", location="NA", phone="NA", json=None):

        if json != None:
            name = json.get('name', 'NA')
            url = json.get('url', 'NA')
            image_url = json.get('image_url', 'NA')
            review_count = json.get('review_count', 'NA')
            categories = json.get('categories', 'NA')
            rating = json.get('rating', 'NA')
            coordinates = json.get('coordinates', 'NA')
            transactions = json.get('transactions', 'NA')
            price = json.get('price', 'NA')
            location = json.get('location', 'NA')
            phone = json.get('display_phone', 'NA')

        self.name = name
        self.url = url
        self.image_url = image_url
        self.review_count = review_count
        self.categories = categories
        self.rating = rating
        self.coordinates = coordinates
        self.transactions = transactions
        self.price = price
        self.location = location
        self.phone = phone

    def info(self):
        """ Return basic restaurant info
        Parameters:
            self
        Returns:
            String
        """
        return f"Restaurant: {self.name}, url: {self.url}"

    def to_dict(self):
        """ Convert object to dictionary for graph generation
        Parameters:
            self
        Returns:
            Dictionary
        """
        return {
            'name': self.name,
            'url': self.url,
            'image_url': self.image_url,
            'review_count': self.review_count,
            'categories': self.categories,
            'rating': self.rating,
            'transactions': self.transactions,
            'phone': self.phone,
            'price': self.price,
            'longitude': self.coordinates.get('longitude'),
            'latitude': self.coordinates.get('latitude')
        }


def tree_price(json_str):
    """ Convert json_str to tree which has internal nodes about price information
    Parameters:
        Dictionary
    Returns:
        Tree
            - Attribute (internal) nodes: $, $$, $$$, $$$$, NA
            - Restaurant (leaf) nodes: Business objects
    """
    tree = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    for resto_json in json_str:
        if resto_json.get('price') not in tree:
            tree[resto_json.get('price')] = []
        tree[resto_json.get('price')].append(Business(json=resto_json))
    tree['NA'] = tree.pop(None)
    return tree


def tree_price_rating(json_str):
    """ Convert json_str to tree which has internal nodes about price and rating information
    Parameters:
        Dictionary
    Returns:
        Tree
            - Attribute (internal) nodes: $, $$, $$$, $$$$, NA, and different ratings
            - Restaurant (leaf) nodes: Business objects
    """
    tree = {'$': {}, '$$': {}, '$$$': {}, '$$$$': {}}
    for resto_json in json_str:
        if resto_json.get('price') not in tree:
            tree[resto_json.get('price')] = {}
        if resto_json.get('rating') not in tree:
            tree[resto_json.get('price')][resto_json.get('rating')] = []
        tree[resto_json.get('price')][resto_json.get(
            'rating')].append(Business(json=resto_json))
    tree['NA'] = tree.pop(None)
    return tree


def save_tree_price(json_str):
    """ Save tree which has internal nodes about price information to tree_price.json
    Parameters:
        Dictionary
    Returns:
        Tree
            - Attribute (internal) nodes: $, $$, $$$, $$$$, NA, and different ratings
            - Restaurant (leaf) nodes: Business objects
    """
    tree = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    for resto_json in json_str:
        if resto_json.get('price') not in tree:
            tree[resto_json.get('price')] = []
        tree[resto_json.get('price')].append(
            Business(json=resto_json).to_dict())
    tree['NA'] = tree.pop(None)
    with open("tree_price.json", "w") as outfile:
        json.dump(tree, outfile)
    return tree


def save_tree_price_rating(json_str):
    """ Save tree which has internal nodes about price and rating information to tree_price_rating.json
    Parameters:
        Dictionary
    Returns:
        Tree
            - Attribute (internal) nodes: $, $$, $$$, $$$$, NA, and different ratings
            - Restaurant (leaf) nodes: Business objects
    """
    tree = {'$': {}, '$$': {}, '$$$': {}, '$$$$': {}}
    for resto_json in json_str:
        if resto_json.get('price') not in tree:
            tree[resto_json.get('price')] = {}
        if resto_json.get('rating') not in tree:
            tree[resto_json.get('price')][resto_json.get('rating')] = []
        tree[resto_json.get('price')][resto_json.get(
            'rating')].append(Business(json=resto_json).to_dict())
    tree['NA'] = tree.pop(None)
    with open("tree_price_rating.json", "w") as outfile:
        json.dump(tree, outfile)
    return tree


if __name__ == '__main__':
    main()
