from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.button import Button
import random

Builder.load_file("LoginPage.kv")

class LoginPageApp(App):
    def build(self):
        return LoginManager()

class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class LoginManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answerquestion(self, bool):
        if(bool):
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

users = {"Bobby": "Hill"}
numbers = "1234567890"
specials = "~`!@#$%^&*()-_=+|][}{':;/?.>,<"
colors = [[1, 0.5, 0.5, 1.0], [1, 1, 0.5, 1.0], [0.5, 1, 0.5, 1.0], [0.5, 1, 1, 1.0], [0.5, 0.5, 1, 1.0], [1, 0.5, 1, 1.0]]

class MainScreen(Screen):
    def register(self):
        self.manager.current = "register"
    def login(self, username, password):
        if(username in users):
            if(users[username] == password):
                self.ids.issue.text = ""
                self.manager.current = "silly"
            else:
                self.ids.issue.text = "Incorrect password"
        else:
            self.ids.issue.text = "Username '"+username+"' does not exist"

class RegisterScreen(Screen):
    def register(self, user, pass1, pass2):
        unique = False
        capital = False
        lowercase = False
        number = False
        character = False
        eight = False
        spaceless = False
        match = False
        if(not user in users):
            unique = True
            self.ids.unique.text = ""
        else:
            self.ids.unique.text = "Username '"+user+"' already taken"
        if(pass1.lower() != pass1):
            capital = True
            self.ids.capital.color = (0.5, 0.5, 0.5)
        else:
            self.ids.capital.color = (1, 0.5, 0.5)
        if (pass1.upper() != pass1):
            lowercase = True
            self.ids.lowercase.color = (0.5, 0.5, 0.5)
        else:
            self.ids.lowercase.color = (1, 0.5, 0.5)
        for num in numbers:
            if(num in pass1):
                number = True
                self.ids.number.color = (0.5, 0.5, 0.5)
        if(not number):
            self.ids.number.color = (1, 0.5, 0.5)
        for special in specials:
            if(special in pass1):
                character = True
                self.ids.character.color = (0.5, 0.5, 0.5)
        if(not character):
            self.ids.character.color = (1, 0.5, 0.5)
        if(len(pass1) >= 8):
            eight = True
            self.ids.eight.color = (0.5, 0.5, 0.5)
        else:
            self.ids.eight.color = (1, 0.5, 0.5)
        if(not " " in pass1):
            spaceless = True
            self.ids.spaceless.color = (0.5, 0.5, 0.5)
        else:
            self.ids.spaceless.color = (1, 0.5, 0.5)
        if(pass1 == pass2):
            match = True
            self.ids.match.color = (0.5, 0.5, 0.5)
        else:
            self.ids.match.color = (1, 0.5, 0.5)
        if(unique and capital and lowercase and number and character and eight and spaceless and match):
            users[user] = pass1
            self.manager.current = "main"

class SillyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        silliness = Button(text="Silly Button", pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint=(0.15, 0.15), color=[1, 0.5, 0.5, 1.0], background_color=[1, 0.5, 0.5, 1.0])
        self.add_widget(silliness)
    def logout(self):
        self.manager.current = "main"
    def silly(self):
        self.ids.sillybutton.pos_hint = {"center_x": random.uniform(0.2, 0.8), "center_y": random.uniform(0.2, 0.8)}
        self.ids.sillybutton.color = colors[(colors.index(self.ids.sillybutton.color)+1)%6]
        self.ids.sillybutton.background_color = colors[(colors.index(self.ids.sillybutton.background_color)+1)%6]

class Question2Screen(Screen):
    def answerquestion(self, text):
        if(text.lower() == "deep in the heart of texas"):
            self.manager.current = "correct"
        else:
            self.ids.invalid.text = "Wrong.  Try again."

class CorrectScreen(Screen):
    def press(self):
        self.manager.current = "question2"

class ErrorScreen(Screen):
    def press(self):
        self.manager.current = "question2"

LoginPageApp().run()