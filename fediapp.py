from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from login import (LoginPage, codeEntryPage)
from home import HomePage

class FediApp(MDApp):
    def on_start(self):
        super().on_start()
        self.root.dispatch('on_enter')

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        Builder.load_file('fedi.kv')
        sm = MDScreenManager()
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(codeEntryPage(name='code'))
        sm.current = 'login'

        return sm
    def disabled_widgets(self):
        ...

FediApp().run()