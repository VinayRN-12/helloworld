# # Step 1: Import libraries
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# # Step 2: Sample dataset (study hours vs marks)
# data = {
#     "Hours": [1, 2, 3, 4.5, 5, 6, 7, 8.5, 9, 10],
#     "Marks": [20, 35, 40, 55, 60, 65, 70, 85, 88, 95]
# }
# df = pd.DataFrame(data)

# # Step 3: Visualize data
# plt.scatter(df["Hours"], df["Marks"], color='blue')
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.title("Study Hours vs Marks")
# plt.show()

# # Step 4: Prepare data
# X = df[["Hours"]]
# y = df["Marks"]

# # Step 5: Train/test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# # Step 6: Train the model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Step 7: Predict
# y_pred = model.predict(X_test)

# # Step 8: Results
# print("Predicted marks:", y_pred)
# print("Actual marks:   ", list(y_test))
# print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# # Step 9: Predict new value
# hours = [[7.5]]
# predicted_marks = model.predict(hours)
# print(f"Predicted marks for 7.5 study hours: {predicted_marks[0]:.2f}")


for i in range(1,10):
    if(i==3):
        continue
    print(i)

for i in range(1,10):
    if(i==3):
        break
    print(i)



