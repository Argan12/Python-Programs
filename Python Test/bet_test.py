# -*-coding:utf-8 -*

import os
from random import randrange

gains = 50
restart = 1

while (restart == 1):
	print("Il vous reste ", gains, " euros")

	randomNumber = randrange(50)
	number_bet = input("Sur quel nombre souhaitez-vous miser ? ")
	number_bet = int(number_bet)
	
	while number_bet < 0 or number_bet > 50:
		number_bet = input("Sur quel nombre souhaitez-vous miser ? ")		
		try:
			number_bet = int(number_bet)
		except ValueError:
			print("Vous n'avez pas saisi de nombre")
			continue
		if number_bet < 0:
			print("Veuillez entrer un nombre positif")
		if number_bet > 50:
			print("Veuillez entrer un nombre compris en 0 et 50")
	
	money_bet = 0
	
	while money_bet > gains or money_bet <= 0:
		money_bet = input("Combien d'argent souhaitez-vous miser ? ")
		try:
			money_bet = int(money_bet)
		except ValueError:
			print("Veuillez saisir une mise")
			continue
		if money_bet > gains:
			print("Vous ne pouvez pas miser une somme supérieur à votre capital points")
		if money_bet < 0:
			print("Vous ne pouvez pas miser une somme négative")
			

	if (number_bet == randomNumber):
		print("Félicitations ! Le nombre à deviner était bien ", randomNumber)
		gains = gains + money_bet * 3
	elif ((number_bet%2 == 0 and randomNumber%2 == 0) or (number_bet%2 != 0 and randomNumber%2 != 0)):
		print("Bien, le nombre à deviner était ", randomNumber)
		gains = gains + money_bet/2
	else:
		print("Raté ! Le nombre à deviner était : ", randomNumber)
		gains = gains - money_bet
		
	restart = input("Souhaitez-vous refaire une partie ? ")
	restart = int(restart)

print("A bientôt")

os.system("pause")