import threading

class Happiness:




    def __init__(self,happiness):
        self.happiness=happiness
        self.decay_happiness()

    def decay_happiness(self):
        threading.Timer(5.0,self.decay_happiness).start()
        if self.happiness>10 :
            self.happiness*=0.96

    def add_happiness(self, increase):
        self.happiness+=increase

    def throw_happiness_message(self):
        if (self.happiness < 0):
            return "I'm kind of sad ( ˘⊖˘) ♡♡♡♡"
        elif (self.happiness < 100):
            return "I'm alright ㄟ( ･ө･ )ㄏ ♡♡♡♡♡"
        elif (self.happiness < 200): 
            return "I'm pretty happy ˎ₍•ʚ•₎ˏ ♥♡♡♡♡"
        elif (self.happiness < 300):
            return "I'm happy (　＾Θ＾) ♥♥♡♡♡"
        elif (self.happiness < 400):   
            return "I'm super happy! (•ө•)♡ ♥♥♥♡♡"
        elif (self.happiness < 500): 
            return "I'm super happy! (•ө•)♡ ♥♥♥♥♡"
        else:
            return "I love you!! ♫.(◕∠◕).♫ ♥♥♥♥♥"