from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(df):
       
       x = df["timestamp"].values.reshape(-1,1)
       y = df["current_price"].values
       
       X_train, X_test, y_train, y_test = train_test_split( x , y, test_size= 0.2, random_state=42)
       
       model = LinearRegression()
       model.fit(X_train, y_train)
       
       score = model.score(X_test,  y_test)
       
       print(f" precision del modelo : {score:.2%}")
       return model

