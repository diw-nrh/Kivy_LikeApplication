from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ตั้งค่าคีย์บอร์ด
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()

        # ตั้งเวลาอัปเดตการเคลื่อนไหว
        Clock.schedule_interval(self.move_step, 0.016)  # อัปเดตที่ประมาณ 60 FPS

        # วาดตัวละคร
        with self.canvas:
            self.hero = Rectangle(source='D:\code_vs_stady\PYTHON_TEST_STUDY\Application_study\LAP_KIVY\LAP_kv_4\download.jpg', pos=(0, 0), size=(100, 100))

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print('down', text)
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        print('up', text)
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def move_step(self, dt):
        cur_x, cur_y = self.hero.pos
        step = 200 * dt  # ความเร็วเคลื่อนไหว

        # ตรวจสอบปุ่มที่กด
        if 'w' in self.pressed_keys:
            cur_y += step
        if 's' in self.pressed_keys:
            cur_y -= step
        if 'a' in self.pressed_keys:
            cur_x -= step
        if 'd' in self.pressed_keys:
            cur_x += step

        # ตรวจสอบขอบหน้าต่าง
        cur_x = max(0, min(Window.width - self.hero.size[0], cur_x))
        cur_y = max(0, min(Window.height - self.hero.size[1], cur_y))

        self.hero.pos = (cur_x, cur_y)

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    app = MyApp()
    app.run()
