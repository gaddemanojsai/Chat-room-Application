class Users:

    def assign_name(self, name):
        print(f"{name} is set to user..")
        self.name = name
        #name is the name with which user has joined

    def __repr__(self):
        print("returning the name and address of the user connected....")
        #assigning an address to the user...
        return f"({self.address}, {self.name})"

    def __init__(self, obj, address):
        #store name of the user
        self.temp=None
        self.name = self.temp
        self.address = address
        print(self.address)
        # address will store the address of listening and sending address
        self.client = obj
        print(self.client)
        #contains all the information regarding the users joined

