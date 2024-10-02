print("Please enter the average size of the package (L): ")
L = float(input("L: "))
if L < 0:
    while L < 0:
        print("Please enter the average size of the package, again (L): ")
        L = float(input("L: "))

print("Please enter the number of the nodes during (T1,T2) (N): ")
N = int(input("N: "))
if N < 0:
    while N < 0:
        print("Please enter the number of the nodes during (T1,T2), again (N): ")
        N = int(input("N: "))

print("Please enter the Bit-Rate of the nodes (R) : ")
R = float(input("R: "))
if R < 0:
    while R < 0:
        print("Please enter the Bit-Rate of the nodes, again (R): ")
        R = int(input("R: "))

print("Now please enter the value of the fragmentation (F): ")
F = float(input("F: "))
if F < 0:
    while F < 0:
        print("Please enter the the value of the fragmentation, again (F):")
        F = float(input("F: "))

print("And last but not least, please enter the height value of the title (H): ")
H = float(input("H: "))
if H < 0:
    while H < 0:
        print("Please enter the height value of the title, again (H):")
        H = float(input("L: "))

if F == 0 and H == 0:
    Delay = (N - 1) * L / R

elif F == 0 and H != 0:
    Delay = (L / R) + (N - 2) * (F / R)

else:
    Delay = ((L / F) * (F + H) / R) + ((N - 2) * (F + H) / R)

print("The delay is: %.10f" %Delay)
