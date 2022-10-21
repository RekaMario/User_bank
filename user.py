class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
        self.make_withdrawal  
    
    

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    

    def display_balance(self):
        print(f"User : {self.name}",f", Balance is: {self.account_balance} $" )
   

    def transfert(self,other_user,amount):
        self.account_balance -=amount
        other_user.account_balance += amount
        self.display_balance()
        other_user.display_balance()


guido = User("Guido")
mrnibbles = User ("Mr. Nibles")
bennybob = User ("Benny Bob")
bank_name = User ("First National Dojo Bank")

guido.make_deposit(100).make_deposit(400).make_deposit(250).make_deposit(50).make_deposit(10000)
print( 'User :', guido.name ,',', 'Balance:', guido.account_balance ,'$', )
print (guido.name , "withdraw 200 $", )
guido.make_withdrawal(200).display_balance()
mrnibbles.make_deposit(100).make_deposit(400)
print( 'User :', mrnibbles.name ,',', 'Balance:', mrnibbles.account_balance ,'$', )	
bennybob.make_deposit(100).make_deposit(400).make_withdrawal(6000)
print( 'User :', bennybob.name ,',', 'Balance:', bennybob.account_balance ,'$', )
print(guido.name , "transfert 6000$ to:" , bennybob.name)	
guido.transfert(bennybob,6000)
print("Thank You by :",  bank_name.name  )
