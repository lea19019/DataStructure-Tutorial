# Declare our Queue
my_queue = []

# Ask for the number of turns
number = int(input('How many turns do we need?: '))

for num in range(1,number+1):
    # Let's Enqueue every element to our Queue
    my_queue.append(num)

turn = 0

# Let us loop until we finish with all turns
while turn < number:
    print("\nTurn in line: ", my_queue[0])

    # In charge to Dequeue our list
    del my_queue[0]
    turn = turn + 1

    # We will not keep moving forward until client have stated he's done
    not_done = True
    while not_done:
        answer = input('Enter "done" when you have finish: ')
        if answer == 'done' or answer == 'Done':
            not_done = False
    

print('\nAll turns have been attended.')
print('Have a nice day!')

