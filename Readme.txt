#-------- Name --------#
Cat-nip

#-------- Description --------#
The Cat-nip is a text based adventure game of an indoor cat, or not...

#-------- Story --------#
You wake up in the bedroom. It is dark and you don't feel like sleeping anymore.
You go to the living room and play with your toy mouse Bob.
You hear noises in the dining room. 
Keep playing with Bob:
(If you select to keep playing 3 times in a row,) you will play with Bob forever.
Game over.
You go to investigate: 
As you enter the room, a giant Wortex of SpaceTime consumes you and you suddenly wake up in the bedroom.
You hide under the sofa in the living room:
You wait and wait and wait until the noises stop, but you already fell asleep and you wake up in the bedroom.

(After 5 rounds of choosing the same option or 3 rounds each of the two),
you wake up and realise that it was all just a dream.
So you get dressed and go to work... boring human.
Game over.

#-------- Structure --------#
Scene
	- enter
	* Bedroom
	* LivingRoom
		x play_bob
		x investigate
		x hide
	* DiningRoom
	* wakeup
	* EndGame

Engine
	- play

Map
	- next_scene
	- opening_scene
