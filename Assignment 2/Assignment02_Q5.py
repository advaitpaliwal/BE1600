def rect_area(A_length, A_width, B_length, B_width):
    A_area = A_length * A_width
    B_area = B_length * B_width
    result = ""
    if A_area > B_area:
        result = "Area A is greater than Area B"
    elif B_area > A_area:
        result = "Area B is greater than Area A"
    else:
        result = "Area A is equal to Area B"
    return A_area, B_area, result


A_length = int(input("What is the length for rectangle A? "))
A_width = int(input("What is the width for rectangle A? "))
B_length = int(input("What is the length for rectangle B? "))
B_width = int(input("What is the width for rectangle B? "))
A_area, B_area, result = rect_area(A_length, A_width, B_length, B_width)
print(f"Area A: {A_area}\nArea B: {B_area}\n{result}")
