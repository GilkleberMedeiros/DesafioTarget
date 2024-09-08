def main():
    n = int(input("Digite um número inteiro: "))

    if in_fibo(n):
        print(f"O número {n} está na sequência de fibonacci!")
    else:
        print(f"O número {n} não está na sequência de fibonacci!")

def in_fibo(n: int, val1: int = 0, val2: int = 1):
    if n == val1 or n == val2:
        return True
    elif val2 > n:
        return False
    
    soma = val1 + val2

    return in_fibo(n, val1=val2, val2=soma)


main()