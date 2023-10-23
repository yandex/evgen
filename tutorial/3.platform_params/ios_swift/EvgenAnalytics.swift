/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
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

public struct EvgenAnalyticsGlobalParams {

    public func makeOptions() -> [String: Any] {
        let options: [String: Any] = [:]
        return options
    }

    public init() {
    }
}

public struct EvgenAnalyticsPlatformParams {
    public var hasSubscription: Bool
    
    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["hasSubscription"] = hasSubscription
        return options
    }
    
    public init(hasSubscription: Bool) {
        self.hasSubscription = hasSubscription
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
    
    /**
        Also event description

    */
    public func alsoMyEventLogged() {
        var options: [String: Any] = [:]
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("AlsoMyEvent.Logged", withOptions: options)
    }

    /**
        Event description

    */
    public func myEvent() {
        var options: [String: Any] = [:]
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("MyEvent", withOptions: options)
    }

}
