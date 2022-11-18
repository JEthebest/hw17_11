class Birds:
    def __init__(self, poroda, age):
        self.poroda = poroda
        self.age = age

    def eat(self):
        return f'I am eat worms'


    def swim(self):
        return f'I cannot swim'


    def fly(self):
        return f'I cannot fly'


class Mammals:
    def __init__(self, poroda, age):
        self.poroda = poroda
        self.age = age

    def eat(self):
        return f'I am eat grass'

    def swim(self):
        return f'I cannot swim'


    def fly(self):
        return f'I cannot fly'

class Fishes:
    def __init__(self, poroda, age):
        self.poroda = poroda
        self.age = age

    def eat(self):
        return f'I am eat worms'


    def swim(self):
        return f'I can swim'


    def fly(self):
        return f'I cannot fly'

class Falcon(Birds):
    def eat(self):
        return f'I am eat meat'


class Penquin(Birds):
    def eat(self):
        return f'I am eat fish'

    def swim(self):
        return f'I can swim'

    def fly(self):
        return f'I cannot fly'

class Trout(Fishes):
    def eat(self):
        return f'I am eat korm'
    

class Whale(Fishes):
    def eat(self):
        return f'I am eat planktons'

    def swim(self):
        return f'I can swim'

    
ping = Penquin('royal', 12)
print(ping.eat())
print(ping.swim())
print(ping.fly())

# falc = Falcon('орёл', 1)
# print(ping.eat())
# print(ping.swim())
# print(ping.fly())

# forel = Trout('балык', 2)
# print(ping.eat())
# print(ping.swim())
# print(ping.fly())

# kit = Whale('чон балык', 3)
# print(ping.eat())
# print(ping.swim())
# print(ping.fly())