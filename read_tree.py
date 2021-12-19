#################################
##### Name: May Chang       #####
##### Uniqname: ruqinch     #####
##### SI507 Final Project   #####
##### Fall 2021             #####
#################################

# A stand alone python file that reads the json of trees

import json


def main():
    f1 = open('tree_price_rating.json')
    f2 = open('tree_price.json')
    tree_price_rating = json.load(f1)
    tree_price = json.load(f2)
    # tree_price_rating
    # tree_price


if __name__ == '__main__':
    main()
