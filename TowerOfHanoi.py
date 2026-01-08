#                                     Hands-on Activity 2.1: The Tower of Hanoi Problem 
#Losaria, Jose Anton Paolo F.                                               08/01/2026
#CPE22S3                                                                    Engr. Neal Barton James Matira


def printdic(poles):
    print(f"  Pole A: {poles['A']}")
    print(f"  Pole B: {poles['B']}")
    print(f"  Pole C: {poles['C']}")


def TowerOfHanoi(n, disks, src, aux, des):
    if n==1:
        disk = disks[src].pop()
        disks[des].append(disk)
        print(f"Moving disk {disk} from {src} to {des}")
        printdic(disks)
        return
    TowerOfHanoi(n-1, disks, src, des, aux)
    disk = disks[src].pop()
    disks[des].append(disk)
    print(f"Moving disk {disk} from {src} to {des}")
    printdic(disks)
    TowerOfHanoi(n-1, disks, aux, src, des)

disks = {
    'A': [4,3,2,1],
    'B': [],
    'C': []
}
Source = "A"
Auxillary = "B"
Destination = "C"
totalofDisk = len(disks[Source])
printdic(disks)
TowerOfHanoi(totalofDisk, disks, Source, Auxillary, Destination)
print(f"Destination: {disks[Destination]}")


""" Through the use of recursion, this program works by having a condition that will only move the values from the source to the destination if the n is 1, as it starts
from the length of the list of the source, it will continue call itself from the first recursive line until the value of n is 1 then it will proceed to run the if condition. 
It will then remove the top from the source to the set destination based on what is the current given parameter as the parameter changes due to the recursive lines. When the
if condition is true, then it will run then when the return is called, it will return to the last call then continues the code which will now start at line 14 then continues to
run like that until it finishes. There is also a function that shortens the code to prints the contents of a dictionary 
"""
    