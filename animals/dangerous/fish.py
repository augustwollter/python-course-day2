class Fish:
    def __init__(self):
        ''' Constructor for this class'''
        # Create some Fish
        self.members = ['Cod','Salmon','Great White Shark']
    def printMembers(self):
        ''' Prints member Fish '''
        print("Printing members of the Fish class:")
        for member in self.members:
            print(f"\t{member}")
