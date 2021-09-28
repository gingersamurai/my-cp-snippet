import os


os.system('g++ solution.cpp -o solution')
os.system('g++ dummy.cpp -o dummy')


for test_num in range(1, 10000):
    os.system(f'python3 gen.py {str(test_num)} > input.txt')
    os.system('./solution < input.txt > solution.txt')
    os.system('./dummy < input.txt > dummy.txt')
    
    solution = open('solution.txt').read()
    dummy = open('dummy.txt').read()
    test_input = open('input.txt').read()
    print(f'test {test_num}', end=' ')
    if solution == dummy:
        print('OK')
    else:
        print('WA')
        print('\tINPUT DATA:')
        print(test_input)
        print('\tRIGHT:')
        print(dummy)
        print('\tWRONG:')
        print(solution)
        break