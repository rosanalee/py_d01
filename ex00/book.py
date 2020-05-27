import sys
from datetime import datetime
from recipe import Recipe


class Book():
    def __init__(self):
        print('Enter a name for this Book')
        reponse = input()
        self.name = reponse
        self.last_update = datetime.today()
        self.creation_date = datetime.today()
        self.recipe_list = dict(starter=list(), lunch=list(), dessert=list())
        print(f"""The book \"{self.name}\" has successfully been created.""")

    def get_creation_date(self):
        readable_crea_date = datetime.strftime(my_book.creation_date, '%d %b %Y at %H:%M')
        print(f"\"{self.name}\" has been created on the {readable_crea_date}.")
    
    def get_last_update(self):
        readable_update = datetime.strftime(my_book.last_update, '%d %b %Y at %H:%M')
        print(f"\"{self.name}\"\'s last updated on the {readable_update}.")

    def check_name(self):
        if self.name == '':
            print('Name can\'t be empty')
            sys.exit()
    
    def get_all_recipe_names(self, name):
        l = ""
        for n in self.recipe_list['starter']:
            l = n.get(name) 
        if l is None:
            for n in self.recipe_list['lunch']:
                l = n.get(name)
            if l is None:
                for n in self.recipe_list['dessert']:
                    l = n.get(name)
        if l is None:
            print('Recipe does not exist in this book')
        else:
            print("Here are the info of {name}:")
            print(l)

    def get_type(self, type):
        print(f'Recipes if type {type}')
        for n in self.recipe_list[type]:
            print(n)
            
    
    def add_recipe(self):
        print('Let\'s add a new recipe!')
        print('Enter a name (cannot be empty)')
        new_name = str(input())
        print('Enter a description')
        new_desc = str(input())
        print('Enter a cooking level between 1 and 5')
        new_cook_lvl = input()
        print('Enter the ingredients (separate each one by a space)')
        new_ing = str(input())
        print('Enter the meal type: write \'starter\', \'lunch\' or \'dessert\'')
        new_type = str(input())
        print('Enter the number of minutes needed (ex: 15)')
        new_time = input()
        try:
            recipe_c = Recipe(new_name, new_cook_lvl, new_time, new_ing, new_desc, new_type)
            add = recipe_c.check_attr()
            self.recipe_list[new_type].append(add)
            print(self.recipe_list[new_type])
            print(self.recipe_list)
            my_book.get_last_update()
            print(f"{new_name} has been added to {new_type} category.")
        except:
            print('')

my_book = Book()
while True:
    try:
        res = str(input())
        if res == 'crea':
            my_book.get_creation_date()
        elif res == 'x':
            print('Bye bye')
            sys.exit()
        elif res == 'add':
            try:
                my_book.add_recipe()
            except:
                print('Try again.')
        elif res == 'update':
            my_book.get_last_update()
        elif res == 'name':
            print('Enter a name:')
            name_r = str(input())
            my_book.get_all_recipe_names(name_r)
        elif res == 'type':
            print('Enter type:')
            tyep_r = str(input())
            my_book.get_type(tyep_r)
        else:
            sys.exit()
    except:
        print('exit')
        sys.exit()

