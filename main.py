from kivy.app import App
from kivy.uix.button import Button


class LanguageLearnerApp(App):
    def build(self):
        return Button(
            text='Hello World',
            pos=(50, 50),
            size=(100, 100),
            size_hint=(None,None)
        )


if __name__ == '__main__':
    LanguageLearnerApp().run()