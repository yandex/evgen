## .GlobalParams

|| Название события | Параметры | Описание | Комментарий |                    
|---:|:---|:---|:---|:---|
|0|.GlobalParams|0. appVersion: <code>String</code><br/>1. userId: <code>Long Int</code><br/>2. deviceId: <code>String</code><br/>|0. appVersion - Версия приложения<br/>1. userId - ID пользователя<br/>2. deviceId - ID устройства<br/>|Эти параметры добавляются к параметрам каждого события.|

## .PlatformParams

| | Платформа | Параметры | Описание |
|---:|:---|:---|:---|
|0|web_smart_tv|0. tvModel: <code>String</code><br/>1. firmwareVersion: <code>String</code><br/>|0. tvModel - Модель ТВ<br/>1. firmwareVersion - Версия прошивки<br/>|
|1|ios|0. browserName: <code>String</code><br/>1. browserVersion: <code>String</code><br/>|0. browserName - Имя браузера<br/>1. browserVersion - Версия браузера<br/>|

## MyMovies
| | Название события | Версия события | Параметры | Описание | Комментарий | ios | web_smart_tv | android |
|---:|:---|:---|:---|:---|:---|:---|:---|:---|
|0|MyMovies.SelectionItem.Navigated|1|0. from: "MyMoviesScreen"<br>1. to: Enum(MovieScreen, SelectionScreen)<br>2. cardPosition: Int<br>3. contentId: String<br>|0. from - Страница, с которой произошел переход<br>1. to - Страница, на которою произошел переход<br>2. cardPosition - Позиция карточки в подборке<br>3. contentId - ID контента, по карточке которого произошел переход<br>|Переход по карточке контента|В разработке https://link.to/ticket-123|1.0 - 2.0 https://link.to/ticket-124|В разработке https://link.to/ticket-127|
|1|MyMovies.SelectionItem.Navigated|2|0. from: "MyMoviesScreen"<br>1. to: Enum(MovieScreen, SelectionScreen)<br>2. cardPosition: Int<br>3. contentId: String<br>4. rating: Double<br>|0. from - Страница, с которой произошел переход<br>1. to - Страница, на которою произошел переход<br>2. cardPosition - Позиция карточки в подборке<br>3. contentId - ID контента, по карточке которого произошел переход<br>4. rating - Рейтинг контента<br>|Переход по карточке контента||В разработке https://link.to/ticket-125|В разработке https://link.to/ticket-127|

