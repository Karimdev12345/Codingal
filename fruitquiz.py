import random

class FruitQuiz:

    def __init__(self):
        self.fruits= {'apple': 'red', 'orange': 'orange', 'watermelon': 'green', 'banana': 'yellow'}
    def quiz(self):
        while(True):

            fruit, color= random.choice(list(self.fruits.items()))

            print("What is the color of {}".format(fruit))
            user_answer= input()