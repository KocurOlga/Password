new_pass = input('Ведите пароль: ')
correct_pass = 'Ваш пароль состоит только из цифр'
try:
    correct_pass_zero = 10 / len(new_pass)
    correct_pass_num = int(new_pass)
except ZeroDivisionError:
    correct_pass = 'Вы ввели пустой пароль'
except ValueError:
    correct_pass = 'Требования к паролю соблюдены'
print(correct_pass)
