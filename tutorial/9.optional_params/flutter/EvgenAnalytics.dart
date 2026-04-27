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

/// 0. optionalGlobal - Необязательный глобальный параметр
class EvgenAnalyticsGlobalParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsGlobalParams({
    String? optionalGlobal,
  }) : parameters = {
          'optionalGlobal': optionalGlobal,
        };
}

/// 0. optionalPlatformHint - Необязательная подсказка с платформы
class EvgenAnalyticsPlatformParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsPlatformParams({
    String? optionalPlatformHint,
  }) : parameters = {
          'optionalPlatformHint': optionalPlatformHint,
        };
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
    mergedParameters.removeWhere((_, value) => value == null);
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

  ///  Событие с optional-параметрами; клиент может не передавать их, тогда при merge null-ключи отфильтровываются
  ///
  ///  1. requiredId - Обязательный идентификатор
  ///  2. optionalContext - Необязательный контекст
  ///  3. optionalScore - Необязательное числовое значение
  void optionalNamespaceDemoEvent({
    required String requiredId,
    String? optionalContext,
    int? optionalScore,
  }) {
    final parameters = <String, dynamic>{
      'requiredId': requiredId,
      'optionalContext': optionalContext,
      'optionalScore': optionalScore,
    };

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('OptionalNamespace.DemoEvent', parameters);
  }
}

