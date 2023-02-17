def find_lowest(row):
    while not len(row) == 1:
        counter = 0
        next_row = []
        try:
            for i in row:
                if i == row[counter + 1]:
                    next_row.append(i)
                else:
                    next_row.append("RGB".replace(i, "").replace(row[counter + 1], ""))
                counter += 1
        except IndexError:
            pass

        row = next_row

    return row


print("The lowest triangle letter is: " + str(find_lowest(input("Enter the top layer of the triangle: "))))