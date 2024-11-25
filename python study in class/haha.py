#创建一个类
class Student:
    #定义一个对象，并赋予它性质
    def __init__(self,name):
        #绑定到对象身上
        self.name=name
        self.information={"属于":0,"喜好":0,"生日":0}
    #对所定义的对象加上性质
    def set_information(self,information,detail):
        if information in self.information:
            self.information[information]=detail
    #输出对象的信息
    def print_information(self):
        print(f"学生：{self.name}")
        for information in self.information:
            print(f"{information}:{self.information[information]}")
#创建一个小类,继承上面的类
class Lover(Student):
    def __init__(self,name):
        #继承name属性
        super().__init__(name)
        self.love=True
    def print_love(self):
        print("是你所爱吗："+str(self.love))

Yuuka=Lover("Yuuka")
Yuuka.set_information("属于","千禧年科技学院")
Yuuka.set_information("喜好","计算")
Yuuka.set_information("生日","3月14日")
Yuuka.print_information()
Yuuka.print_love()