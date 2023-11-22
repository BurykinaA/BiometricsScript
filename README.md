# BiometricsScript
face anti-spoofing solution for Biometrics hackathon

## Использование скрипта
Эта инструкция позволит запустить скрипт на операционных системах Linux и Windows.

### Шаг 1: Клонировать репозиторий
Если у вас еще нет локальной копии репозитория, клонируйте его из Git-репозитория:

```bash
git clone https://github.com/BurykinaA/BiometricsScript.git
cd BiometricsScript
```

### Шаг 2: Загрузить фотографии для проверки
Фотографии загружаются в папку *ImagesForTest*

### Шаг 3: Запуск скрипта
```bash
python make_prediction.py
```

### Результат
Результат проверки выводится в консоль и сохраняется в *result.csv* в формате --название файла изображения --результат 'real' или 'fake'
