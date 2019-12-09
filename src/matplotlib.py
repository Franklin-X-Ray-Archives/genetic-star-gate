import matplotlib
matplotlib.use('Agg')
import matplotlib as plt
fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot([1,2,3])
fig.savefig('test.png')
exit() 
