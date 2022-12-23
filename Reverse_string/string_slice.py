arr[start:stop]         # items start through stop-1
arr[start:]             # items start through the rest of the array
arr[:stop]              # items from the beginning through stop-1
arr[:]                  # a copy of the whole array
arr[start:stop:step]    # start through not past stop, by step

// The actual code

s = "palani"
print(s[::-1])