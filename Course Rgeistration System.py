class RegisterCourse:
    def __init__(self, name, ):
        self.name = name
        self.courses = []

    def add_course(self, course):
        if course in self.courses:
            print('This course has been added already')
        else:
            self.courses.append(course)
            print('Course has been successfully added')


    def drop_course(self, course):
        if course in self.courses:
            self.courses.pop(course)
            print(f'✅{course} has successfully been dropped')
        elif course not in self.courses:
            print('This course cannot be found')
        else:
            print('This course has already been dropped')

    def my_course(self):
        if not self.courses:
            print('You have not registered any course')
        else:
            print(f'{self.name} below are your registered courses')
            for idx, course in enumerate(self.courses, 1):
                print(f'{idx}. {course}')

def main():
    name = input('Enter your name: ').capitalize()
    student1 = RegisterCourse(name)

    while True:
        print('\nMenu')
        print('1)Add course')
        print('2)Drop course')
        print('3)View course')
        print('4)Exit')

        choice = int(input('Enter your preference: '))

        if choice == 1:
            course = input('Enter course to add: ').capitalize()
            student1.add_course(course)
        elif choice == 2:
            course = input('Enter course to drop: ').capitalize()
            student1.drop_course(course)
        elif choice == 3:
            student1.my_course()
        elif choice == 4:
            print(f"👋 Bye {name}")
            break
        else:
            print("❌Invalid Choice! Select a valid option.")


if __name__ == "__main__":
         main()
