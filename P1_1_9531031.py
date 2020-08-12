# Developed by Parham Rahimi 9531031
class State:  # My state data structure
    startingState = False  # if it is the starting state
    finalState = False  # if it is a final state

    def __init__(self, name):  # initialization function
        self.name = name
        self.nextStates = {}

    def add_next_state(self, input_alphabet, next_state):  # function to add next state
        self.nextStates[input_alphabet] = next_state

    def next_state(self, input_alphabet):  # function to check next state (if not available returns trap)
        if input_alphabet in self.nextStates:
            return self.nextStates[input_alphabet]
        else:
            return "trap"


file = open('DFA_Input_1.txt', 'r')  # input file
Lines = file.readlines()

count = -1
alphabet = []  # automate alphabet
states = []  # automate states
startingState = State('trap')
for line in Lines:
    count += 1
    thisLine = line.strip().split()
    print(thisLine)
    if count > 3:  # linking states
        for state in states:
            if state.name == thisLine[0]:
                state.nextStates[thisLine[1]] = thisLine[2]
                break
    elif count == 0:  # adding alphabet
        alphabet = thisLine
    elif count == 1:  # adding states names
        for thisState in thisLine:
            states.append(State(thisState))
    elif count == 2:  # marking starting state
        for thisState in thisLine:
            for state in states:
                if state.name == thisState:
                    state.startingState = True
                    startingState = state
    elif count == 3:  # marking final state
        for thisState in thisLine:
            for state in states:
                if state.name == thisState:
                    state.finalState = True

for state in states:  # printing states and their links
    print(state.name, "->", state.nextStates)

inputString = input('Enter your string: ')  # input string to check with automate
currentState = startingState
acceptedString = True
for char in inputString:  # moving in automate with each char in input
    if currentState.next_state(char) == 'trap':
        print('String is not accepted by DFA!')
        acceptedString = False
        break
    else:
        for state in states:
            if state.name == currentState.next_state(char):
                currentState = state
                break

if acceptedString:  # printing whether our automate accepted the input string or not
    if currentState.finalState:
        print('String accepted by DFA!')
    else:
        acceptedString = False
        print('String not accepted by DFA!')
