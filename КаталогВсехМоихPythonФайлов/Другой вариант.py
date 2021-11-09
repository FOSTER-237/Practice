r = [7, 14, 21, 56]
t = input("Try to guess the number: ")
int(t)
while t == r[0] or r[1] or r[2] or r[3]:
    print("Enter \"x\" if you want exit")
    print("You didn't guess, try again")
print("You guess")         
