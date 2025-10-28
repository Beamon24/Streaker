"""Application de développement personnel"""
import toga
from toga.style.pack import COLUMN, ROW, Pack
from toga import Label, TextInput, Button

class Streaker(toga.App):
    # Liste interne pour simuler le stockage des habitudes (comme self.liste en Kivy)
    liste_habitudes = []
    
    def startup(self):
        # -------------------- 1. Déclaration des Widgets --------------------
        
        # Champ de saisie pour la nouvelle habitude
        self.habit_input = TextInput(
            placeholder="Nom de l’habitude (ex: Boire 2L d'eau)",
            style=Pack(flex=1) # Permet au champ de prendre l'espace disponible
        )
        
        # Label pour afficher la liste des habitudes
        self.list_label = Label(
            "Appuyez sur 'Ajouter' pour commencer le suivi.",
            style=Pack(flex=1, padding_top=10) # Utilise flex=1 pour occuper l'espace
        )

        # Bouton d'ajout
        add_button = Button(
            "Ajouter",
            on_press=self.add_habit, # Lien vers la méthode Python
            style=Pack(padding_left=5)
        )
        
        # -------------------- 2. Structure du Layout --------------------
        
        # A. Conteneur pour la saisie et le bouton (Disposition Horizontale - ROW)
        input_container = toga.Box(
            style=Pack(direction=ROW, padding=10),
            children=[
                self.habit_input,
                add_button
            ]
        )
        
        # B. Conteneur Principal (Disposition Verticale - COLUMN)
        main_box = toga.Box(
            style=Pack(direction=COLUMN),
            children=[
                input_container,
                self.list_label
            ]
        )

        # -------------------- 3. Fenêtre Principale --------------------
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    # -------------------- 4. Logique d'Interaction --------------------
    def add_habit(self, widget):
        """Méthode appelée lors du clic sur le bouton 'Ajouter'."""
        
        nom_habitude = self.habit_input.value.strip() # En Toga, le texte est dans .value
        
        if nom_habitude:
            # 1. Ajout à la liste interne
            self.liste_habitudes.append(nom_habitude)
            
            # 2. Mise à jour du Label
            texte_a_afficher = "\n".join(self.liste_habitudes)
            self.list_label.text = "Vos habitudes :\n" + texte_a_afficher
            
            # 3. Effacer le champ de saisie
            self.habit_input.value = ""
        else:
            print("Le champ d'habitude est vide. Rien n'a été ajouté.")


def main():
    return Streaker()