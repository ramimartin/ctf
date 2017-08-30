str1 = "30167b0eb4eef511ec82272b4b47a2d71471"
str2 = "1319057cb23c1dcbf616876372617fff8b48"

decoded = ''
for x in range(0, len(str1), 2):
    int_value1 = int(str1[x] + str1[x + 1], 16)
    int_value2 = int(str2[x] + str2[x + 1], 16)
    decoded = decoded + ("%0.2X" % (int_value1 ^ int_value2))

print(decoded)
