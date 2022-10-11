from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def get_user(self):
        print(self.ids.user.text)