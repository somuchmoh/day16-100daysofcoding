#Calling modules, class and objects
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink", "CornflowerBlue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


#Calling a package to create a table
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ['NAME', 'LOCATION', 'ROLE']
table.add_rows(
    [
        ['Mary', 'Bangalore', 'SDE2'],
        ['Sally', 'Mumbai', 'Content Manager'],
        ['Paul', 'Delhi', 'Sales Associate']
    ]
)
table.align = 'l'
#left align the table

print(table)