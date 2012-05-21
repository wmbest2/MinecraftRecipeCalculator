import gtk
import math
from Ingredient import *

class RecipeCard(gtk.Window):

    def addTotals(self):
        parent = gtk.Frame("Raw Materials")

        totals = dict()
        self.recipe.output_totals(totals, 1.0)
        table = gtk.Table(len(totals.keys()), 20, False)
        parent.add(table)
        for c, k in enumerate(totals.keys()):
            label = gtk.Label(str(int(math.ceil(totals[k]))))
            label.set_alignment(1.0, 0.5)
            label.set_padding(10, 2)
            table.attach(label, 0, 1, c, c + 1)
            label = gtk.Label(k)
            label.set_alignment(0.0, 0.5)
            table.attach(label, 1, 20, c, c + 1)

        self.parent_vbox.pack_start(parent, False, False, 0)

    def view_recipe(self, widget, *data):
        recipe_card = RecipeCard(self.recipes, data[0])
        recipe_card.show_all();

    def addIngredients(self):
        parent = gtk.Frame("Ingredients")
        table = gtk.Table(len(self.recipe.ingredients), 20, False)
        parent.add(table)
        for c, i in enumerate(self.recipe.ingredients):
            label = gtk.Label(str(i.count))
            label.set_alignment(1.0, 0.5)
            label.set_padding(10, 2)
            table.attach(label, 0, 1, c, c + 1)
            label = gtk.Label(i.material.name)
            label.set_alignment(0.0, 0.5)
            table.attach(label, 1, 18, c, c + 1)
            if i.material.__class__.__name__ == 'Recipe':
                btn = gtk.Button("View Recipe")
                table.attach(btn, 18, 20, c, c + 1)
                btn.connect('clicked', self.view_recipe, i.material.name)

        self.parent_vbox.pack_start(parent, False, False, 0)

    def __init__(self, recipes, recipe_index):
        super(RecipeCard, self).__init__()

        self.recipe = recipes[recipe_index]
        self.recipes = recipes

        self.connect("destroy", gtk.main_quit)
        self.set_title(self.recipe.name)
        self.set_size_request(640, 480)
        self.set_position(gtk.WIN_POS_CENTER)

        self.parent_vbox = gtk.VBox(False, 5)
        self.add(self.parent_vbox)

        self.addIngredients()
        self.addTotals()

        self.show_all()
