class Room:
    name = ""   #data members
    
    def __init__(self,name,walls):   #constructor
        self.name = name
        self.floors = 1
        self.walls = walls
        self.door = 1

    def open_door(self):   #member functions
        print("door has been opened for ",self.name)

    def see_walls(self):
        print("the ",self.name," has ",self.walls," walls")

bedroom = Room("bed-room",4)
bedroom.open_door()
bedroom.see_walls()

drawingroom = Room("drawing-room",5)
drawingroom.open_door()
drawingroom.see_walls()

kitchen = Room("kitchen",5)
kitchen.open_door()
kitchen.see_walls()