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
 * 0. optionalGlobal - Необязательный глобальный параметр
 */
public struct EvgenAnalyticsGlobalParams {
    public var optionalGlobal: String?

    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["optionalGlobal"] = optionalGlobal
        return options
    }

    public init(optionalGlobal: String? = nil) {
        self.optionalGlobal = optionalGlobal
    }
}

/**
 * 0. optionalPlatformHint - Необязательная подсказка с платформы
 */
public struct EvgenAnalyticsPlatformParams {
    public var optionalPlatformHint: String?
    
    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["optionalPlatformHint"] = optionalPlatformHint
        return options
    }
    
    public init(optionalPlatformHint: String? = nil) {
        self.optionalPlatformHint = optionalPlatformHint
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
        let payload = mergedOptions.filter { _, value in
            !(value is NSNull)
        }
        eventTracker.trackEvent(event, withOptions: payload)
    }
    
    private func makeMeta(_ event_version: Int, interfaces: [String: Any]) -> [String: Any] {
        var metaDict: [String: Any] = [:]
        var eventDict: [String: Any] = [:]
        eventDict["version"] = event_version
        metaDict["event"] = eventDict
        metaDict["interfaces"] = interfaces
        return metaDict
    }
    
    /**
     *  Событие с optional-параметрами; клиент может не передавать их, тогда при merge null-ключи отфильтровываются
     *
     *  1. requiredId - Обязательный идентификатор
     *  2. optionalContext - Необязательный контекст
     *  3. optionalScore - Необязательное числовое значение
     */
    public func optionalNamespaceDemoEvent(requiredId: String, optionalContext: String? = nil, optionalScore: Int? = nil) {
        var options: [String: Any] = [:]
        options["requiredId"] = requiredId
        options["optionalContext"] = optionalContext
        options["optionalScore"] = "\(optionalScore)"
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("OptionalNamespace.DemoEvent", withOptions: options)
    }

}
