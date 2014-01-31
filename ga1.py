import string
import random
import sys

class GA1:
    def __init__(self, word):
        self.word = word
        self.population = []
        self.pop_count = 1000
        self.symbols = string.uppercase+string.lowercase
        self.not_done = True
        self.generations = 0

    def calculate(self): #Calculate cost of chromosome then put it in population as ("string", score)
        for pop_num,x in enumerate(self.population):
            if isinstance(x, tuple):
                x = x[0] 
            chromosome = x
            x = list(x)
            score = []
            for num, y in enumerate(self.word):
                score.append(abs(ord(y) - ord(x[num])))
            total = 0
            for x in score:
                total += x
            if total == 0:
                self.not_done = False
            self.population[pop_num] = (chromosome, total)
        
        self.population = sorted(self.population, key=lambda x: x[1])

    def mate(self):
        new = []
        for x in self.population:
            first = list(self.population[0][0])
            second = list(self.population[1][0])
            to_split = len(first)/2
            f1, f2 = first[:to_split], first[to_split:]
            s1, s2 = second[:to_split], second[to_split:]
            mutate = random.randint(0,100)
            second = ''.join(f1 + s2)
            first = ''.join(s1 + f2)
            if mutate == 0:
                choice = random.randint(0,1)
                if choice == 0:
                    check = random.randint(0, len(first)-1)
                    first = list(first)
                    greatest = 0
                    on = 0
                    for num, x in enumerate(self.word):
                        check = abs(ord(x) - ord(first[num]))
                        if check > greatest:
                            on = num
                            greatest = check

                    first[on] = random.choice(list(self.symbols))
                    first = ''.join(first)

                else:
                    check = random.randint(0, len(second)-1)
                    second = list(second)
                    greatest = 0
                    on = 0
                    for num, x in enumerate(self.word):
                        check = abs(ord(x) - ord(second[num]))
                        if check > greatest:
                            on = num
                            greatest = check
            
                    second[on] = random.choice(list(self.symbols))
                    first = ''.join(first)

            new.append(first)
            new.append(second)
            self.population.pop(0)
            self.population.pop(0)
            if len(self.population) < 2:
                break
        self.population = new
    def main(self):

        self.population = [''.join([random.choice(list(self.symbols)) for x in range(len(self.word))]) for x in range(self.pop_count)]
        while self.not_done:
            self.generations += 1
            self.calculate()
            print self.population[:5]
            self.mate()

        print "Evolution took {0} generations".format(self.generations)
if __name__ == "__main__":
    GA1(sys.argv[1]).main()
