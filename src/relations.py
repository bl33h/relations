#/**
 #* *Copyright (C), 2022-2023, Sara Echeverria (bl33h)
    # *@author Sara Echeverria
    # *FileName: relations
    # @version: I
    #- Creation: 25/11/2022
    #- Last modification: 27/11/2022

# Imports
import numpy as np
List = []
row = []
p = []

# Variables & lists
run = True

# While cycle for the menu
while run:
    print("\n")
    print("--- What would you like to do? ---")
    print("1. Determine the type of relation (reflexive, symmetric, antisymmetric or transitive).")
    print("2. Find the relations SoR & RoS.")
    option = input("\nType the number that corresponds to the option you wanna execute: ")
    
    # First option || Relation types
    if option == "1":
        matrixElements = input("Enter the elements of the set separated by space: \n").split(" ")
        print("Enter one adjacent vertex at a time in the same way, separated by spaces. It should orrespond to the same number of elements from the previous step.")
        for i in matrixElements:
            adj = input("Adjacent vertices: ")
            List.append(adj.split(" "))

        for i in range(len(matrixElements)):
            argument = []
            for ar in matrixElements:
                argument.append(0)
            for j in List[i]:
                argument.pop(matrixElements.index(j))
                argument.insert(matrixElements.index(j), 1)
            row.append(argument)

        matrix = np.matrix(argument)
        transposedMatrix = matrix.getT()
        matrix2 = matrix**2
        Bmatrix = np.where(matrix2>1,1,matrix2)

        d = np.full((1, len(matrixElements)), 1, dtype=int)

        if np.allclose(matrix.diagonal(), d):
            p.append(1)
        else:
            p.append(0)

        if np.allclose(matrix, transposedMatrix):
            p.append(1)
        else:
            p.append(0)
        
        z1 = (matrix & transposedMatrix) - np.identity(len(matrixElements), int)
        z2 = np.where(z1<0,0,z1)
        z3 = np.full((1, len(matrixElements)), 0, dtype = int)

        if np.allclose(z2, z3):
            p.append(1)
        else:
            p.append(0)
        meet = matrix & Bmatrix
        if meet.sum() <= matrix.sum() and Bmatrix.sum() <= matrix.sum():
            p.append(1)
        else:
            p.append(0)
        
        print(f"\nThe result is: P = {p}\n")
    
    if option == 2:
        print("Pendant.")