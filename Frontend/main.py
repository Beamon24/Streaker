import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

kivy.require('2.0.0')

class MainPage(Screen):
    habit_name_input = ObjectProperty(None)
    liste_habitude = ObjectProperty(None)

    def __init__(self,**kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.liste = []

    def ajout_habitude(self):
        nom_habitude = self.habit_name_input.text.strip()
        
        if nom_habitude:
            self.liste.append(nom_habitude)
            print(f"Habitude ajoutée : {nom_habitude}")
            self.habit_name_input.text = ""
            
            texte_a_afficher = "\n".join(self.liste)
            self.ids.liste_habitude.text = texte_a_afficher
            
        else:
            print("Le champ d'habitude est vide. Rien n'a été ajouté.")

class SettingsScreen(Screen):
    pass

class HabitTrackerManager(ScreenManager):
    pass

class StreakerApp(App):
    def build(self):
        return HabitTrackerManager()


if __name__ == "__main__":
    Streaker = StreakerApp()
    Streaker.run()