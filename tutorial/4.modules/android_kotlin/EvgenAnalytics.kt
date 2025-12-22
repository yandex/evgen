/**
 * AUTO-GENERATED FILE. DO NOT MODIFY
 * This class was automatically generated.
 */
/* ktlint-disable */

interface EvgenAnalyticsTracker {
    fun trackEvent(event: String, parameters: Map<String, Any>)
}

interface EvgenAnalyticsGlobalParamsProvider {
    fun getGlobalParams(): EvgenAnalyticsGlobalParams
}

interface EvgenAnalyticsPlatformParamsProvider {
    fun getPlatformParams(): EvgenAnalyticsPlatformParams
}

/**
 * 0. globalParam - Глобальный параметр, который добавится к каждомоу событию
 */
class EvgenAnalyticsGlobalParams(
    globalParam: String,
) {
    val parameters: Map<String, Any> = mapOf(
        "globalParam" to globalParam,
    )
}

class EvgenAnalyticsPlatformParams(
) {
    val parameters: Map<String, Any> = mapOf(
    )
}

class EvgenAnalytics(
    private val eventTracker: EvgenAnalyticsTracker,
    private val globalParamsProvider: EvgenAnalyticsGlobalParamsProvider,
    private val platformParamsProvider: EvgenAnalyticsPlatformParamsProvider,
) {
    private fun trackEvent(event: String, parameters: MutableMap<String, Any>) {
        val mergedParameters: HashMap<String, Any> = HashMap<String, Any>()
        mergedParameters.putAll(parameters)
        mergedParameters.putAll(globalParamsProvider.getGlobalParams().parameters)
        mergedParameters.putAll(platformParamsProvider.getPlatformParams().parameters)
        eventTracker.trackEvent(event, mergedParameters)
    }

    private fun makeMeta(event_version: Int, interfaces: Map<String, Any>): Map<String, Any> {
        val metaDict = HashMap<String, Any>()
        val eventDict = HashMap<String, Any>()
        eventDict["version"] = event_version
        metaDict["event"] = eventDict
        metaDict["interfaces"] = interfaces
        return metaDict
    }

    typealias UserId = String
    typealias ContentId = String
    typealias Timestamp = Long
    typealias Price = Double
    typealias ViewCount = Int
    enum class PageId(val eventValue: String) {
        Home("home"),
        Catalog("catalog"),
        MovieCard("movie_card"),
        SeriesCard("series_card"),
    }
    typealias MetadataV1 = Map<String, Any>
    typealias MetadataV2 = Map<String, Any>
    typealias ContentItems = List<Any>

    /**
     *  Первое событие с переиспользуемым параметром
     *
     *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    fun anotherNamespaceEvent1(
        reusedParam: String,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["reusedParam"] = reusedParam
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("AnotherNamespace.Event1", parameters)
    }


    /**
     *  Второе событие с переиспользуемым параметром
     *
     *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    fun anotherNamespaceEvent2(
        reusedParam: String,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["reusedParam"] = reusedParam
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("AnotherNamespace.Event2", parameters)
    }


    /**
     *  Просмотр страницы (использует глобальный тип PageId)
     *
     *  1. pageId - ID страницы
     */
    fun globalTypesDemoPageView(
        pageId: PageId,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["pageId"] = pageId
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("GlobalTypesDemo.PageView", parameters)
    }


    /**
     *  Покупка контента (примитивные глобальные типы)
     *
     *  1. userId - ID пользователя
     *  2. contentId - ID контента
     *  3. price - Цена покупки
     *  4. timestamp - Время покупки
     */
    fun globalTypesDemoPurchase(
        userId: UserId,
        contentId: ContentId,
        price: Price,
        timestamp: Timestamp,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["userId"] = userId
        parameters["contentId"] = contentId
        parameters["price"] = price
        parameters["timestamp"] = timestamp
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("GlobalTypesDemo.Purchase", parameters)
    }


    /**
     *  Просмотр списка контента (использует Metadata.v1)
     *
     *  1. items - Элементы контента
     *  2. metadata - Метаданные запроса (базовая версия)
     */
    fun globalTypesDemoContentListView(
        items: ContentItems,
        metadata: MetadataV1,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["items"] = items
        parameters["metadata"] = metadata
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("GlobalTypesDemo.ContentListView", parameters)
    }


    /**
     *  Просмотр списка контента (использует Metadata.v2 с тегами)
     *
     *  1. items - Элементы контента
     *  2. metadata - Метаданные запроса (расширенная версия с тегами)
     */
    fun globalTypesDemoContentListViewV2(
        items: ContentItems,
        metadata: MetadataV2,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["items"] = items
        parameters["metadata"] = metadata
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(2, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("GlobalTypesDemo.ContentListView", parameters)
    }


    /**
     *  События со всеми возможными типами параметров
     *
     *  1. paramFromAnotherFile - Параметр, описанный в отдельным файле.
     *  2. batchParam1 - Параметр, описанный в отдельным файле.
     *  3. batchParam2 - Параметр, описанный в отдельным файле.
     *  4. stringParam - Парамтер типа String
     *  5. intParam - Параметр типа Int
     */
    fun myNamespaceMyEvent(
        paramFromAnotherFile: String,
        batchParam1: String,
        batchParam2: String,
        stringParam: String = "val1",
        intParam: Int = 42,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["paramFromAnotherFile"] = paramFromAnotherFile
        parameters["batchParam1"] = batchParam1
        parameters["batchParam2"] = batchParam2
        parameters["stringParam"] = stringParam
        parameters["intParam"] = intParam.toString()
        parameters["сonstParam"] = "shop_page"
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("MyNamespace.MyEvent", parameters)
    }

}
