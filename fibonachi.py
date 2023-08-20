#Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
n=int(input("Введите номер числа фиббоначи: "))-1
def fibonachi_recursion(n):
    if n == 0 :
        return 0  
    if n in (1, 2):
        return 1
    return fibonachi_recursion(n - 1) + fibonachi_recursion(n - 2)
print(fibonachi_recursion(n))     
