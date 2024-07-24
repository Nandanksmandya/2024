"""Square"""
# width = 4
# height = 4
# for i in range(width):
#     for j in range(height):
#         print("*", end="  ")
#     print("\n  ")

r = 7
c = 7

for i in range(0, r):
    for j in range(0, c):
        if i == j or j == 0 or j == r-1:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()
print("\n")

rows = 7
cols = 4

for i in range(0, rows):
    for j in range(0, cols):
        if i == 0 or j == 0 or i == rows // 2 or j == cols - 1:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()

print("\n")

r = 7
c = 7

for i in range(0, r):
    for j in range(0, c):
        if i == j or j == 0 or j == r-1:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()

print("\n")



