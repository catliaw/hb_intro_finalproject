# Creating 1 deck of 52 cards in a dictionary
import random
print "\n\nNEW TRY"
deck52 = {"Heart-Ace": 1, "Heart-2": 2, "Heart-3": 3, "Heart-4": 4, "Heart-5": 5, "Heart-6": 6, "Heart-7": 7, "Heart-8": 8, "Heart-9": 9, "Heart-10": 10, "Heart-Jack": 10, "Heart-Queen": 10, "Heart-King": 10, "Diamond-Ace": 1, "Diamond-2": 2, "Diamond-3": 3, "Diamond-4": 4, "Diamond-5": 5, "Diamond-6": 6, "Diamond-7": 7, "Diamond-8": 8, "Diamond-9": 9, "Diamond-10": 10, "Diamond-Jack": 10, "Diamond-Queen": 10, "Diamond-King": 10, "Spade-Ace": 1, "Spade-2": 2, "Spade-3": 3, "Spade-4": 4, "Spade-5": 5, "Spade-6": 6, "Spade-7": 7, "Spade-8": 8, "Spade-9": 9, "Spade-10": 10, "Spade-Jack": 10, "Spade-Queen": 10, "Spade-King": 10, "Club-Ace": 1, "Club-2": 2, "Club-3": 3, "Club-4": 4, "Club-5": 5, "Club-6": 6, "Club-7": 7, "Club-8": 8, "Club-9": 9, "Club-10": 10, "Club-Jack": 11, "Club-Queen": 12, "Club-King": 13}

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
print play52
print "---"
print play52[0]
print play52[1]
print play52[2]
print play52[3]
print play52[4]
print play52[5]
print play52[6]
print play52[7]

have_ace = False

def ace_in_hand(card_value):
	if card_value == 1:
		have_ace = True

print "\n---DEALER---"
card_counter = 0
print "Dealer's first card is", play52[card_counter]+"."
dealertotal = deck52[play52[card_counter]]
card_counter +=1
print "Dealer's second card is", play52[card_counter]+"."
dealertotal += deck52[play52[card_counter]]
print "The total of the dealer's hand is %i." % (dealertotal)


print"\n---PLAYER A---"
card_counter+=1
print "Player's first card is", play52[card_counter]+"."
ace_in_hand(deck52[play52[card_counter]])
playertotal = deck52[play52[card_counter]]
card_counter+=1
print "Player's second card is", play52[card_counter]+"."
ace_in_hand(deck52[play52[card_counter]])
# 1 or 11?
playertotal += deck52[play52[card_counter]]

print "The total of Player's hand is %i." % (playertotal)

print"\n---DEALER---"

if dealertotal < 21:
	while dealertotal < 17:
		card_counter += 1
		print "Dealer's next card is", play52[card_counter]+"."
		dealertotal += deck52[play52[card_counter]]
		print "The total of the dealer's hand is %i.\n" % (dealertotal)
	print "Dealer does not take another card.\nThe FINAL TOTAL of the dealer's hand is %i." % (dealertotal)
else:
	print "The dealer loses."

print"\n---PLAYER A---"

if playertotal == 21:
	print "Player wins!"
elif playertotal < 21:
	player_hit_me = raw_input("Do you want another card? 'True' or 'False'?")
	while player_hit_me == "True" and playertotal < 21:
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
			player_hit_me = raw_input("Do you want another card? 'True' or 'False'?")
	else:
		print "Player does not take another card.\nThe FINAL TOTAL of the player's hand is %i." % (playertotal)
else:
	print "Player loses."

# while playertotal < 21:
	# ask player wants to hit
		# if player respond yes then:
			# +1 counter, new total
			# if new total = 21
				# print player win!
				# break out of game
			# if new total > 21
				# print player loses!
				# break out of game
		#if player responds no then:
			#





# for i in range(2):

# 	print random.choice(deck52.keys())

# print "----DECK 2----"
# random.shuffle(deck52.keys())

# for i in range(10):
# 	print random.choice(deck52.keys())