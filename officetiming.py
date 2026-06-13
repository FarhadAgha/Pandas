import pandas as pd

class Employee:
    def __init__(self, name, dept, in_time, out_time):
        name_parts = name.split()
        self.first_name = name_parts[0]
        self.last_name = name_parts[-1] if len(name_parts) > 1 else ""
        self.full_name = name
        self.dept = dept
        self.in_time = in_time
        self.out_time = out_time
    def hours_worked(self):
        in_h = int(self.in_time.split(':')[0])
        in_m = int(self.in_time.split(':')[1])
        out_h = int(self.out_time.split(':')[0])
        out_m = int(self.out_time.split(':')[1])
        hours = (out_h - in_h) + (out_m - in_m) / 60
        return round(hours, 1)
class Office:
    def __init__(self, filename):
        df = pd.read_csv(filename)
        self.employees = [Employee(r['name'], r['department'], r['in_time'], r['out_time']) 
                          for _, r in df.iterrows()]
    def show_report(self):
        print("\nOFFICE HOURS REPORT")
        print("-" * 50)
        for e in self.employees:
            print(f"{e.first_name} {e.last_name} ({e.dept}) | {e.in_time} → {e.out_time} | Hours: {e.hours_worked()}")

office = Office('officeemploiestiming.csv')
office.show_report()