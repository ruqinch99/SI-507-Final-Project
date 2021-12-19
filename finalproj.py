#################################
##### Name: May Chang       #####
##### Uniqname: ruqinch     #####
##### SI507 Final Project   #####
##### Fall 2021             #####
#################################

import json
import random
import webbrowser
import pandas as pd
import plotly.express as px


def main():
    """ Main function for the program
    """
    yelp_file = open('yelp.json')
    yelp_json = json.load(yelp_file)
    restaurants = resto_list(yelp_json)
    price_tree = tree_price(yelp_json)
    # save_tree_price(yelp_json)
    price_rating = tree_price_rating(yelp_json)
    # save_tree_price_rating(yelp_json)
    df = pd.DataFrame.from_records(
        [resto.to_dict() for resto in restaurants])
    yelp_file.close()
    opentable = pd.read_csv('opentable.csv')

    print("Welcome to Ann Arbor Restaurant Picker!")
    print("The program will provide you with visualizations about Ann Arbor's restaurants and pick restaurants according to your price preference.")
    print()
    map_input = input(
        "Would you like to see a scatter plot showing Ann Arbor's restaurants' locations? (yes/no) ")
    if map_input.lower() in ['yes', 'y', 'yep', 'yup', 'sure', 'ya']:
        fig = px.scatter(df, x="longitude", y="latitude", hover_name="name", color='price', color_discrete_map={
                         'NA': 'gray', '$$$$': '#1E3F66', '$$$': '#528AAE', '$$': '#91BAD6', '$': '#BCD2E8'}, title='Restaurants in Ann Abor')
        fig.show()
        print("Please see the graph in pop-up window.")
    else:
        print("Sure.")

    print()
    pie_input = input(
        "Would you like to see a pie chart showing Ann Arbor's restaurants' price level distribution? (yes/no) ")
    if pie_input.lower() in ['yes', 'y', 'yep', 'yup', 'sure', 'ya']:
        fig = px.pie(df, names='price',
                     title='Yelp Price levels of Restaurants in Ann Abor')
        fig.show()
        print("Please see the graph in pop-up window.")
    else:
        print("Sure.")

    print()
    hist_input = input(
        "Would you like to see a histogram showing Ann Arbor's restaurants' rating distribution? (yes/no) ")
    if hist_input.lower() in ['yes', 'y', 'yep', 'yup', 'sure', 'ya']:
        fig = px.histogram(df, x="rating", title="Histogram of Yelp Rating of Restaurants in Ann Arbor", color='price', color_discrete_map={
                           'NA': 'gray', '$$$$': '#1E3F66', '$$$': '#528AAE', '$$': '#91BAD6', '$': '#BCD2E8'})
        fig.show()
        print("Please see the graph in pop-up window.")
    else:
        print("Sure.")

    print()
    while True:
        price_level = input(
            "What is your preferred price level? ($, $$, $$$, $$$$, NA, Exit) ")
        if price_level == '$':
            recommendation(price_level, price_rating,
                           price_tree, restaurants, opentable)
        elif price_level == '$$':
            recommendation(price_level, price_rating,
                           price_tree, restaurants, opentable)
        elif price_level == '$$$':
            recommendation(price_level, price_rating,
                           price_tree, restaurants, opentable)
        elif price_level == '$$$$':
            recommendation(price_level, price_rating,
                           price_tree, restaurants, opentable)
        elif price_level.lower() == 'na':
            recommendation(price_level, price_rating,
                           price_tree, restaurants, opentable)
        elif price_level.lower() == 'exit':
            break
        else:
            print(
                "Sorry, please enter $, $$, $$$, $$$, NA (for no preference), or Exit (to exit program).")
            continue
        print()
        again_bool = True
        while True:
            again = input("Do you want another recommendation? (yes/no) ")
            if again.lower() in ['yes', 'y', 'yep', 'yup', 'sure', 'ya']:
                again_bool = True
                break
            elif again.lower() in ['no', 'n', 'nope']:
                again_bool = False
                break
            else:
                print(
                    "Sorry, I didn't understand that. Please enter yes if you want another recommendation or entre no to quit.")
        if again_bool == False:
            break
        print()

    print('Thank you for using nn Arbor Restaurant Picker! Bye!')
    print()


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


def print_detail(Business):
    """ Function to print detail information fo a Business object
    Parameters:
        Business object
    Returns:
        NA
    """
    print(f'Name: {Business.name}')
    address = Business.location['display_address']
    print(f'Location : {", ".join(address)}')
    print(f'Phone: {Business.phone}')
    print(f'Price Level: {Business.price}')
    print(f'Rating: {Business.rating}')
    print(f'Review Count: {Business.review_count}')
    category_list = []
    for category in Business.categories:
        category_list.append(category['title'])
    print(f'Category(s): {", ".join(category_list)}')
    print(f'Transactions type(s): {", ".join(Business.transactions)}')


def open_yelp_site(resto):
    """ Function to ask if user would like to open the restaurant's Yelp site and open site regarding user input 
    Parameters:
        Business object
    Returns:
        NA
    """
    if resto.url != 'NA':
        open = input(
            f"Would you like to open {resto.name}'s Yelp site? (yes/no) ")
        if open.lower() in ['yes', 'y', 'yep', 'yup', 'sure', 'ya']:
            webbrowser.open(resto.url, new=0)
            print("Please see a pop-up window.")
            print()
        else:
            print("Sure.")
            print()
    else:
        print(f"No Yelp site available for {resto.name}")


def match_opentable(resto, opentable):
    """ Function to check if a restaurant is available on the OpenTable dataset. If data is available, give the user 
            option to display information.
    Parameters:
        resto: Business object
        opentable: dictionary
    Returns:
        NA
    """
    if resto.name not in opentable.values:
        print(f"{resto.name} cannot be found in the OpenTable dataset. No additional information will be provided.")
    else:
        ot = input(
            f"Would you like to see more information of {resto.name} from OpenTable? (yes/no) ")
        if ot.lower() in ['yes', 'y', 'yep', 'yup', 'sure', 'ya']:
            match = opentable.loc[opentable['Name'] == resto.name]
            ot_name = match['Name'].to_string(index=False)
            ot_rating = match['Rating'].to_string(index=False)
            ot_review = match['Reviews'].to_string(index=False)
            ot_price = match['Price'].to_string(index=False)
            ot_cuisine = match['Cuisine'].to_string(index=False)
            print()
            print(f'Name: {ot_name}')
            print(f'Rating: {ot_rating}')
            print(f'Review: {ot_review}')
            print(f'Price: {ot_price}')
            print(f'Cuisine: {ot_cuisine}')
        else:
            print("Sure.")


def recommendation(price_level, price_rating, price_tree, restaurants, opentable):
    """ Function to provide restaurant recommendations based on user's input.
    Parameters:
        price_level: string
        price_rating: tree
        price_tree: tree
        restaurants: dictionary
        opentable: dictionary
    Returns:
        NA
    """
    if price_level in ('$', '$$', '$$$', '$$$$'):
        keys = list(price_rating[price_level].keys())
        keys.sort()
        print(f'{price_level} restaurants have the following rating: {keys}.')
        print()
        rating = input(
            f"Would you want me to pick a restaurant with a specific rating for you? {keys}, or any string for no preference. ")
        if rating in [str(x) for x in keys]:
            print(
                f'I will pick a {price_level} restaurant with {str(rating)} rating for you.')
            rating = float(rating)
            resto = random.choice(price_rating[price_level][rating])
            print()
            print_detail(resto)
            print()
        else:
            print(
                f'No rating preference. I will pick a {price_level} restaurant for you.')
            resto = random.choice(price_tree[price_level])
            print()
            print_detail(resto)
            print()
    elif price_level.lower() == "na":
        print(f'No price level preference. I will pick a restaurant for you.')
        resto = random.choice(restaurants)
        print()
        print_detail(resto)
        print()

    open_yelp_site(resto)
    match_opentable(resto, opentable)


def resto_list(json_str):
    """ Fuction to convert json file to a list with all businesses
    Parameters:
        json_str
    Returns:
        list
    """
    restaurants = []
    for resto_json in json_str:
        restaurants.append(Business(json=resto_json))
    return restaurants


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
