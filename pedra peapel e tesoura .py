import random
print("vamos jogar pedra,papel ou tesoura.")

player_choice = input("escolha entre pedra,papel ou tesoura !").lower()

choices =["pedra","papel","tesoura"]

computer_choice = random.choice(choices)

print(f"Computador escolheu: {computer_choice}")

if(player_choice == "pedra" and computer_choice=="tesoura")or (player_choice =="tesoura"and computer_choice == "papel")or (player_choice == "papel"and computer_choice == "pedra"):
    winner ="Player"

elif player_choice == computer_choice:

    winner = "Tie" #empatou

else:

    winner = "Computer"


if winner == "Player":

    print("voce ganhou")

elif winner == "Computer":

    print("voce perdeu")

else:

    print("empatou") 
