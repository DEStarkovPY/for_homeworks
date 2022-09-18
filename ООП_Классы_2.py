#def _protected(arg): - нижнее подчёркивание говорит, что это метод, который можно использовать только в этом и дочерних классах
#def __private(arg): - двойное подчёркивание говорит, что этот метод можно использовать только для данного класса
#def global(arg): - методы классов, которые можно использовать для всего

class Primate:
    def eat (self, food):
        pass
    
    
class Man(Primate): # - пример наследования в классах, класс Primate - родительский
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Spider:
    def _web_shooting (self, power):
        pass
    
    def eat (self, food, poison):
        pass
    
    def __init__ (self, weight, hight):
        pass
    
class SpyderMan(Man, Spider): # - пример наследования классов с несколькими "родителями"
    def _hp(self, number):
        pass

def __init__ (self,name, age):
    super().__init__(name,age) #метод super, позволяющий перенести родительский метод в класс, чтобы добавить к нему нужное свойство или атрибут
    self.backpack = []
    
def eat(self,target): # - пример использовавние бета - родителя, то есть параллельного в ветке MRO (Так же можно использовать методы любых классов при создании своего метода)
    super().eat(target)
    Spider.eat(self,target)
    
def comprasion(self, target): # - приём проверки принадлежности экземпляра к классу
    if isinstance(target, SpyderMan):
        pass
#Рекурсия - ошибка, вызванная повторенями одного и того же метода за счёт отсутствия super() для определения родительского метода в ООП

PiterParker = SpyderMan('Piter', 18) # - MRO, то есть то, как наследуется метод у родителей, если метод есть и там, и там (Используется метод первостоящего родителя "Man")
SpyderMan.mro() # - показывает иерархию наследования класса 

def __str__(self): # - "магический" метод, позволяющий вернуть заложенный в него текст при попытке принтовать экземпляр класса 
    res = f'Моё имя {self.name}'
    return res

