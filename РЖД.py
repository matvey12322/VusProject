def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        if line.startswith('• '):
            # Удаляем символ • и пробел в начале строки
            line = line[2:]
            # Разделяем строку на сокращение и расшифровку
            parts = line.split(' - ', 1)
            if len(parts) == 2:
                abbreviation, description = parts
                processed_lines.append(f"{abbreviation.strip()},{description.strip()}\n")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

def main():
    input_file = 'output_РЖД.txt'  # Имя входного файла
    output_file = 'Dictionary(RZD).txt'  # Имя выходного файла

    process_file(input_file, output_file)
    print(f"Обработка завершена. Результат сохранен в {output_file}")

if __name__ == "__main__":
    main()
