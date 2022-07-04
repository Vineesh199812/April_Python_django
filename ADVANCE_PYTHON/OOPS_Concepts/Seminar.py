class Access:

    def __init__(self):

        #public attribute
        self.name= input('Enter your name :')

        #private attribute
        self.__secretcode=input("Enter your secret code :")

    def permit(self):
        if self.name =='abc' and self.__secretcode =='123!':
         print("Access Granted" )
        else:
         print('Access Denied')

ob = Access()
ob.permit()

#print(ob.name)     #public attribute is visible to external world
#print(ob._secretcode)  #private attribute is invisible to external world
print(ob.name)     #public attribute is visible to external world
print(ob._Access__secretcode)