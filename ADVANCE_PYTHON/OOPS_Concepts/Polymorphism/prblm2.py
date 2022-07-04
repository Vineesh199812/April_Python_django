class C:
    def printa(self):
        print("Method 1")
    def printa(self):
        print("Method 2")

ob=C()          #the last method will execute (Method overriding)
ob.printa()