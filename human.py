import matplotlib.pyplot as plt

from helpers import *

class Human:
    def __init__(self, age, sex, location, profession, lifestyle, habit, hours_per_year=150):
        self.age = age
        self.sex = sex
        self.location = location
        self.profession = profession
        self.lifestyle = lifestyle
        self.hours_per_year = hours_per_year
        self.habit = habit

    def show_risks(self):
        print('Ризик смертельної небезпеки внаслідок соматичних та генетичних захворювань, а також через природне старіння організму')
        print('R1*=К*R1={}*{}={}'.format(living_place['illness'][self.location][self.sex], genetic[self.age], r1 := living_place['illness'][self.location][self.sex] * genetic[self.age]))

        print('Ризик загибелі протягом року внаслідок можливого нещасного випадку на виробництві')
        print('R2*=T*R2={}*{}={}'.format(hobbies[self.profession], 2024, r2 := hobbies[self.profession] * 2024))

        print('Ризик наразитися на смертельну небезпеку протягом року внаслідок можливого нещасного випадку в побуті')
        print('R3*=K*R3={}*{}={}'.format(living_place['accidents'][self.location][self.sex], pobut[self.age], r3 := living_place['accidents'][self.location][self.sex] * pobut[self.age]))

        print('Ризик наразитися на смертельну небезпеку протягом року, зумовлений індивідуальним способом життя людини')
        print('R4*=К*R4={}*{}={}'.format(living_place['illness'][self.location][self.sex], habits[self.habit], r4 := living_place['illness'][self.location][self.sex] * habits['drinking']))

        print('R4**=К*R4*T={}*{}*{}={}'.format(living_place['accidents'][self.location][self.sex], hobbies[self.lifestyle], self.hours_per_year, r41 := living_place['accidents'][self.location][self.sex] * hobbies['driving'] * self.hours_per_year))

        height = [r1, r2, r3, r4, r41]
        summary_risk = sum(height)
        print(f'Сумарний ризик: {summary_risk}')
        if summary_risk < 10 ** -8:
            print('Знехтуваний')
        elif 10 ** -8 <= summary_risk < 10 ** -7:
            print('Низький')
        elif 10 ** -7 <= summary_risk < 10 ** -6:
            print('Відносно низький')
        elif 10 ** -6 <= summary_risk < 10 ** -5:
            print('Середній')
        elif 10 ** -5 <= summary_risk < 10 ** -4:
            print('Відносно середній')
        elif 10 ** -4 <= summary_risk < 10 ** -3:
            print('Високий')
        elif 10 ** -3 <= summary_risk < 10 ** -2:
            print('Дуже високий')
        else:
            print('Екстремальний')

        left = [i for i in range(1, 6)]

        tick_label = ['R1', 'R2', 'R3', 'R4', 'R4**']

        plt.bar(left, height, tick_label=tick_label, width=.8, color=['blue'])

        plt.title('Діаграма ризиків смертельних небезпек')
        plt.show()