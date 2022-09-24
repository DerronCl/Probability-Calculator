import copy
import random
# Consider using the modules imported above.

class Hat :
    
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
          for i in range(value):
              self.contents.append(key)
        return None
                    
    def draw(self, amount) :
        if amount > len(self.contents) :
            return self.contents
        result = []
        for x in range(amount):
            choice = random.randrange(len(self.contents))
            result.append(self.contents.pop(choice))
        return result
        
    def __str__(self):
        return 

def experiment( hat, expected_balls, num_balls_drawn, num_experiments) :           
    count = 0
    
    for i in range(num_experiments):
        balls_taken = copy.deepcopy(hat).draw(num_balls_drawn)
        colors = [ True if balls_taken.count(key) >= value else False for key, value in expected_balls.items()]
        count += 1 if all(colors) else 0

    return (count/(num_experiments))

                   
            
            
        
    
    
