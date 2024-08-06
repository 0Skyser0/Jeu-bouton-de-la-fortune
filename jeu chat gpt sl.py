import random
import time

def play_game():
    money = 0
    game_over = False

    while not game_over:
        print(f"\nArgent actuel : {money} €")
        print("1. Jouer")
        print("2. Encaisser")
        print("3. Quitter")

        choice = input("Choisissez une option (1/2/3) : ")

        if choice == '1':
            if random.randint(1, 100) == 1:  # 1 chance sur 100 pour le game over
                game_over = True
                print("Game Over! Vous avez perdu.")
                time.sleep(5)  # Attendre 5 secondes avant de quitter
            else:
                money += 1000
                print("Vous avez gagné 1 000 € !")
        elif choice == '2':
            print(f"Vous avez encaissé {money} €")
            time.sleep(5)  # Attendre 5 secondes avant de quitter
            break
        elif choice == '3':
            print(f"Vous avez quitté le jeu avec {money} €")
            time.sleep(5)  # Attendre 5 secondes avant de quitter
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    play_game()
