"""Application de développement personnel"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, BOLD, ITALIC, RIGHT

class Streaker(toga.App):
    # Stockage de la référence du champ d'entrée
    input_field = None 
    main_window = None
    
    # Liste interne des habitudes (simulées)
    habits_data = [
        {"id": 1, "text": "Lire 15 minutes", "done": False},
        {"id": 2, "text": "Boire 2L d'eau", "done": True},
        {"id": 3, "text": "Méditer 5 minutes", "done": False},
    ]

    # --- MÉTHODES DE NAVIGATION ET D'INTERACTION (Doivent être dans la classe!) ---
    
    def show_home(self, command): # <-- Cette méthode DOIT exister
        """Affiche l'écran principal des habitudes."""
        self.main_window.content = self._create_home_content()

    def show_settings(self, command): # <-- Cette méthode DOIT exister
        """Affiche l'écran des paramètres."""
        self.main_window.content = toga.Label(
            "Écran des Paramètres (À développer)", 
            style=Pack(margin=50, font_size=20)
        )
    
    def add_habit(self, widget): # <-- Cette méthode DOIT exister
        """Ajoute une habitude à la liste et met à jour l'affichage."""
        nom_habitude = self.input_field.value.strip() 
        
        if nom_habitude:
            self.habits_data.append({"id": len(self.habits_data) + 1, "text": nom_habitude, "done": False})
            self.input_field.value = ""
            self.main_window.content = self._create_home_content()
        else:
            self.main_window.info_dialog('Erreur', "Veuillez saisir le nom de l'habitude.")

    # --- MÉTHODE DE CONSTRUCTION DU CONTENU DE L'ÉCRAN ---
    
    def _create_home_content(self): # <-- Cette méthode DOIT exister
        """Construit et retourne le layout de l'écran d'accueil."""
        # Note: Cette méthode n'est pas censée être appelée directement par l'utilisateur, 
        # d'où l'usage du préfixe "_"
        BROWN_COLOR = "#5C4033" 
        MARBLE_BG = "#F5F5DC" 

        # --- Widgets pour l'interaction ---
        # NOTE: self.input_field doit être défini ici
        self.input_field = toga.TextInput(
            placeholder="Nouvelle habitude...",
            style=Pack(flex=1, margin_right=5)
        )
        
        add_button = toga.Button(
            "Ajouter",
            on_press=self.add_habit,
            style=Pack(width=100)
        )

        input_container = toga.Box(
            style=Pack(direction=ROW, margin=10, background_color=MARBLE_BG),
            children=[self.input_field, add_button]
        )
        
        # --- Affichage de la Liste ---
        data_rows = []
        for item in self.habits_data:
            status = "✅" if item['done'] else "☐"
            data_rows.append((status, item['text']))

        habits_table = toga.Table(
            headings=["Statut", "Habitude"], 
            data=data_rows,
            style=Pack(flex=1, margin=(0, 10, 10, 10))
        )
        
        content_box = toga.Box(
            style=Pack(direction=COLUMN, background_color="#FFFFFF", margin=15, flex=1),
            children=[habits_table]
        )
        
        title_label = toga.Label(
            "Mes Habitudes",
            style=Pack(font_size=24, font_weight=BOLD, color=BROWN_COLOR, margin=(50, 20, 10, 20), text_align=CENTER)
        )
        
        home_content = toga.Box(
            style=Pack(direction=COLUMN, background_color=MARBLE_BG, flex=1, align_items=CENTER),
            children=[title_label, content_box, input_container]
        )
        
        return home_content
        
    # --- MÉTHODE DE DÉMARRAGE PRINCIPALE ---
    
    def startup(self):
        # Création de la main_window pour que les Commandes fonctionnent
        self.main_window = toga.MainWindow(title=self.formal_name)
        
        # Le contenu initial est créé
        home_content = self._create_home_content()
        self.main_window.content = home_content
        
        # Déclaration et ajout des Commandes de navigation
        self.commands.add(
            toga.Command(self.show_home, text="Habitudes", tooltip="Mes Habitudes", icon=toga.Icon.DEFAULT_ICON),
            toga.Command(self.show_settings, text="Paramètres", tooltip="Paramètres", icon=toga.Icon.DEFAULT_ICON)
        )

        self.main_window.show()


def main():
    # S'assurer que le nom formel est passé pour le titre de la fenêtre.
    return Streaker('Streaker', 'com.simon.streaker')