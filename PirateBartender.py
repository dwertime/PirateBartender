import random
 
questions = {
    "strong": "Do ye like yer drinks strong? Enter: yes or no",
    "salty": "Do ye like it with a salty tang? Enter: yes or no",
    "bitter": "Are ye a lubber who likes it bitter? Enter: yes or no",
    "sweet": "Would ye like a bit of sweetness with yer poison? Enter: yes or no",
    "fruity": "Are ye one for a fruity finish? Enter: yes or no",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
#now I want to ask the questions in dictionary "questions"
#want to store answers to those questions in a new list
#that list should contain the type of ingredients desired
#a construct_drink function must loop through the list of preferences and randomly pull one corresponding value from the ingredients dictionary
#then print those values

preferences = []

def style_inquiry():
    """populate a list called preferences capturing the affirmative answers to the questions drawn from values in dictionary questions"""
    for k, v in questions.items():
        user_input = input(v)
        if user_input in ('y', 'ye', 'yes', 'Y', 'Ye', 'Yes'):
            preferences.append(k)

def construct_drink():
    """if and where items in list "preferences" match keys in ingredients dictionary, print a randomly chosen value matching that key"""
    print("Argh, let me put these here ingredients together for a delicious drink:")    
    for x in preferences:
        if x in ingredients:
            print(random.choice(ingredients[x]))

def drink_cycle():
    """this function allows the user to order multiple drinks up to a hard-coded drink_stock quantity; part of the extra project challenges"""
    drink_stock = 0
    drinking = True
    
    while drinking:
        if drink_stock <= 2:
            style_inquiry()
            construct_drink()
            drunkard_input = input("Now would ye like another, ya lubbable drunkard??")
            if drunkard_input in ('y', 'ye', 'yes', 'Y', 'Ye', 'Yes'):
                preferences[:] = []
                drink_stock += 1
            
            else:
                print("Had enough, have ye? Fare the well!")
                drinking = False
        else: 
            print("Argh, that's all the booze I've got in this here bar for today, laddie.")
            drinking = False
    
if __name__ == "__main__":
    drink_cycle()
