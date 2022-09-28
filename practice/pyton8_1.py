class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

pr = Person("鈴木",23)
pr1 = Person("高橋",999)

n=pr.getName()
a=pr.getAge()
b=pr1.getName()
c=pr1.getAge()

print(n,"さんは",a,"歳です")
print(b,"さんは",c,"歳です")
