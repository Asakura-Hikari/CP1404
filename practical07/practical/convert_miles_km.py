from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        result = self.get_value() + value
        self.root.ids.input_miles.text = str(result)

    def convert(self):
        result = self.get_value() * MILES_TO_KM
#        result = round(result, 2)
        self.root.ids.output_label.text = str(result)

    def handle_press(self):
        self.message = self.root.ids.input_miles.text

    def get_value(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


if __name__ == '__main__':
    ConvertMilesKmApp().run()
