import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class agrid(GridLayout):
    def __init__  (self,**kwargs):
        super (agrid,self).__init__()
        self.cols=2
        self.add_widget(Label(text="Name:"))
        self.aname= TextInput()
        self.add_widget(self.aname)

        self.add_widget(Label(text="marks:"))
        self.amarks = TextInput()
        self.add_widget(self.amarks)

        self.add_widget(Label(text="roll:"))
        self.aroll = TextInput()
        self.add_widget(self.aroll)

        self.press = Button(text="Click me")
        self.press.bind(on_press= self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        print("Name is" + self.aname.text)
        print("marks" + self.amarks.text)
        print("roll "+ self.aroll.text)

class ApexaApp(App):
    def build(self):
        return agrid() 

if __name__=="__main__":
    ApexaApp().run()