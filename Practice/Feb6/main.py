from function import AddTwo, AddThree

print(AddTwo(1,2))

#user name generator
import random

def gen_username():
  try:
    name = input("Please input your first name: ")
    number = int(input("Please input a random number"))
  except ValueError:
    print("That was not a valid number! Please insert a number")
    gen_username()
  else:
    x = random.randint(1, number)
    user = (name[:5] + (str(x))).lower()
    print(f"Your new username is {user}")
    return user
  finally:
    print("thanks for using this generator!")

gen_username()

'''
Being able to separate your code amongst different files and import it into a main file is definitely 
the most useful to me. This allows you to clean your code up a lot more rather than it being a jumbled up 
mess. I also think the "try, except, else, finally" statements are also really useful. These statements can
eliminate a lot of extra, unneccesary code.
'''