import random

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


#Ask customer drink pref

def ask_style_drink():
    customer_preferences = {}
    for key in questions:
        answer = (str (input (questions[key]))).lower()     
        if answer == "y" or answer == "yes":
            customer_preferences[key] = True
        else:
            customer_preferences[key] = False

    return customer_preferences



# Create a drink based on preferences
def construct_drink(customer_preferences):
    global ingredients
    drink=[]
    for type_ingredient in customer_preferences:
        if customer_preferences[type_ingredient] == True:
            drink.append(random.choice(ingredients[type_ingredient]))
    print (drink)
    return drink    
    


if __name__ == '__main__':
    thirsty = str(input ("Are you Thirsty? ")).lower()
    #print (thirsty)
    while thirsty == "y" or thirsty == "yes":
        print( "Your drink consists of: " , construct_drink(ask_style_drink()))
        print ("Thanks for drinking")
        thirsty = str(input ("Are you Thirsty? ")).lower()
        if thirsty == "n" or thirsty == "no":
            thirsty = "n"
    print ("Have a great night!")
    
