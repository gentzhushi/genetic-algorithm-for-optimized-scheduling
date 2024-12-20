# qitu vjen krejt kodi ig

"""
    qka ka me ndodh qitu:
        1 - ki me pas ni array me machines (secila e ka ka ni task, edhe duration sa zgat) 
            aka machineName -> [task name, task duration]
        2 - golla osht me minimizu total duration (fitness functiuon osht total duration, minimalet tu u zgjedh)
        3 - funksionon nbaz t3 funksioneve: 
            crossover - i bon crossover 2 genotypes
            mutation - e merr ni gjen, edhe ja shton ni curveball
            selection - i zgjedh top fittest genes prej ni popullation
        4 - duhet me keep track t gjeneratave t orareve sa t ekzekutohet algoritmi(me i grafu)
        
    params:
        1 - lista e tasqeve
        2 - lista e duracioneve
        3 - machine constraints

    returns:
        - [optimal schedule, prduction time]
"""