import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.money = 100
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress +=0.12
        self.gladness -= 3

    def to_work(self):
        print("Time to work")
        self.progress +=0.12
        self.gladness -= 3
        self.money += 5



    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5

    def is_alive(self):
        if self.progress <  - 0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
        elif self.money <= 0:
            print("bankrupt")
            self.alive = False
        elif self.progress >5:
            print("Done")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Money = {self.money}")
        print(f"Progress = {round(self.progress, 2)}")

    def life(self, day):
        day = "Day" +str(day)+"of"+self.name+"life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 4:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 1:
            self.to_work()
        self.end_of_day()
        self.is_alive()


vasya = Student(name="Vasya")
for day in range(365):
    if vasya.alive == False:
        break
    vasya.life(day)

