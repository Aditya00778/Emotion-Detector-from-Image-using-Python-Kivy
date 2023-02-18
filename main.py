from deepface import DeepFace
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window

Window.clearcolor= (0,0,0,1)


hello= '''

Manager:
	Screen1:
	Screen2:
	Screen3:
		
<Screen1>:
    name:"scr1"
    BoxLayout:
    	orientation:"vertical"
        Label:
    	    text:"Emotion Detector"
    	    color:"red"
    	    bold:True
    	    italic:True
    	    pos_hint:{"center_x":0.5}
    	    font_size:"32sp"
    	Image:
    		source:"emotionlogo.png"
    		allow_stretch:True
    	Label:
    		text:"Made with Python Kivy"
    		color:"yellow"
    		underline:True
    		font_size:"20sp"
    		pos_hint:{"center_x":0.5}
    	Button:
    	    text:"---->"
    	    font_size:"32sp"
    	    color:"red"
    	    size_hint:(0.4,0.3)
    	    pos_hint:{"center_x":0.5}
    	    on_release:
    	    	app.root.current="scr2"
    	    
		
<Screen2>:
	name:"scr2"
	id:s2
	BoxLayout:
		orientation: "vertical"
		Image:
			id:img
			source:""
		FileChooserIconView:
			id:choose
			on_selection:
				s2.selected(choose.selection)
		Button:
			text:"---->"
			font_size:"32sp"
    	    color:"red"
    	    size_hint:(0.4,0.3)
    	    pos_hint:{"center_x":0.5}
			on_release:
				app.root.current="scr3"
		Button:
			text:"<----"
			font_size:"32sp"
    	    color:"red"
    	    size_hint:(0.4,0.3)
    	    pos_hint:{"center_x":0.5}
			on_release:
				app.root.current="scr1"
			

<Screen3>:
    name:"scr3"
    BoxLayout:
    	orientation:"vertical"
    	Image:
    		id:img1
    		source:""
    		allow_stretch:True
    		
    	Button:
    		id:btn1
    		text:"Load Image"
    		font_size:"20sp"
    	    color:"red"
    	    size_hint:(0.4,0.3)
    	    pos_hint:{"center_x":0.5}
    		on_release:
    			app.func1(img1,btn2)
    		
    	Label:
    	    id:res
    		text:""
    		color:"red"
    	    bold:True
    	    italic:True
    	    pos_hint:{"center_x":0.5}
    	    font_size:"32sp"
    		
    	Button:
    		id:btn2
    		text:"Detect Emotion"
    		disabled:True
    		font_size:"20sp"
    	    color:"red"
    	    size_hint:(0.4,0.3)
    	    pos_hint:{"center_x":0.5}
    	    on_release:
    	        app.func2(btn2,img1,res)
    	Button:
    		text:"<----"
    		font_size:"20sp"
    		color:"red"
    		size_hint:(0.4,0.3)
    		pos_hint:{"center_x":0.5}
    		on_release:
    			app.root.current="scr2"


'''

class Screen1(Screen):
	pass
	
	
class Screen2(Screen):
	def selected(self,filename):
		try:
			global a
			a=filename[0]
			self.ids.img.source=a
			
		except:
			pass
	
class Screen3(Screen):
	pass
	
	
	
class Manager(ScreenManager):
	pass


class ImageviewApp(App):
	def build(self):
		bldr= Builder.load_string(hello)
		return bldr
		
	def func1(self,img1,btn2):
		try:
		    img1.source=a
		    btn2.disabled=False
		except:
			pass

	def func2(self,btn2,img1,res):
		try:
		    img=cv2.imread(a)
		    result= DeepFace.analyze(img, actions = ["emotion"])
		    y = result[0]['dominant_emotion']
		    l=y.capitalize()
		    res.text=l
		except:
			res.text="Face Not Clear"

		
		
		
ImageviewApp().run()