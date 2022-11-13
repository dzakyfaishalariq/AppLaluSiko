from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class infoBencana(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/infoBencana.kv')
        super().__init__(**kwargs)