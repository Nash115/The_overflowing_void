# Index of all rooms

## **Room n°1 :** *The maze*
A simple maze, go to the exit to finish the room.

## **Room n°2 :** *The inverted maze*
A maze but... "inverted". Walls and ground textures are not trustworthy ! The left of the maze is the right, and the right is the left. The exit is on the right but you need to follow the maze with a different point of view...

## **Room n°3 :** *The invisible maze*
Does a maze have to reveal its walls? This one doesn't. You have to find your way through the maze without seeing the walls. You can only see the exit.

## **Room n°4 :** *The invisible maze 2*
Wait... Are the walls real?

# Rooms files architecture :
- "lvX.json" : Room X data
    - "spawn" : Spawn position
    - "win" : Win position
    - "plate" : Level's plate
    - "collisions" : Level's collisions (null if collisions are sames as plate)

# TODO :
- Add the "tunnel"
- Add the "teleporter"