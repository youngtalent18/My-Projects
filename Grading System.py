class GradingSystem:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def calculate_total(self):
        return sum(self.subjects.values())


    def add_subjects(self, subject, mark):
        self.subjects[subject] = mark


    def calculate_average(self):
        if self.subjects:
            return self.calculate_total()/len(self.subjects)
        return 0

    @staticmethod
    def get_grade( average):
        if average >= 90:
            return "A+"
        elif average >= 85:
            return "A"
        elif average >= 75:
            return "B+"
        elif average >= 65:
            return "B"
        elif average >= 55:
            return "C+"
        elif average >= 50:
            return "C"
        elif average <= 50:
            return "A+"
        else:
            return "F"

    def show_results(self):
        print('🎓Welcome To ATU Grading System')
        print('--------------------------------')
        print(f'Name: {self.name}')
        print('Subject and Marks')
        for subject, mark in self.subjects.items():
            print(f'{subject}: {mark}')
        total = self.calculate_total()
        avg = self.calculate_average()
        grade = GradingSystem.get_grade(avg)
        print(f'Grade: {grade}')
        print(f'Total Score: {total}')
        print(f'Average: {avg}')




def main():


    name = input('Enter your name: ')
    student = GradingSystem(name)


    num_of_courses = int(input('Enter the number of subjects: '))

    for _ in range(num_of_courses):
        subject = input('Enter subject: ')
        mark = float(input('Enter the mark: '))
        student.add_subjects(subject,mark)

    student.show_results()



if __name__ == "__main__":
    main()