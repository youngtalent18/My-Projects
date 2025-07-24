#STATIC METHODS

#class Employee:
    #  def __init__(self, name, position):
#      self.name = name
        #       self.position = position

        #   def get_info(self):
        #       return f"{self.name} = {self.position}"

    #   @staticmethod
    #  def is_valid_position(position):
#      valid_position = ['Engineer', 'Data Scientist', 'AI Engineer', 'Wed DEV']
 #       return position in valid_position

#employee1 = Employee('Stephen', 'AI Engineer')

#print(Employee.is_valid_position('engineer'))
#print(employee1.get_info())

#class Student:

    #count = 0
    #total_gpa = 0

    #def __init__(self, name, gpa):
        #self.name = name
        #self.gpa = gpa
        #Student.count+=1
        #   Student.total_gpa+=gpa

    #   def get_info(self):
#   return f'{self.name} : {self.gpa}'

    #@classmethod
    #   def get_count(cls):
#   return f"{cls.count}"


    #@classmethod
    #    def calculate_average(cls):
#   if cls.count == 0:
    #           return 0
            #   else:
    #           return f"Average: {cls.total_gpa / cls.count:.2f}"

#student1 = Student("Stephen", 4.5)
#student2 = Student("Emma", 4.0)
#student3 = Student("Lucy", 4.2)
#print(student1.get_info())
#print(Student.calculate_average())

#MAGIC METHODS

#class Book:
# def __init__(self,title,author,num_pages):
#    self.title = title
      #  self.author = author
     #   self.num_pages = num_pages

        #  def __str__(self):
        #     return f"{self.title} by {self.author}"

        # def __eq__(self,other):
        #     return self.title  == other.title and self.author  == other.author

        # def __gt__(self,other):
        #    return self.num_pages > other.num_pages

        # def __lt__(self, other):
        #  return self.num_pages < other.num_pages


#book1 = Book('life begins at SHS', 'Rev Theophilus', 50)
#book2 = Book('99 reasons why you should divorce your wife', 'Rev Theophilus', 64)

#print('life' in book1)

#import os as s

#file_path = "exampl.txt"

#if s.path.exists(file_path):
 #   print('This location exists')
#else:
 #   print('This file does not exist')

#txt_data = "i like pizza"

#file_path = "example.txt"
#with open(file_path, "w") as file:
 #   file.write(txt_data)
  #  print(f'txt {file_path} was created successfully')

#import threading
#import time

#def sleep():
 #   time.sleep(3)
  #  print('Time is up wake up')

#def walk_the_dog(name):
 #   time.sleep(5)
  #  print(f'You walked {name}')

#def finish_the_chores():
 #   time.sleep(4)
  #  print('You finished the house chores')


#chore1 = threading.Thread(target = sleep)
#chore1.start()



