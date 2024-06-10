// ignore_for_file: lines_longer_than_80_chars

/**
 * AUTO-GENERATED FILE. DO NOT MODIFY
 * This class was automatically generated.
 */

abstract interface class EvgenAnalyticsTracker {
  void trackEvent(String event, Map<String, dynamic> parameters);
}

abstract interface class EvgenAnalyticsGlobalParamsProvider {
  EvgenAnalyticsGlobalParams getGlobalParams();
}

abstract interface class EvgenAnalyticsPlatformParamsProvider {
  EvgenAnalyticsPlatformParams getPlatformParams();
}

/**
 * 0. globalParam - Глобальный параметр, который добавится к каждому событию
 */
class EvgenAnalyticsGlobalParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsGlobalParams(
    String globalParam,
  ) : parameters = {
          'globalParam': globalParam,
        };
}

class EvgenAnalyticsPlatformParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsPlatformParams() : parameters = const {};
}

class EvgenAnalytics {
  final EvgenAnalyticsTracker eventTracker;
  final EvgenAnalyticsGlobalParamsProvider globalParamsProvider;
  final EvgenAnalyticsPlatformParamsProvider platformParamsProvider;

  EvgenAnalytics(
    this.eventTracker,
    this.globalParamsProvider,
    this.platformParamsProvider,
  );

  void trackEvent(String event, Map<String, dynamic> parameters) =>
      eventTracker.trackEvent(
        event,
        {
          ...parameters,
          ...globalParamsProvider.getGlobalParams().parameters,
          ...platformParamsProvider.getPlatformParams().parameters,
        },
      );

  Map<String, dynamic> makeMeta(
    int eventVersion,
    Map<String, dynamic> interfaces,
  ) =>
      {
        'event': <String, dynamic> { 'version': eventVersion },
        'interfaces': interfaces,
      };

  /**
   * Первое событие с переиспользуемым параметром
   *
   * 0. reusedParam - Параметр, который переиспользуется в нескольких событиях
   */
  void anotherNamespaceEvent1({
    required String reusedParam,
  }) {
    final parameters = <String, dynamic>{
      'reusedParam': reusedParam,
    };

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('AnotherNamespace.Event1', parameters);
  }

  /**
   * Второе событие с переиспользуемым параметром
   *
   * 0. reusedParam - Параметр, который переиспользуется в нескольких событиях
   */
  void anotherNamespaceKebabCaseEvent2({
    required String reusedParam,
  }) {
    final parameters = <String, dynamic>{
      'reusedParam': reusedParam,
    };

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('AnotherNamespace.kebab-case-event-2', parameters);
  }

  /**
   * События со всеми возможными типами параметров
   *
   * 0. stringParam - Параметр типа String
   * 1. intParam - Параметр типа Int
   * 2. longIntParam - Параметр типа Long Int
   * 3. boolParam - Параметр типа Bool
   * 4. doubleParam - Параметр типа Double
   * 5. constParam - Параметр типа Const. Не участвует в сигнатуре функции, но логируется в при отправке в трекер
   * 6. enumParam - Параметр типа Enum. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
   * 7. enumParamInt - Параметр типа Enum Int. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
   * 8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages. Если какой-то enum используется больше одного раза, то лучше давать ему явное имя, разботчики смогут обращаться к нему однообразно
   * 9. dictParam - параметр типа Dict.
   * 10. dictElementType - параметр типа Dict енумов.
   * 11. typedDictParam - типизированный Dict.
   * 12. typedListParam - типизированный List.
   * 13. platformConst - Платформозависимая константа
   * 14. listOfInt - Список целочисленных параметров
   * 15. listOfDouble - Список флотовых параметров
   * 16. listOfString - Cписок строк
   * 17. listOfEnum - Cписок енумов
   */
  void myNamespaceMyEvent({
    String stringParam = 'val',
    int intParam = 42,
    required int longIntParam,
    bool boolParam = true,
    required double doubleParam,
    MyNamespaceMyEventEnumParam enumParam = MyNamespaceMyEventEnumParam.option1,
    MyNamespaceMyEventEnumParamInt enumParamInt = MyNamespaceMyEventEnumParamInt.num1,
    required Pages namedEnumParam,
    required Map<String, dynamic> dictParam,
    required Map<String, MyNamespaceMyEventEnumParam> dictElementType,
    required Map<String, dynamic> typedDictParam,
    required List<dynamic> typedListParam,
    List<int> listOfInt = const [],
    List<double> listOfDouble = const [],
    List<String> listOfString = const [],
    List<MyNamespaceMyEventEnumParam> listOfEnum = const [],
  }) {
    final parameters = <String, dynamic>{
      'stringParam': stringParam,
      'intParam': intParam,
      'longIntParam': longIntParam,
      'boolParam': boolParam,
      'doubleParam': doubleParam,
      'constParam': 'ValueToLog',
      'enumParam': enumParam.value,
      'enumParamInt': enumParamInt.value,
      'namedEnumParam': namedEnumParam.value,
      'dictParam': dictParam,
      'dictElementType': dictElementType,
      'typedDictParam': typedDictParam,
      'typedListParam': typedListParam,
      'platformConst': 'FlutterValue',
      'listOfInt': listOfInt,
      'listOfDouble': listOfDouble,
      'listOfString': listOfString,
      'listOfEnum': listOfEnum,
    };

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('MyNamespace.MyEvent', parameters);
  }
}

enum MyNamespaceMyEventEnumParam {
  option1('option1'),
  option2('option2'),
  option3('option3');

  final dynamic value;

  const MyNamespaceMyEventEnumParam(this.value);
}

enum Pages {
  screen1('screen_1'),
  screen2('screen_2'),
  screen3('screen_3');

  final dynamic value;

  const Pages(this.value);
}

enum MyNamespaceMyEventEnumParamInt {
  num1(1),
  num2(2),
  num3(3);

  final dynamic value;

  const MyNamespaceMyEventEnumParamInt(this.value);
}
