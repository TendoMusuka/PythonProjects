from turtle import Screen,Turtle # turtle graphics
from turtle import Turtle
from prettytable import PrettyTable

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red", "green")
timmy.forward(100)

my_screen = Screen()
print(my_screen)
my_screen.exitonclick()


table = PrettyTable() #Table is the new table
table.field_names= ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmeter", "Fire"]
])

print(table)

