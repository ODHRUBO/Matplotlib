from matplotlib import pyplot as plt
ages=[59,51,40,48,66,61,45,40,
      59,51,58,50,56,60,63,66,
      40,47,53,49,63,51,45,70,
      42,48,60,64,68,63,70,71,
      57,52,53,47,48,46,41,49,47,
      43,46,72,85,46,50,54,58,61,67
      ,68,69,63,64,62,68,59,57,59,53,
      52,74,76,72,71,73,79,65,47,68,65,
      47,48,49,61,70,44,43,47,47,43,44,58,
      64,68,62,64,68,49,49,59,56,70,67,58,60]
plt.hist(ages,color="hotpink")
plt.title("Histrogram")
plt.xlabel("Ages")
plt.ylabel("frequency")
plt.show()
