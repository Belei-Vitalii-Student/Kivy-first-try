from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.textinput import TextInput

class MainScreen(Screen):
    def __init__(self, name="main"):
        super().__init__(name=name)
        box = BoxLayout()
        first_btn = Button(text="First page")
        second_btn = Button(text="Second page")
        third_btn = Button(text="Third page")
        four_btn = Button(text="Four page")

        first_btn.on_press = self.change_screen_to_first
        second_btn.on_press = self.change_screen_to_second
        third_btn.on_press = self.change_screen_to_third
        four_btn.on_press = self.change_screen_to_four

        box.add_widget(first_btn)
        box.add_widget(second_btn)
        box.add_widget(third_btn)
        box.add_widget(four_btn)

        self.add_widget(box)
        
    def change_screen_to_first(self):
        self.manager.current = "first"
    def change_screen_to_second(self):
        self.manager.current = "second"
    def change_screen_to_third(self):
        self.manager.current = "third"
    def change_screen_to_four(self):
        self.manager.current = "four"

class FirstScreen(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        box = BoxLayout()
        button = Button(text="Go to main")
        button.on_press = self.go_main
        label = Label(text=f"This is {name} screen!")
        switch = Switch()

        box.add_widget(button)
        box.add_widget(label)
        box.add_widget(switch)

        self.add_widget(box)

    def go_main(self):
        self.manager.current = "main"

class SecondScreen(Screen):
    def __init__(self, name="second"):
        super().__init__(name=name)
        box = BoxLayout()
        button = Button(text="Go to main")
        button.on_press = self.go_main
        label = Label(text=f"This is {name} screen!")
        color_picker = ColorPicker()

        box.add_widget(button)
        box.add_widget(label)
        box.add_widget(color_picker)

        self.add_widget(box)

    def go_main(self):
        self.manager.current = "main"

class ThirdScreen(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)
        box = BoxLayout()
        button = Button(text="Go to main")
        button.on_press = self.go_main
        label = Label(text=f"This is {name} screen!")
        text_input = TextInput()

        box.add_widget(button)
        box.add_widget(label)
        box.add_widget(text_input)

        self.add_widget(box)

    def go_main(self):
        self.manager.current = "main"

class FourScreen(Screen):
    def __init__(self, name="four"):
        super().__init__(name=name)
        box = BoxLayout()
        button = Button(text="Go to main")
        button.on_press = self.go_main
        label = Label(text=f"This is {name} screen!")
        spinner = Spinner()

        box.add_widget(button)
        box.add_widget(label)
        box.add_widget(spinner)

        self.add_widget(box)
    def go_main(self):
        self.manager.current = "main"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FourScreen())

        return sm

MyApp().run()