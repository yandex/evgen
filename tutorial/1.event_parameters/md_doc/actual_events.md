## .GlobalParams

|| Название события | Параметры | Описание | Комментарий |                    
|---:|:---|:---|:---|:---|
|0|.GlobalParams|0. globalParam: <code>String</code><br/>|0. globalParam - Глобальный параметр, который добавится к каждомоу событию|Эти параметры добавляются к параметрам каждого события.|


## AnotherNamespace
| | Название события | Версия события | Параметры | Описание | Комментарий | Android | iOS | WebSmartTV |
|---:|:---|:---|:---|:---|:---|:---|:---|:---|
|0|AnotherNamespace.Event1|1|0. reusedParam: String<br>|0. reusedParam - Параметр, который переиспользуется в нескольких событиях<br>|Первое событие с переиспользуемым параметром|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|
|1|AnotherNamespace.Event2|1|0. reusedParam: String<br>|0. reusedParam - Параметр, который переиспользуется в нескольких событиях<br>|Второе событие с переиспользуемым параметром|В разработке https://your-tracker.com|В разработке https://your-tracker.com|В разработке https://your-tracker.com|

## MyNamespace
| | Название события | Версия события | Параметры | Описание | Комментарий | Android | iOS | WebSmartTV |
|---:|:---|:---|:---|:---|:---|:---|:---|:---|
|0|MyNamespace.MyEvent|1|0. stringParam: String<br>1. intParam: Int<br>2. longIntParam: Long Int<br>3. boolParam: Bool<br>4. doubleParam: Double<br>5. constParam: "ValueToLog"<br>6. enumParam: Enum(option1, option2, option3)<br>7. enumParamInt: Enum(1, 2, 3)<br>8. namedEnumParam: Enum(Pages: screen_1, screen_2, screen_3)<br>9. dictParam: Dict<br>10. platformConst: PlatformConst(Android: AndroidValue,iOS: iOSValue,WebSmartTV: WebSmartTVValue,)<br>11. listOfInt: List<br>12. listOfDouble: List<br>13. listOfString: List<br>|0. stringParam - Параметр типа String<br>1. intParam - Параметр типа Int<br>2. longIntParam - Параметр типа Long Int<br>3. boolParam - Параметр типа Bool<br>4. doubleParam - Параметр типа Double<br>5. constParam - Параметр типа Const. Не участвует в сигнатуре функции, но логируется в при отправке в трекер<br>6. enumParam - Параметр типа Enum. При логировании можновыбрать только один вариант. В коде имееттип MyNamespaceMyEventEnumparam<br>7. enumParamInt - Параметр типа Enum Int. При логировании можновыбрать только один вариант. В коде имееттип MyNamespaceMyEventEnumparam<br>8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages.Если какой-то enum используется больше одного раза,то лучше давать ему явное имя, разботчики смогутобращаться к нему однообразно<br>9. dictParam - параметр типа Dict.<br>10. platformConst - Платформозависимая константа<br>11. listOfInt - Список целочисленных параметров<br>12. listOfDouble - Список флотовых параметров<br>13. listOfString - Cписок строк<br>|События со всеми возможными типами параметров|3.14 https://your-tracker.com|4.13 https://your-tracker.com|В разработке https://your-tracker.com|

