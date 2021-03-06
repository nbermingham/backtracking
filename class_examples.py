class ClassExamples:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        """
        function that prints your first and last name
        """
        print(f"Hi, my name is {self.first_name} {self.last_name}")

    @staticmethod
    def add_two_numbers(number_one: int, number_two: int) -> int:
        """
        function that adds two numbers together
        """
        return number_one + number_two

ce = ClassExamples("nick", "bermingham")
ce.print_name()

print(ce.add_two_numbers(1, 2))
#adding in some comments
