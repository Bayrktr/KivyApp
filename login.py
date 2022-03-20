from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class loginPart(GridLayout):
    def __init__(self, **kwargs):
        super(loginPart, self).__init__(**kwargs)
        self.cols = 2  # ekrani iyiye boler
        self.user = Label(text="User Name:")
        self.add_widget(self.user)
        self.userInput = TextInput(multiline=False)
        self.add_widget(self.userInput)
        self.password = Label(text="Password:")
        self.add_widget(self.password)
        self.passwordInput = TextInput(multiline=False, password=True)
        self.add_widget(self.passwordInput)


class app(App):
    def build(self):
        return loginPart()


if __name__ == "__main__":
    app().run()
