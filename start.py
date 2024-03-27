from random import*
class Player():
    def __init__(self, healt, armor, hit, money, iq):
        self.healt = healt
        self.armor = armor
        self.hit = hit
        self.money = money
        self.iq = iq

    def print_info(self):
        print("здоровье:", self.healt)
        print("броня:", self.armor)
        print("урон:", self.hit)
        print("баланс:", self.money)
        print("интетелект:", self.iq)

    def kick(self, enemy):
        enemy.armor -= self.hit
        print("Броня врага:", enemy.armor)
        if enemy.armor <= 0:
            enemy.healt -= self.hit
        elif enemy.armor <=0:
            enemy.healt -= enemy.armor
        else:
            enemy.armor -= self.hit

    def kick(self, enemy):
        enemy.armor -= self.hit
        print('Броня врага:', enemy.armor)

class Strelok(Player):
    def __init__(self, healt, armor, hit, money, bullet,iq):
        super().__init__(healt, armor, hit, money, iq)
        self.bullet = bullet
    
    def crit(self, enemy):
        y = randint(1, 10)
        if y == 3:
            enemy.healt -= enemy.healt
            print("Враг убит!")
        else:
            print('Вы промахнулись')
        
        print(self.bullet)

    def fire(self, enemy):
        enemy.armor -= self.hit * 1.5
        print(enemy.armor)
        if enemy.armor < 0:
            enemy.healt += self.hit - self.hit + enemy.armor
            print("Здоровье врага:", enemy.healt)
            


St = Strelok(100, 100, 100, 100, 59, 50)
Dt = Strelok(500, 100, 100, 50, 59, 50)

St.fire(Dt)