from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class infoOrangIlang(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/infoOrangIlang.kv')
        super().__init__(**kwargs)