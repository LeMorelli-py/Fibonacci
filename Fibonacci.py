print('--'*30)
print('Sequencia de Fibonacci')
print('--'*30)
n = int(input('Que termo deseja encontrar: '))
t1 = 1
t2 = 1
print('~'*30)
print(f'{t1} - {t2} ', end = '')
count = 3
while count <= n:
    t3 = t1 + t2
    print(f' - {t3}', end = '')
    t2 = t1
    t1 = t3
    count += 1
print('- FIM')