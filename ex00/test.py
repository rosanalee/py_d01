from recipe import Recipe
from book import Book
import sys

my_book = Book()
usage = """Commands:
crea: get creation date
add: add new recipe
update: show last update time
type: seach recipe by type
name: seach recipe by name
x: exit
h: show usage
"""
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
