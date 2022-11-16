from kivy.uix.widget import Widget
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import kivysysfile
from kivy.lang import Builder
from kivy.properties import Property
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import subprocess

#Define our different screens

class BoxLa(Screen):
    pass
class choosefileWindows(Screen):
   def select(self, *args):
        try:
            self.label.text = args[1][0]
            print (self.label.text)
            remplace=self.label.text.replace("\\", "\\\\")
            #print (f"bonjou{remplace}")
            subprocess.Popen(f"python object_tracker.py --video {remplace} --output .\\outputs\\video1.mp4 --model yolov4 --dont_show --info",stdin=subprocess.PIPE, shell=True )

        except: pass
#    def video_path(self, *args):
#         try: 
#             self.label.text = args[1][0]
#             p = subprocess.Popen("python object_tracker.py --video {self.label.txt} --output .\\outputs\\video1.mp4 --model yolov4 --dont_show --info",stdin=subprocess.PIPE, shell=True )
#         except: pass
class WindowManager(ScreenManager):
    pass

# red = [1, 0, 0, 1]
# green = [0, 1, 0, 1]
# blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

# class in which we are creating the button by using boxlayout
# defining the App class
kv = Builder.load_file('AwesomeBoxLayoutApp.kv')


class AwesomeBoxLayoutAp(App):
    
    def build(self):
        Window.clearcolor = (1,0,1,1)
        return kv
    
if __name__ == '__main__':
    AwesomeBoxLayoutAp().run()  
