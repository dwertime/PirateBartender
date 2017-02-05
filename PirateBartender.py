questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
#now I want to ask the questions in dictionary "questions"
#want to store answers to those questions in a new dictionary 
#that dictionary should contain the type of ingredients mapped to boolean values
#program must code answers like yep, yes, sure, or strong as specific ingredients or guide user to proper form
#must match selected  intredients from new dictionary to corresponding ingredients from ingredients dictionary
#use random.choice function to choose ONE ingredient from each selected type
#use if '_name_' == '_main_': to call function at command line; it should run the style and construct functions in order and then print ingredients

def style_inquiry():
    """I print the values from the questions dictionary and gather responses in a new dictionary"""
    for question in questions:
        print(question)
    
def construct_drink:
    """I randomly choose ingredients from selected types in ingredients dictionary and print them"""
    