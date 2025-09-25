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

  ///  Показ экрана магазина
  ///
  ///  1. page - Название страницы
  ///  2. pageId - Идентификатор страницы
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

  ///  Показ экрана магазина
  ///
  ///  1. page - Название страницы
  ///  2. movieName - Название фильма
  ///  3. movieId - Идентификатор фильма
  ///  4. pageId - Идентификатор страницы
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

  ///  Показ экрана магазина
  ///
  ///  1. page - Название страницы
  ///  2. movieName - Название фильма
  ///  3. pageId - Идентификатор страницы
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

