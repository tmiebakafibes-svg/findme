from kivy.app import App
from kivy.uix.label import Label
class MyLock(App):
 def build(self):
  return Label(text="MY LOCK - PIN 1234")
MyLock().run()
