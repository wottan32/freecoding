def celcius_fahrenheit(celcius):
  return celcius *9 / 5 +32

def fahrenheit_celcius(fahrenheit):
  return (fahrenheit -32) *5 / 9







# def lista_terminos(**terminos):
#   for key, value in terminos.items():
#     print(f'{key}; {value}')
         
# lista_terminos(IDE='integrated development enviroment', PK='Primary Key')

# def deplegar(nombres):
#   for nombre in nombres:
#     print(nombre)


# nombres = ['Francisco','Felipe','Mario']
# deplegar(nombres)

# def factorial(numero):
#   if numero == 1:
#     return 1
#   else:
#     return numero * factorial(numero -1)


# numero = 995
# resultado = factorial(numero)
# print(f'El facorial de {numero} es {resultado}')

# def calcular_total_pago(pago_sin_impuesto, impuesto):
#   pago_total= pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
#   return pago_total

# pago_sin_impuesto = float(input('proporciones el pago sin impuesto: \n'))
# impuesto =float(input('Proporcione el monto del impuesto: \n'))
# pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
# print(f'el pago con impuesto:\n {pago_con_impuesto}')