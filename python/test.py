import re
import pylab as plt

with open("residuals.log", "r") as f:
	data = f.read().split("\n")

m = []
n = []
for i in xrange(len(data)):
	if data[i][:2]=="((":
		m.append(i)
	elif data[i][0:1]==")":
		n.append(i)

x = map(lambda s:eval(s.split()[0]), data[m[1]+1:n[1]])
y = map(lambda s:eval(s.split()[1]), data[m[1]+1:n[1]])

plt.plot(x,y)
plt.show()
