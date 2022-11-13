from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class beritaTerkini(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/beritaTerkini.kv')
        super().__init__(**kwargs)