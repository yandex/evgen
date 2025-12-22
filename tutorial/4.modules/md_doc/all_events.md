## .GlobalParams

|| Название события | Параметры | Описание | Комментарий |                    
|---:|:---|:---|:---|:---|
|0|.GlobalParams|0. globalParam: <em>String</em><br>|0. globalParam - Глобальный параметр, который добавится к каждомоу событию<br>|Эти параметры добавляются к параметрам каждого события.|


## AnotherNamespace
| | Название события | Версия события | Неймспейсы | Параметры | Описание | Комментарий | Android | iOS | Flutter | WebSmartTV | Unity |
|---:|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0|AnotherNamespace.Event1|1||0. reusedParam: String<br>|0. reusedParam - Параметр, который переиспользуется в нескольких событиях<br>|Первое событие с переиспользуемым параметром|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|
|1|AnotherNamespace.Event2|1||0. reusedParam: String<br>|0. reusedParam - Параметр, который переиспользуется в нескольких событиях<br>|Второе событие с переиспользуемым параметром|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|

## GlobalTypesDemo
| | Название события | Версия события | Неймспейсы | Параметры | Описание | Комментарий | Android | iOS | Flutter | WebSmartTV | Unity |
|---:|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0|GlobalTypesDemo.PageView|1||0. pageId: PageId<br>|0. pageId - ID страницы<br>|Просмотр страницы (использует глобальный тип PageId)|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|
|1|GlobalTypesDemo.Purchase|1||0. userId: UserId<br>1. contentId: ContentId<br>2. price: Price<br>3. timestamp: Timestamp<br>|0. userId - ID пользователя<br>1. contentId - ID контента<br>2. price - Цена покупки<br>3. timestamp - Время покупки<br>|Покупка контента (примитивные глобальные типы)|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|
|2|GlobalTypesDemo.ContentListView|1||0. items: ContentItems<br>1. metadata: Metadata.v1<br>|0. items - Элементы контента<br>1. metadata - Метаданные запроса (базовая версия)<br>|Просмотр списка контента (использует Metadata.v1)|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|
|3|GlobalTypesDemo.ContentListView|2||0. items: ContentItems<br>1. metadata: Metadata.v2<br>|0. items - Элементы контента<br>1. metadata - Метаданные запроса (расширенная версия с тегами)<br>|Просмотр списка контента (использует Metadata.v2 с тегами)|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|

## MyNamespace
| | Название события | Версия события | Неймспейсы | Параметры | Описание | Комментарий | Android | iOS | Flutter | WebSmartTV | Unity |
|---:|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0|MyNamespace.MyEvent|1||0. paramFromAnotherFile: String<br>1. batchParam1: String<br>2. batchParam2: String<br>3. stringParam: String<br>4. intParam: Int<br>5. сonstParam: "shop_page"<br>|0. paramFromAnotherFile - Параметр, описанный в отдельным файле.<br>1. batchParam1 - Параметр, описанный в отдельным файле.<br>2. batchParam2 - Параметр, описанный в отдельным файле.<br>3. stringParam - Парамтер типа String<br>4. intParam - Параметр типа Int<br>5. сonstParam - Constant parameter<br>|События со всеми возможными типами параметров|3.14 https://your-tracker.com|4.13 https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|

