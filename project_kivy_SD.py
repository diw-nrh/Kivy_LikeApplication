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
        self.mole_speed = 1.2
        self.clock_event = None
        self.boom_event = 0.3
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

    def hit_mole(self, instance):
        if instance == self.active_mole and instance.text != "!":
            self.score += 1
            self.root.ids.score_label.text = f"Score: {self.score}"
            self.hide_mole(instance)
            self.increase_speed()

    def hit_bomb_mole(self, instance):
        if instance == self.active_mole and instance.text == "!":
            self.score -= 1
            self.root.ids.score_label.text = f"Score: {self.score}"
            self.hide_mole(instance)

    def start_game(self):
        self.root.ids.start_button.opacity = 0
        self.root.ids.start_button.disabled = True
        self.clock_event = Clock.schedule_interval(self.show_random_mole, self.mole_speed)

    def increase_speed(self):
        self.mole_speed = max(0.3, self.mole_speed - 0.01)
        if self.clock_event:
            self.clock_event.cancel()
            self.clock_event = Clock.schedule_interval(self.show_random_mole, self.mole_speed)

    def show_random_mole(self, dt):
        if self.active_mole:
            self.hide_mole(self.active_mole)

        mole = random.choice(self.moles)
        if random.random() < self.boom_event:
            self.show_bomb_mole(mole)
        else:
            self.show_mole(mole)

    def show_mole(self, mole):
        mole.opacity = 1
        mole.text = ""
        mole.background_normal = "image_file/Mole.png"
        mole.background_down = "image_file/Mole_pressed.png"
        self.active_mole = mole
        mole.unbind(on_press=self.hit_bomb_mole)
        mole.bind(on_press=self.hit_mole)

    def show_bomb_mole(self, mole):
        mole.opacity = 1
        mole.text = "!"
        mole.background_normal = "image_file\BOMB.png"  # แสดงภาพ Bomb
        mole.background_down = "image_file\BOMB.png"  # แสดงภาพเมื่อกด
        self.active_mole = mole
        mole.unbind(on_press=self.hit_mole)
        mole.bind(on_press=self.hit_bomb_mole)

    def hide_mole(self, mole):
        mole.opacity = 0
        mole.text = ""
        mole.background_color = [1, 1, 1, 1]
        self.active_mole = None
        mole.unbind(on_press=self.hit_mole)
        mole.unbind(on_press=self.hit_bomb_mole)

    def reset_game(self):
        self.score = 0 
        self.mole_speed = 1.2
        self.boom_event = 0.3
        self.root.ids.score_label.text = f"Score: {self.score}"
        
    def upbomb_button(self):
        self.boom_event += 0.01

    def downbomb_button(self):
        self.boom_event -= 0.01    

    def leave_game(self):
        print("leave game")
        App.get_running_app().stop()
        exit()

if __name__ == "__main__":
    WhackAMoleApp().run()