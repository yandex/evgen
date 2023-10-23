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
    public var appVersion: String
    public var userId: Int
    public var deviceId: String

    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["appVersion"] = appVersion
        options["userId"] = "\(userId)"
        options["deviceId"] = deviceId
        return options
    }

    public init(appVersion: String, userId: Int, deviceId: String) {
        self.appVersion = appVersion
        self.userId = userId
        self.deviceId = deviceId
    }
}

public struct EvgenAnalyticsPlatformParams {
    public var browserName: String
    public var browserVersion: String
    
    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["browserName"] = browserName
        options["browserVersion"] = browserVersion
        return options
    }
    
    public init(browserName: String, browserVersion: String) {
        self.browserName = browserName
        self.browserVersion = browserVersion
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
    
    public enum MyMoviesSelectionItemNavigatedTo: String {
        case movieScreen = "MovieScreen"
        case selectionScreen = "SelectionScreen"
    }
    
    /**
        Переход по карточке контента

        0. from - Страница, с которой произошел переход
        1. to - Страница, на которою произошел переход
        2. cardPosition - Позиция карточки в подборке
        3. contentId - ID контента, по карточке которого произошел переход
    */
    public func myMoviesSelectionItemNavigated(to: MyMoviesSelectionItemNavigatedTo, cardPosition: Int, contentId: String) {
        var options: [String: Any] = [:]
        options["from"] = "MyMoviesScreen"
        options["to"] = to.rawValue
        options["cardPosition"] = "\(cardPosition)"
        options["contentId"] = contentId
        var interfacesDict: [String: Any] = [:]
        var selectionItemGeneral: [String: Any] = [:]
        selectionItemGeneral["version"] = 1
        interfacesDict["SelectionItem.General"] = selectionItemGeneral
        var generalNavigated: [String: Any] = [:]
        generalNavigated["version"] = 1
        interfacesDict["General.Navigated"] = generalNavigated
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("MyMovies.SelectionItem.Navigated", withOptions: options)
    }

}
