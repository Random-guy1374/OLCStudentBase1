import random
the_num = 21
suits = ["C","D","H","S"] #Club, Diamond, Heart, Spades
face = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

num_player = int(input("Enter the number of players:"))
holding = "00"
list_num = []
for i in range(num_player):
    while True:
        if holding in list_num:
            break
        else:
            num_face = random.randint(0,len(face))
            num_suit = random.randint(0,len(suits))
            holding = suits[num_suit]+face[num_face]

        