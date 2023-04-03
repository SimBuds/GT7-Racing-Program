import manager as m

class Application:
    def __init__(self):
        self.manager = m.Manager()
        self.exit = False
        self.mainMenu()

    def mainMenu(self):
        while not self.exit:
            print("Main Menu")
            print("1. Add Lap")
            print("2. View Laps")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addLap()
            elif choice == "2":
                self.viewLaps()
            elif choice == "3":
                self.exit = True
            else:
                print("Invalid choice. Try again.")

    def addLap(self):
        print("Add Lap")
        print("1. Bathurst Mt. panorama")
        print("2. Monza")
        print("3. Spa")
        print("4. Nurburgring")
        print("5. Suzuka")
        print("6. Watkins Glen")
        mapChoice = input("Enter the number of the map: ")
        if mapChoice == "1":
            mapChoice = "Bathurst Mt. panorama"
        elif mapChoice == "2":
            mapChoice = "Monza"
        elif mapChoice == "3":
            mapChoice = "Spa"
        elif mapChoice == "4":
            mapChoice = "Nurburgring"
        elif mapChoice == "5":
            mapChoice = "Suzuka"
        elif mapChoice == "6":
            mapChoice = "Watkins Glen"
        else:
            print("Invalid choice. Try again.")
            return
        carType = input("Enter the car type: ")
        lapTime = input("Enter the lap time: ")
        playerName = input("Enter your name: ")
        self.manager.AddLap(mapChoice, carType, lapTime, playerName)

    def viewLaps(self):
        print("View Laps")
        print("1. Bathurst Mt. panorama")
        print("2. Monza")
        print("3. Spa")
        print("4. Nurburgring")
        print("5. Suzuka")
        print("6. Watkins Glen")
        mapChoice = input("Enter the number of the map: ")
        if mapChoice == "1":
            mapChoice = "Bathurst Mt. panorama"
        elif mapChoice == "2":
            mapChoice = "Monza"
        elif mapChoice == "3":
            mapChoice = "Spa"
        elif mapChoice == "4":
            mapChoice = "Nurburgring"
        elif mapChoice == "5":
            mapChoice = "Suzuka"
        elif mapChoice == "6":
            mapChoice = "Watkins Glen"
        else:
            print("Invalid choice. Try again.")
            return
        self.manager.ViewLaps(mapChoice)

if __name__ == "__main__":
    app = Application()