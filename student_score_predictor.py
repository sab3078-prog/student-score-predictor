import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# 1. Create the dataset


data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Sleep_Hours": [6, 6, 7, 6, 8, 7, 8, 7, 8, 9],
    "Attendance": [70, 72, 75, 78, 80, 82, 85, 88, 92, 95],
    "Score": [35, 40, 48, 55, 62, 68, 75, 82, 88, 94]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)


# 2. Separate input and output


X = df[["Hours_Studied", "Sleep_Hours", "Attendance"]]
y = df["Score"]



# 3. Split data into training
#    and testing data


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



# 4. Create and train model


model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel trained successfully!")


# 5. Test the model


predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", round(error, 2))



# 6. Take input from user


print("\nEnter student details:")

hours = float(input("Hours studied: "))
sleep = float(input("Hours of sleep: "))
attendance = float(input("Attendance percentage: "))



# 7. Make prediction


student_data = pd.DataFrame({
    "Hours_Studied": [hours],
    "Sleep_Hours": [sleep],
    "Attendance": [attendance]
})

predicted_score = model.predict(student_data)[0]

# Keep score between 0 and 100
predicted_score = max(0, min(100, predicted_score))

print("\nPredicted Score:",
      round(predicted_score, 2))



# 8. Plot the dataset


plt.scatter(df["Hours_Studied"], df["Score"])

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Hours Studied vs Exam Score")

plt.show()