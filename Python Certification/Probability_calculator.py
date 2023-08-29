import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls):
        self.contents = []
        for key,val in balls.items():
            for x in range(0,val):
                self.contents.append(key)
    
    def draw(self,num):
        if num > len(self.contents):
            return self.contents
        #pop random index
        expelled = []
        while len(expelled) < num:
            random_ball = random.randrange(len(self.contents))
            x = self.contents.pop(random_ball)
            expelled.append(x)
        
        if num > len(self.contents):
            return self.contents
        
        return expelled
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for exp in range(0,num_experiments):
        copy = hat.contents.copy()
        result = (hat.draw(num_balls_drawn))
        # changing results do dict
        result_dict = {key: result.count(key) for key in set(result)}
        # creating "shared items" which contain {'red': 2+, 'green': 1+}
        shared_items = {key: result_dict[key] for key in result_dict if key in expected_balls and result_dict[key] >= expected_balls[key]}
        
        if sorted(shared_items) == sorted(expected_balls):
            m += 1
        hat.contents = copy
        
    probability = float(m/num_experiments)
    return probability