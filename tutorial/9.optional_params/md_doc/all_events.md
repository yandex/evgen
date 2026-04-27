## .GlobalParams

|| Название события | Параметры | Описание | Комментарий |                    
|---:|:---|:---|:---|:---|
|0|.GlobalParams|0. optionalGlobal: <em>String</em><br>|0. optionalGlobal - Необязательный глобальный параметр<br>|Глобальные параметры для tutorial optional + not_send_null_parameters.|

## .PlatformParams

| | Платформа | Параметры | Описание |
|---:|:---|:---|:---|
|0|Android|0. optionalPlatformHint: <em>String</em><br>|0. optionalPlatformHint - Необязательная подсказка с платформы<br>|
|1|iOS|0. optionalPlatformHint: <em>String</em><br>|0. optionalPlatformHint - Необязательная подсказка с платформы<br>|
|2|Flutter|0. optionalPlatformHint: <em>String</em><br>|0. optionalPlatformHint - Необязательная подсказка с платформы<br>|
|3|WebSmartTV|0. optionalPlatformHint: <em>String</em><br>|0. optionalPlatformHint - Необязательная подсказка с платформы<br>|
|4|Unity|0. optionalPlatformHint: <em>String</em><br>|0. optionalPlatformHint - Необязательная подсказка с платформы<br>|

## OptionalNamespace
| | Название события | Версия события | Неймспейсы | Параметры | Описание | Комментарий | Android | iOS | Flutter | WebSmartTV | Unity |
|---:|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0|OptionalNamespace.DemoEvent|1||0. requiredId: String<br>1. optionalContext: String<br>2. optionalScore: Int<br><strong>Android:</strong><br>0. androidOnlyLocal: String<br>|0. requiredId - Обязательный идентификатор<br>1. optionalContext - Необязательный контекст<br>2. optionalScore - Необязательное числовое значение<br><strong>Android:</strong><br>0. androidOnlyLocal - <br>|Событие с optional-параметрами; клиент может не передавать их, тогда при merge null-ключи отфильтровываются|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|

