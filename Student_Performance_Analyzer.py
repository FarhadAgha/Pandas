#In this project we are Createing student dataset that Calculate average marks, Find the toper and lowest performer,
# Sort students by performance, and Calculate class average.
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Zain", "Hina"],
    "Math": [85, 92, 78, 60, 88],
    "Science": [90, 85, 80, 70, 95],
    "English": [88, 90, 85, 65, 92]
}

df = pd.DataFrame(data)

print("=== Student Data ===")
print(df)

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

topper = df.loc[df["Average"].idxmax()]

lowest = df.loc[df["Average"].idxmin()]

sorted_df = df.sort_values(by="Average", ascending=False)

class_avg = df["Average"].mean()

print("\n=== Final Result Table ===")
print(df)

print("\n=== Topper Student ===")
print(topper)

print("\n=== Lowest Performer ===")
print(lowest)

print("\n=== Students Sorted by Performance ===")
print(sorted_df)

print("\nClass Average:", class_avg)

