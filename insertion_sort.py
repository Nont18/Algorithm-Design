# a = [5, 2, 4, 6, 1]
# a = [31, 41, 59, 26, 41, 58]
# a = [6, 3, 98, 67, 43, 197, 209, 210, 476, 90, 4, 1]
a = [37, 89, 14, 52, 71, 9, 66, 44, 28, 7, 50, 61, 83, 95, 19, 76,
     2, 68, 34, 56, 93, 11, 72, 30, 84, 5, 23, 78, 47, 64, 16, 98, 39, 57, 21,
     87, 13, 70, 45, 81, 8, 31, 74, 49, 26, 69, 92, 12, 59, 4, 41, 75, 27, 53,
     90, 20, 65, 3, 88, 18, 48, 79, 33, 60, 91, 22, 86, 10, 37, 55, 77, 35, 67,
     1, 58, 96, 17, 82, 29, 43, 63, 6, 80, 25, 51, 38, 73, 15, 94, 24, 62, 42,
     99, 32, 54, 40, 85, 46, 97, 36, 100]


for j in range(1, len(a)): #store number to temp begin with index = 1 until end of array
    temp = a[j] 
    for i in range(j - 1, -1, -1): #compare the number that already sorted in array and temp (<--)
        if a[i] > temp: #once if number in array more than temp then shift number in array to right
            a[i + 1] = a[i]
        else: #if a[i] <= temp   break
            break
    a[i + 1] = temp  #replace with temp

for x in range(1,len(a)): #print number that already sorted
    print(x, end=" ")
