from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_label.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_press=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.name_to_phone[name])
        self.root.ids.phone_number.text = self.status_text

    def clear_all(self):
        """"""
        self.root.ids.places_list.clear_widgets()


if __name__ == '__main__':
    DynamicLabelsApp().run()
