import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


kivy.require('2.0.0')

class GameView(BoxLayout):
    def __init___(self):
        super(GameView, self).__init__()

class StreakerApp(App):
    def build(self):
        return GameView()

Streaker = StreakerApp()
Streaker.run()