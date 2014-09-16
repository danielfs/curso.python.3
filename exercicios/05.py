carros = 100
espaco_em_um_carro = 4.0
motoristas = 30
passageiros = 90
carros_sem_motorista = carros - motoristas
carros_com_motorista = motoristas
capacidade_total_dos_carros = carros_com_motorista * espaco_em_um_carro
media_passageiros_por_carro = passageiros / carros_com_motorista

print( "Há", carros, "disponíveis." )
print( "Há somente", motoristas, "disponíveis." )
print( "Hoje haverão", carros_sem_motorista, "carros vazios." )
print( "Hoje podemos transportar", capacidade_total_dos_carros, "pessoas." )
print( "Hoje temos", passageiros, "passageiros." )
print( "Precisamos colocar cerca de", media_passageiros_por_carro, "em cada carro." )
