#  fibonacci Generation

fibonacci = [0,1]
first_term = 0
second_term = 1
user_input = int(input("How many terms you want to generate:"))
for i in range(2,user_input):
    next_term = first_term +second_term
    fibonacci.append(next_term)
    first_term = second_term
    second_term = next_term
print("*********Fibonacci Series******")
print(fibonacci)

# 2nd way iterative approch

print("using Iterrative approch")
def Fib(N):
    fibonacci_series = []
    f_term,s_term = 0,1
    while len(fibonacci_series) < N:
        fibonacci_series.append(f_term)
        f_term,s_term = s_term, f_term+s_term
    return fibonacci_series
print(Fib(5))


# Using Dynamic Programming
def Fib2(N):
    fib_series = [0]*N
    print(len(fib_series))
    if N < 1:
        fib_series[0] = 0
    if N > 1:
        fib_series[1] = 1
    for i in range(2,N):
        fib_series[i] = fib_series[i-2] +fib_series[i-1]
    return fib_series
print("using dynamic programming approch")
user_input = int(input("how many terms U want to gererate : "))
print(Fib2(user_input))