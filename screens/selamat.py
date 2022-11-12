from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class selamat(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/selamat.kv')
        super().__init__(**kwargs)
