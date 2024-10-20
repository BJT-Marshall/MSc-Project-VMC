#Manual Implmentation of the Hamiltonian and solving for its gorund state energy.
#Instead of following the tutorial to represent states as binary bits and collectively a byte, this program will use vectors with elements of +/- 1
#to represent spin states.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#Representation of states
#To create a vector representation of states in the z-spinor basis, use numpy to convert lists of +/-1's into numpy vectors

import numpy as np

#test_states = [[1,-1,1],[-1,1,-1]] #EXAMPLE
#print(stateVector(test_states))

def stateVectors(states): #Takes in a list of states
    state_vectors=[np.array(i) for i in states] #list comprehension to convert all states into numpy vectors
    return state_vectors


#Creates a list of basis vectors as tuples for the whole hilbert space (used to assign an ordering to the Hamiltonian matrix)
def basisVectors(N):
    basis_vectors = [[] for i in range(N)]
    basis_tuples = []
    for j in range(len(basis_vectors)):
        for q in range(N):
            basis_vectors[j].append(0)
    for r in range(N):
        basis_vectors[r][r] = 1
    for h in range(N):
        basis_tuples.append(tuple(basis_vectors[h]))      
    return basis_tuples

#Generating all states in the Hilbert space of an N-site chain of spin 1/2 particles
def generateStates(N):
    listOfStates = [[] for i in range(2**N)] #creates 2^N lists in the listOfStates to hold our states
    
    #Generate the list of binary strings for each state

    binList = ["{0:b}".format(i) for i in range(0,2**N)] #x[i] IS binary of integer i.
    #print(binList)
    StateVectorLength = len(binList[-1]) #The length of the vectors in the state space is the number of bits needed to represent the 'highest' state
    #print(StateVectorLength)
    for j in range(len(listOfStates)):
        for k in range(StateVectorLength):
            listOfStates[j].append(-1) #each list in the list of states is ammended with a default configuration of an array of -1 local states
    print(listOfStates)
    
    #Recognise binary 0's as -1 and binary 1's as +1:
    #Starting from the END of the list representing each state, alter the array of -1's to be equivelant to the binary
    for m in range(0,2**N):
        positionsToFlip = [len(binList[m])-p for p in range(len(binList[m])) if binList[m][p] == '1']
        for q in positionsToFlip:
            listOfStates[m][q-1] =1
    
    #DONE.Should have a list of lists that look like [-1,-1],[1,-1],[-1,1],[1,1] for the N=2 case 
    
    return listOfStates

#N = input("Enter the number of spin 1/2 particles in the chain:")
#N = int(N)
#print(generateStates(N))
#print("The number of states in the Hilbert space is: ",len(generateStates(N)))

#print(stateVectors(generateStates(2)))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#Initialise an empty matrix to be used for the Hamiltonian operator
#Each element of the matrix is assinged, through the basis map, a pair of indices whose keys in the basis map dictionary are the tuples representing the relevant basis vectors
def emptyH(N):
    basisMap = {}
    stateID = 0
    for state in basisVectors(N):
        basisMap[state] = stateID
        stateID+=1
    NH = stateID
    H_matrix = np.zeros([NH,NH])
    return H_matrix


    