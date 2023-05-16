#1
try:
    print('Start:')
    print(error)  #після цього рядка программа не продовжується
    print('We have no problems')
except:
    print('We have a problem')


#2
def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f'Неможливо працювати з типом {type(var_1)}, потібно str')
    else:
        print(var_1)
first = 6
checker(first)

#3
class BuildingError(Exception):
    def __str__(self):
        return 'Неможливо збудувати будівлю, матеріальів замало '
def check_materail(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return 'Все добре'
    else:
        raise BuildingError()

materials = 123
print(check_materail(materials, 300))