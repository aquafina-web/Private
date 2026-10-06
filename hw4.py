#private
class user:
    name = ''
    __password = ''

    def __init__(self,name,password):
        self.name = name
        self.__password = password

    #setter method
    def set_password(self, new_password):
        self.__password = new_password

u1 = user("momo", "1234")

#setter method use kore password change
u1.set_password('5678')

print(f"name: {u1.name}\nnew password: {u1.get_password()}")
