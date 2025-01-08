from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)

        with self.canvas:
            Rectangle(source="",pos=(0, 0), size=(110, 100))

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    MyApp().run()
