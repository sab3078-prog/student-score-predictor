# student-score-predictor
A beginner ML project that predicts student exam scores using Linear Regression
# Student Score Prediction

A beginner machine learning project that predicts a student's exam score based on their study hours, sleep hours, and attendance.

I made this project to understand the basics of **Machine Learning and Linear Regression using Python**.

## What the project does

The program takes three inputs:

* Hours studied
* Hours of sleep
* Attendance percentage

It then uses these values to predict an exam score.

The project also shows a simple graph of **Hours Studied vs Exam Score**.

## Tech Used

* Python
* Pandas
* Scikit-learn
* Matplotlib

## How it works

The dataset contains information about students and their exam scores.

I used:

* `Hours_Studied`
* `Sleep_Hours`
* `Attendance`

as the input features, and:

* `Score`

as the value the model tries to predict.

The model used is **Multiple Linear Regression**.

The dataset is split into training and testing data using `train_test_split()`.

After training, the model is tested using **Mean Absolute Error (MAE)**.

## Running the project

First, install the required libraries:

```bash
pip install pandas matplotlib scikit-learn
```

Then run:

```bash
python student_score_prediction.py
```

The program will ask for the student's details:

```text
Hours studied: 7
Hours of sleep: 8
Attendance percentage: 85
```

and give a predicted score.

## Example

```text
Enter student details:

Hours studied: 7
Hours of sleep: 8
Attendance percentage: 85

Predicted Score: XX.XX
```

The exact prediction can change depending on the training data split.

## Model Evaluation

I used **Mean Absolute Error (MAE)** to check how close the predicted scores were to the actual scores.

```python
error = mean_absolute_error(y_test, predictions)
```

A lower MAE means the predictions are closer to the actual scores.

## Limitations

This is a small project made mainly for learning.

The dataset currently has only 10 entries, so the model isn't meant to be used for making real student predictions. The data is also manually created.

A larger dataset would make the project much more useful.

## Things I could improve

Some things I'd like to add later:

* Use a larger dataset
* Add more factors that can affect scores
* Try other regression models
* Compare the performance of different models
* Build a simple UI for entering student details
* Turn it into a small web application

## What I learned

While making this project, I got familiar with:

* Pandas DataFrames
* Features and target variables
* Train/test splitting
* Linear Regression
* Making predictions with Scikit-learn
* MAE
* Basic data visualization with Matplotlib

## Author

**Sabrish D**

B.Tech CSE
VIT Chennai

