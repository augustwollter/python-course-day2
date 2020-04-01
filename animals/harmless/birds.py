class Birds:
    def __init__(self):
        ''' Constructor for this class'''
        # Create some Birds
        self.members = ['Sparrow','Robin','Duck']
    def printMembers(self):
        ''' Prints member Birds '''
        print("Printing members of the Birds class:")
        for member in self.members:
            print(f"\t{member}")
