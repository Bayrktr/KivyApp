from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file("loginKivy.kv")


class login(GridLayout):
    pass

class app(App):
    def build(self):
        return login()


if __name__ == "__main__":
    app().run()
