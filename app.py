from models.restaurantes import Restaurante

# Restaurante da Praça
restaurante_praca = Restaurante("restaurante da praça", "Comida Caseira")
restaurante_praca.alternar_status()

# Avaliações
restaurante_praca.receber_avaliacao('João', 8)
restaurante_praca.receber_avaliacao('Maria', 6)
restaurante_praca.receber_avaliacao('Jussara', 5)

# Pizza Sabor Itália
restaurante_pizza = Restaurante("Pizza Sabor Itália", "Italiana")
restaurante_pizza.alternar_status()

# Avaliações
restaurante_pizza.receber_avaliacao('Pedro', 9)
restaurante_pizza.receber_avaliacao('Carol', 7)
restaurante_pizza.receber_avaliacao('Naty', 5)

# Sushi Jotão
restaurante_sushi = Restaurante("Sushi Jotão", "japosesa")
restaurante_sushi.alternar_status()

# Avaliações
restaurante_sushi.receber_avaliacao('Mayumi', 5)
restaurante_sushi.receber_avaliacao('Kyoto Jr', 8)
restaurante_sushi.receber_avaliacao('Masha', 7)

restaurante_tacos = Restaurante('Tacos Food Mexico', 'Mexicano')



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
