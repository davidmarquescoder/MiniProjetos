"""
This is an example of kaki app usin kivymd modules.
"""
import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "Screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "Screens/login_screen/loginscreen.kv"),
        os.path.join(os.getcwd(), "Screens/login_screen/temascreen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "Screens.screenmanager",
        "LoginScreen": "Screens.login_screen.loginscreen",
        "TemaScreen": "Screens.login_screen.temascreen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        Window.size = (380,620)
        self.theme_cls.primary_palette = 'Green'

        return Factory.MainScreenManager()
    
    def tema_dark(self):
        self.theme_cls.theme_style = 'Dark'
    def tema_light(self):
        self.theme_cls.theme_style = 'Light'
    def tema_outro(self):
        self.theme_cls.primary_palette = 'Red'
    def get_user(self):
        print(self.root.ids.user.text)



# finally, run the app
if __name__ == "__main__":
    LiveApp().run()