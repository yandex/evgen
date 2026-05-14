/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */

import Foundation

public protocol ApplicationAnalyticsTracker {
    func trackEvent(_ event: String, withOptions options: [String: Any])
}

public protocol ApplicationAnalyticsGlobalParamsProvider: AnyObject {
    func getGlobalParams() -> ApplicationAnalyticsGlobalParams
}

public protocol ApplicationAnalyticsPlatformParamsProvider: AnyObject {
    func getPlatformParams() -> ApplicationAnalyticsPlatformParams
}

public struct ApplicationAnalyticsGlobalParams {

    public func makeOptions() -> [String: Any] {
        let options: [String: Any] = [:]
        return options
    }

    public init() {
    }
}

public struct ApplicationAnalyticsPlatformParams {
    
    public func makeOptions() -> [String: Any] {
        let options: [String: Any] = [:]
        return options
    }
    
    public init() {
    }
}

public final class ApplicationAnalytics {
    public init(eventTracker: ApplicationAnalyticsTracker, globalParamsProvider: ApplicationAnalyticsGlobalParamsProvider, platformParamsProvider: ApplicationAnalyticsPlatformParamsProvider) {
        self.eventTracker = eventTracker
        self.globalParamsProvider = globalParamsProvider
        self.platformParamsProvider = platformParamsProvider
    }
    
    private let eventTracker: ApplicationAnalyticsTracker
    private let globalParamsProvider: ApplicationAnalyticsGlobalParamsProvider
    private let platformParamsProvider: ApplicationAnalyticsPlatformParamsProvider
    
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
     *  Ивент разворачивания/старта приложения
     *
     *  1. startup_info - My Custom Type
     *  2. startup_info_duplicate - Параметр с дублирующимся кастомным типом
     */
    public func applicationResumed(startupInfo: CustomStartupInfo, startupInfoDuplicate: CustomStartupInfo) {
        var options: [String: Any] = [:]
        options["startup_info"] = startupInfo
        options["startup_info_duplicate"] = startupInfoDuplicate
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Application.Resumed", withOptions: options)
    }

    /**
     *  Ивент с дублирующимся кастомным типом
     *
     *  1. startup_info_v2 - My Custom Type v2
     *  2. list_unnamed_property - 
     *  3. list_named_property - 
     */
    public func applicationResumedV2(startupInfoV2: CustomStartupInfo, listUnnamedProperty: [ListUnnamedProperty], listNamedProperty: [CustomStartupInfo]) {
        var options: [String: Any] = [:]
        options["startup_info_v2"] = startupInfoV2
        options["list_unnamed_property"] = listUnnamedProperty
        options["list_named_property"] = listNamedProperty
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(2, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Application.Resumed", withOptions: options)
    }

}
