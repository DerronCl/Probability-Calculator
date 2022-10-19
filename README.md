#  -- Probability-Calculator --

A basic program to calculate the probability of selecting certain items from a basket of items. In this case, a user will insert a certain amount of different colored balls into a hat and will ask for the probability of getting a certain selection of balls. The program will run a specificed number of expirements to approximate the probability of successfully retrieving the requested outcome. The more expirements that are run, the more approximate the probability is. 

The expirement function which approxmiates the final probability accepts for arguments: 

      - hat: A hat object containing balls that should be copied inside the function.
      - expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability drawing 2 blue balls and 1 red ball from the hat
      - num_balls_drawn: The number of balls to draw out of the hat in each experiment.
      - num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
      
The final probaility will be returned as a percentage.

Here is an example of the hat objects that will be created:

An example of the expirment function in action: 

Shoutout to Freecodecamp for the project inspiration: 

