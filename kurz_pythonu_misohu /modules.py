
import module_math_base

number1 = 2
number2 = 2
result1 = module_math_base.plus(number1, number2)
result2 = module_math_base.minus(number1, number2)
result3 = module_math_base.krat(number1, number2)
result5 = module_math_base.delene(number1, number2)

print(result1,result2,result3,result5)
print(module_math_base.PI)

import module_plus
import module_na_druhu

a = 1
b = 2
print(module_na_druhu.na_druhu(module_plus.plus(a,b)))
