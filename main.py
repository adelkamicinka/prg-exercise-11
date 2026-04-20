from sorting import random_numbers
from student_grades import StudentsGrades

results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

def main():
    vysledeek = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet studentů:", results.count())
    for i in range(vysledeek.count()):
        body = vysledeek.get_by_index(i)
        grade = vysledeek.get_grade(i)
        print(f"Student {i}: {body} points - {grade}")
    print("Studenti se 100 body: ", vysledeek.find(100))
    print("Seřazené výsledky: ", vysledeek.get_sorted())

if __name__ == "__main__":
    main()


