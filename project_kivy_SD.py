from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
import random

class WhackAMoleApp(App):
    def build(self):
        Builder.load_file("whackamole.kv")
        self.score = 0
        self.moles = []
        self.active_mole = None
        self.mole_speed = 1.0
        self.clock_event = None
        return self.root

if __name__ == "__main__":
    WhackAMoleApp().run()
