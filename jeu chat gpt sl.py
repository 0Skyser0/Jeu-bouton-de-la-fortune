import tkinter as tk
from tkinter import messagebox
import random

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Chance")
        
        # Initialiser les variables du jeu
        self.money = 0
        self.game_over = False

        # Création du bouton doré pour jouer
        self.play_button = tk.Button(root, text="Jouer", font=('Helvetica', 16), bg='gold', command=self.play_game)
        self.play_button.pack(pady=20)
        
        # Création du label pour afficher l'argent
        self.money_label = tk.Label(root, text=f"Argent actuel : {self.money} €", font=('Helvetica', 16))
        self.money_label.pack(pady=10)

        # Création du bouton d'encaissement
        self.cashout_button = tk.Button(root, text="Encaisser", font=('Helvetica', 16), command=self.cashout)
        self.cashout_button.pack(pady=5)
        
        # Création du bouton de quitter
        self.quit_button = tk.Button(root, text="Quitter", font=('Helvetica', 16), command=self.quit_game)
        self.quit_button.pack(pady=5)
        
        # Création du bouton pour réessayer après Game Over
        self.retry_button = tk.Button(root, text="Essayer à nouveau", font=('Helvetica', 16), command=self.reset_game)
        self.retry_button.pack(pady=5)
        self.retry_button.pack_forget()  # Masquer le bouton au début

    def play_game(self):
        """Gère la logique du jeu lorsque le joueur appuie sur 'Jouer'."""
        if not self.game_over:
            if random.randint(1, 100) == 1:  # 1 chance sur 100 pour le game over
                self.game_over = True
                self.show_message("Game Over ! Vous avez perdu.")
                self.retry_button.pack(pady=5)  # Afficher le bouton pour réessayer
                self.play_button.config(state=tk.DISABLED)  # Désactiver le bouton jouer
            else:
                self.money += 1000
                self.update_money_label()
                self.show_message("Vous avez gagné 1 000 € !")

    def cashout(self):
        """Gère l'encaissement de l'argent."""
        if not self.game_over:
            self.show_message(f"Vous avez encaissé {self.money} €")
            self.reset_game()  # Réinitialiser le jeu après avoir encaissé
        else:
            self.show_message("Le jeu est terminé. Vous ne pouvez plus encaisser.")

    def quit_game(self):
        """Gère la fermeture du jeu."""
        if not self.game_over:
            self.show_message(f"Vous avez quitté le jeu avec {self.money} €")
        else:
            self.show_message("Le jeu est terminé.")
        self.root.after(5000, self.root.quit)  # Attendre 5 secondes avant de quitter

    def reset_game(self):
        """Réinitialiser les variables du jeu et l'interface."""
        self.money = 0
        self.game_over = False
        self.update_money_label()
        self.retry_button.pack_forget()  # Masquer le bouton réessayer
        self.play_button.config(state=tk.NORMAL)  # Réactiver le bouton jouer

    def update_money_label(self):
        """Mettre à jour l'affichage de l'argent actuel."""
        self.money_label.config(text=f"Argent actuel : {self.money} €")

    def show_message(self, message):
        """Afficher un message d'information."""
        messagebox.showinfo("Information", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
