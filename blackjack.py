# Creating 1 deck of 52 cards in a dictionary
import random
print "\n\nNEW TRY"
deck52 = {"Heart-Ace": 1, "Heart-2": 2, "Heart-3": 3, "Heart-4": 4, "Heart-5": 5, "Heart-6": 6, "Heart-7": 7, "Heart-8": 8, "Heart-9": 9, "Heart-10": 10, "Heart-Jack": 10, "Heart-Queen": 10, "Heart-King": 10, "Diamond-Ace": 1, "Diamond-2": 2, "Diamond-3": 3, "Diamond-4": 4, "Diamond-5": 5, "Diamond-6": 6, "Diamond-7": 7, "Diamond-8": 8, "Diamond-9": 9, "Diamond-10": 10, "Diamond-Jack": 10, "Diamond-Queen": 10, "Diamond-King": 10, "Spade-Ace": 1, "Spade-2": 2, "Spade-3": 3, "Spade-4": 4, "Spade-5": 5, "Spade-6": 6, "Spade-7": 7, "Spade-8": 8, "Spade-9": 9, "Spade-10": 10, "Spade-Jack": 10, "Spade-Queen": 10, "Spade-King": 10, "Club-Ace": 1, "Club-2": 2, "Club-3": 3, "Club-4": 4, "Club-5": 5, "Club-6": 6, "Club-7": 7, "Club-8": 8, "Club-9": 9, "Club-10": 10, "Club-Jack": 10, "Club-Queen": 10, "Club-King": 10}

# dealer1, dealer2, playerA1, playerA2 = random.sample(deck52, 4)
# print dealer1
# print dealer2
# dealertotal =  deck52[dealer1] + deck52[dealer2]
# print dealertotal
# print playerA1
# print playerA2
# playerAtotal = deck52[playerA1] + deck52[playerA2]
# print playerAtotal

play52 = {}

play52 = random.sample(deck52, 52)
# print play52
# print "---"
# print play52[0]
# print play52[1]
# print play52[2]
# print play52[3]
# print play52[4]
# print play52[5]
# print play52[6]
# print play52[7]

have_ace = False

def ace_in_hand(card_value):
	if card_value == 1:
		have_ace = True
		return have_ace

def one_or_eleven(haveace):
	if haveace == True:
		oneoreleven = raw_input("Do you want the Ace to be 1 or 11?")
		if oneoreleven == "11":
			add_to_total = 10 #why does this make playertotal = 10 instead of adding on???
		elif oneoreleven == "1":
			add_to_total = 0
		else:
			add_to_total = 0
		return add_to_total
	else:
		add_to_total = 0
		return add_to_total
	


def more_than_twentyone(total_points):
	if total_points > 21:
		lose = True
		return lose

print"\n---PLAYER A---"
card_counter = 0
print "Player's first card is", play52[card_counter]+"."
ace_in_hand(deck52[play52[card_counter]])
playertotal = deck52[play52[card_counter]]

card_counter+=1
print "Player's second card is", play52[card_counter]+"."
playertotal += deck52[play52[card_counter]] #why doesn't this add to the 10??
print "playertotal", playertotal
player_have_ace = ace_in_hand(deck52[play52[card_counter]])
print "playertotal", playertotal
#1 or 11? need to test -- maybe create first_ace second_ace
addtototal = one_or_eleven(player_have_ace) #why does this not work???
print "playertotal", playertotal
playertotal = playertotal + addtototal
print "playertotal", playertotal
print "The total of Player's hand is %i." % (playertotal)

player_lost = more_than_twentyone(playertotal)
while player_lost == True:
	print "Player loses!"
	break


print "\n---DEALER---"
card_counter+=1
print "Dealer's first card is", play52[card_counter]+"."
dealertotal = deck52[play52[card_counter]]
card_counter +=1
print "Dealer's second card is", play52[card_counter]+"."
dealertotal += deck52[play52[card_counter]]
print "The total of the dealer's hand is %i." % (dealertotal)
dealer_lost = more_than_twentyone(dealertotal)
while dealer_lost == True:
	print "Dealer loses!"
	break


print"\n---PLAYER A---"

if playertotal == 21:
	print "Player wins!"
elif playertotal < 21:
	player_hit_me = raw_input("Do you want another card? 'yes' or 'no'?")
	while player_hit_me == "yes" and playertotal < 21:
		card_counter += 1
		print "Player's next card is", play52[card_counter]+"."
		ace_in_hand(deck52[play52[card_counter]])
		# 1 or 11?
		playertotal += deck52[play52[card_counter]]
		print "The total of the player's hand is %i.\n" % (playertotal)
		if playertotal > 21:
			print "Player loses!"
			break
		else:
			player_hit_me = raw_input("Do you want another card? 'yes' or 'no'?")
	else:
		print "Player does not take another card.\nThe FINAL TOTAL of the player's hand is %i." % (playertotal)
else:
	print "Player loses."


print"\n---DEALER---"

if playertotal <= 21:
	if dealertotal < 21:
		while dealertotal < 17:
			print "Dealer's current total is %i" % (dealertotal)
			card_counter += 1
			print "Dealer hits. Dealer's next card is", play52[card_counter]+"."
			dealertotal += deck52[play52[card_counter]]
			print "The total of the dealer's hand is %i.\n" % (dealertotal)
		print "Dealer does not take another card.\nThe FINAL TOTAL of the dealer's hand is %i.\n" % (dealertotal)
		if dealertotal > 21:
			print "Dealer's hand is greater than 21. Dealer loses!"
	else:
		print "The dealer's hand is greater than 21. The dealer loses."


if playertotal <= 21 and playertotal <= 21:
	if playertotal == dealertotal:
		print "Dealer and Player tie! Play again to determine a winner.\n"
	elif playertotal == 21 and dealertotal == 21:
		print "Dealer and Player tie! Play again to determine a winner.\n"
	elif playertotal == 21 and dealertotal < 21:
		print "Player wins! Player's hand is 21, and Dealer's hand is %i.\n" % (dealertotal)
	elif playertotal < 21 and dealertotal == 21:
		print "Dealer wins! Dealer's hand is 21, and Player's hand is %i.\n" % (playertotal)
	elif playertotal < 21 and dealertotal < 21 and playertotal > dealertotal:
		print "Player's hand of %i beats Dealer's hand of %i. Player wins!\n" % (playertotal, dealertotal)
	elif playertotal < 21 and dealertotal < 21 and dealertotal > playertotal:
		print "Dealer's hand of %i beats Player's hand of %i. Dealer wins!\n" % (dealertotal, playertotal)
	else:
		print "\nPlayer's total: %i. Dealer's total: %i.\n" % (playertotal, dealertotal)


	# elif playertotal > 21 and dealertotal < 21:
	# 	print "Player's hand is greater than 21. Dealer wins!\n"
	# elif playertotal < 21 and dealertotal > 21:
	# 	print "Dealer's hand is greater than 21. Player wins!\n"



# for i in range(2):

# 	print random.choice(deck52.keys())

# print "----DECK 2----"
# random.shuffle(deck52.keys())

# for i in range(10):
# 	print random.choice(deck52.keys())