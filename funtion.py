def mewSit(sitcount:int=10, name:str="pleum"):  #function ชื่อ mewsit, variable คือ sitcount, name และตั้งค่า constant เป็น 10 และ pleum ตามบำดับ,
    if sitcount == 100:             #ถ้า sitcount = 100
        print(name + str(sitcount))   #print ชื่อ + sitcount(set เป็น string)
    return 100                

mewSit()  #start function mewsit

pushupcount=float(input("Mew push up amount: ")) #set variable ผ่าน input ใน type float

def mewPushup(pushupCount:int=0): #function name mewPushup with local variable "pushupCount" in integer type and set constant as 0
    if pushupCount >= 20:              #if pushupCount is greater than 20 print mew is tired
        print("mew is tired")
    elif pushupCount < 20:                #ถ้าเงื่อนไขไม่ตรงกับ if ก่อนหน้า ให้ลงมาเช็คตัวนี่ต่อ if pushupCount is lower than 20 print mew is doing pushup
        print("mew is doing pushup")
    else:                                        #ถ้าไม่ตรงกับทั้งคู่ข้างบนให้ print wrong data type
        print("Wrong data type")

mewPushup(pushupcount)            #start funstion mewPushup and add pushupcount value into the function
