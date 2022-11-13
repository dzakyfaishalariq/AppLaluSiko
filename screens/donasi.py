from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class donasi(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/donasi.kv')
        super().__init__(**kwargs)
