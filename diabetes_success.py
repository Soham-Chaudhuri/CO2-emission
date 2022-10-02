import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']
diabetes = datasets.load_diabetes()
diabetes_x=diabetes.data[:,np.newaxis,2]
diabetes_x_train= diabetes_x[:-30]
diabetes_x_test= diabetes_x[-30:]
diabetes_y_train=diabetes.target[:-30]
diabetes_y_test=diabetes.target[-30:]


model=linear_model.LinearRegression()

model.fit(diabetes_x_train,diabetes_y_train)
diabetes_y_predicted= model.predict(diabetes_x_test)


print("mean squared  error is: ", mean_squared_error(diabetes_y_test,diabetes_y_predicted))

# print(diabetes.DESCR)
# checking the regression model on small datacase
# mean squared  error is:  3035.060115291269
# weights  [941.43097333]
# intercept  153.39713623331644

print("weights ", model.coef_)
print("intercept ", model.intercept_)

# checking the regression model on large datacase
# mean squared  error is:  1826.4841712795044
# weights  [  -1.16678648 -237.18123633  518.31283524  309.04204042 -763.10835067
#   458.88378916   80.61107395  174.31796962  721.48087773   79.1952801 ]
# intercept  153.05824267739402

plt.scatter(diabetes_x_test,diabetes_y_test)
plt.plot(diabetes_x_test,diabetes_y_predicted)
plt.show()