from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


class infoBantuan(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file('kv/infoBantuan.kv')
        super().__init__(**kwargs)
