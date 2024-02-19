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

public struct EvgenAnalyticsGlobalParams {

    public func makeOptions() -> [String: Any] {
        let options: [String: Any] = [:]
        return options
    }

    public init() {
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
    
    /**
     *  Показ экрана магазина
     *
     *  0. page - Название страницы
     *  1. pageId - Идентификатор страницы
     */
    public func shopShowed(page: String, pageId: Int) {
        var options: [String: Any] = [:]
        options["page"] = page
        options["pageId"] = "\(pageId)"
        var interfacesDict: [String: Any] = [:]
        var myInterfacesPage: [String: Any] = [:]
        myInterfacesPage["version"] = 1
        interfacesDict["MyInterfaces.Page"] = myInterfacesPage
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Shop.Showed", withOptions: options)
    }

    /**
     *  Показ экрана магазина
     *
     *  0. page - Название страницы
     *  1. movieName - Название фильма
     *  2. movieId - Идентификатор фильма
     *  3. pageId - Идентификатор страницы
     */
    public func showcaseMovieShowed(page: String, movieName: String, movieId: Int, pageId: Int) {
        var options: [String: Any] = [:]
        options["page"] = page
        options["movieName"] = movieName
        options["movieId"] = "\(movieId)"
        options["pageId"] = "\(pageId)"
        var interfacesDict: [String: Any] = [:]
        var myInterfacesPage: [String: Any] = [:]
        myInterfacesPage["version"] = 1
        interfacesDict["MyInterfaces.Page"] = myInterfacesPage
        var myInterfacesMovie: [String: Any] = [:]
        myInterfacesMovie["version"] = 2
        interfacesDict["MyInterfaces.Movie"] = myInterfacesMovie
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Showcase.Movie.Showed", withOptions: options)
    }

    /**
     *  Показ экрана магазина
     *
     *  0. page - Название страницы
     *  1. movieName - Название фильма
     *  2. pageId - Идентификатор страницы
     */
    public func showcaseTVShowShowed(page: String, movieName: String, pageId: Int) {
        var options: [String: Any] = [:]
        options["page"] = page
        options["movieName"] = movieName
        options["pageId"] = "\(pageId)"
        var interfacesDict: [String: Any] = [:]
        var myInterfacesPage: [String: Any] = [:]
        myInterfacesPage["version"] = 1
        interfacesDict["MyInterfaces.Page"] = myInterfacesPage
        var myInterfacesMovie: [String: Any] = [:]
        myInterfacesMovie["version"] = 1
        interfacesDict["MyInterfaces.Movie"] = myInterfacesMovie
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Showcase.TVShow.Showed", withOptions: options)
    }

}
