from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class WidgetsExample(GridLayout):
    count = 1
    my_test = StringProperty("Hello")

    def on_button_click(self):
        print("Button clicked")
        self.count += 1
        self.my_test = str(self.count)

class ThelapApp(App):
    def build(self):
        return WidgetsExample()

if __name__ == '__main__':
    ThelapApp().run()
