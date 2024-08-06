import random
import streamlit as st
import time

def main():
    # Initialisation de l'état de la session
    if 'money' not in st.session_state:
        st.session_state.money = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

    st.title("Jeu de Chance")

    if st.session_state.game_over:
        st.write("Game Over! Vous avez perdu.")
        time.sleep(5)  # Attendre 5 secondes avant de quitter
        st.stop()
    else:
        st.write(f"Argent actuel : {st.session_state.money} €")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button('Jouer'):
                if random.randint(1, 100) == 1:
                    st.session_state.game_over = True
                    st.write("Game Over! Vous avez perdu.")
                    time.sleep(5)  # Attendre 5 secondes avant de quitter
                else:
                    st.session_state.money += 1000
                    st.write("Vous avez gagné 1 000 € !")

        with col2:
            if st.button('Encaisser'):
                st.write(f"Vous avez encaissé {st.session_state.money} €")
                time.sleep(5)  # Attendre 5 secondes avant de quitter
                st.stop()

        with col3:
            if st.button('Quitter'):
                st.write(f"Vous avez quitté le jeu avec {st.session_state.money} €")
                time.sleep(5)  # Attendre 5 secondes avant de quitter
                st.stop()

if __name__ == "__main__":
    main()
