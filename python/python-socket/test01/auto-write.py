from time import sleep
import random

for i in xrange(100):
    with open("example.out", "a") as f:
        f.write("Hello, "+str(i)+"\n")
    t = random.choice(range(2))
    sleep(t)
