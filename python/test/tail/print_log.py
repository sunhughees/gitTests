import re
# import pylab as plt

with open("residuals.log", "r") as f:
    data = f.read().split("\n")

m = [] # data-start-points
n = [] # data-end-points
labels = [] # data-labels

for i in xrange(len(data)):
    if data[i][:2]=="((":
        m.append(i)
        label_text = re.search(r'".*"', data[i]).group(0).strip('"') # re match labels
        labels.append(label_text)
    elif data[i][0:1]==")":
        n.append(i)

x = map(lambda s:eval(s.split()[0]), data[m[1]+1:n[1]])

y = []


for _i in xrange(len(m)):
    y_i = map(lambda s:eval(s.split()[1]), data[m[_i]+1:n[_i]])
    y.append(y_i)



with open('res.log', 'a') as f:


    title = "index, " + ', '.join(labels)

    print title
    f.writelines(title+'\n')

    for i in xrange(len(x)):
        new = [y[j][i] for j in xrange(len(y))]
        new.insert(0, x[i])
        print ','.join(map(lambda x:str(x), new))
        f.writelines(','.join(map(lambda x:str(x), new))+'\n')
    



