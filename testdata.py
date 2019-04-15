import numpy as np
import pandas as pd


#x = np.array([4.0,2.5,3.2,5.8,7.4,4.4,8.3,8.5])
#y = np.array([2.1,4.0,1.5,6.3,5.0,5.8,8.1,7.1])

#doe linregressie op x-y meting
#invoer: een excel met daarin 3 kolommen:x,y, sample waardes.

#data inlezen uit excel en rijen omzetten naar arrays
df=pd.read_excel('data.xlsx')

conc=np.array(df.iloc[:,0])
sorb=np.array(df.iloc[:,1])
samp=np.array(df.iloc[:,2])

#remove NaN from arrays
samp=samp[~np.isnan(samp)]
conc=conc[~np.isnan(conc)]
sorb=sorb[~np.isnan(sorb)]

x=conc
y=sorb

# Fit x to y
p, y_err = lin_fit(x,y)

# Calculate confidence intervals
p_x, confs = conf_calc(x, y_err, 0.975)

# Calculate the lines for plotting:
# The fit line, and lower and upper confidence bounds
p_y, lower, upper = ylines_calc(p_x, confs, p)

# Plot these lines
plot_linreg_CIs(x, y, p_x, p_y, lower, upper)

#voor iedere sample waarde de x-waarde bepalen en deze plotten
h=0
x_samp=np.zeros(samp.size)

for i in np.nditer(samp):
 x_samp[h]=np.roots(p-i)
 h=h+1

plt.plot(x_samp,samp,'o', color='xkcd:marigold',markersize=6, markeredgecolor='k', markeredgewidth=1, label='Measurements')


plt.legend(loc=0)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=10)

