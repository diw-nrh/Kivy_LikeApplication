from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_test = StringProperty("1")

    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled :
            self.count += 1
            self.my_test = str(self.count)

    def on_toggle_button_state(self, widget):
        print("toggle state : " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self):

class ThelapApp(App):
    def build(self):
        return WidgetsExample()

if __name__ == '__main__':
    ThelapApp().run()
