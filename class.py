# class Person:
#     def _init_(self,name) -> None:
#         self.name = name
#         self.pos = [0,0]

#     def left(self):
#         self.pos[0] -=1

#     def right(self):
#         self.pos[0] +=1

#     def forward(self):
#         self.pos[1] += 1

#     def backward(self):
#         self.pos[1] -= 1
        
    
# p = Person("Saint")
# p.left()

class Calculator:    #ตั้ง blueprint หรือ ทำคอนโดให้ทุกอย่างที่อยู่ในclassมีgroup
    def __init__(self) -> None:  #IDK
        pass

        def choosefunction(self):  #หลังจาก while true ข้างล่างก็จะมาเช็คตรงนี่
            while True:                 
                choice = int(input())   #input choice เข้าไปและต้องเป็น int
                if choice in [1,2,3,4]:  #ถ้าอยู่ใน choice 1234
                    break       #idk
                else:            #ถ้าไม่ใช่ให้ return กลับไปที่ choice ซ้ำ
                    print('Please enter the choice')
            return choice
        
        def multiplyFunc(self):
            num1 = int(input('Enter first num'))
            num2 = int(input('Enter second num'))
            multiplyValue = num1*num2
            print( multiplyValue)
        
        def addFunc(self):                             #เริ่ม function ใส่ตัวเลขแล้วก็บวกแแกมา
                num1 = int(input('Enter first num'))
                num2 = int(input('Enter second num'))
                addValue = num1+num2
                print(addValue)
            
        def substractFunc(self):
                num1 = int(input('Enter first num'))
                num2 = int(input('Enter second num'))
                substractValue = num1-num2
                print(substractValue)
            
        def divideFunc(self):
                num1 = int(input('Enter first num'))
                num2 = int(input('Enter second num'))
                divideValue = num1/num2
                print( divideValue)
        
        def run():        #Start while True c= choosefunction ไปที่ function  "choose function"
                while True:
                    c = self.choosefunction   #มาเช็คว่า choice ที่ใส่ไปเป็นเลขอะไรจะได้ไป +,-,*,/ ต่อ
                    if c == 1:
                        self.multiplyFunc()
                    elif c==2:                  #สมมุติว่าเลือก c==2 ให้เริ่ม addfunction 
                        self.addFunc()
                    elif c == 3:
                        self.substractFunce()

                    elif c == 4:
                        self.divideFunc()

abac = Calculator()
abac.run()                
            

        #     pick = input("Pick one: 1=multiply / 2=add / 3=substract / 4=divide")
        #     if pick in [1,2,3,4]:
        #         self.choose_function()
        #     else:
        #         print("Not in choice")

        #     return pick
                
        # def choose_function(self):
        #     if pick == 1:
        #         self.multiply()
        #     elif pick == 2:
        #         self.add()
        #     elif pick == 3:
        #         self.substract()
        #     elif pick == 4:
        #         self.divide()

        #     def multiply(self):
        #         A = float(input("Enter your number: "))
        #         B = float(input("Enter your number: "))
        #         return A*B
        
        #     def add(self):
        #         A = float(input("Enter your number: "))
        #         B = float(input("Enter your number: "))
        #         return A+B
            
        #     def substract(self):
        #         A = float(input("Enter your number: "))
        #         B = float(input("Enter your number: "))
        #         return A-B
            
        #     def divide(self):
        #         A = float(input("Enter your number: "))
        #         B = float(input("Enter your number: "))
        #         return A/B
            
