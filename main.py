from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class Funkybutton(Button):
	pass

		
class GameScreen(Widget):
	"""docstring for """
#	def __init__(self, arg):
#		super(GameScreen, self).__init__()
#		self.arg = arg
	pass		





class DrinkingGameApp(App):
	def build (self):
		return GameScreen()



if __name__ == '__main__':
 	DrinkingGameApp().run()
