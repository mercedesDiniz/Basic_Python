# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros, milimetros e outros.

print('{:=^50}'.format('COVERSOR'))
valorMetros = float(input('Insira o valor em metros: '))

# Km-hm-dam_m_dm-cm-mm
kilometro = valorMetros/1000
hectometros = valorMetros/100
decametros = valorMetros/10

decimetros = valorMetros*10
centimetros = valorMetros*100
milimetros = valorMetros*1000

print('{:.3f}m :\n {:.3f}km = {:.3f}hm = {:.3f}dam = {:.3f}dm = {:.3f}cm = {:.3f}mm'.format(valorMetros, kilometro, hectometros,decametros, decimetros, centimetros, milimetros))