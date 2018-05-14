
# 面向对象特性：封装，继承，多态。类、方法

# 重复的代码是非常不好的低级行为，你写的代码要经常变更（易读，易改）

class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)


r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色
