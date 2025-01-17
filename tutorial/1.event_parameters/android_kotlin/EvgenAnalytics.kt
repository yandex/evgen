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
 * 0. globalParam - Глобальный параметр, который добавится к каждому событию
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

    enum class MyNamespaceMyEventEnumParam(val eventValue: String) {
        Option1("option1"),
        Option2("option2"),
        Option3("option3"),
    }
    enum class Pages(val eventValue: String) {
        Screen1("screen_1"),
        Screen2("screen_2"),
        Screen3("screen_3"),
    }
    /**
     * - screen_1 - My description screen_1 
     * - screen_2 - My description screen_2 
     * - screen_3 - My description screen_3 
     */
    enum class PagesWithDescriptions(val eventValue: String) {
        Screen1("screen_1"),
        Screen2("screen_2"),
        Screen3("screen_3"),
    }
    enum class DictInEnumType(val eventValue: String) {
        Option1("option1"),
        Option2("option2"),
    }

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
    fun anotherNamespaceKebabCaseEvent2(
        reusedParam: String,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["reusedParam"] = reusedParam
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("AnotherNamespace.kebab-case-event-2", parameters)
    }

    enum class MyNamespaceMyEventEnumParamInt(val eventValue: String) {
        Int1("1"),
        Int2("2"),
        Int3("3"),
    }

    /**
     *  События со всеми возможными типами параметров
     *
     *  1. stringParam - Параметр типа String
     *  2. intParam - Параметр типа Int
     *  3. longIntParam - Параметр типа Long Int
     *  4. boolParam - Параметр типа Bool
     *  5. doubleParam - Параметр типа Double
     *  6. enumParam - Параметр типа Enum. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
     *  7. enumParamInt - Параметр типа Enum Int. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
     *  8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages. Если какой-то enum используется больше одного раза, то лучше давать ему явное имя, разботчики смогут обращаться к нему однообразно
     *  9. enumWithDescriptionsParam - Enum с описанием возможных значений 
     *  10. dictParam - параметр типа Dict.
     *  11. dictElementType - параметр типа Dict енумов.
     *  12. typedDictParam - типизированный Dict.
     *  13. typedListParam - типизированный List.
     *  14. listOfInt - Список целочисленных параметров
     *  15. listOfDouble - Список флотовых параметров
     *  16. listOfString - Cписок строк
     *  17. listOfEnum - Cписок енумов
     *  18. defaultNullParam - Параметр типа String со значением null по умолчанию
     */
    fun myNamespaceMyEvent(
        stringParam: String = "val",
        intParam: Int = 42,
        longIntParam: Long,
        boolParam: Boolean = true,
        doubleParam: Double,
        enumParam: MyNamespaceMyEventEnumParam = MyNamespaceMyEventEnumParam.Option1,
        enumParamInt: MyNamespaceMyEventEnumParamInt = MyNamespaceMyEventEnumParamInt.Int1,
        namedEnumParam: Pages,
        enumWithDescriptionsParam: PagesWithDescriptions,
        dictParam: Map<String, Any>,
        dictElementType: Map<String, DictInEnumType>,
        typedDictParam: Map<String, Any>,
        typedListParam: List<Any>,
        listOfInt: List<Int> = listOf<Int>(),
        listOfDouble: List<Double> = listOf<Double>(),
        listOfString: List<String> = listOf<String>(),
        listOfEnum: List<MyNamespaceMyEventEnumParam> = listOf<MyNamespaceMyEventEnumParam>(),
        defaultNullParam: String? = null,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["stringParam"] = stringParam
        parameters["intParam"] = intParam.toString()
        parameters["longIntParam"] = longIntParam.toString()
        parameters["boolParam"] = boolParam.toString()
        parameters["doubleParam"] = doubleParam.toString()
        parameters["constParam"] = "ValueToLog"
        parameters["enumParam"] = enumParam.eventValue
        parameters["enumParamInt"] = enumParamInt.eventValue
        parameters["namedEnumParam"] = namedEnumParam.eventValue
        parameters["enumWithDescriptionsParam"] = enumWithDescriptionsParam.eventValue
        parameters["dictParam"] = dictParam
        parameters["dictElementType"] = dictElementType
        parameters["typedDictParam"] = typedDictParam
        parameters["typedListParam"] = typedListParam
        parameters["platformConst"] = "AndroidValue"
        parameters["listOfInt"] = listOfInt
        parameters["listOfDouble"] = listOfDouble
        parameters["listOfString"] = listOfString
        parameters["listOfEnum"] = listOfEnum
        parameters["defaultNullParam"] = defaultNullParam
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("MyNamespace.MyEvent", parameters)
    }

}
