import sqlite3
import pandas as pd

class ResultManagementSystem:
    def __init__(self, db_name="department_results.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        # Creating tables with logical relationships
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                student_id TEXT PRIMARY KEY,
                name TEXT,
                batch TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Courses (
                course_code TEXT PRIMARY KEY,
                course_name TEXT,
                credits INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Results (
                result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                course_code TEXT,
                semester INTEGER,
                marks_obtained REAL,
                FOREIGN KEY(student_id) REFERENCES Students(student_id),
                FOREIGN KEY(course_code) REFERENCES Courses(course_code)
            )
        ''')
        self.conn.commit()

    def add_student(self, student_id, name, batch):
        self.cursor.execute("INSERT OR IGNORE INTO Students VALUES (?, ?, ?)", (student_id, name, batch))
        self.conn.commit()

    def add_course(self, course_code, course_name, credits):
        self.cursor.execute("INSERT OR IGNORE INTO Courses VALUES (?, ?, ?)", (course_code, course_name, credits))
        self.conn.commit()

    def add_result(self, student_id, course_code, semester, marks):
        self.cursor.execute("INSERT INTO Results (student_id, course_code, semester, marks_obtained) VALUES (?, ?, ?, ?)",
                            (student_id, course_code, semester, marks))
        self.conn.commit()

    def get_statistical_insights(self, semester=None):
        """Fetches data and provides statistical insights using Pandas."""
        query = '''
            SELECT r.semester, c.course_name, r.marks_obtained, s.name 
            FROM Results r
            JOIN Courses c ON r.course_code = c.course_code
            JOIN Students s ON r.student_id = s.student_id
        '''
        df = pd.read_sql_query(query, self.conn)
        
        if df.empty:
            print("No data available for insights.")
            return

        if semester:
            df = df[df['semester'] == semester]
            print(f"\n--- Statistical Insights for Semester {semester} ---")
        else:
            print("\n--- Overall Department Statistical Insights ---")

        # 1. Subject-wise Average, Max, and Min Marks
        subject_stats = df.groupby('course_name')['marks_obtained'].agg(['mean', 'max', 'min']).round(2)
        print("\nSubject-wise Performance:")
        print(subject_stats)

        # 2. Pass Percentage per Course (Assuming passing marks > 40)
        df['passed'] = df['marks_obtained'] >= 40
        pass_percentage = df.groupby('course_name')['passed'].mean() * 100
        print("\nPass Percentage per Course:")
        print(pass_percentage.round(2).astype(str) + '%')

        # 3. Department Topper
        topper = df.loc[df['marks_obtained'].idxmax()]
        print(f"\nHighest Scorer: {topper['name']} in {topper['course_name']} with {topper['marks_obtained']} marks.")

    def close_connection(self):
        self.conn.close()


# ==========================================
# Example Usage and Execution
# ==========================================
if __name__ == "__main__":
    app = ResultManagementSystem()

    # Populating sample data
    app.add_student("CS01", "Alice", "2024-2026")
    app.add_student("CS02", "Bob", "2024-2026")
    
    app.add_course("CS101", "Data Structures", 4)
    app.add_course("CS102", "Python Programming", 3)

    # Adding Sem 1 Results
    app.add_result("CS01", "CS101", 1, 85)
    app.add_result("CS01", "CS102", 1, 92)
    app.add_result("CS02", "CS101", 1, 38) # Failed Data Structures
    app.add_result("CS02", "CS102", 1, 75)

    # Generate Insights
    app.get_statistical_insights(semester=1)
    
    app.close_connection()