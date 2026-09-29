import matplotlib.pyplot as plt 

f1,(x ,y) = plt.subplots(2,1,figsize = (10 ,4))
x.plot([1,2,3],[4,5,6],color = 'blue')
y.bar(['a','b','c'],[3,7,8],color = 'green')


plt.show()
