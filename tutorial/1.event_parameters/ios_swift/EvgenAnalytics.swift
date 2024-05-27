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
 * 0. globalParam - Глобальный параметр, который добавится к каждому событию
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
    
    public enum MyNamespaceMyEventEnumParam: String {
        case option1 = "option1"
        case option2 = "option2"
        case option3 = "option3"
    }
    
    public enum Pages: String {
        case screen1 = "screen_1"
        case screen2 = "screen_2"
        case screen3 = "screen_3"
    }
    
    /**
     *  Первое событие с переиспользуемым параметром
     *
     *  0. reusedParam - Параметр, который переиспользуется в нескольких событиях
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
     *  0. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    public func anotherNamespaceKebabCaseEvent2(reusedParam: String) {
        var options: [String: Any] = [:]
        options["reusedParam"] = reusedParam
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("AnotherNamespace.kebab-case-event-2", withOptions: options)
    }

    public enum MyNamespaceMyEventEnumParamInt: String {
        int1 = 1,
        int2 = 2,
        int3 = 3,
    }
    
    /**
     *  События со всеми возможными типами параметров
     *
     *  0. stringParam - Параметр типа String
     *  1. intParam - Параметр типа Int
     *  2. longIntParam - Параметр типа Long Int
     *  3. boolParam - Параметр типа Bool
     *  4. doubleParam - Параметр типа Double
     *  5. constParam - Параметр типа Const. Не участвует в сигнатуре функции, но логируется в при отправке в трекер
     *  6. enumParam - Параметр типа Enum. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
     *  7. enumParamInt - Параметр типа Enum Int. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
     *  8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages. Если какой-то enum используется больше одного раза, то лучше давать ему явное имя, разботчики смогут обращаться к нему однообразно
     *  9. dictParam - параметр типа Dict.
     *  10. dictElementType - параметр типа Dict енумов.
     *  11. typedDictParam - типизированный Dict.
     *  12. typedListParam - типизированный List.
     *  13. platformConst - Платформозависимая константа
     *  14. listOfInt - Список целочисленных параметров
     *  15. listOfDouble - Список флотовых параметров
     *  16. listOfString - Cписок строк
     *  17. listOfEnum - Cписок енумов
     */
    public func myNamespaceMyEvent(stringParam: String = "val", intParam: Int = 42, longIntParam: Int, boolParam: Bool = true, doubleParam: Double, enumParam: MyNamespaceMyEventEnumParam = MyNamespaceMyEventEnumParam.option1, enumParamInt: MyNamespaceMyEventEnumParamInt = MyNamespaceMyEventEnumParamInt.int1, namedEnumParam: Pages, dictParam: [String: Any], dictElementType: [String: MyNamespaceMyEventEnumParam], typedDictParam: [String: Any], typedListParam: [Any], listOfInt: [Int] = [], listOfDouble: [Double] = [], listOfString: [String] = [], listOfEnum: [MyNamespaceMyEventEnumParam] = []) {
        var options: [String: Any] = [:]
        options["stringParam"] = stringParam
        options["intParam"] = "\(intParam)"
        options["longIntParam"] = "\(longIntParam)"
        if boolParam {
            options["boolParam"] = "true"
        } else {
            options["boolParam"] = "false"
        }
        options["doubleParam"] = "\(doubleParam)"
        options["constParam"] = "ValueToLog"
        options["enumParam"] = enumParam.rawValue
        options["enumParamInt"] = enumParamInt.rawValue
        options["namedEnumParam"] = namedEnumParam.rawValue
        options["dictParam"] = dictParam
        options["dictElementType"] = dictElementType
        options["typedDictParam"] = typedDictParam
        options["typedListParam"] = typedListParam
        options["platformConst"] = "iOSValue"
        options["listOfInt"] = listOfInt
        options["listOfDouble"] = listOfDouble
        options["listOfString"] = listOfString
        options["listOfEnum"] = listOfEnum
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("MyNamespace.MyEvent", withOptions: options)
    }

}
