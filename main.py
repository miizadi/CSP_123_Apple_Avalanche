#   a123_apple_1.py
import turtle as trtl
import random
lt = trtl.Turtle()
#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape
back_image = "background.gif"

applevowels = ["a", "i", "u", "e", "o"]

pearconsonants = ["f", "j", "p", "h", "l", "x", "c", "v", "b", "n", "m", "k", "j", "s","t", "r", "z", "q", "g", "d"]

ap = random.randint(0,1)
if ap == 0:
  apple_image = "pear.gif"
  rand_vowel = random.choice(pearconsonants)
else:
  apple_image = "apple.gif"
  rand_vowel = random.choice(applevowels)

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)#Make the screen aware of the newfile
wn.addshape(back_image)
apple = trtl.Turtle()
back = trtl.Turtle()
apple.speed(0)

lt.penup()
lt.goto(0,200)
lt.write(rand_vowel, font=("Arial", 50, "bold"))
apple.left(90)
yes = False
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
rand_x = random.randint(-200,200)
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  apple.showturtle()
  apple.penup()

  apple.goto(rand_x,150)

def blnk():
  moni = 0
def appole_fall():
  global drew
  global rand_vowel
  yes = False
  drew = 0
  apple.speed(1)
  apple.color("blue")
  wn.onkeypress(letter_apple, rand_vowel)
  wn.listen()
  apple.sety(-200)
  apple.color("red")
  wn.onkeypress(blnk, rand_vowel)
  apple.speed(0)
  
  letter_apple()
  lt.clear()

    
def letter_apple():
  global drew, rand_vowel
  if drew == 0:
    apple.write(rand_vowel, font=("Arial", 50, "bold"))
    drew = 1


def draw_background(active_back):
  active_back.shape(back_image)
  wn.update()

#-----function calls-----
draw_background(back)
draw_apple(apple)
appole_fall()
wn.listen()
wn.onkeypress(letter_apple, rand_vowel)
wn.listen()
apple.hideturtle()


while True:
  ap = random.randint(0,1)
  if ap == 0:
    apple_image = "pear.gif"
    rand_vowel = random.choice(pearconsonants)
  else:
    apple_image = "apple.gif"
    rand_vowel = random.choice(applevowels)
  
  wn.addshape(apple_image)#Make the screen aware of the newfile
  apple.speed(0)
  
  lt.penup()
  lt.goto(0,200)
  lt.write(rand_vowel, font=("Arial", 50, "bold"))
  
  yes = False
  #-----functions-----
  # given a turtle, set that turtle to be shaped by the image file
  rand_x = random.randint(-200,200)
  rand_y = random.randint(150,200)
  draw_apple(apple)
  appole_fall()
  wn.listen()
  wn.onkeypress(letter_apple, rand_vowel)
  wn.listen()
  apple.hideturtle()

wn.mainloop()