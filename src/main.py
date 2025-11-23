from src.structures import Queue, Stack
from src.functions import Functions
from src.sorting import Sortings

names = {}
f = Functions()
s = Sortings()

def parse_line(line: str):
    ''' Функция, обеспечивающая функционал парсера для интеративного ввода '''
    line_split = line.split()
    if line_split[0].lower() in ['queue','stack']:
        if len(line_split) == 2:
            if line_split[0] == 'queue':
                names[line_split[1]] = Queue()
            else:
                names[line_split[1]] = Stack()
        elif len(line_split) == 3:
            if line_split[0] == 'queue':
                names[line_split[1]] = Queue(value=[int(elem) for elem in line_split[2].replace('[', '').replace(']','').split(',')])
            else:
                names[line_split[1]] = Stack(value=[int(elem) for elem in line_split[2].replace('[', '').replace(']','').split(',')])
    elif line_split[0].lower() in ['factorial', 'factorial_recursive', 'fibo', 'fibo_recursive']:
        n = int(line_split[1])
        match line_split[0].lower():
            case 'factorial':
                print(f'Factorial from {n}: {f.factorial(n)}')
            case 'factorial_recursive':
                print(f'Factorial from {n}: {f.factorial_recursive(n)}')
            case 'fibo':
                print(f'Fibo from {n}: {f.fibo(n)}')
            case 'fibo_recursive':
                print(f'Fibo from {n}: {f.fibo_recursive(n)}')
    elif line_split[0].lower() in ['bubble_sort', 'quick_sort', 'counting_sort', 'radix_sort', 'bucket_sort', 'heap_sort']: # name list
        args = [float(elem) for elem in line_split[1].replace('[', '').replace(']','').split(',')]
        match line_split[0].lower():
            case 'bubble_sort':
                print(s.bubble_sort(args))
            case 'quick_sort':
                print(s.quick_sort(args))
            case 'counting_sort':
                print(s.counting_sort([int(elem) for elem in args]))
            case 'radix_sort':
                print(s.radix_sort([int(elem) for elem in args]))
            case 'bucket_sort':
                print(s.bucket_sort(args))
            case 'heap_sort':
                print(s.heap_sort(args))
    elif '.' in line_split[0]:
        name = line_split[0][:line_split[0].find('.')]
        func = line_split[0][line_split[0].find('.')+1:line_split[0].find('(')]
        if line_split[0].find('(') != line_split[0].find(')')-1:
            arg = line_split[0][line_split[0].find('(')+1:-1]
        else:
            arg = False
        if name not in names.keys():
            raise Exception('Bad input')
        match func:
            case 'push':
                if arg:
                    names[name].push((int(int(arg))))
                else:
                    names[name].push()
            case 'pop':
                if arg:
                    print(names[name].pop((int(int(arg)))))
                else:
                    print(names[name].pop())
            case 'peek':
                if arg:
                    print(names[name].peek(int(arg)))
                else:
                    print(names[name].peek())
            case 'len':
                print(len(names[name]))
            case 'is_empty':
                if arg:
                    print(names[name].is_empty(int(arg)))
                else:
                    print(names[name].is_empty())
            case 'min':
                if arg:
                    print(names[name].min(int(arg)))
                else:
                    print(names[name].min())
            case 'max':
                if arg:
                    print(names[name].max(int(arg)))
                else:
                    print(names[name].max())
            case 'print':
                if arg:
                    names[name].print(int(arg))
                else:
                    names[name].print()
            case 'enqueue':
                if arg:
                    names[name].enqueue((int(int(arg))))
                else:
                    names[name].enqueue()
            case 'dequeue':
                if arg:
                    print(names[name].dequeue((int(int(arg)))))
                else:
                    print(names[name].dequeue())
            case 'front':
                if arg:
                    print(names[name].front(int(arg)))
                else:
                    print(names[name].front())
    else:
        raise Exception('Bad input')
while True:
    line = str(input('> '))
    if line == 'q':
        break
    try:
        parse_line(line)
    except Exception:
        print('Bad input')
