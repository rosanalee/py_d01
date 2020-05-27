import sys


class Recipe():
    def __init__(self, name, cooking_lvl, cooking_time,ingredients, descripti, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients.split()
        self.descripti = descripti
        self.recipe_type = recipe_type

    def check_attr(self):
        """d = y_recipe.__dict__"""
        try:
            if type(self.name) is not str or self.name == "":
                print('Name provided must be a string and can\'t be empty')
                sys.exit()
            if (self.cooking_lvl).isnumeric() is False or self.cooking_lvl == "":
                print('Cooking level cannot be empty and has to be a digit')
                sys.exit()
            elif int(self.cooking_lvl) not in range(1, 6):
                print('Cooking level is out of range, must be between 1 and 5')
                sys.exit()
            if (self.cooking_time).isnumeric() is False or self.cooking_time == "":
                print('Cooking time cannot be empty and has to be a digit')
                sys.exit()
            if self.recipe_type != 'starter' and self.recipe_type != 'lunch' and self.recipe_type != 'dessert':
                print("""
                Recipe type must one of the following: starter, lunch, dessert""")
                sys.exit()
            else:
                print(f'\"{self.name}\" has been added to your book. Now go cook it.')
                print(str(self))
                final_r = dict(name=self.name, lvl=self.cooking_lvl, time=self.cooking_time, type=self.recipe_type, ingredients=self.ingredients, description=self.descripti)
                final_f = { self.name : final_r}
                print(final_f)
                return final_f
        except:
            print('Try again :)')
            sys.exit()
    
    def __str__(self):
        ing_formatted = ', '.join(self.ingredients)
        if self.descripti == "":
            self.descripti = 'None'
        txt = f"""Recipe name: {self.name}
Cooking level: {self.cooking_lvl}
Cooking time: {self.cooking_time}
Ingredient(s): {ing_formatted}
Description: {self.descripti} 
Type: {self.recipe_type}"""
        return txt
    
    


#y_recipe = Recipe('ss', '6', '2','baguette champignons', '', 's')
#y_recipe.check_attr()
#recipe_info = str(y_recipe)

