# НейроТексты
Микросервис для составления тестов для бригады специального подвижного состава (СПС)

Официальная страница проекта: https://wish.rut.digital/tproduct/795847057-833187679012-neiroteksti

# Содержимое
- [О сервисе](#о-сервисе)
- [Стек](#стек)
- [Machine Learning](#machine-learning)

# О сервисе
*Микросервис под линукс (предпочтительно debian) для работы в кластере серверов приложений портала отчётности АСУ СПС НП с характеристиками: 24 ядра, 64 ГБ, 200 ГБ*

**AS IS**

Есть хранилище с данными в которое загружают [документы](https://drive.google.com/file/d/15yn1O_j-OSAQzrxV7L6M3a_bGqlgygM5/view?usp=drive_link). Далее по этим документам специальный человек составляет руками/ChatGPT тесты а потом загружает все в АСУ СПС. Примерно вот так это выглядит [тык](https://drive.google.com/file/d/1dQ4vWZLzzHfbaKpxuZpZKTcaF6mc9yOF/view?usp=drive_link)

**TO BE**

Из хранилища подлягиваются pdf на их основе создается текст и автоматически загружается в АСУ СПС

# Стек
ЯП: Python
* Transformers
* Pandas
* PyTorch
* FastAPI 
* Docker (optional)
* PyPDF2
* Pdfplumber
* easyocr

# Machine Learning
1. Распознать текст из PDF
2. Сгенерировать тест
   * Суммаризация
   * Вопрос по суммаризированому тексту
   * Ответ по суммаризированому тексту
   * Переводчик (optional)
   
**ИЛИ**

Использовать готовую модель для генерации тестов

**ИЛИ**

Использовать LLM (Типа ChatGPT, Mistral, llama) с правильным промптом

# ML идеи
Модель для генерации тестов (не работает, нужно фиксить) [тык](https://huggingface.co/valhalla/t5-small-qg-hl)

Неплохой переводчик, но мб есть лучше [тык](https://huggingface.co/deepset/roberta-base-squad2)

Хорошо отвечает на вопросы [тык](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en)

Модель которая сможет задавать вопрос по тексту [не самая лучшая, но пока лучше не нашел](https://huggingface.co/ZhangCheng/T5v1.1-Base-Fine-Tuned-for-Question-Generation)

Все эти модели работают только на английском языке
   
