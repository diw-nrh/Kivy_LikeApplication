from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)  # Corrected here

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print("Key Down has been pressed")

        with self.canvas:
            Rectangle(source="D:\code_vs_stady\PYTHON_TEST_STUDY\Application_study\LAP_KIVY\LAP_kv_4\download.jpg", pos=(0, 0), size=(110, 100))

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    MyApp().run()