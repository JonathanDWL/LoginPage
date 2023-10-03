from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App

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

class MainScreen(Screen):
    pass

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