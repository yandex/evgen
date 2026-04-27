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
 * 0. optionalGlobal - Необязательный глобальный параметр
 */
class EvgenAnalyticsGlobalParams(
    optionalGlobal: String? = null,
) {
    val parameters: Map<String, Any> = mapOf(
        "optionalGlobal" to optionalGlobal,
    )
}

/**
 * 0. optionalPlatformHint - Необязательная подсказка с платформы
 */
class EvgenAnalyticsPlatformParams(
    optionalPlatformHint: String? = null,
) {
    val parameters: Map<String, Any> = mapOf(
        "optionalPlatformHint" to optionalPlatformHint,
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
        mergedParameters.entries.removeAll { it.value == null }
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


    /**
     *  Событие с optional-параметрами; клиент может не передавать их, тогда при merge null-ключи отфильтровываются
     *
     *  1. requiredId - Обязательный идентификатор
     *  2. optionalContext - Необязательный контекст
     *  3. optionalScore - Необязательное числовое значение
     *  4. androidOnlyLocal - Локальный параметр только для Android (не в общем списке и не на других платформах)
     */
    fun optionalNamespaceDemoEvent(
        requiredId: String,
        optionalContext: String? = null,
        optionalScore: Int? = null,
        androidOnlyLocal: String? = null,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["requiredId"] = requiredId
        parameters["optionalContext"] = optionalContext
        parameters["optionalScore"] = optionalScore.toString()
        parameters["androidOnlyLocal"] = androidOnlyLocal
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("OptionalNamespace.DemoEvent", parameters)
    }

}
