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
    appVersion: String,
    userId: Long,
    deviceId: String,
) {
    val parameters: Map<String, Any> = mapOf(
        "appVersion" to appVersion,
        "userId" to userId,
        "deviceId" to deviceId,
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
    private val platformParamsProvider: EvgenAnalyticsPlatformParamsProviderm,
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

    enum class MyMoviesSelectionItemNavigatedTo(val eventValue: String) {
        MovieScreen("MovieScreen"),
        SelectionScreen("SelectionScreen"),
    }

    /**
     * Переход по карточке контента
     *
     * 0. from - Страница, с которой произошел переход
     * 1. to - Страница, на которою произошел переход
     * 2. cardPosition - Позиция карточки в подборке
     * 3. contentId - ID контента, по карточке которого произошел переход
     */
    fun myMoviesSelectionItemNavigated(
        to: MyMoviesSelectionItemNavigatedTo,
        cardPosition: Int,
        contentId: String,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["from"] = "MyMoviesScreen"
        parameters["to"] = to.eventValue
        parameters["cardPosition"] = cardPosition.toString()
        parameters["contentId"] = contentId
        val interfacesDict = HashMap<String, Any>()
        val selectionItemGeneral = HashMap<String, Any>()
        selectionItemGeneral["version"] = 1
        interfacesDict["SelectionItem.General"] = selectionItemGeneral
        val generalNavigated = HashMap<String, Any>()
        generalNavigated["version"] = 1
        interfacesDict["General.Navigated"] = generalNavigated
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("MyMovies.SelectionItem.Navigated", parameters)
    }

    enum class MyMoviesSelectionItemNavigatedV2To(val eventValue: String) {
        MovieScreen("MovieScreen"),
        SelectionScreen("SelectionScreen"),
    }

    /**
     * Переход по карточке контента
     *
     * 0. from - Страница, с которой произошел переход
     * 1. to - Страница, на которою произошел переход
     * 2. cardPosition - Позиция карточки в подборке
     * 3. contentId - ID контента, по карточке которого произошел переход
     * 4. rating - Рейтинг контента
     */
    fun myMoviesSelectionItemNavigatedV2(
        to: MyMoviesSelectionItemNavigatedV2To,
        cardPosition: Int,
        contentId: String,
        rating: Double,
    ) {
        val parameters = mutableMapOf<String, Any>()
        parameters["from"] = "MyMoviesScreen"
        parameters["to"] = to.eventValue
        parameters["cardPosition"] = cardPosition.toString()
        parameters["contentId"] = contentId
        parameters["rating"] = rating.toString()
        val interfacesDict = HashMap<String, Any>()
        val selectionItemGeneral = HashMap<String, Any>()
        selectionItemGeneral["version"] = 1
        interfacesDict["SelectionItem.General"] = selectionItemGeneral
        val generalNavigated = HashMap<String, Any>()
        generalNavigated["version"] = 1
        interfacesDict["General.Navigated"] = generalNavigated
        val _meta = makeMeta(2, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("MyMovies.SelectionItem.Navigated", parameters)
    }

}
