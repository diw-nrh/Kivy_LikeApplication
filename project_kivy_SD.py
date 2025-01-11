from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout  
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # สร้างปุ่ม 10 ปุ่ม
        for i in range(0, 10):
            b = Button(
                text=str(i + 1),
                size_hint=(None, None),
                size=(dp(100), dp(100)))
            self.add_widget(b)

# class GridLayouExample(GridLayout):
#     pass

# class AnchorLayouExample(AnchorLayout):
#     pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = 'vertical'
    #     b1 = Button(text='A')
    #     b2 = Button(text='B')
    #     b3 = Button(text='C')
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget): 
    pass

class ThelapApp(App):
    def build(self):
        return StackLayoutExample()

if __name__ == '__main__':
    ThelapApp().run()