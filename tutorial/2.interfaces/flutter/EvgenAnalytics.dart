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
   * Показ экрана магазина
   *
   * 0. page - Название страницы
   * 1. pageId - Идентификатор страницы
   */
  void shopShowed({
    required String page,
    required int pageId,
  }) {
    final parameters = <String, dynamic>{
      'page': page,
      'pageId': pageId,
    };

    final interfacesDict = <String, dynamic>{
      'MyInterfaces.Page': <String, dynamic>{ 'version': 1 },
    };

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('Shop.Showed', parameters);
  }

  /**
   * Показ экрана магазина
   *
   * 0. page - Название страницы
   * 1. movieName - Название фильма
   * 2. movieId - Идентификатор фильма
   * 3. pageId - Идентификатор страницы
   */
  void showcaseMovieShowed({
    required String page,
    required String movieName,
    required int movieId,
    required int pageId,
  }) {
    final parameters = <String, dynamic>{
      'page': page,
      'movieName': movieName,
      'movieId': movieId,
      'pageId': pageId,
    };

    final interfacesDict = <String, dynamic>{
      'MyInterfaces.Page': <String, dynamic>{ 'version': 1 },
      'MyInterfaces.Movie': <String, dynamic>{ 'version': 2 },
    };

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('Showcase.Movie.Showed', parameters);
  }

  /**
   * Показ экрана магазина
   *
   * 0. page - Название страницы
   * 1. movieName - Название фильма
   * 2. pageId - Идентификатор страницы
   */
  void showcaseTVShowShowed({
    required String page,
    required String movieName,
    required int pageId,
  }) {
    final parameters = <String, dynamic>{
      'page': page,
      'movieName': movieName,
      'pageId': pageId,
    };

    final interfacesDict = <String, dynamic>{
      'MyInterfaces.Page': <String, dynamic>{ 'version': 1 },
      'MyInterfaces.Movie': <String, dynamic>{ 'version': 1 },
    };

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('Showcase.TVShow.Showed', parameters);
  }
}

