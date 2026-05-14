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
     *  Демонстрация param_name_case: одинаковое событие для Android, iOS, Flutter, WebSmartTV, Unity.
     *  
     *
     *  1. user_session_id - Ключ в YAML в snake_case
     *  2. screenTitle - Ключ в YAML в camelCase (без подчёркиваний)
     */
    fun caseDemoSampleEvent(
        userSessionId: String = "guest",
        screenTitle: String,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["USER_SESSION_ID"] = userSessionId
        parameters["SCREEN_TITLE"] = screenTitle
        val interfacesDict = HashMap<String, Any>()
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("CaseDemo.SampleEvent", parameters)
    }

}
