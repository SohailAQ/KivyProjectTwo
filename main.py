from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('Main.kv')

    def login(self):
        username = self.root.ids.username.text
        if username == 'sohail':
            self.root.ids.welcome_label.text = username

    def clear(self):
        self.root.ids.welcome_label.text = 'WELCOME'
        self.root.ids.username.text = ''
        self.root.ids.password.text = ''

MainApp().run()