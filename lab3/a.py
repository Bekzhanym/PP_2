def function():
    print("HELLO WORLD")

function()

#Calling a Function
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Argument


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Arbitrary Arguments, *args

