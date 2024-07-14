import turtle
import time
import random
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'orange', 'yellow', 'blue', 'black', 'cyan', 'brown', 'purple', 'maroon']


def get_number_of_racers():
    racers = 0
    while True:
            racers = input('Enter the number of racers(2-10): ')
            if racers.isdigit():
                racers = int(racers)
            else:
                print("Invalid input1")
                continue
            if 2 <= racers <=10:
                return racers
            else:
                print('Number not in range 2-10. try agaiin')


def create_racers(colors):
    racers = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, each_single_color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(each_single_color) # Gives single color to each turtles
        # racer.color(colors) #  try to Give every color to each turtles which throws error
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        racers.append(racer)
    return racers

def start_race(colors):
    racers = create_racers(colors)

    while True:
        for racer in racers:
            distance =  random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[racers.index(racer)]

def init_race():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Race Game')
    
racers = get_number_of_racers()
init_race()

random.shuffle(COLORS)
colors = COLORS[:racers]
# create_racers(colors)
winner = (start_race(colors)).upper()
print(f"{winner} turtle wins the race!!")
time.sleep