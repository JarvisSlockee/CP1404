from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometresConverter(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Convert Miles To Kilometres"
        self.root = Builder.load_file('miles_to_kilometres_converter.kv')
        return self.root

    def handle_calculate(self, miles_input):
        result = miles_input * 1.609
        self.root.ids.output_label.text = str(result)


MilesToKilometresConverter().run()
