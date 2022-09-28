class Fish:
    def __init__(self,name,build="ほね",eyelids=False):
        self.name=name
        self.build=build
        self.eyelids=eyelids

    def swim(self):
        print("こちらの魚は泳ぎます")

    def swim_back(self):
        print("こちらの魚は後ろにも泳ぎます")


class Medaka(Fish):
    def swim_speed(self):
        print("この魚は140km/sで泳ぎます")


n0=Fish("魚１号（親クラス）")
print("骨格：",n0.build)
print("まぶた：",n0.eyelids)
n0.swim()
n0.swim_back()

n01=Medaka("魚２号（継承クラス）")
print("骨格：",n01.build)
print("まぶた：",n01.eyelids)
n01.swim()
n01.swim_back()
