
class Student:
    def __init__(self,number,name,old,gender,height,weight):
        self.number=number
        self.name=name
        self.old=old
        self.gender=gender
        self.height=height
        self.weight=weight
            
    def getNumber(self):
        return self.number
        
    def getName(self):
        return self.name
        
    def getOld(self):
        return self.old
        
    def getGender(self):
        return self.gender
        
    def getHeight(self):
        return self.height
        
    def getWeight(self):
        return self.weight
        
student_data={}
    
k=0
with open("student_data.txt",mode="r",encoding="utf-8")as f:
    for sen in f:
        k=k+1
        student_data[k]=sen.split()
                 
text=input("番号　欲しい情報を入力：\n")
text=text.split()
n0=int(text[0])
if n0>100 or n0<1:
    print("存在しない番号です。")
else:
    stu=student_data[n0]
    pr=Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5])
    print(pr.getNumber(),end=" ")
    for sen in text:
        if sen==text[0]:
            continue
        if sen=="name":
            print(pr.getName(),end=" ")
        elif sen=="old":
            print(pr.getOld(),end=" ")
        elif sen=="gender":
            print(pr.getGender(),end=" ")
        elif sen=="heigh":
            print(pr.getHeight(),end=" ")
        elif sen=="weight":
            print(pr.getWeight(),end=" ")
        else:
            print("指定情報を間違っています。")
    print()
