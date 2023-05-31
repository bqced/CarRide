class Car:
#Variables are initialised and set to zero
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
#The value of the speed variable which is zero at the monent is put inside the string
    def say_state(self):
        print("I'm going {} kph!".format(self.speed))
#Increase the speed by 5, everytime the user inputs A(accelerate)
    def accelerate(self):
        self.speed += 5
#Decreases speed everytime the user inputs B(brake)
    def brake(self):
        self.speed -= 5
#Calculates distance traveled when user inputs 0(odometer), time increases by an hour when speed is increased
    def step(self):
        self.odometer += self.speed
        self.time += 1
#Calculates average speed by dividing total distance by total time, the function works as long as the time isnt 0
    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

#it checks if the letter the user inputs is in the action variable and if the it's only one letter, if it matches then it outputs different values depending on the letter the user inputted
if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                 "show [O]dometer, or show average [S]peed?").upper
        if action not in input or len(action) != 1:
            print("I don't know how to do that")
            else:
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()
