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

    def on_start(self):

        self.moles = [
            self.root.ids.mole_0,
            self.root.ids.mole_1,
            self.root.ids.mole_2,
            self.root.ids.mole_3,
            self.root.ids.mole_4,
            self.root.ids.mole_5,
            self.root.ids.mole_6,
            self.root.ids.mole_7,
            self.root.ids.mole_8,
            self.root.ids.mole_9,
            self.root.ids.mole_10,
            self.root.ids.mole_11,
            self.root.ids.mole_12,
            self.root.ids.mole_13,
            self.root.ids.mole_14,
            self.root.ids.mole_15,
            self.root.ids.mole_16,
            self.root.ids.mole_17,
            self.root.ids.mole_18,
            self.root.ids.mole_19,
            self.root.ids.mole_20,
            self.root.ids.mole_21,
            self.root.ids.mole_22,
            self.root.ids.mole_23,
            self.root.ids.mole_24,
            self.root.ids.mole_25,
            self.root.ids.mole_26,
            self.root.ids.mole_27,
            self.root.ids.mole_28,
            self.root.ids.mole_29,
        ]

        for mole in self.moles:
            mole.bind(on_press=self.hit_mole)

if __name__ == "__main__":
    WhackAMoleApp().run()
