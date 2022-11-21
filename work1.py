# Стек - абстрактный тип данных, представляющий собой список элементов, 
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»). 
# Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. 
# Или с магазином в огнестрельном оружии(стрельба начнётся с патрона, заряженного последним).

class Stack:
    def __init__(self):
        self.chains = list([])

    # is_empty - проверка стека на пустоту. Метод возвращает True или False.
    def is_empty(self):
        if len(self.chains) == 0:
            return False
        else:
            return True

    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, chain):
        return self.chains.append(chain)

    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.chains.pop()

    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.chains[-1]

    def peek_all(self):
        return self.chains[0:]

    # size - возвращает количество элементов в стеке.
    def size(self):
        return len(self.chains)+1

def solution_work_1():
    list_ = Stack()
    print('Введите три элемента через Enter')

    a, b, c = input(), input(), input()
    print(f'Добавим 3 элемента: {a}, {b}, {c} в список\n')
    list_.push(a)
    list_.push(b)
    list_.push(c)
    
    print(f'Выведем последний эелемент - "{c}"')
    print(f'{list_.peek()}\n')

    print(f'Удалим последний эелемент - "{c}", отобразиться "{b}"')
    list_.pop()
    print(f'{list_.peek()}\n')

    print(f'Проверим количество элементов')
    print(f'{list_.size()}\n')

    print(f'Проверим наличие элементов в списке')
    print(f'{list_.is_empty()}\n')

def work_2(list_bracket):
    counter = {
        'in_square': 0, # [
        'in_round': 0, # (
        'in_curly': 0, # {
        'out_square': 0, # ]
        'out_round': 0, # )
        'out_curly': 0 # }
    }
    stack = Stack()
    for element in list_bracket:
        stack.push(element)
        if element == '[':
            counter['in_square'] += 1
        elif element == '(':
            counter['in_round'] += 1
        elif element == '{':
            counter['in_curly'] += 1
        elif element == ']':
            counter['out_square'] += 1
        elif element == ')':
            counter['out_round'] += 1
        elif element == '}':
            counter['out_curly'] += 1

    if counter['in_square'] == counter['out_square'] and counter['in_round'] == counter['out_round'] and counter['in_curly'] == counter['out_curly']:
        return 'Скобки сбалансированы'
    else:
        return 'Скобки не сбалансированы'

if __name__ == "__main__":
    solution_work_1() # первая задача
    
    list_yes = '[({})]()'
    list_no = '[({})])'
    print(list_yes, work_2(list_yes)) # вторая задача (сбалансированы)
    print(list_no, work_2(list_no)) # вторая задача (не сбалансированы)