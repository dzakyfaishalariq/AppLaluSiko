# kivy -> digunakan untuk membuat aplikasi dasktop
# kivymd -> digunakan untuk membuat aplikasi mobile
# import os
# from kaki.app import App
from kivymd.tools.hotreload.app import MDApp  # import relode app otomatis
from kivy.uix.screenmanager import ScreenManager
from screens.screen import *
from kivy.core.text import LabelBase
#import MDFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
# class inheriten from App


class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):
    dialog = None
    # CLASS = {
    #     'index': index,
    # }
    # AUTORELOADER_PATHS = [
    #     # (os.getcwd(), {'recursive': True}),
    #     (".", {"recursive": True}),
    # ]
    # KV_FILES = [
    #     # os.path.join(os.getcwd(), "kv", "index.kv"),
    #     'kv/index.kv',
    # ]

    def login_google(self):
        if not self.dialog:
            close_button = MDFlatButton(
                text="Close", on_release=self.close_dialog_google)
            self.dialog = MDDialog(
                title="Google Popap",
                text="Maaf google belum tersambung harap hubungi developer",
                size_hint=(0.8, 1),
                # membuat button tutup dialog dan fungsinya
                buttons=[close_button],
            )
        self.dialog.open()

    def close_dialog_google(self, obj):
        self.dialog.dismiss()

    def build_app(self):
        # mealukan exekusi di file index.kv
        self.wm = WindowManager()
        # Buat title aplikasi kanvas
        self.title = "LaluSiko"
        # router
        screens = [
            index(name='index'),
            login(name='login'),
            selamat(name='selamat'),
        ]
        for i in screens:
            self.wm.add_widget(i)
        return self.wm


if __name__ == '__main__':
    MyApp().run()
