#How to create a class

class Person: # #how to create 'Methods' in a class
    def reading(self): #instance keyword 'self'
        print("reading books") #method1
    def writting(self):
        print("writing a book") #method2
pe=Person()
pe.reading()
pe.writting()

pe1=Person()
pe1.writting()

pe2=Person()
pe2.reading()