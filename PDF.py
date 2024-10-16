import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import pandas as pd

# Настройка для Windows
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    path_to_poppler_exe = Path(r"C:\Program Files\poppler-24.08.0\Library\bin")  # Укажите правильный путь к Poppler
else:
    path_to_poppler_exe = None

# Путь к папке с PDF файлами
pdf_folder = Path(r"PDF")
output_csv = Path(r"output_data.csv")

# Список для хранения данных
data = []


def main():
    ''' Главная точка выполнения программы '''
    pdf_files = list(pdf_folder.glob("*.pdf"))
    total_files = len(pdf_files)

    print(f"Найдено {total_files} PDF файлов в папке '{pdf_folder}'.")

    for pdf_file in pdf_files:
        print(f"\nОбработка файла: {pdf_file.name}")

        with TemporaryDirectory() as tempdir:
            image_file_list = []

            # Конвертация PDF в изображения
            print("Конвертация PDF в изображения...")
            if platform.system() == "Windows":
                pdf_pages = convert_from_path(pdf_file, 500, poppler_path=path_to_poppler_exe)
            else:
                pdf_pages = convert_from_path(pdf_file, 500)

            # Итерация по страницам
            for page_number, page in enumerate(pdf_pages, start=1):
                filename = f"{tempdir}/page_{page_number:03}.jpg"
                page.save(filename, "JPEG")
                image_file_list.append(filename)

            print(f"Конвертировано {len(image_file_list)} страниц в изображения.")

            # Извлечение текста из изображений
            full_text = ''
            print("Извлечение текста из изображений...")
            for image_file in image_file_list:
                # Извлечение текста из изображения
                text = pytesseract.image_to_string(Image.open(image_file), lang='rus')  # Указание русского языка
                full_text += text + '\n'

            # Добавляем только название PDF и извлечённый текст
            data.append([pdf_file.name, full_text.strip()])

            print(f"Текст успешно извлечен из {len(image_file_list)} изображений.")

    # Создание DataFrame и сохранение в CSV файл
    print("\nСоздание CSV файла с извлеченными данными...")
    df = pd.DataFrame(data, columns=['PDF Name', 'Extracted Text'])
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')

    print(f"Данные успешно сохранены в '{output_csv}'.")


if __name__ == "__main__":
    main()
