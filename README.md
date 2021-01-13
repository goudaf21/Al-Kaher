# Al-Kaher
Al-Kaher Video game using PyGame
Al Kaher is a 4-level battle game where each level you (Al Kaher) face number of enemies with different abilities. Every level’s goal is to eliminate all enemies,
while dodging their bullets, your own bullets, and enemies’ collisions. Every bullet you shoot going to the right bounces off the wall and can hit you for double 
damage. The characters’ movements use drifting as movement technique, making it harder to control movement or dodge. The only way of dealing damage is by shooting
using the space bar. You can use one of two weapons: a pistol, shooting one bullet at a time, or a shotgun, shooting 3 bullets at a time with a longer cooldown. 
You can toggle between these weapons by pressing Z. Enemies in this game have two different difficulties, one that shoot bullets at you from a distance, and one 
that chases you and kills you on collision, forcing you to restart the level. Every level is significantly harder than the one before it, and each level has its 
unique background that reflects what I would like the scene to look like in the battle scenes. 
When choosing my backgrounds, I used big images, where the actual background only used a small part of the image, giving the player more imagination on what the 
setting is. 

At the beginning of my project at the time of proposing my game pitch, I proposed a platform game similar to Mario, that also runs on a story line. I also wanted
my game mechanics to rely on dodging and shooting to defeat enemies, which I was able to achieve in my game. My plans changed soon after, when I wanted my characters
to move in every direction in a 2 d world instead of jumping. I also wanted to focus more on the difficulty of the game, the different battle mechanisms, and making 
sure that it is challenging but not unfair. The levels of the game to me I think add a level of learning to the game as the player gets used to the difficulty and get
prepared for the level after.
The features I was able to achieve in my game are menus, music and sound effects, levels, enemy AI, movement and animations.
When coding my menus, I used different states from my screen manager, which dictate which menu displays to the screen, with each menu having its own options.
All Menus used were Cursor menus, to make the game controls with keyboard input only. I coded music and sound using pygame.mixer to play music for as long as the game
is running, which can be muted by pressing the N key. The game also implements some shooting sound effects that demonstrate the weapon used. 
When coding different levels, instead of using a level manager, I created a list of game managers that the screen manager can display, and update based on the level of 
the game we are on. Each level imports its enemy data and starting position to create Al Kaher, and all the enemies, from a text file that encodes all this information.
This makes it easier to add and edit levels. After winning each level by defeating all enemies in it, the level ends and the player gets a choice to either level up, 
restart level or exit game. 
For enemy AI, I implemented two different thinking techniques with the enemies. For enemy, it follows the main character’s Y position and shoots bullets at the player 
that damages his health bar. The main importance of this type of enemy is to be a ranged, relatively weaker enemy that you cannot ignore and has a lot of health points.
The other AI, is  a more advanced enemy that chases the main character and kills the player on collision. 
For movement and animations, I used basic animations for my characters, but implemented a drifting movement method that we used in class, which I thought made a game
more challenging and enjoyable.
One aspect of the game that I spent a lot of time working on is tuning the game to give it a good level of difficulty, which was one of my favorite parts coding and 
testing this game. 

