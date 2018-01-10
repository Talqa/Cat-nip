from sys import exit
#from random import randint

class Scene(object):
	
	def enter(self):
		print "Not implemented..."
		exit(1)
	
	#FIX IT!
	#def answer_check(self, choice):
		# if choice == "1" or choice == "2" or choice == "3":
			# return choice
		# else:
			# print "I didn't understand. Can you repeat your choice?"
			# try:
				# choice = int(raw_input("Type number 1, 2 or 3: "))
			# except ValueError:
				# print "I do not recognise this as number 1, 2 or 3."


class Bedroom(Scene):
	
	def enter(self):
		print "\n\n\tHello little cat!\n"
		print "What is your name?\n"
		name = raw_input("> ")
		print "\nNice to meet you %s!\n" % name
		
		print "\t   ^-^"
		print "\t =(o.o)="
		print "\t  (  _  )--'"
		print "\t   !! !!"
		
		print "\n\nThis is your story %s!" % name
		print "\n-------------\n"
		print "You wake up in the bedroom."
		print "It is dark and you don't feel like sleeping anymore."
		print "You go to the living room and play with your toy mouse Bob."
		return 'living_room'

		
class LivingRoom(Scene):
	
	def enter(self):
		print "\n\t<:3 ) ~~~~~~~~~~\n"
		print "\n\n...\n\n"
		print "What is it?\n\n"
		print "You hear noises in the dining room."
		print "\n\n...\n\n"
		print "What do you do?\n"
		
		#def choices(self):
		print "1) I'll just keep playing with Bob and pretend I didn't hear that."
		print "2) I'm a very curious cat and go to investigate!"
		print "3) Aaaaa, that's scary! I'll hide under the sofa :("
		print "\n"
		
		choice = int(raw_input("Type number 1, 2 or 3: "))
		#self.answer_check(choice)
		#choice1_count = 0
		#choice2_count = 0
		#choice3_count = 0
		while True:		
			if choice == 1:
				#choice1_count += 1
				#while choice1_count < 4:
					#print "You keep playing with Bob, ignoring noises coming from dining room."
					#print "\n@-------------@\n"
					#print "\n\n...\n\n"
					#print "You feel a bit nervous about those noises. What do you do?"
					#self.choices()
					#new_choice = int(raw_input("Type number 1, 2 or 3: "))
					#if new_choice == 1:
					#	choice1_count += 1
					#else:
				print "\n\n"
				print "You are having so much fun playing with Bob!"
				print "\n\tWeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\n"
				print "You are extatic! Best thing in the world!"
				print "\n\n...\n\n"
				return 'endgame1'
			elif choice == 2:
				print "\n\n"
				print "You can't stop your curiosity and decide to enter the dining room."
				print "Brave kitty!"
				return 'dining_room'
			elif choice == 3:
				print "\n\n"
				print "Sooo scary! You quickly hide under the sofa, leaving Bob behind."
				print "You wait and wait and wait until the noises stop."
				print "\n\n...\n\n"
				print "But you already fell asleep."
				print "\n\n...\n\n"
				return 'wakeup'
			else:
				print "Did you choose 1, 2, or 3? I didn't understand."
				raw_input("Type number 1, 2 or 3: ")

		
class DiningRoom(Scene):
	
	def enter(self):
		print "As you slowly enter..."
		print "\n\n...\n\n"
		print "a giant Wortex of SpaceTime consumes you."
		return 'wakeup'
		
		
class Wakeup(Scene):
	
	def enter(self):
		print "\n\n"
		print "What an adventure!\n"
		print "You wake up in the bedroom."
		print "It is dark and you don't feel like sleeping anymore."
		print "You go to the living room and play with your toy mouse Bob."
		print "You have a strange feeling that this happened before..."
		return 'living_room'
		
class EndGame1(Scene):

	def enter(self):
		print "You wake up and realise that it was all just a dream."
		print "So you get dressed and go to work... boring human."
		print "\n\n...\n\n"
		print "\t----Game over----\n"

class EndGame2(Scene):

	def enter(self):
		print "You wake up very tired and realise that it was all just a dream."
		print "So you get dressed and go to work... boring tired human."
		print "\n\n...\n\n"
		print "\t----Game over----\n" 
		
class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('endgame1')
		
		bed_count = 0
		din_count = 0

		while current_scene != last_scene and din_count < 4:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
			if current_scene == 'bedroom':
				bed_count += 1
			elif current_scene == 'dining_room':
				din_count += 1	
			
		#make sure to print out the last scene
		current_scene.enter()
		return 'endgame2'
		
class Map(object):
	
	scenes = {
		'bedroom': Bedroom(),
		'living_room': LivingRoom(),
		'dining_room': DiningRoom(),
		'wakeup': Wakeup(),
		'endgame1': EndGame1(),
		'endgame2': EndGame2()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		

a_map = Map('bedroom')
a_game = Engine(a_map)
a_game.play()

