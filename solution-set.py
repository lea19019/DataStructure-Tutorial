# Let's get the number of kids answering
kids = int(input('How many kids in the class?'))

# Create an empty set to contain the cartoons
cartoonSet = set()

for kid in range(0, kids):
    cartoon = input('What is your favorite cartoon?')
    cartoonSet.add(cartoon)

print(cartoonSet)