import random
#This is a simplyfied BlackJack game from the command line, you can play but also you can see the odds while you're playing
#You can't bet or split, the ace value is always 11
#The game include the odds

print('WELCOME TO BLACKJACK, RULES ARE THE SAME BUT YOU CAN\'T SPLIT AND THE ACE VALUE IS ALWAYS 11')
print('#1  ---> Ace\n#11 ---> Jack\n#12 ---> Queen\n#13 ---> King')


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,        #The deck has two regular decks of 52 cards each
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,        #1  ---> Ace
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,        #11 ---> Jack
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,        #12 ---> Queen
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,        #13 ---> King
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


user_cards = [0, 0]
dealer_cards = [0, 0]

user_cards[0] = deck.pop(int(random.random()*len(deck))) #Takes a random card from the deck and pop it from the array deck
user_cards[1] = deck.pop(int(random.random()*len(deck))) #assign it to the user hand

dealer_cards[0] = deck.pop(int(random.random()*len(deck)))
dealer_cards[1] = deck.pop(int(random.random()*len(deck)))

print('')
print('Your hand is: ' + str(user_cards) + '\n')
print('The dealer hand is: ' + str(dealer_cards[0]) + '\n')

def calc_score(card) :               
    result = 0                      
    if card != 1 and card < 11 :        #Calculate the score of a hand given one card at the time
        result += card                  #The score is based on the blackjack rules except that the ace value is always 11
    elif card != 1 and card >= 11 :
        result += 10
    else :
        result += 11

    return result

score = 0
score += calc_score(user_cards[0])
score += calc_score(user_cards[1])

def odds(score) :
    
    difference = 21 - score            #This function handle completely the odds
    case_in_favor_up = 0               #Calculated as cases in favor/ all possible cases  
    case_in_favor_under = 0
    prob_up_21 = 0
    prob_under_21 = 0
    
    if difference < 10 :
        for i in deck :
            if i >= difference or i == 1 :
                case_in_favor_up += 1
            else :
                case_in_favor_under += 1
    
    elif difference >= 11 :
        case_in_favor_up += 0
        case_in_favor_under += len(deck)  
    
    else : #if difference == 10 :
        for i in deck :
            if i == 1 :
                case_in_favor_up += 1
            else :
                case_in_favor_under += 1

    prob_up_21 = (case_in_favor_up/len(deck)) * 100
    prob_under_21 = (case_in_favor_under/len(deck)) * 100

    print('The probability to go up 21 with the next card is: ' + str(prob_up_21) + ' %\n')
    print('The probability to NOT go up 21 with the next card is: ' + str(prob_under_21)  + ' %')
    


print('Your score is: ' + str(score) + '\n')
#odds(score)
print('-------------------------------------------------------------------------------------------------------')

while score <= 21 : 
    odds(score)         #The user can take cards until he has a maximum score of 21                   
    next_move = input('You want a card or want to stay? card/stay\n')
    
    
    if next_move == 'card' :
        user_cards.append(deck.pop(int(random.random()*len(deck))))
        score += calc_score(user_cards[len(user_cards) - 1])
        print('Now you have: ' + str(user_cards) + '\n')
        print('Your score is: ' + str(score) + '\n')
    elif next_move == 'stay' :
        break
    else :
        print('Please choose a valid move\n')

    

print('-------------------------------------------------------------------------------------------------------')
   
if score > 21 :
    #print('Your score is: ' + str(score) + '\n')
    print('YOU LOSE')
    exit()
    
dealer_score = 0
dealer_score += calc_score(dealer_cards[0])
dealer_score += calc_score(dealer_cards[1])  

def winner_text(result) :
    print('Your hand is: ' + str(user_cards) + '\n')
    print('Your score is: ' + str(score) + '\n')
    print('The dealer hand is: ' + str(dealer_cards) + '\n')
    print('The dealer score is: ' + str(dealer_score) + '\n')
    print('YOU ' + result)  
    
while dealer_score <= 17 :     #The dealer as to take cards until he has at least 17 of score
        
    dealer_cards.append(deck.pop(int(random.random()*len(deck))))
    dealer_score += calc_score(dealer_cards[len(dealer_cards) - 1])
    
if  score > dealer_score and score <= 21 :
        winner_text('WON')
elif score < dealer_score and dealer_score <= 21 :
        winner_text('LOSE')
elif dealer_score > 21 :
        winner_text('WON')
elif score == dealer_score :
        winner_text('TIED')

