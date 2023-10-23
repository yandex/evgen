/**
 * AUTO-GENERATED FILE. DO NOT MODIFY
 * This class was automatically generated.
 */
/* ktlint-disable */

interface EvgenAnalyticsTracker {
    fun trackEvent(event: String, parameters: Map<String, Any>)
}

interface EvgenAnalyticsGlobalParamsProvider {
    fun getGlobalParams() : EvgenAnalyticsGlobalParams
}

interface EvgenAnalyticsPlatformParamsProvider {
    fun getPlatformParams() : EvgenAnalyticsPlatformParams
}

class EvgenAnalyticsGlobalParams() {
    val parameters: Map<String, Any> = mapOf (
    )
}

class EvgenAnalyticsPlatformParams(appVersion: String) {
    val parameters: Map<String, Any> = mapOf (
        "appVersion" to appVersion,
    )
}

class EvgenAnalytics(private val eventTracker: EvgenAnalyticsTracker, private val globalParamsProvider: EvgenAnalyticsGlobalParamsProvider, private val platformParamsProvider: EvgenAnalyticsPlatformParamsProvider) {
    
    private fun trackEvent(event: String, parameters: MutableMap<String, Any>) {
        val mergedParameters: HashMap<String, Any> = HashMap<String, Any>()
        mergedParameters.putAll(parameters)
        mergedParameters.putAll(globalParamsProvider.getGlobalParams().parameters)
        mergedParameters.putAll(platformParamsProvider.getPlatformParams().parameters)
        eventTracker.trackEvent(event, mergedParameters)
    }
    
    private fun makeMeta(event_version: Int, interfaces: Map<String, Any>): Map<String, Any> {
        val metaDict = HashMap<String, Any>();
        val eventDict = HashMap<String, Any>();
        eventDict["version"] = event_version;
        metaDict["event"] = eventDict;
        metaDict["interfaces"] = interfaces;
        return metaDict;
    }
    
    /**
     * Also event description
     *
     */
    fun alsoMyEventLogged() {
        val parameters = mutableMapOf<String, Any>()
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("AlsoMyEvent.Logged", parameters)
    }

    /**
     * Event description
     *
     */
    fun myEvent() {
        val parameters = mutableMapOf<String, Any>()
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("MyEvent", parameters)
    }

}
