import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
random between 5 - 20

What was the smallest number you could have seen, what was the largest?
5, 20

What did you see on line 2?
random in 3 5 7 9

What was the smallest number you could have seen, what was the largest?
9

Could line 2 have produced a 4?
no

What did you see on line 3?
random between 2.5 - 5.5 

What was the smallest number you could have seen, what was the largest?
2.55258326884966
5.452030719053132
"""

print(random.randint(1, 100))