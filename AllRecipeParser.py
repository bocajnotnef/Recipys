#!/usr/bin/env python3

# AllRecipes Webscraper Script
#
# Author: Steven Jorgensen
# Date: 12/27/16
#
# Script to rip recipes from given url and turn them into RST files. Works only
# with AllRecipes url.
#
# Usage: python3 AllRecipeParser.py [url]

from bs4 import BeautifulSoup
import urllib.request
import argparse

# Handle Arguments
parser = argparse.ArgumentParser()
parser.add_argument("url", type=str, nargs=1, help='AllRecipes URL')
args = parser.parse_args()
###


def WriteIngredient(ingred, rst_file):
    rst_file.write(" * " + ingred + "\n")
    pass


def WriteInstruction(instruct, rst_file):
    rst_file.write(" #. " + instruct + "\n")
    pass


try: local_filename, headers = urllib.request.urlretrieve(str(args.url[0]))
except:
    print("\n### Unable to open webpage ### \n")
    exit(-1)

html = open(local_filename)
raw_html = html.read()
ingredients = []
instructions = []

# Parse the HTML
soup = BeautifulSoup(raw_html, 'html.parser')

for item in soup.find_all("span", class_="recipe-ingred_txt added"):
    ingredients.append(item.text)

for instruction in soup.find_all("span", class_="recipe-directions__list--item"):
    instruct = str(instruction.text)
    instruct = instruct.replace('\n', '')

    if instruct != "":
        instructions.append(instruct)

dish_name = soup.find("h1", class_="recipe-summary__h1")
dish_name = dish_name.text

servings = soup.find("div", class_="subtext")

rst_name = dish_name.replace(' ', '') + ".rst"

# Write the ripped info to an RST file to be used with sphynx ###
rst_file = open(rst_name, 'w')
print("\n {} has been created\n".format(rst_name))

rst_file.write(dish_name + "\n")

title_line = ""
for i in range(len(dish_name)):
    title_line = title_line + "="  # Underline must match length of the title

rst_file.write(title_line + "\n")

rst_file.write("\nIngredients\n-----------\n")
for item in ingredients:
    WriteIngredient(item, rst_file)

rst_file.write("\nInstructions\n-------------\n")
for item in instructions:
    WriteInstruction(item, rst_file)

rst_file.write("\nServes: " + servings.text + '\n')

rst_file.write("\nNotes\n-----\n * \n * \n")
rst_file.write("\nAdditional Links\n----------------\n")
rst_file.write(" * `Original Recipe <" + args.url[0] + ">`__")

rst_file.close()
