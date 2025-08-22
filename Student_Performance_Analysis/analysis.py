import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_data.csv")

# Summary statistics
print(df.describe())

# Average marks per subject
avg_marks = df.groupby("Subject")["Marks"].mean()
print("Average Marks by Subject:\n", avg_marks)

# Plot marks distribution
plt.hist(df["Marks"], bins=5, color="skyblue", edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
