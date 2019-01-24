import time
import calendar
import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name 
        self.__hunger = hunger
        self.__boredome = boredom
    
    def __pass_time(self):
        """A method to pass time"""
        seconds = calendar.timegm(time.gmtime())
        current_second = seconds % 60
        minutes = seconds // 60
        current_minute = minutes % 60
        hours = minutes // 60
        current_hour = hours % 24

        if 1 in current_minute:
            self.__hunger +=1
            self.__boredome += 1
        
    
    @property
    def mood(self):
        """A method to specify the mood of the critter"""
        unhappiness = self.__hunger + self.__boredome
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        """A method to allow the critter to talk"""
        print("I'm", self.name, "and I currently feel", self.mood, "\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("Brruppp. Thank you.")
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()
    
    def play(self, fun = 4):
        """A method to allow the user to play with critter"""
        print("Wheee!")
        self.__boredome -= fun
        if self.__boredome < 0:
            self.__boredom = 0
        self.__pass_time()

def main():
    while True:
        crit_name = input("What do you what to name your critter? ")
        if crit_name == "":
            print("sorry try again")
        else:
            crit = Critter(crit_name)
    
    choice = None
    while choice != "0":
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed you critter
        3 - Play with your critter
        4 - Display the current time
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye")
            break
        
        # critter talk
        elif choice == "1":
            crit.talk()
        
        # feed critter
        elif choice == "2":
            crit.eat()
        
        # play with critter
        elif choice == "3":
            crit.play()

        elif choice == "4":
            print(current_hour,":")
        
        # try again
        else:
            print("Please try again")

main()
