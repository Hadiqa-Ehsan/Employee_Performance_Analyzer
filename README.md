
# 📈 Employee Performance Analyzer

A Python tool to evaluate employee metrics, track performance, and generate insightful reports for HR and management teams.

## ✨ Features

- **Employee Data Input** – Add employee names, departments, and roles
- **Performance Metrics** – Track productivity, quality, attendance, and punctuality
- **Score Calculation** – Automatically calculate overall performance scores
- **Performance Ratings** – Classify employees as Excellent, Good, Average, or Needs Improvement
- **Department-wise Analysis** – Compare performance across different teams
- **Top Performers** – Identify highest-rated employees
- **CSV Export** – Save reports for documentation

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** – Data manipulation and analysis
- **CSV Module** – Data storage
- **Statistics Module** – Mean, median, and other calculations

## 📁 Project Structure

```
Employee_Performance_Analyzer/
├── employee_analyzer.py   # Main program
├── employee_data.csv      # Stored employee records
├── performance_report.csv # Generated reports
└── README.md              # Documentation
```

## 🔧 How to Run

1. Download or clone the project
2. Open terminal in the project folder
3. Install dependencies:

```bash
pip install pandas
```

4. Run the program:

```bash
python employee_analyzer.py
```

## 📖 Usage Example

```
--- Employee Performance Analyzer ---

1. Add Employee
2. Record Performance
3. Generate Report
4. View Top Performers
5. Exit

Enter your choice: 1
Enter employee name: Sarah Khan
Enter department: Sales
Enter role: Senior Associate

Enter choice: 2
Select employee: Sarah Khan
Productivity score (0-100): 88
Quality score (0-100): 92
Attendance score (0-100): 95
Punctuality score (0-100): 90

--- Performance Summary ---
Employee: Sarah Khan
Department: Sales
Overall Score: 91.25
Rating: Excellent 🌟
```

## 📊 Performance Rating Scale

| Score Range | Rating |
|-------------|--------|
| 90 - 100 | Excellent 🌟 |
| 75 - 89 | Good ✅ |
| 60 - 74 | Average 📊 |
| Below 60 | Needs Improvement ⚠️ |

## 📌 Future Improvements

- Add graphical charts using matplotlib
- Compare performance across months
- Set performance goals and track progress
- Email reports to managers
- GUI interface with Tkinter

## 👩‍💻 Author

**Hadiqa Ehsan**  
[GitHub Profile](https://github.com/Hadiqa-Ehsan)

## 📄 License

MIT License

---

⭐ Star this repo if you found it useful for HR analytics!
