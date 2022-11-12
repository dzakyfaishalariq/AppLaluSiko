from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class login(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/login.kv')
        super().__init__(**kwargs)