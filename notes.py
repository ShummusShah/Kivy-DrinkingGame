#Button
#		return Button(
#			text='Hello World',
#			pos=(50,50),
#			size=(500,500),
#			size_hint=(None,None))

#Size hint starts at 1,1 naturally, which is 100% of the page, better to use this than put a static size as above as this will not change with screens size




#This is a class for buttons

#class Funkybutton(Button):
#	def __init__(self,**kwargs):
#		super(Funkybutton, self).__init__(**kwargs)
#		self.text = "Funky Button"
#		self.pos = (100,100)
#		self.size_hint = (0.3,0.3)
		
#class DrinkingGameApp(App):
#	def build (self):
#		return Funkybutton()




#for kv file

#<funkyButton>:
#	canvas:
#		Rectangle:
#			pos: self.x + 50, self.y + 50
#			size: 100,100






#For kv file, 2 floating buttons to customise
#<GameScreen>:
#	
#	FloatLayout:
#		pos: 0,0
#		size: root.width, root.height
#
#		Button:
#			text: 'Button 1'
#			pos_hint: {'x': 0.1, 'y': 0.1 }
#			size_hint: 0.8 , 0.1		
#
#
#		Button:
#			text: 'Button 2'
#			pos_hint: {'x': 0.1 , 'y': 0.6 }
#			size_hint: 0.8 , 0.1
