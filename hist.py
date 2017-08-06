import matplotlib.pyplot as plt

import pickle
#f= open("NameProtein","r+")
f = open("NameProtein","r+")

#protein_frequency = pickle.load(f)
rna_frequency = pickle.load(f)
f.close()

x=[]
y=[]
other=0
print len(rna_frequency)
for i,j in rna_frequency.iteritems():
     if len(i)<=1:
               continue
     if (j>200):
         #print len(i),j
         x.append(i)
         y.append(j)
     #else:
         other+=1

#x.append("others")
#y.append(other)

import matplotlib.pyplot as plt

#plt.title('Frequency distributions of Entity Names VS frequency of Mentions')
plt.title("frequency distribution for ProteinEntity")
plt.xlabel('Frequency')
plt.ylabel("Names of protein's")
plt.barh(range(len(y)), y, align='center')
plt.yticks(range(len(y)), x, size='small')
plt.show()
