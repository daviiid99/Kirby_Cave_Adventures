from resources import *
from kirby import *

class Stage :

	def __init__(self) :
		self.screen = WIN
		self.running = True
		self.kirby = Kirby(self.running)
		self.theme = pygame.mixer.Sound("assets/sounds/theme.ogg")
		self.roof = pygame.Rect(0, 0, 1000, 280)
		self.floor = pygame.Rect(0, 550, 1000, 120)

	def draw_stage(self) :

		while self.running : 

			# Draw stage
			self.screen.blit(cave, (0,0))

			# Kirby
			self.screen.blit(self.kirby.current_kirby_anim, (self.kirby.kirby_x, self.kirby.kirby_y))

			# Rectangles
			# Only enable to watch the rectangles position on display
			#pygame.draw.rect(WIN, WHITE, self.roof) 
			#pygame.draw.rect(WIN, WHITE, self.floor) 

			pygame.display.update()


	def start(self) :
		# Create threads
		thread_1 = threading.Thread(target=self.draw_stage, name="ui")
		thread_2 = threading.Thread(target=self.kirby.kirby_action, name="npc")
		self.theme.play()

		# Start threads
		thread_1.start()
		thread_2.start()

		# Avoid freeze
		movement = self.kirby.kirby_action()

		# Wait for all threads to end
		while self.running :
			thread_1.join()
			thread_2.join()
