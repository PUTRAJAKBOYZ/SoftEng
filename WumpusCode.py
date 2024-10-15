import random

class Cave:
    def __init__(self):
        self.rooms = {0: "You are in room 0",
                      1: "You are in room 1",
                      2: "You are in room 2",
                      3: "You are in room 3",
                      4: "You are in room 4",
                      5: "You are in room 5"}
        self.wumpus_room = random.choice(list(self.rooms.keys()))
        self.player_room = random.choice(list(self.rooms.keys()))
        self.bat_rooms = random.sample(list(self.rooms.keys()), 2)

    def move_player(self, new_room):
        if new_room in self.rooms:
            self.player_room = new_room
            return True
        return False

    def check_wumpus(self):
        return self.player_room == self.wumpus_room

    def check_bats(self):
        return self.player_room in self.bat_rooms

def main():
    cave = Cave()
    print(cave.rooms[cave.player_room])

    while True:
        move = input("Which room do you want to go to (0-5)? ")
        if move.isdigit():
            move = int(move)
            if cave.move_player(move):
                print(cave.rooms[cave.player_room])
                if cave.check_wumpus():
                    print("You encountered the Wumpus! You lose!")
                    break
                elif cave.check_bats():
                    print("You were carried away by bats! You lose!")
                    break
                else:
                    print("You are safe for now.")
            else:
                print("Invalid room. Try again.")
        else:
            print("Please enter a number.")

if __name__ == "__main__":
    main()

//https://replit.com/@samuelsinurat05/Python//