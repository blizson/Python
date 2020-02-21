class Animal:
    def __init__(self, Arms, Legs):
        self.arms = Arms
        self.legs = Legs
        
    def limbs(self):
        return self.arms + self.legs
    
spider = Animal(4,4)
spidlimbs = spider.limbs()
print("limbs of spider : " + str(spidlimbs))
