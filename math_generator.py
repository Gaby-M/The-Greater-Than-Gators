import random


class MathGenerator:  # Class for generating math problems at checkpoints
    level_one_operator_list = ["+", "-"]  # addition and subtraction
    level_two_operator_list = ["+", "-",
                               "*"]  # addtion, subtraction, and multiplication

    def __init__(self,level=0,answer=0): 
        self.level = level
        self.answer = answer
        self.problem = ""

    def math_problem_generator(self, level):
        if level == 1:  # Level 1 (easy) addtion and subtraction questions
            generate_operator = MathGenerator.level_one_operator_list[random.randint(0, 1)]
            if generate_operator == "+":
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                self.problem = self.problem + str(x) + " " + "+" + " " + str(y)
                self.answer = x + y
        

            elif generate_operator == "-":  # Level one subtraction generator
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                if x > y:  # if x is greater than y, x - y
                    self.problem = self.problem + str(x) + " " + "-" + " " + str(y)
                    self.answer = x - y
                else:  # if y is greater then x, y - x
                    self.problem = self.problem + str(y) + " " + "-" + " " + str(x)
                    self.answer = y - x

        if level == 2:  # Level 2 Medium difficulty arithmetic questions
            generate_operator = MathGenerator.level_two_operator_list[
                random.randint(0, 2)]
            if generate_operator == "+":  # if the random operator generator generates a plus
                x = random.randint(4, 6)
                y = random.randint(4, 6)
                self.problem = self.problem + str(x) + " " + "+" + " " + str(y)
                self.answer = x + y
            elif generate_operator == "-":  # if the random operator generator generates a minus
                x = random.randint(4, 6)
                y = random.randint(4, 6)
                if x > y:  # if x is greater than y, x - y
                    self.problem = str(x) + " " + "-" + " " + str(y)
                    self.answer = x - y
                else:  # if y is greater than y, y - x
                    self.problem = self.problem +  str(y) + " " + "-" + " " + str(x)
                    self.answer = y - x
            elif generate_operator == "*":  # if random generator generates a multiplication symbol
                x = random.randint(4, 6)
                y = random.randint(4, 6)
                self.problem = self.problem + str(x) + " " + "*" + " " + str(y)
                self.answer = x * y

        if level == 3:  # Level 3 Hard difficulty arithmetic questions
            generate_operator = MathGenerator.level_two_operator_list[
                random.randint(0, 2)]
            if generate_operator == "+":  # Addition questions
                x = random.randint(7, 12)
                y = random.randint(7, 12)
                self.problem = str(x) + " " + "+" + " " + str(y)
                self.answer = x + y
            elif generate_operator == "-":  # Subtraction questions
                x = random.randint(7, 12)
                y = random.randint(7, 12)
                if x > y:
                    self.problem = self.problem + str(x) + " " + "-" + " " + str(
                            y)  # No negative integers
                    self.answer = x - y
                else:
                    self.problem = self.problem + str(y) + " " +  "-" + " " + str(x)
                    self.answer = y - x
            elif generate_operator == "*":  # Multiplication questions
                x = random.randint(7, 12)
                y = random.randint(7, 12)
                self.problem = self.problem + str(x) + " " + "*" + " " + str(y)
                self.answer = x * y
        return self.problem
