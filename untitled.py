class Human(object):
    
    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender 
        self.race = race
    def introduce_self(self):
        print("Hello my name is", self.name)
    def discribe_self(self):
        print("I have", self.hair_color, "hair")
        print("I have", self.eye_color, "eyes")
        print("I am", self.height, " m tall")
        print("I weigh", self.weight, "lbs")
        print("I am a", self.race, self.gender, "with an IQ of", self.iq)
    def bmi(self):
        """Calculates bmi for Human""" 

eric = Human("Eric", "Black", "Brown", 1.72,
             195, 300, "Male", "White")
eric.introduce_self()
eric.discribe_self()

bob = Human("Bob", "Blonde", "Blue", 6.4,
             200, 94, "Male", "White")
bob.introduce_self()
bob.discribe_self()

green_giant = Human("Green", "Green", "Green", 50,
                     3000, None, "Male", "Green Giant")
green_giant.introduce_self()
green_giant.discribe_self()
