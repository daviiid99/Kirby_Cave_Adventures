from resources import *

class Kirby :

	def __init__(self, running) :

		# Environment variables
		self.playing = running
		self.isPressed = False
		self.clock = clock

		# Kirby variables
		self.hp = 2

		# Define state variables
		self.running = False
		self.flying = False
		self.walking = False
		self.balloon = False

		# Define coordinates variables
		self.kirby_x = 50
		self.kirby_y = 470

		# Define Kirby speds
		self.walking_speed = 25
		self.running_speed = 30

		# Define kirby containers
		# Kirby containers are a way to determine and save npc values

		self.vel_container = 0

		# Define movement variables
		self.left = False
		self.right = False
		self.up = False
		self.down = False

		# Eating variables
		self.isEnemy = False
		self.isFood = False

		# Kirby animations
		self.kirby_left_animations = [kirby_default_left, kirby_left_right_foot, kirby_left_left_foot, kirby_left_all_foots]
		self.kirby_right_animations = [kirby_default_right, kirby_right_right_foot, kirby_right_left_foot, kirby_right_all_foots]
		self.kirby_exhale_flying_right_animations = [kirby_flying_4, kirby_flying_3, kirby_flying_2, kirby_flying_1]
		self.kirby_inhale_flying_right_animations = [kirby_flying_1, kirby_flying_2, kirby_flying_3, kirby_flying_4]
		self.kirby_flying_right_animations = [kirby_flying_5, kirby_flying_6, kirby_flying_7, kirby_flying_8, kirby_flying_9, kirby_flying_10]
		self.current_kirby_anim = kirby_default_right
		self.animation_counter = 0


	def kirby_bon_appetit(self) :
		# Kirby is able to eat objects or/and enemies from the stage
		return 0


	def verify_movement(self, movement, space) :

		# A function that checks the current kirby movement state and assigns a new state
		# This is useful since kirby is able to jump and move himself on both directions at the same time
		# We can restrict the movement to all possibilities

		# LEFT/RIGHT MOVEMENT
		if "right" in movement :
			self.right = True
			self.left = False 

		else :
			self.left = True
			self.right = False


		if "flying" in space :
			self.flying = True # We're flying
			self.walking = False

		else :
			self.walking = True # We're walking
			self.flying = False



	def kirby_coordinates(self) :
		# After verifying the movement, Kirby is ready to play

		if self.isPressed :

			# KIRBY X movement

			if self.walking :

				if self.left:
					if (self.kirby_x - self.walking_speed) > 0 :
						self.kirby_x -= self.walking_speed
						self.kirby_animations()
						
				else :
					if (self.kirby_x + self.walking_speed) < 1000 :
						self.kirby_x += self.walking_speed
						self.kirby_animations()
						

			# Kirby Y movement

			elif self.flying :

				if self.left :
					if (self.kirby_y - self.walking_speed) > 0 :
						self.kirby_y -= self.walking_speed
						self.kirby_animations()

					if (self.kirby_x - self.walking_speed) > 0 :
						self.kirby_x -= self.walking_speed
						self.kirby_animations()

				else :
					if (self.kirby_y - self.walking_speed) > 280 :
						self.kirby_y -= self.walking_speed
						self.kirby_animations()

					if (self.kirby_x + self.walking_speed) < 1000 :
						self.kirby_x += self.walking_speed
						self.kirby_animations()


	def kirby_animations(self) :
		# To assign an animation, we're using the last animation as reference

		if self.isPressed :

			if self.walking :

				if self.left :
					for animation in self.kirby_left_animations :
						if self.isPressed :
							current_anim = 0

							while current_anim < 10 :
								if self.isPressed :
									self.clock.tick(244)
									self.current_kirby_anim = animation
									current_anim +=1

						else :
							self.current_kirby_anim = self.kirby_left_animations[0]
						

				elif self.right :
					for animation in self.kirby_right_animations :
						if self.isPressed :
							current_anim = 0

							while current_anim < 10 :
								if self.isPressed :
									self.clock.tick(244)
									self.current_kirby_anim = animation
									current_anim +=1

						else :
							self.current_kirby_anim = self.kirby_right_animations[0]

			elif self.flying :

				if self.right : 
					if self.kirby_y >= 500 :
						for animation in self.kirby_inhale_flying_right_animations :
							if self.isPressed :
								current_anim = 0

								while current_anim < 10 :
									if self.isPressed :
										self.clock.tick(244)
										self.current_kirby_anim = animation
										current_anim +=1

					else :
						for animation in self.kirby_flying_right_animations :
							if self.isPressed :
								current_anim = 0

								while current_anim < 10 :
									if self.isPressed :
										self.clock.tick(244)
										self.current_kirby_anim = animation
										current_anim +=1

									else :
										for animation in self.kirby_flying_right_animations :
											current_anim = 0
											while self.kirby_y < 470 :
												while current_anim < 10 :
													self.kirby_y += 20
													self.clock.tick(20)
													self.current_kirby_anim = animation
													current_anim +=1

											if self.kirby_y >= 470 :
												for animation in self.kirby_exhale_flying_right_animations :
													current_anim = 0
													while self.kirby_y < 470 :
														while current_anim < 10 :
															self.kirby_y += 20
															self.clock.tick(20)
															self.current_kirby_anim = animation
															current_anim +=1
				
	def kirby_action(self) :
		while self.playing :
			for event in pygame.event.get() :

				keys = pygame.key.get_pressed()

				if event.type == pygame.KEYDOWN :


					if keys[pygame.K_LEFT] :
						self.verify_movement("left", "walking")

					if keys[pygame.K_LEFT] and keys[pygame.K_SPACE] :
						self.verify_movement("left", "flying")

					if keys[pygame.K_RIGHT]:
						if self.kirby_y >= 470 :
							self.verify_movement("right", "walking")

						else :
							self.verify_movement("right", "flying")


					if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] :
						self.verify_movement("right", "flying")


			# If we press a key, we need a real-time execution way to check if the button is being pressed or not
			# This loop is part ot the main stage thread, this means it will be executed all time

			keys = pygame.key.get_pressed()

			# Check all posibilities

			# RIGHT
			self.isPressed = keys[pygame.K_RIGHT]

			# LEFT
			if self.isPressed == False :
				self.isPressed = keys[pygame.K_LEFT]

			# Call the movement function
			self.kirby_coordinates()


 










