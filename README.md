# Ближайшие бары

Скрипт возвращает самый большой и самый маленький бар из файла bars.json.
Также он возвращает ближайший бар для выбранных координат.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
Biggest bar is: {'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'prope
rties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23b
f3a8', 'Attributes': {'global_id': 169375059, 'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'Ope
ratingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Даниловский район', 'Address': '
Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCount': 4
50, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
Smallest bar is: {'geometry': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'prope
rties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': '17adc22c-5c41-4e4b-872f-815b521f
2b53', 'Attributes': {'global_id': 20675518, 'Name': 'БАР. СОКИ', 'IsNetObject': 'нет', 'OperatingCompany': No
ne, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Митино', 'Address': 'Дубравная ули
ца, дом 34/29', 'PublicPhone': [{'PublicPhone': '(495) 258-94-19'}], 'SeatsCount': 0, 'SocialPrivileges': 'нет
'}}, 'type': 'Feature'}
Input your longitude: 5
Input your latitude: 4
Closest bar is: {'geometry': {'coordinates': [36.900000000253, 55.303299999814], 'type': 'Point'}, 'properties
': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'bb9eb30d-d16b-4821-8d9c-894b581ac762'
, 'Attributes': {'global_id': 281494712, 'Name': 'Staropramen', 'IsNetObject': 'нет', 'OperatingCompany': None
, 'AdmArea': 'Центральный административный округ', 'District': 'Красносельский район', 'Address': 'Садовая-Спа
сская улица, дом 19, корпус 1', 'PublicPhone': [{'PublicPhone': '(985) 069-34-47'}], 'SeatsCount': 50, 'Social
Privileges': 'нет'}}, 'type': 'Feature'}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
