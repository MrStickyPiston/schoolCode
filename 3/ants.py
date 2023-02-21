class Ant:
    def __init__(self, name, type):
        self.name = name
        self.type = type


def ant_switches(antsleft, antsright, seconds):
    ants = []
    for i in antsleft:
        ants.append(Ant(i, "left"))
    for i in antsright:
        ants.append(Ant(i, "right"))

    for i in range(seconds):
        temp_ants = []
        counter = 0
        for i in ants:
            if i.type == "left" and ants[counter + 1].type == "right":
                temp_ants.append(ants[counter + 1])
            elif i.type == "right" and ants[counter - 1].type == "left":
                temp_ants.append(ants[counter - 1])
            else:
                temp_ants.append(i)
            counter += 1
        ants = temp_ants
    return "".join([i.name for i in ants])

if __name__ == "__main__":
    print(ant_switches("ALJ", "CRUO", 3))
