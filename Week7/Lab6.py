# Lab6
# Author: Nate Harris


## add in functions from test.py's test statements here to make the pytest work
# write a function to calculate the area of a rectangle given its length and width
def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width

    Args:
        length (float): length of the rectangle
        width (float): width of the rectangle

        Returns: 
       float: Area of a rectangle (length * width)
    """
    return length * width

#write a function to calculate the hypotenuse of a right triangle given the lengths of the other two sides
def calculate_hypotenuse(side1: float, side2: float) -> float:
    """
    Calculate the hypotenuse of a right triangle given the lengths of the other two sides

    Args:
        side1 (float): length of the first side
        side2 (float): length of the second side

        Returns:
        float: Hypotenuse of a right triangle (sqrt(side1^2 + side2^2))
    """
    return (side1 ** 2 + side2 ** 2) ** 0.5

#write a function to determine if a number is even
def is_even(number: int) -> bool:
    """
    Determine if a number is even

    Args:
        number (int): number to check

        Returns:
        bool: True if number is even, False otherwise
    """
    return number % 2 == 0

#write a function to find the maximum of two numbers
def find_maximum(number1: float, number2: float) -> float:
    """
    Find the maximum of two numbers

    Args:
        number1 (float): first number
        number2 (float): second number

        Returns:
        float: maximum of the two numbers
    """
    return max(number1, number2)

#write a function to calculate a letter grade given a numeric score
def grade_calculator(score: float) -> str:
    """
    Calculate a letter grade given a numeric score

    Args:
        score (float): numeric score

        Returns:
        str: letter grade
    """
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"      


def main():
    pass


if __name__ == "__main__":
    main()
