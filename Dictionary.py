import pandas as pd
from pathlib import Path

# Путь к файлам
input_csv = Path("output_data.csv")
dictionary_file = Path("Dictionary(RZD).txt")
output_csv = Path("dic_output.csv")


def load_dictionary(file_path):
    ''' Загружает словарь сокращений из файла '''
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if ',' in line:
                key, value = line.strip().split(',', 1)
                dictionary[key.strip()] = value.strip()
    return dictionary


def expand_abbreviations(text, dictionary):
    ''' Заменяет сокращения на их расшифровки '''
    changes_count = {}
    for abbreviation, full_form in dictionary.items():
        occurrences = text.count(abbreviation)
        if occurrences > 0:
            text = text.replace(abbreviation, full_form)
            changes_count[abbreviation] = (full_form, occurrences)  # Сохраняем полное название и количество
    return text, changes_count


def main():
    # Загрузка данных из CSV файла
    df = pd.read_csv(input_csv, encoding='utf-8-sig')

    # Загрузка словаря сокращений
    print("Загрузка словаря сокращений...")
    dictionary = load_dictionary(dictionary_file)

    # Обработка второго столбца и замена сокращений
    print("Начинаем замену сокращений в тексте...")
    changes_summary = {}

    for index, row in df.iterrows():
        original_text = row['Extracted Text']
        expanded_text, changes = expand_abbreviations(original_text, dictionary)
        df.at[index, 'Extracted Text'] = expanded_text

        # Сохранение изменений
        for abbr, (full_form, count) in changes.items():
            if abbr in changes_summary:
                changes_summary[abbr][1] += count  # Суммируем количество замен
            else:
                changes_summary[abbr] = [full_form, count]  # Сохраняем полное название и количество

    # Сохранение результата в новый CSV файл
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')

    # Вывод статистики изменений
    print("\nЗамены завершены. Изменения:")
    for abbr, (full_form, count) in changes_summary.items():
        print(f"{abbr} ({full_form}): заменено {count} раз(а)")


if __name__ == "__main__":
    main()
