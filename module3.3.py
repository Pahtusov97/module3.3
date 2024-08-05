def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [10, 15, 20]
values_dict = {'a': 88005553535, 'b':'Alexandr', 'c': 1997}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['Черепашки', 'ниндзя']
print_params(*values_list_2, 2)