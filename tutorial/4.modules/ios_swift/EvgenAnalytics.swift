/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */

import Foundation

public protocol EvgenAnalyticsTracker {
    func trackEvent(_ event: String, withOptions options: [String: Any])
}

public protocol EvgenAnalyticsGlobalParamsProvider: AnyObject {
    func getGlobalParams() -> EvgenAnalyticsGlobalParams
}

public protocol EvgenAnalyticsPlatformParamsProvider: AnyObject {
    func getPlatformParams() -> EvgenAnalyticsPlatformParams
}

/**
 * 0. globalParam - Глобальный параметр, который добавится к каждомоу событию
 */
public struct EvgenAnalyticsGlobalParams {
    public var globalParam: String

    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["globalParam"] = globalParam
        return options
    }

    public init(globalParam: String) {
        self.globalParam = globalParam
    }
}

public struct EvgenAnalyticsPlatformParams {
    
    public func makeOptions() -> [String: Any] {
        let options: [String: Any] = [:]
        return options
    }
    
    public init() {
    }
}

public final class EvgenAnalytics {
    public init(eventTracker: EvgenAnalyticsTracker, globalParamsProvider: EvgenAnalyticsGlobalParamsProvider, platformParamsProvider: EvgenAnalyticsPlatformParamsProvider) {
        self.eventTracker = eventTracker
        self.globalParamsProvider = globalParamsProvider
        self.platformParamsProvider = platformParamsProvider
    }
    
    private let eventTracker: EvgenAnalyticsTracker
    private let globalParamsProvider: EvgenAnalyticsGlobalParamsProvider
    private let platformParamsProvider: EvgenAnalyticsPlatformParamsProvider
    
    private func trackEvent(_ event: String, withOptions options: [String: Any]) {
        var mergedOptions = options
        let globalParams = globalParamsProvider.getGlobalParams()
        for (key, value) in globalParams.makeOptions() {
            assert(mergedOptions[key] == nil, "Global parameter conflicts with event parameter: \(key). Will be overwritten.")
            mergedOptions[key] = value
        }
        let platformParams = platformParamsProvider.getPlatformParams()
        for (key, value) in platformParams.makeOptions() {
            assert(mergedOptions[key] == nil, "Platform parameter conflicts with event parameter: \(key). Will be overwritten.")
            mergedOptions[key] = value
        }
        eventTracker.trackEvent(event, withOptions: mergedOptions)
    }
    
    private func makeMeta(_ event_version: Int, interfaces: [String: Any]) -> [String: Any] {
        var metaDict: [String: Any] = [:]
        var eventDict: [String: Any] = [:]
        eventDict["version"] = event_version
        metaDict["event"] = eventDict
        metaDict["interfaces"] = interfaces
        return metaDict
    }
    
    public typealias UserId = String
    public typealias ContentId = String
    public typealias Timestamp = Int
    public typealias Price = Double
    public typealias ViewCount = Int
    public enum PageId: String {
        case home = "home"
        case catalog = "catalog"
        case movieCard = "movie_card"
        case seriesCard = "series_card"
    }
    
    public typealias MetadataV1 = [String: Any]
    public typealias MetadataV2 = [String: Any]
    public typealias ContentItems = [Any]
    /**
     *  Первое событие с переиспользуемым параметром
     *
     *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    public func anotherNamespaceEvent1(reusedParam: String) {
        var options: [String: Any] = [:]
        options["reusedParam"] = reusedParam
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("AnotherNamespace.Event1", withOptions: options)
    }

    /**
     *  Второе событие с переиспользуемым параметром
     *
     *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    public func anotherNamespaceEvent2(reusedParam: String) {
        var options: [String: Any] = [:]
        options["reusedParam"] = reusedParam
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("AnotherNamespace.Event2", withOptions: options)
    }

    /**
     *  Просмотр страницы (использует глобальный тип PageId)
     *
     *  1. pageId - ID страницы
     */
    public func globalTypesDemoPageView(pageId: PageId) {
        var options: [String: Any] = [:]
        options["pageId"] = pageId
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("GlobalTypesDemo.PageView", withOptions: options)
    }

    /**
     *  Покупка контента (примитивные глобальные типы)
     *
     *  1. userId - ID пользователя
     *  2. contentId - ID контента
     *  3. price - Цена покупки
     *  4. timestamp - Время покупки
     */
    public func globalTypesDemoPurchase(userId: UserId, contentId: ContentId, price: Price, timestamp: Timestamp) {
        var options: [String: Any] = [:]
        options["userId"] = userId
        options["contentId"] = contentId
        options["price"] = price
        options["timestamp"] = timestamp
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("GlobalTypesDemo.Purchase", withOptions: options)
    }

    /**
     *  Просмотр списка контента (использует Metadata.v1)
     *
     *  1. items - Элементы контента
     *  2. metadata - Метаданные запроса (базовая версия)
     */
    public func globalTypesDemoContentListView(items: ContentItems, metadata: MetadataV1) {
        var options: [String: Any] = [:]
        options["items"] = items
        options["metadata"] = metadata
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("GlobalTypesDemo.ContentListView", withOptions: options)
    }

    /**
     *  Просмотр списка контента (использует Metadata.v2 с тегами)
     *
     *  1. items - Элементы контента
     *  2. metadata - Метаданные запроса (расширенная версия с тегами)
     */
    public func globalTypesDemoContentListViewV2(items: ContentItems, metadata: MetadataV2) {
        var options: [String: Any] = [:]
        options["items"] = items
        options["metadata"] = metadata
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(2, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("GlobalTypesDemo.ContentListView", withOptions: options)
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
    public func myNamespaceMyEvent(paramFromAnotherFile: String, batchParam1: String, batchParam2: String, stringParam: String = "val1", intParam: Int = 42) {
        var options: [String: Any] = [:]
        options["paramFromAnotherFile"] = paramFromAnotherFile
        options["batchParam1"] = batchParam1
        options["batchParam2"] = batchParam2
        options["stringParam"] = stringParam
        options["intParam"] = "\(intParam)"
        options["сonstParam"] = "shop_page"
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("MyNamespace.MyEvent", withOptions: options)
    }

}
