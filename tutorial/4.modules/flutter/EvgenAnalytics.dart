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

    final interfacesDict = <String, dynamic>{};

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

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('AnotherNamespace.Event2', parameters);
  }

  ///  Просмотр страницы (использует глобальный тип PageId)
  ///
  ///  1. pageId - ID страницы
  void globalTypesDemoPageView({
    required PageId pageId,
  }) {
    final parameters = <String, dynamic>{
      'pageId': pageId,
    };

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('GlobalTypesDemo.PageView', parameters);
  }

  ///  Покупка контента (примитивные глобальные типы)
  ///
  ///  1. userId - ID пользователя
  ///  2. contentId - ID контента
  ///  3. price - Цена покупки
  ///  4. timestamp - Время покупки
  void globalTypesDemoPurchase({
    required UserId userId,
    required ContentId contentId,
    required Price price,
    required Timestamp timestamp,
  }) {
    final parameters = <String, dynamic>{
      'userId': userId,
      'contentId': contentId,
      'price': price,
      'timestamp': timestamp,
    };

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('GlobalTypesDemo.Purchase', parameters);
  }

  ///  Просмотр списка контента (использует Metadata.v1)
  ///
  ///  1. items - Элементы контента
  ///  2. metadata - Метаданные запроса (базовая версия)
  void globalTypesDemoContentListView({
    required ContentItems items,
    required MetadataV1 metadata,
  }) {
    final parameters = <String, dynamic>{
      'items': items,
      'metadata': metadata,
    };

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('GlobalTypesDemo.ContentListView', parameters);
  }

  ///  Просмотр списка контента (использует Metadata.v2 с тегами)
  ///
  ///  1. items - Элементы контента
  ///  2. metadata - Метаданные запроса (расширенная версия с тегами)
  void globalTypesDemoContentListViewV2({
    required ContentItems items,
    required MetadataV2 metadata,
  }) {
    final parameters = <String, dynamic>{
      'items': items,
      'metadata': metadata,
    };

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(2, interfacesDict);
    trackEvent('GlobalTypesDemo.ContentListView', parameters);
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

    final interfacesDict = <String, dynamic>{};

    parameters['_meta'] = makeMeta(1, interfacesDict);
    trackEvent('MyNamespace.MyEvent', parameters);
  }
}


typedef UserId = String;

typedef ContentId = String;

typedef Timestamp = int;

typedef Price = double;

typedef ViewCount = int;

enum PageId {
  home('home'),
  catalog('catalog'),
  movieCard('movie_card'),
  seriesCard('series_card');

  final dynamic value;

  const PageId(this.value);
}

typedef MetadataV1 = Map<String, dynamic>;

typedef MetadataV2 = Map<String, dynamic>;

typedef ContentItems = List<dynamic>;
