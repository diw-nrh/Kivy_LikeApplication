from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout  
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

class StackLayoutExample(StackLayout):
    def __init__(self, **kwarge):
        super().__init__(**kwarge)
        b = Button(text="Z",size_hint=(.2, .2))
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
    pass

if __name__ == '__main__':
    ThelapApp().run()