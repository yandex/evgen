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

class EvgenAnalyticsGlobalParams(
) {
    val parameters: Map<String, Any> = mapOf(
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


    /**
     *  Первое событие с переиспользуемым параметром
     *
     *  1. firstParam - Первый параметр
     *  2. paramFromAnotherFile - Параметр, описанный в отдельным файле.
     *  3. reusedParam - Description
     *  4. batchParam1 - Параметр, описанный в отдельным файле.
     *  5. batchParam2 - Параметр, описанный в отдельным файле.
     *  6. lastParam - Последний параметр
     */
    fun namespaceEvent(
        firstParam: Int,
        paramFromAnotherFile: String,
        reusedParam: String,
        batchParam1: String,
        batchParam2: String,
        lastParam: String,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["firstParam"] = firstParam.toString()
        parameters["paramFromAnotherFile"] = paramFromAnotherFile
        parameters["reusedParam"] = reusedParam
        parameters["batchParam1"] = batchParam1
        parameters["batchParam2"] = batchParam2
        parameters["lastParam"] = lastParam
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("Namespace.Event", parameters)
    }

}
