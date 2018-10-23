"""Relied heavily on dynamic_widgets example."""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class NameLabellerApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        self.title = "Name Labeller"
        self.root = Builder.load_file('name_label.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name, id=name)
            # temp_button.bind(on_release=self.press_entry)
            self.root.ids.name_label_boxes.add_widget(temp_button)

    # def press_entry(self, instance):
    #     self.status_text = "Names are: {}".format(self.names)
    #
    # def clear_all(self):
    #     self.root.ids.name_label_boxes.clear_widgets()


NameLabellerApp().run()
