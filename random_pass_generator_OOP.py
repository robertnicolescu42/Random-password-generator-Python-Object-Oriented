import random

def rand_symb_gen():
	lines = open('symbols.txt').read().splitlines()
	myline = random.choice(lines)
	return str(myline)

class Word:
    def __init__(self):
        self.string = "a"

    def pick(self,lang):
        rand_number = random.randint(1,1000)
        myline = 0
        myline2 = 0
        #myline1 is the first word
        #myline2 is the second word
        #we're adding the first word to myline2
        if lang=="1":
            file1=open("wordsENG.txt","r")
            file2=open("wordsENG2.txt","r")
        elif lang=="2":
            file1=open("wordsRO.txt","r")
            file2=open("wordsRO2.txt","r")
        lines = file1.read().splitlines()
        myline =random.choice(lines)

        lines2 = file2.read().splitlines()

        if rand_number%2 == 0:
            myline = myline.upper()

        if rand_number%3 == 0:
            myline2 = myline + random.choice(lines2)
        elif rand_number%3 == 2:
            myline2 = myline
        else:
            myline2 = random.choice(lines2) + myline
        self.string = str(myline2)

    def easy_pass_gen(self, lang):
        self.pick(lang)
        rand_number = random.randint(1,1000)
        if rand_number%2 == 0:
            easypass = self.string + str(rand_number%100)
        else:
            easypass = str(rand_number%100) + self.string
        return easypass

    def strong_pass_gen(self, lang):
        rand_number = random.randint(1,1000)
        temppass = rand_symb_gen()

        for i in range(rand_number%4):
            symbol = rand_symb_gen()
            temppass = temppass + symbol

        epg = self.easy_pass_gen(lang)

        l = list(temppass)
        random.shuffle(l)
        temppass = ''.join(l)

        l = list(epg)
        random.shuffle(l)
        if rand_number%2 == 0:
            temppass = temppass + ''.join(l)
        else:
            temppass = ''.join(l) + temppass
        return temppass

    def level(self):
        lang = input("EN/RO?")
        answer = input("Do you want a weak or strong password ? (1=weak, 2=strong) : ")
        if answer == "1":
            return self.easy_pass_gen(lang)
        else:
            return self.strong_pass_gen(lang)

    def execute(self):
        print(self.level())


def main():
   w = Word()
   w.execute()
    


if __name__== "__main__":
    main()