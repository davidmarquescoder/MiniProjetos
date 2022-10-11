from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def get_user(self):
        definicao_user = 'janne010'
        definicao_pass = 'janne.1022'
        validacao_user = self.ids.user.text
        validacao_pass = self.ids.password.text
        if definicao_user == validacao_user and definicao_pass == validacao_pass:
            print('logado')
        else:
            print('Senha ou login incorreto')