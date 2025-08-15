from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# إعداد نافذة التطبيق
Window.size = (360, 640)  # حجم شبيه بشاشة الهاتف
Window.clearcolor = (0.95, 0.95, 0.95, 1)  # خلفية فاتحة مثل تطبيقات الهاتف

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = 10
        self.spacing = 10

        # شاشة العرض
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=48,
            size_hint=(1, 0.2),
            background_color=(0.9, 0.9, 0.9, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.add_widget(self.display)

        # أزرار الأرقام والعمليات
        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+']
        ]

        for row in buttons:
            h_layout = GridLayout(cols=4, size_hint_y=None, height=100, spacing=10)
            for label in row:
                # ألوان شبيهة بتطبيقات الهاتف
                if label in ['=', '+', '-', '*', '/']:
                    color = (0.2, 0.6, 0.86, 1)  # أزرار العمليات باللون الأزرق
                else:
                    color = (0.85, 0.85, 0.85, 1)  # أزرار الأرقام باللون الرمادي الفاتح

                button = Button(
                    text=label,
                    font_size=32,
                    background_color=color,
                    color=(0, 0, 0, 1)
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)

    def on_button_press(self, instance):
        text = instance.text
        if text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += text

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()