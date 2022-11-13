from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class infoCuaca(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/infoCuaca.kv')
        super().__init__(**kwargs)