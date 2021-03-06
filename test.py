from Ingredient import *
import json
from pprint import pprint

item_data = open('recipes.json')
items = json.load(item_data)['recipes']
item_data.close()

recipes = Recipe.load_from_json(items);

my_recipe = Recipe("Cool stuff ahead")
my_recipe.ingredients.append(Ingredient(recipes['Redstone Repeater'], 1))
my_recipe.print_ingredients()
print
my_recipe.print_totals()

print
print

my_recipe = Recipe("Kaboom")
my_recipe.ingredients.append(Ingredient(recipes['TNT Block'], 4))
my_recipe.ingredients.append(Ingredient(recipes['Redstone Repeater'], 1))
my_recipe.print_ingredients()
print
my_recipe.print_totals()

print
print

my_recipe = Recipe("Hidden Door")
my_recipe.ingredients.append(Ingredient(recipes['Sticky Piston'], 6))
my_recipe.ingredients.append(Ingredient(recipes['Redstone Repeater'], 8))
my_recipe.print_ingredients()
print
my_recipe.print_totals()

