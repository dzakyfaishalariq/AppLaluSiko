from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class index(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/index.kv')
        super().__init__(**kwargs)
