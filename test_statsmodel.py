##################### fit an ARX(1) model ###############################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

exog = [0.05006667 ,0.05036667, 0.05143333, 0.04983333 ,0.05006667 ,0.04843333,
        0.04406667, 0.04496667, 0.0487,     0.0463  ,   0.0426,     0.0401,
        0.03973333, 0.03763333, 0.03493333 ,0.0336 ,    0.03536667 ,0.0389,
        0.0438 ,    0.0429    ] # exogenous variable
endog = [-0.00747451 ,-0.01205813 ,-0.00899203 , 0.00942409, -0.00727726, -0.0278912,
         -0.01763623 , 0.00745353 , 0.00438131 ,-0.01059955, -0.00413446 , 0.01286785,
         0.00805098 , 0.00516204 , 0.01551592 , 0.01543293,  0.00837698  ,0.00882242,
         0.01890189 , 0.01434118] # endogenous variable
arma_model = sm.tsa.ARMA(endog,order=(1,0),exog=exog)
arma_res = arma_model.fit()
sresult = arma_model.predict(arma_res.params) #in sample fit returned from predict() function
print(arma_res.summary())
#########################################################################
myresult=[sresult[0]] # list for my own in sample fit result
arparam= 0.2675  # arparam from statsmodel
beta=-1.2765 # exogenous coeffcient from statsmodel
const=0.0576 # const param from sm
for idx in range(1,len(endog)): # apply the ARX model
    prediction = arparam*(endog [idx-1]) + beta*(exog [idx]) + const
    myresult.append(prediction )
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)
ax.plot(np.array(myresult),"red",label="my result")
ax.plot(sresult, label="stats model result")
ax.set_title("Why they are different?")
ax.legend()
plt.show()
###############################################################