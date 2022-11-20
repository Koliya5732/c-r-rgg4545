class Person:
  def init(self,Damage):
    self.Damage = 0 
    self.helth = 0
    self.age = 0
  def atack(self):
    print ("я нападаю  ")

class Hero(Person):
  def init(self,Damage):
    self.reputation = 0
    super().init(Damage)
  def atack(self):
    super().Damage()
    print ("я сильнее тебя")
  def Mood(self):
    print ("I am in a very good mood")
class Enemy(Person):
  def init(self,Damage):
    self.villainy = 0
    super().init(Damage)
  def atack(self):
    super().Damage()
    print ("я сильнее тебя")
  def villainy1 (self):
    print ("Я уничтожу мир")

