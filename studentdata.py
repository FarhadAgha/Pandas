import pandas as pd

df = pd.read_csv('studentdata.csv')

print("=" * 50)
print("STUDENT GRADES ANALYZER")
print("=" * 50)

df['final_grade'] = (df['score'] * 0.4) + (df['attendance'] * 0.3) + (df['homework'] * 0.3) 

print("\n Complete Student Data:")
print(df.to_string(index=False))

print("\n Average Final Grade by Subject:")
subject_avg = df.groupby('subject')['final_grade'].mean().round(2)
for subject, grade in subject_avg.items():
    print(f"  {subject}: {grade}%")

print("\n Student Performance Summary:")
student_summary = df.groupby('name').agg({
    'final_grade': 'mean',
    'score': 'mean',
    'attendance': 'mean',
    'homework': 'mean'
}).round(2)

student_summary.columns = ['Avg Final Grade', 'Avg Score', 'Avg Attendance', 'Avg Homework']
print(student_summary)

top_student = student_summary['Avg Final Grade'].idxmax()
top_grade = student_summary['Avg Final Grade'].max()
print(f"\n Top Student: {top_student} (Final Grade: {top_grade}%)")

needs_improvement = student_summary[student_summary['Avg Final Grade'] < 75]
if not needs_improvement.empty:
    print("\n Students who need improvement (Grade < 75%):")
    for student in needs_improvement.index:
        print(f"  - {student}")
else:
    print("\n All students are doing well!")

print("\n Subject Difficulty Ranking (Hardest to Easiest):")
subject_difficulty = df.groupby('subject')['score'].mean().sort_values()
for i, (subject, avg_score) in enumerate(subject_difficulty.items(), 1):
    print(f"  {i}. {subject} (Avg Score: {avg_score:.1f})")

perfect_attendance = df[df['attendance'] == 100]['name'].unique()
if len(perfect_attendance) > 0:
    print(f"\n Students with Perfect Attendance: {', '.join(perfect_attendance)}")

print("\n" + "=" * 50)
print(" Analysis Complete!")
print("=" * 50)
