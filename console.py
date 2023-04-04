import db as manager

class ConsoleApplication:
    def __init__(self):
        self.manager = manager.Manager()
        self.exit = False
        self.mainMenu()

    def mainMenu(self):
        while not self.exit:
            print("Main Menu")
            print("1. Add Lap")
            print("2. View Laps")
            print("3. View All Laps")
            print("4. View All Players")
            print("5. View Player Laps")
            print("6. View Specific Map's Best Lap")
            print("7. View Specific Map's Average Lap")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addLap()
            elif choice == "2":
                self.viewLaps()
            elif choice == "3":
                self.manager.ViewAllLaps()
            elif choice == "4":
                self.manager.ViewAllPlayers()
            elif choice == "5":
                playerName = input("Enter the player name: ")
                self.manager.ViewPlayerLaps(playerName)
            elif choice == "6":
                mapChoice = input("Enter the map: ")
                self.manager.ViewBestLap(mapChoice)
            elif choice == "7":
                mapChoice = input("Enter the map: ")
                self.manager.ViewAverageLap(mapChoice)
            elif choice == "8":
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

    def viewSpecificMapBestLap(self):
        print("View Specific Map's Best Lap")
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
        self.manager.ViewBestLap(mapChoice)

    def viewSpecificMapAverageLap(self):
        print("View Specific Map's Average Lap")
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
        self.manager.ViewAverageLapTime(mapChoice)

if __name__ == "__main__":
    app = ConsoleApplication()