from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class jadwalHarian(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/jadwalHarian.kv')
        super().__init__(**kwargs)