from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class WidgetsExample(GridLayout):
    count = 1
    coont_enabled = False
    my_test = StringProperty("1")

    def on_button_click(self):
        print("Button clicked")
        if self.coont_enabled :
            self.count += 1
            self.my_test = str(self.count)

    def on_toggle_button_state(self, widget):
        print("toggle state : " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.coont_enabled = False
        else:
            widget.text = "ON"
            self.coont_enabled = True

class ThelapApp(App):
    def build(self):
        return WidgetsExample()

if __name__ == '__main__':
    ThelapApp().run()
