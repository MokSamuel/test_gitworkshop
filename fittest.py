
import numpy as np

import matplotlib.pyplot as plt


x = np.array([0,1,2,3,4,5])

y = np.array([0, 0.8, 2.1, 2.9, 4.1, 5.3])

z = np.polyfit(x,y,1)
p = np.poly1d(z)
fit = p(x)

c_y = [np.min(fit),np.max(fit)]
c_x = [np.min(x),np.max(x)]


#slope, intercept, r_value, p_value, std_err = linregress(x,y)
#funcstr='equation: '+str(round(intercept,3))+'+'+str(round(slope,3))+'*x'+'\n'+'$r^2$ = '+str(round(r_value,3)) + ''

#plot settings
plt.figure(figsize=(10,10))
ax=plt.subplot(111)
ax.spines["top"].set_visible(False)    
ax.spines["right"].set_visible(False)    

ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()  


#data for plot

plt.plot(x,y,'o',label='orig data')
plt.plot(x,intercept+slope*x,'r',label='fit')
plt.legend()


#ax.annotate(funcstr, xytext=(x[x.size-2],y[y.size-2]*0.8),xy=(x[x.size-3],intercept+slope*x[x.size-3]))


plt.ylim(0,6)
plt.xlim(0,6)
plt.show()