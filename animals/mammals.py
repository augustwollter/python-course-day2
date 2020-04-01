class Mammals:
    def __init__(self):
        ''' Constructor for this class'''
        # Create some Mammals
        self.members = ['Tiger','Elephant','Wild Cat']
    def printMembers(self):
        ''' Prints member Mammals '''
        print("Printing members of the Mammals class:")
        for member in self.members:
            print(f"\t{member}")
