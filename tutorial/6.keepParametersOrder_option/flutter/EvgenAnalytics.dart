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

class EvgenAnalyticsGlobalParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsGlobalParams() : parameters = const {};
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
  ///  1. firstParam - Первый параметр
  ///  2. paramFromAnotherFile - Параметр, описанный в отдельным файле.
  ///  3. reusedParam - Description
  ///  4. batchParam1 - Параметр, описанный в отдельным файле.
  ///  5. batchParam2 - Параметр, описанный в отдельным файле.
  ///  6. lastParam - Последний параметр
  void namespaceEvent({
    required int firstParam,
    required String paramFromAnotherFile,
    required String reusedParam,
    required String batchParam1,
    required String batchParam2,
    required String lastParam,
  }) {
    final parameters = <String, dynamic>{
      'firstParam': firstParam,
      'paramFromAnotherFile': paramFromAnotherFile,
      'reusedParam': reusedParam,
      'batchParam1': batchParam1,
      'batchParam2': batchParam2,
      'lastParam': lastParam,
    };

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('Namespace.Event', parameters);
  }
}

