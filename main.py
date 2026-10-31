from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from ai_brain import SuperAI

class SuperAIApp(App):
    def build(self):
        self.ai = SuperAI()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="SUPER AI READY\nBol kya karna hai?", font_size=20)
        self.input = TextInput(hint_text="Yaha likh...", size_hint_y=0.2)
        self.btn = Button(text="BHEJ", size_hint_y=0.2, background_color=(0,1,0.7,1))
        self.btn.bind(on_press=self.ask)
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(self.btn)
        return layout

    def ask(self, x):
        ans = self.ai.chat(self.input.text)
        self.label.text = ans

SuperAIApp().run()