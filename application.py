import manager

manager = manager.Manager()

def run():
    while True:
        
        print("1. Add Map")
        print("2. Add Player")
        print("3. Add Lap")
        print("4. Show Map")
        print("5. Show Player")
        print("6. Show Lap")
        print("7. Show All")
        print("8. Exit")

        Input = input("Enter your choice: ")

        if Input == "1":
            MapName = input("Enter Map Name: ")
            manager.AddMap(MapName)
        elif Input == "2":
            PlayerName = input("Enter Player Name: ")
            manager.AddPlayer(PlayerName)
        elif Input == "3":
            MapId = input("Enter Map Id: ")
            LapTime = input("Enter Lap Time: ")
            PlayerId = input("Enter Player Id: ")
            manager.AddLap(MapId, LapTime, PlayerId)
        elif Input == "4":
            MapId = input("Enter Map Id: ")
            manager.GetMap(MapId)
        elif Input == "5":
            PlayerId = input("Enter Player Id: ")
            manager.GetPlayer(PlayerId)
        elif Input == "6":
            LapId = input("Enter Lap Id: ")
            manager.GetLap(LapId)
        elif Input == "7":
            manager.ShowAllMaps()
        elif Input == "8":
            break
        else:
            print("Invalid Input")