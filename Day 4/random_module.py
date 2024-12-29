import random
import my_module

r_int = random.randint(1, 100)
print(r_int) 
print(my_module.pi) # 3.141592653589793

no_0_to_1 = random.random()*10
print(no_0_to_1) # 0.0 to 0.9999999999999999

random_float = random.uniform(1, 10)
print(random_float) # 1.0 to 10.0

random_heads_tails = random.randint(0, 1)
print(random_heads_tails)
if random_heads_tails == 0:
    print("Heads")
else:
    print("Tails")