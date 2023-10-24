# Definição da função que calcula o número esperado de ocorrências

def expected_occurrences(L, k, num_sequences):
    probability = 1 / 4 ** k  # Calcula a probabilidade de um determinado 9-mer ocorrer em uma posição
    occurrences_single_sequence = L - k + 1  # Calcula o número de ocorrências em uma única sequência
    total_expected_occurrences = occurrences_single_sequence * probability  # Calcula o total esperado de ocorrências em todas as sequências
    total_expected_occurrences *= num_sequences  
    return round(total_expected_occurrences, 4)  

# Definindo os valores de L, k e o número de sequências
L = 1000  # Comprimento da sequência
k = 9  # Comprimento do 9-mer
num_sequences = 500  # Número de sequências

result = expected_occurrences(L, k, num_sequences)  
print(f"O número esperado de ocorrências é aproximadamente: {result}")  