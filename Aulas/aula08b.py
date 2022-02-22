import random 
num = random.random()  # Gera um numero aleatorio entre 0 e 1
num1 = random.randint(1, 10) # Gera um inteiro aleatorio entre 1 e 10
print('{}\n{}'.format(num, num1))

import emoji
print(emoji.emojize("Olá mundo :sunglasses:", use_aliases=True))