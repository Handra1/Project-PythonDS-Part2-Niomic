"""while loop"""
error = 50
while error > 1 :
    error = error/4
    print(error)

"""for loop"""
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)
print(fam[0])

for height in fam :
    print(height)

for index, height in enumerate(fam):
    print("index" + str(index)+ ":"+ str(height))
