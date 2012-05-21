import gtk
from Ingredient import *
from RecipeCard import *

recipes = Recipe.load_from_file('recipes.json')

my_recipe = Recipe("Hidden Door")
my_recipe.ingredients.append(Ingredient(recipes['Sticky Piston'], 6))
my_recipe.ingredients.append(Ingredient(recipes['Redstone Repeater'], 8))
recipes['Hidden Door'] = my_recipe

my_recipe_card = RecipeCard(recipes, 'Hidden Door')

gtk.main()
