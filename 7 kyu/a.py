from timeit import Timer

a = [1] * 1000000
poop = a.pop
pop_timer = Timer('poop(0)', 'from __main__ import a')
print(f'pop_timer: {pop_timer.timeit(number=1000)}')
a = [1] * 1000000
remove_timer = Timer('a.remove(1)', 'from __main__ import a')
print(f'remove_timer: {remove_timer.timeit(number=1000)}')
a = [1] * 1000000
del_timer = Timer('del a[0]', 'from __main__ import a')
print(f'del_timer: {del_timer.timeit(number=1000)}')