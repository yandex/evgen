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

  ///  Also event description
  ///
  ///  Опциональное поле, сюда можно написать, например, требования по логированию или дать ссылку.
  void alsoMyEventLogged() {
    final parameters = const <String, dynamic>{};

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('AlsoMyEvent.Logged', parameters);
  }

  ///  Forced Event Name
  ///
  ///  Если нужно, чтобы в качестве имени события вместо конкатенированных через точку неймспесов было какое-то кастомное значение, то можно использовать поле "force_event_name"
  void forcedNamesMyCustomEvent() {
    final parameters = const <String, dynamic>{};

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('my-custom-event-name', parameters);
  }

  ///  Event description
  void myEvent() {
    final parameters = const <String, dynamic>{};

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('MyEvent', parameters);
  }
}

