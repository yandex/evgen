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

  void trackEvent(String event, Map<String, dynamic> parameters) {
    final mergedParameters = <String, dynamic>{
      ...parameters,
      ...globalParamsProvider.getGlobalParams().parameters,
      ...platformParamsProvider.getPlatformParams().parameters,
    };
    eventTracker.trackEvent(event, mergedParameters);
  }

  Map<String, dynamic> makeMeta(
    int eventVersion,
    Map<String, dynamic> interfaces,
  ) =>
      {
        'event': <String, dynamic> { 'version': eventVersion },
        'interfaces': interfaces,
      };

  ///  Демонстрация param_name_case: одинаковое событие для Android, iOS, Flutter, WebSmartTV, Unity.
  ///  
  ///
  ///  1. user_session_id - Ключ в YAML в snake_case
  ///  2. screenTitle - Ключ в YAML в camelCase (без подчёркиваний)
  void caseDemoSampleEvent({
    String userSessionId = 'guest',
    required String screenTitle,
  }) {
    final parameters = <String, dynamic>{
      'USER_SESSION_ID': userSessionId,
      'SCREEN_TITLE': screenTitle,
    };

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('CaseDemo.SampleEvent', parameters);
  }
}

