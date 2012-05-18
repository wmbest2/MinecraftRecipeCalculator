import math

class ImageChunk:
    pass

class Material:
    def __init__(self, name):
        self.name = name
        self.makes = 1.0

    def output_for_count(self, count = 1):
        return str(float(count)) + " " + self.name + "\n"

    def output_totals(self, totals, count):
        if totals.has_key(self.name) != True:
            totals[self.name] = float(0)
        totals[self.name] += float(count)

class Recipe(Material):
    def __init__(self, name, makes=1.0):
        self.name = name
        self.ingredients=[]
        self.makes=float(makes)

    def output_for_count(self, count = 1.0):
        output = Material.output_for_count(self, count);
        for i in self.ingredients:
            output += i.material.output_for_count(i.count)
        return output

    def output_totals(self, totals, count = 1.0):
        for i in self.ingredients:
            i.material.output_totals(totals, float(count) * (float(i.count) / i.material.makes))

    def print_ingredients(self):
        print Material.output_for_count(self);
        print "Ingredients ------------------------------------"
        for i in self.ingredients:
            print "  " + str(int(i.count)) + " " + i.material.name

    def print_totals(self):
        totals = dict()
        self.output_totals(totals, 1.0)

        print "Totals -----------------------------------------"
        for k in totals.keys():
            print "  " + k + " " + str(int(math.ceil(totals[k])))

    @staticmethod
    def load_from_json(json):
        recipes = dict()
        for i in json:
            if i['type'] == 0:
                recipes[i['name']] = Material(i['name'])
            else:
                if i.has_key('makes'):
                    recipe = Recipe(i['name'], i['makes'])
                else:
                    recipe = Recipe(i['name'])
                for ing in i['ingredients']:
                    if ing.has_key('count'):
                        recipe.ingredients.append(Ingredient(recipes[ing['name']], ing['count']))
                    else:
                        recipe.ingredients.append(Ingredient(recipes[ing['name']]))
                recipes[i['name']] = recipe
        return recipes


class Ingredient:
    def __init__(self, material, count = 1.0):
        self.material = material
        self.count = float(count)

