import random
the_num = 21
suits = ["C","D","H","S"] #Club, Diamond, Heart, Spades
face = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

num_player = int(input("Enter the number of players: "))
holding = "00"
list_num = ["01"]

# num_face = random.randint(0,len(face))
# num_suit = random.randint(0,len(suits))

# print("num_face, num_suit",num_face,num_suit)

# holding = suits[num_suit] + face[num_face]
# print(holding)
print(holding in list_num)
for i in range(num_player-1):
    while True:
        if holding in list_num:
            break
        else:
            num_face = random.randint(0,len(face))
            num_suit = random.randint(0,len(suits))
            holding = str(suits[num_suit])+str(face[num_face])
            list_num.append(holding)
    print(holding)

        