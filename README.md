# MLops-HW

## Практическое задание 1.
Для запуска кода:
0. выполните команду ```git clone``` для данного проекта и перейдите в директорию проекта ```cd mlops-demo```
1. установите зависимости из файла requirements.txt, который находится в корне проекта - ```pip install -r requirements.txt```
2. перейдите в директорию *lab1* - ```cd lab1```
3. загляните в скрипт *job.sh* и если данные после работы скрипта понадобятся вам в будущем, то закоментируйте последнюю строку ```python3 ./mlops-demo/lab1/cleaner.py``` т.к. именно очищает систему от сгенерированных данных.
4. далее запустите скрипт *job.sh* командой ``./job.sh``` предварительно убедившись, что файл является исполняемым ```(ls -la && chmod u+x job.sh)```

Запуск отдельных скриптов из первоначальной директории до шага 0:
```python3 ./mlops-demo/lab1/data_creation.py``` - генерирует данные и записывает в соответствующие файлы (тренировочные и тестовые/валидационные)
```python3 ./mlops-demo/lab1/model_preprocessing.py``` - подготавливает данные для дальнейшей обработки
```python3 ./mlops-demo/lab1/model_preparation.py``` - создается и обучается на тренировочных данных модель, после чего записывается в отдельный файл
```python3 ./mlops-demo/lab1/model_testing.py``` - проверяет метрики модели на тестовых данных
