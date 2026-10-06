#private
class user:
    name = ''
    __password = ''

    def __init__(self,name,password):
        self.name = name
        self.__password = password

    #getter method
    def get_password(self):
        return self.__password

u1 = user("momo", "1234")
#getter diye password dekhbo
print(f"name: {u1.name}\npassword: {u1.get_password()}")

