def soma(i):
    if(i == 10):
        print(f"i = {i}")
        return i
    soma(i + 1)

print(soma(2))