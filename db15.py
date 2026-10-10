import pandas as pd                 # csv aur table handle karne ke liye
import matplotlib.pyplot as plt     # chart ke liye

# ---- Pehle CSV me 10 records daalo ----
data = {
    "StudID":   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "StudName": ["Rahul", "Riya", "Amit", "Neha", "Rohan",
                 "Priya", "Raj", "Sneha", "Karan", "Ritu"],
    "Sub1": [90, 85, 70, 88, 95, 60, 92, 78, 65, 89],
    "Sub2": [92, 80, 65, 90, 91, 70, 95, 82, 60, 93],
    "Sub3": [95, 88, 72, 85, 94, 65, 90, 80, 70, 96]
}
pd.DataFrame(data).to_csv("Stud_Data.csv", index=False)   # csv file ban gayi

# ---- Ab CSV read karo ----
df = pd.read_csv("Stud_Data.csv")

# ---- A. Total Marks column ----
df["Total Marks"] = df["Sub1"] + df["Sub2"] + df["Sub3"]
print(df)

# ---- B. Naam 'R' se start ho aur Total Marks > 270 ----
result = df[(df["StudName"].str.startswith("R")) & (df["Total Marks"] > 270)]
print("\nR se start hone wale aur Total > 270:")
print(result["StudName"])

# ---- C. Bar chart: StudName (X) vs Sub1 (Y) ----
plt.bar(df["StudName"], df["Sub1"], color="skyblue", label="Sub1 Marks")
plt.xlabel("Student Name")          # x-axis label
plt.ylabel("Sub1 Marks")            # y-axis label
plt.title("Student Name vs Sub1 Marks")   # title
plt.legend()                        # legend
plt.show()                          # chart dikhao
