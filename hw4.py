#private
class user:
    __password = ''

    def __init__(self,password):
        self.__password = password

    #getter method
    def get_password(self):
        return self.__password
    
    #setter method
    def set_password(self, new_password):
        self.__password = new_password

u1 = user("1234")
#getter diye password dekhbo
print(f"password: {u1.get_password()}")

#setter method use kore password change
u1.set_password('5678')

print(f"new password: {u1.get_password()}")
