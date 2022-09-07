from resources import *
from stage import *

class Main :

	def __init__(self) :
		self.screen = WIN
		self.screen_rect = self.screen.get_rect()
		self.waiting_to_start = True
		self.clock = clock


	def mouse(self) :
		while self.waiting_to_start :

			for event in pygame.event.get() :

				# If user click the mouse
				if event.type == pygame.MOUSEBUTTONDOWN :
					if self.screen_rect.collidepoint(event.pos) :
						self.waiting_to_start = False
						stage = Stage()
						stage.start()


	def draw_title_screen(self) :

		logo_width = 800
		logo_height = 396
		x = 100
		y = 420

		while self.waiting_to_start :
			for anim in range(1, 60) :

				if self.waiting_to_start : # Check all time if game started

					if logo_width < 900 :
						logo_width += 50
						logo_height += 25
						x -= 20

					else :
						logo_width = 800
						logo_height = 396
						x = 100


					# Infinite loop
					if anim == 60 :
						anim = 1

					# Draw on display
					self.draw(logo_width, logo_height,x , y)
					self.clock.tick(1)



	def draw(self, logo_width, logo_height, x, y) :

		# Background
		self.screen.blit(cave, (0,0))

		# Logo
		self.screen.blit(pygame.transform.scale(logo, (600, 250)), (200, 30))

		# Kirby
		self.screen.blit(kirby_default_right, (50, 470))

		# Press to start
		self.screen.blit(pygame.transform.scale(press, (logo_width, logo_height)), (x, y))

		pygame.display.update()



	def start_game(self) :

		# Create main screen threads
		# This class will introduce the plyer into the gameplay


		thread_1 = threading.Thread(target= self.draw_title_screen, name="ui") # Display
		thread_2 = threading.Thread(target = self.mouse, name="mouse") # mouse

		# Start the threads
		thread_1.start()
		thread_2.start()

		# Fix possible UI freeze
		self.mouse()

		# Wait for all threads to end
		while self.waiting_to_start :
			thread_1.join()
			thread_2.join()

main = Main()
main.start_game()