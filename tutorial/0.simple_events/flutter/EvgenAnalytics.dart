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

class EvgenAnalyticsGlobalParams {
  final Map<String, dynamic> parameters;

  EvgenAnalyticsGlobalParams() : parameters = const {};
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
   * Also event description
   *
   */
  void alsoMyEventLogged() {
    final parameters = const <String, dynamic>{};

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('AlsoMyEvent.Logged', parameters);
  }

  /**
   * Forced Event Name
   *
   */
  void forcedNamesMyCustomEvent() {
    final parameters = const <String, dynamic>{};

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('my-custom-event-name', parameters);
  }

  /**
   * Event description
   *
   */
  void myEvent() {
    final parameters = const <String, dynamic>{};

    final interfacesDict = const <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('MyEvent', parameters);
  }
}

