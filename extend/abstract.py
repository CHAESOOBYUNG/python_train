from abc import ABC, abstractmethod

# 추상 클래스 정의
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass # 추상 메서드, 하위 메서드에서 반드시 구현

    def sleep(self):
        print("This aniaml is sleeping")

# 추상 메서드를 상속받는 구체적인 클래스
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
# 인스턴스 생성
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
dog.sleep()
cat.sleep()