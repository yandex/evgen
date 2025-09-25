// ignore_for_file: lines_longer_than_80_chars
// ignore_for_file: one_member_abstracts

// AUTO-GENERATED FILE. DO NOT MODIFY
// This class was automatically generated.

abstract interface class IEvgenAnalyticsTracker {
  void trackEvent(String event, Map<String, dynamic> parameters);
}

abstract interface class IEvgenAnalyticsGlobalParamsProvider {
  EvgenAnalyticsGlobalParams getGlobalParams();
}

abstract interface class IEvgenAnalyticsPlatformParamsProvider {
  EvgenAnalyticsPlatformParams getPlatformParams();
}

/// 0. globalParam - Глобальный параметр, который добавится к каждомоу событию
class EvgenAnalyticsGlobalParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsGlobalParams({
    required String globalParam,
  }) : parameters = {
          'globalParam': globalParam,
        };
}

class EvgenAnalyticsPlatformParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsPlatformParams() : parameters = const {};
}

class EvgenAnalytics {
  final IEvgenAnalyticsTracker eventTracker;
  final IEvgenAnalyticsGlobalParamsProvider globalParamsProvider;
  final IEvgenAnalyticsPlatformParamsProvider platformParamsProvider;

  EvgenAnalytics({
    required this.eventTracker,
    required this.globalParamsProvider,
    required this.platformParamsProvider,
  });

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

  ///  Первое событие с переиспользуемым параметром
  ///
  ///  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
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

  ///  Второе событие с переиспользуемым параметром
  ///
  ///  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
  void anotherNamespaceEvent2({
    required String reusedParam,
  }) {
    final parameters = <String, dynamic>{
      'reusedParam': reusedParam,
    };

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('AnotherNamespace.Event2', parameters);
  }

  ///  События со всеми возможными типами параметров
  ///
  ///  1. paramFromAnotherFile - Параметр, описанный в отдельным файле.
  ///  2. batchParam1 - Параметр, описанный в отдельным файле.
  ///  3. batchParam2 - Параметр, описанный в отдельным файле.
  ///  4. stringParam - Парамтер типа String
  ///  5. intParam - Параметр типа Int
  void myNamespaceMyEvent({
    required String paramFromAnotherFile,
    required String batchParam1,
    required String batchParam2,
    String stringParam = 'val1',
    int intParam = 42,
  }) {
    final parameters = <String, dynamic>{
      'paramFromAnotherFile': paramFromAnotherFile,
      'batchParam1': batchParam1,
      'batchParam2': batchParam2,
      'stringParam': stringParam,
      'intParam': intParam,
      'сonstParam': 'shop_page',
    };

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('MyNamespace.MyEvent', parameters);
  }
}

