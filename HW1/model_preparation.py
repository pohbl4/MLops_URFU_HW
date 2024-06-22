import pandas as pd
from sklearn.linear_model import LinearRegression
import os


df_train = pd.read_csv('./train/result_train.csv')
df_test = pd.read_csv('./test/result_test.csv')

X_train = df_train.drop('target', axis=1)
y_train = df_train['target']
X_test = df_test.drop('target', axis=1)

model = LinearRegression()
print("--- Model created")

predict_path = os.path.join("./test", "predict.csv")
model.fit(X_train, y_train)
print("--- Model trained")

predict_df = pd.DataFrame(model.predict(X_test))
predict_df.to_csv(predict_path, index=False)

if os.path.exists(predict_path):
    print(f"--- The model performed the calculation and wrote the data to a file {predict_path}")
