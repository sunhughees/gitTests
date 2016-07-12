from time import sleep

for i in xrange(100):
    with open("example.out", "w") as f:
        f.write("Hello, "+str(i))
        sleep(1)
