class MyClass:
    class_var = 10 # 클래스 변수

    def instance_method(self, test):
        self.test = test
        print("Instance method in my class")
        print(f"Test is {test}")
        return self.test + 100
    
# 인스턴스 생성
obj = MyClass()
print(obj.instance_method(100))

# obj의 __class__ 속성 확인
print(obj.__class__) # <class '__main__.MyClass'>
print(obj.__class__.class_var) # 10
print(obj.__class__.instance_method) # <function MyClass.instance_method at 0x0000020DF96D8F40>