#!/usr/bin/env python

'''
Calculating confidence intervals for a linear regression
Heavily inspired (read: copied) from:
    linfit.py - example of confidence limit calculation for linear
                regression fitting.
    
    http://tomholderness.wordpress.com/2013/01/10/confidence_intervals/
# References: 
# - Statistics in Geography by David Ebdon (ISBN: 978-0631136880)
# - Reliability Engineering Resource Website: 
# - http://www.weibull.com/DOEWeb/confidence_intervals_in_simple_linear_regression.htm
# - University of Glascow, Department of Statistics:
# - http://www.stats.gla.ac.uk/steps/glossary/confidence_intervals.html#conflim
By Kirstie Whitaker, on 27th September 2013
    Contact:  kw401@cam.ac.uk
    GitHubID: HappyPenguin
    
'''

# ====== IMPORTS =============================================================
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
# ============================================================================

# ====== FUNCTIONS ===========================================================
def lin_fit(x,y):
    '''
    Predicts the values for a best fit between numpy arrays x and y
    
    Parameters
    ----------
    x: 1D numpy array
    y: 1D numpy array (same length as x)
    
    Returns
    -------
    p:     parameters for linear fit of x to y
    y_err: 1D array of difference between y and fit values    
               (same length as x)
    
    '''
    
    z = np.polyfit(x,y,1)
    p = np.poly1d(z)
    fit = p(x)

    y_err = y - fit
    
    return p, y_err

# ----------------------------------------------------------------------------

def conf_calc(x, y_err, c_limit=0.975):
    '''
    Calculates confidence interval of regression between x and y
    
    Parameters
    ----------
    x:       1D numpy array
    y_err:   1D numpy array of residuals (y - fit)
    c_limit: (optional) float number representing the area to the left
             of the critical value in the t-statistic table
             eg: for a 2 tailed 95% confidence interval (the default)
                    c_limit = 0.975
    Returns
    -------
    confs: 1D numpy array of predicted y values for x inputs
    
    '''
    # Define the variables you need
    # to calculate the confidence interval
    mean_x = np.mean(x)			# mean of x
    n = len(x)				# number of samples in origional fit
    tstat = t.ppf(c_limit, n-1)         # appropriate t value
    s_err = np.sum(np.power(y_err,2))	# sum of the squares of the residuals

    # create series of new test x-values to predict for
    p_x = np.linspace(np.min(x),np.max(x),50)

    confs = tstat * np.sqrt((s_err/(n-2))*(1.0/n + (np.power((p_x-mean_x),2)/
			((np.sum(np.power(x,2)))-n*(np.power(mean_x,2))))))

    return p_x, confs
    
# ----------------------------------------------------------------------------

def ylines_calc(p_x, confs, fit):
    '''
    Calculates the three lines that will be plotted
    
    Parameters
    ----------
    p_x:   1D array with values spread evenly between min(x) and max(x)
    confs: 1D array with confidence values for each value of p_x
    fit:   
    
    Returns
    -------
    p_y:    1D array with values corresponding to fit line (for p_x values)
    upper:  1D array, values corresponding to upper confidence limit line
    lower:  1D array, values corresponding to lower confidence limit line
    
    '''
    # now predict y based on test x-values
    p_y = p(p_x)
    
    # get lower and upper confidence limits based on predicted y and confidence intervals
    lower = p_y - abs(confs)
    upper = p_y + abs(confs)

    return p_y, lower, upper
   
# ----------------------------------------------------------------------------
 
def plot_linreg_CIs(x, y, p_x, p_y, lower, upper):

    # set-up the plot
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Linear regression and confidence limits')

    # plot sample data
    plt.plot(x,y,'x',label='Sample observations',markersize=4,color='k')

    # plot line of best fit
    plt.plot(p_x,p_y,'-',label='Regression line',color='xkcd:scarlet')

    # plot confidence limits
    plt.plot(p_x,lower,'-',label='Lower confidence limit (95%)',color='xkcd:grey green')
    plt.plot(p_x,upper,'-',label='Upper confidence limit (95%)',color='xkcd:grey blue')

    
    ax = plt.gca()
    ax.fill_between(p_x, upper, p_y,color='xkcd:grey blue',alpha=0.3)
    ax.fill_between(p_x, lower, p_y,color='xkcd:grey green',alpha=0.3)
  

    
    # show the plot
    plt.show()


