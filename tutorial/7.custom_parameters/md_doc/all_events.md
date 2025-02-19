## .GlobalParams

|| Название события | Параметры | Описание | Комментарий |                    
|---:|:---|:---|:---|:---|
|0|.GlobalParams||||


## Application
| | Название события | Версия события | Неймспейсы | Параметры | Описание | Комментарий | iOS |
|---:|:---|:---|:---|:---|:---|:---|:---|
|0|Application.Resumed|1||0. startup_info: Custom(see yaml spec)<br>1. startup_info_duplicate: Custom(see yaml spec)<br>|0. startup_info - My Custom Type<br>1. startup_info_duplicate - Параметр с дублирующимся кастомным типом<br>|Ивент разворачивания/старта приложения|В разработке https://your-tracker.com|
|1|Application.Resumed|2||0. startup_info_v2: Custom(see yaml spec)<br>1. list_unnamed_property: List<br>2. list_named_property: List<br>|0. startup_info_v2 - My Custom Type v2<br>1. list_unnamed_property - <br>2. list_named_property - <br>|Ивент с дублирующимся кастомным типом|В разработке https://your-tracker.com|

