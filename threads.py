import threading

# Função para calcular a soma parcial da lista
def partial_sum(numbers, result, index):
    result[index] = sum(numbers)

def main():

    print("Caso 1: Lista Pequena")
    numbers = [1, 2, 3, 4]
    run_sum_with_threads(numbers)

    print("\nCaso 2: Lista Média")
    numbers = [5, 10, 15, 20, 25, 30, 35, 40]
    run_sum_with_threads(numbers)

    print("\nCaso 3: Lista Grande")
    numbers = [i for i in range(1, 101)]
    run_sum_with_threads(numbers)

# Função para dividir a lista e calcular a soma usando threads
def run_sum_with_threads(numbers):
    mid = len(numbers) // 2 
    part1 = numbers[:mid]
    part2 = numbers[mid:]

    result = [0, 0]  # Lista para armazenar resultados parciais
    
    # Cria threads para calcular a soma de cada parte
    thread1 = threading.Thread(target=partial_sum, args=(part1, result, 0))
    thread2 = threading.Thread(target=partial_sum, args=(part2, result, 1))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    # Soma total dos resultados parciais
    total_sum = result[0] + result[1]
    
    print(f"A soma total é: {total_sum}")

if __name__ == "__main__":
    main()
