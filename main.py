in_the_pocket = 0
for year in range(5):
    for j in range(12):
        in_the_pocket += 30000
        in_the_pocket *= 1 + 0.2/12
    print("year:" + str(year+1) + " " + str(in_the_pocket))