def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

N = int(input("Enter N: "))
for square in generate_squares(N):
    print(square, end=" ")
