from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import os


target = pd.read_csv(os.path.join('test', 'target_test.csv'))
predict = pd.read_csv(os.path.join('test', 'predict.csv'))

print(f"MAE - {mean_absolute_error(target, predict)}")
print(f"MSE - {mean_squared_error(target, predict)}")
print(f"RMSE - {mean_squared_error(target, predict)**0.5}")
print(f"r2 - {r2_score(target, predict, multioutput='variance_weighted')}")
