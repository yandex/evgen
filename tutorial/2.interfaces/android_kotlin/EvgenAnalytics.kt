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
     * Показ экрана магазина
     *
     * 0. page - Название страницы
     * 1. pageId - Идентификатор страницы
     */
    fun shopShowed(
        page: String,
        pageId: Int,
    ) {
        val parameters = mutableMapOf<String, Any?>()
        parameters["page"] = page
        parameters["pageId"] = pageId.toString()
        val interfacesDict = HashMap<String, Any>()
        val myInterfacesPage = HashMap<String, Any>()
        myInterfacesPage["version"] = 1
        interfacesDict["MyInterfaces.Page"] = myInterfacesPage
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("Shop.Showed", parameters)
    }


    /**
     * Показ экрана магазина
     *
     * 0. page - Название страницы
     * 1. movieName - Название фильма
     * 2. movieId - Идентификатор фильма
     * 3. pageId - Идентификатор страницы
     */
    fun showcaseMovieShowed(
        page: String,
        movieName: String,
        movieId: Int,
        pageId: Int,
    ) {
        val parameters = mutableMapOf<String, Any?>()
        parameters["page"] = page
        parameters["movieName"] = movieName
        parameters["movieId"] = movieId.toString()
        parameters["pageId"] = pageId.toString()
        val interfacesDict = HashMap<String, Any>()
        val myInterfacesPage = HashMap<String, Any>()
        myInterfacesPage["version"] = 1
        interfacesDict["MyInterfaces.Page"] = myInterfacesPage
        val myInterfacesMovie = HashMap<String, Any>()
        myInterfacesMovie["version"] = 2
        interfacesDict["MyInterfaces.Movie"] = myInterfacesMovie
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("Showcase.Movie.Showed", parameters)
    }


    /**
     * Показ экрана магазина
     *
     * 0. page - Название страницы
     * 1. movieName - Название фильма
     * 2. pageId - Идентификатор страницы
     */
    fun showcaseTVShowShowed(
        page: String,
        movieName: String,
        pageId: Int,
    ) {
        val parameters = mutableMapOf<String, Any?>()
        parameters["page"] = page
        parameters["movieName"] = movieName
        parameters["pageId"] = pageId.toString()
        val interfacesDict = HashMap<String, Any>()
        val myInterfacesPage = HashMap<String, Any>()
        myInterfacesPage["version"] = 1
        interfacesDict["MyInterfaces.Page"] = myInterfacesPage
        val myInterfacesMovie = HashMap<String, Any>()
        myInterfacesMovie["version"] = 1
        interfacesDict["MyInterfaces.Movie"] = myInterfacesMovie
        val _meta = makeMeta(1, interfacesDict)
        parameters["_meta"] = _meta
        trackEvent("Showcase.TVShow.Showed", parameters)
    }

}
