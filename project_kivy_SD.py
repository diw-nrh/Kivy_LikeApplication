from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty


class WidgetsExample(GridLayout):
    count = 1  # ตัวนับเริ่มต้น
    count_enabled = BooleanProperty(False)  # ตัวแปรสำหรับเปิด/ปิดปุ่ม Count
    my_test = StringProperty("1")  # เก็บค่าที่จะแสดงผลใน Label

    def on_button_click(self):
        # ฟังก์ชันเมื่อกดปุ่ม Count
        if self.count_enabled:
            self.count += 1
            self.my_test = str(self.count)

    def on_toggle_button_state(self, widget):
        # ฟังก์ชันเมื่อ ToggleButton เปลี่ยนสถานะ
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        # ฟังก์ชันเมื่อ Switch ถูกเปิด/ปิด
        print(f"Switch active: {widget.active}")

    def on_slider_value_change(self, widget):
        # ฟังก์ชันเมื่อค่า Slider เปลี่ยน
        print(f"Slider value: {widget.value}")


class ThelapApp(App):
    def build(self):
        return WidgetsExample()


if __name__ == '__main__':
    ThelapApp().run()

