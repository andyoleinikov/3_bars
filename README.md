# Ближайшие бары

Скрипт возвращает название самого большого и самого маленького бара из файла bars.json.
Также он возвращает название ближайшего бара для выбранных координат.
Файл можно скачать на [портале открытых данных правительства Москвы](https://data.mos.ru/opendata/7710881420-bary).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:
```bash
$ python bars.py <path to file> # possibly requires call of python3 executive instead of just python
```

### Пример запуска на Linux

```bash

$ python bars.py bars.json
Biggest bar name is: Спорт бар «Красная машина»
Smallest bar name is: БАР. СОКИ
Input your longitude: 37.621587946152012
Input your latitude: 55.765366956608361
Closest bar name is: Юнион Джек

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
