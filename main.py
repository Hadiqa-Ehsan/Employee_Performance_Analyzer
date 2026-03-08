import pandas as pd
import matplotlib.pyplot as plt

# Employee dataset
data = {
    "Employee": ["Ali", "Sara", "Ahmed", "Zara", "Bilal"],
    "Score": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Employee Dataset:")
print(df)

# Average Score
average_score = df["Score"].mean()

# Total Score (optional, for practice)
total_score = df["Score"].sum()

print("Average Score:", average_score)
print("Total Score:", total_score)
# Top performer
top_employee = df.loc[df["Score"].idxmax()]

print("Top Performer:")
print(top_employee)

# Bar Graph
plt.bar(df["Employee"], df["Score"])
plt.title("Employee Scores Bar Graph")
plt.xlabel("Employees")
plt.ylabel("Score")
plt.show()

# Line Graph
plt.plot(df["Employee"], df["Score"], marker='o')
plt.title("Employee Scores Line Graph")
plt.xlabel("Employees")
plt.ylabel("Score")
plt.show()