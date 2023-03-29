import manager as manager

manager = manager.Manager()

manager.AddMap("Map1")
manager.AddMap("Map2")
manager.AddMap("Map3")

manager.AddPlayer("Player1")
manager.AddPlayer("Player2")
manager.AddPlayer("Player3")

manager.AddLap(1, 1000, 1)
manager.AddLap(1, 2000, 2)
manager.AddLap(1, 3000, 3)

manager.DisplayLaps()

manager.DisplayMaps()

manager.DisplayPlayers()