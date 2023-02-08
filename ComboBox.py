currentKw = 1
firstKw = currentKw - 4
lastKw = currentKw + 4
KwArray = []
KwArray.append("")
for addKw in range(currentKw-4, currentKw+4):
  if addKw > 0:
    KwArray.append(addKw)
  else:
    KwArray.append(52 + addKw)
print(KwArray)
