import time
import calendar
import random

class Critter(object):
    """A virtual pet"""
    def __init__(self,name):
        print("A new critter has been born!")
        self.name = name
        self.__hunger = random.randint(0, 15)
        self.__boredom = random.randint(0, 15)
        
    def __pass_time(self):
        """A method to pass time"""
        seconds = calendar.timegm(time.gmtime())
        current_second = seconds % 60
        minutes = seconds // 60
        current_minute = minutes % 60
        hours = minutes // 60
        current_hour = hours % 24

        @property
        def hunger(self):
            return self.__hunger

        @property
        def boredom(self):
            return self.__boredom
        if 1 in current_minute:
            hunger += 1
            boredom += 1
        return current_second, current_minute, current_hour
            
    
    def play(self):
        """A method to allow the user to play with critter"""
        print("Lets play!")

        @property
        def boredom(self):
            return self.__boredom
        fun = random.randint(0, 5)
        boredom = boredom - fun

    
    def talk(self):
        """A method to allow the critter to talk"""
        print("hello my name is:", end = " ")
        print(self.name)
        print("My current mood is:", end = " ")
        print(self.__mood)
    
    def eat(self):
        """A method to give the critter food"""
        print("Feed me")

        @property
        def hunger(self):
            return self.__hunger
        food = random.randint(0, 5)
        hunger = hunger - food

        if hunger < 0:
            hunger = 0
            self.__pass_time()
        else:
            self.__pass_time()
    
    def __mood(self):
        """A method to specify the mood of the critter"""

def main():
    while True:
        critName = input("Please enter a name for your critter ")
        if critName == "":
            print("sorry try again")
        else:
            crit1 = Critter(critName)
        break
    print(crit1.talk)
main()