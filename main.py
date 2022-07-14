from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex


class Demo(FloatLayout):
    pass


class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")
        return Demo()


Main().run()
