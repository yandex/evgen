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

enum class subService(val eventValue: String) {
    Afisha("afisha"),
    Drive("drive"),
    Eats("eats"),
    KinopoiskWeb("kinopoisk_web"),
    KinopoiskYaserp("kinopoisk_yaserp"),
    KinopoiskYaefir("kinopoisk_yaefir"),
    KinopoiskYavideo("kinopoisk_yavideo"),
    KinopoiskYasport("kinopoisk_yasport"),
    KinopoiskApp("kinopoisk_app"),
    KinopoiskAndroidtv("kinopoisk_androidtv"),
    KinopoiskAppletv("kinopoisk_appletv"),
    KinopoiskYandextvLauncher("kinopoisk_yandextv_launcher"),
    KinopoiskYandextv("kinopoisk_yandextv"),
    KinopoiskSmarttv("kinopoisk_smarttv"),
    KinopoiskGift("kinopoisk_gift"),
    Lavka("lavka"),
    Market("market"),
    MusicWeb("music_web"),
    MusicApp("music_app"),
    MusicYastation("music_yastation"),
    MusicMtsru("music_mtsru"),
    MusicWindows("music_windows"),
    MusicRadio("music_radio"),
    MusicNavi("music_navi"),
    MusicYaauto("music_yaauto"),
    MusicMusickp("music_musickp"),
    MusicPp("music_pp"),
    MusicMtsbw("music_mtsbw"),
    Navi("navi"),
    Plus("plus"),
    PlusGift("plus_gift"),
    Taxi("taxi"),
    Zapravki("zapravki"),
    Device("device"),
    Fintech("fintech"),
    Aon("aon"),
}

class EvgenAnalyticsGlobalParams(testIds: String, childMode: Boolean, experiment: Map<String, Any>, subService: subService) {
    val parameters: Map<String, Any> = mapOf (
        "testIds" to testIds,
        "childMode" to childMode,
        "experiment" to experiment,
        "subService" to subService.eventValue,
        "serviceName" to "ott-mobile-android",
    )
}

class EvgenAnalyticsPlatformParams() {
    val parameters: Map<String, Any> = mapOf (
        "androidParam" to "android",
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
    
    enum class SubscriptionPage(val eventValue: String) {
        MyMoviesScreen("my_movies_screen"),
        ShopScreen("shop_screen"),
        ProfileScreen("profile_screen"),
        PaymentWidget("payment_widget"),
        OnboardingScreen("onboarding_screen"),
        LockedSubscriptionScreen("locked_subscription_screen"),
    }
    
    enum class ErrorType(val eventValue: String) {
        BackendError("backend_error"),
        ParserError("parser_error"),
        NetworkError("network_error"),
    }
    
    /**
     * Успешное оформление подписки
     * 
     * 0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
     * 1. page - Название экрана, где было предложение о подписке
     * 2. extraParams - Доп параметры
     */
    fun marketingSubscriptionSucceed(subscriptionType: String, page: SubscriptionPage, extraParams: Map<String, Any>) {
        val parameters = mutableMapOf<String, Any>()
        parameters["subscriptionType"] = subscriptionType
        parameters["page"] = page.eventValue
        parameters["extraParams"] = extraParams
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Marketing.Subscription.Succeed", parameters)
    }
    
    /**
     * Успешное оформление подписки
     * 
     * 0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
     */
    fun marketingSubscriptionSucceedV2(subscriptionType: String) {
        val parameters = mutableMapOf<String, Any>()
        parameters["subscriptionType"] = subscriptionType
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(2, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Marketing.Subscription.Succeed", parameters)
    }
    
    /**
     * Успешное оформление триальной подписки
     * 
     * 0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
     * 1. page - Название экрана, где было предложение о подписке
     */
    fun marketingSubscriptionTrialSubsSucceed(subscriptionType: String, page: SubscriptionPage) {
        val parameters = mutableMapOf<String, Any>()
        parameters["subscriptionType"] = subscriptionType
        parameters["page"] = page.eventValue
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Marketing.Subscription.TrialSubs.Succeed", parameters)
    }
    
    /**
     * Успешное оформление регулярной подписки
     * 
     * 0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
     * 1. page - Название экрана, где было предложение о подписке
     */
    fun marketingSubscriptionRegularSubsSucceed(subscriptionType: String, page: SubscriptionPage) {
        val parameters = mutableMapOf<String, Any>()
        parameters["subscriptionType"] = subscriptionType
        parameters["page"] = page.eventValue
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Marketing.Subscription.RegularSubs.Succeed", parameters)
    }
    
    enum class PaymentWidgetSubscriptionOfferShowedV2Path(val eventValue: String) {
        PaymentWidget("payment_widget"),
        PurchaseOption("purchase_option"),
    }
    
    /**
     * Показ предложения оформления подписки
     * 
     * 0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
     * 1. offerTitle - Текст кнопки
     * 2. offerText - Текст оффера
     * 3. eventType - Константа для единообразной обработки кросссервисных событий.
     * 4. offerType - Константа для единообразной обработки кросс платформенных логов.
     * 5. monetizationModel - Константа для единообразной обработки кросссервисных событий.
     * 6. billingProductId - id продукта в биллинге
     * 7. position - Порядковый номер оффера одного типа. Считаютсясвехру вниз, слева направо. Например, если этобаннеры (upsale) на витрине Магазина, тосчитаются сверху вниз от экрана.
     * 8. page - название экрана, где находится оффер
     * 9. path - Путь до оффера.
     * 10. title - Название контента, для которого вызван виджет оплаты,если виджет вызван для контретного контента. Иначе пустая строка
     * 11. uuid - Universally unique identifier контента, для которого вызван виджет оплаты, если виджет вызван для контретного контента. Иначе -1
     */
    fun paymentWidgetSubscriptionOfferShowedV2(subscriptionType: String, offerTitle: String = "Offer Title", offerText: String, billingProductId: Int, position: Int = -1, path: PaymentWidgetSubscriptionOfferShowedV2Path = PaymentWidgetSubscriptionOfferShowedV2Path.PaymentWidget, title: String, uuid: String) {
        val parameters = mutableMapOf<String, Any>()
        parameters["subscriptionType"] = subscriptionType
        parameters["offerTitle"] = offerTitle
        parameters["offerText"] = offerText
        parameters["eventType"] = "offerShow"
        parameters["offerType"] = "subscription"
        parameters["monetizationModel"] = "SVOD"
        parameters["billingProductId"] = billingProductId.toString()
        parameters["position"] = position.toString()
        parameters["page"] = "payment_widget"
        parameters["path"] = path.eventValue
        parameters["title"] = title
        parameters["uuid"] = uuid
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(2, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("PaymentWidget.SubscriptionOffer.Showed", parameters)
    }
    
    /**
     * Переход на оплату подписки
     * 
     * 0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
     * 1. offerTitle - Текст кнопки
     * 2. offerText - Текст оффера
     * 3. eventType - Константа для единообразной обработки кросссервисных событий.
     */
    fun paymentWidgetSubscriptionOfferNavigated(subscriptionType: String, offerTitle: String = "Offer Title", offerText: String) {
        val parameters = mutableMapOf<String, Any>()
        parameters["subscriptionType"] = subscriptionType
        parameters["offerTitle"] = offerTitle
        parameters["offerText"] = offerText
        parameters["eventType"] = "offerClick"
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", parameters)
    }
    
    enum class PaymentWidgetSubscriptionOfferNavigatedV2Path(val eventValue: String) {
        PaymentWidget("payment_widget"),
        PurchaseOption("purchase_option"),
    }
    
    /**
     * Переход на оплату подписки
     * 
     * 0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
     * 1. offerTitle - Текст кнопки
     * 2. offerText - Текст оффера
     * 3. eventType - Константа для единообразной обработки кросссервисных событий.
     * 4. offerType - Константа для единообразной обработки кросс платформенных логов.
     * 5. monetizationModel - Константа для единообразной обработки кросссервисных событий.
     * 6. billingProductId - id продукта в биллинге
     * 7. position - Порядковый номер оффера одного типа. Считаютсясвехру вниз, слева направо. Например, если этобаннеры (upsale) на витрине Магазина, тосчитаются сверху вниз от экрана.
     * 8. page - название экрана, где находится оффер
     * 9. path - Путь до оффера.
     * 10. title - Название контента, для которого вызван виджет оплаты,если виджет вызван для контретного контента. Иначе пустая строка
     * 11. uuid - Universally unique identifier контента, для которого вызван виджет оплаты, если виджет вызван для контретного контента. Иначе -1
     */
    fun paymentWidgetSubscriptionOfferNavigatedV2(subscriptionType: String, offerTitle: String = "Offer Title", offerText: String, billingProductId: Int, position: Int = -1, path: PaymentWidgetSubscriptionOfferNavigatedV2Path = PaymentWidgetSubscriptionOfferNavigatedV2Path.PaymentWidget, title: String, uuid: String) {
        val parameters = mutableMapOf<String, Any>()
        parameters["subscriptionType"] = subscriptionType
        parameters["offerTitle"] = offerTitle
        parameters["offerText"] = offerText
        parameters["eventType"] = "offerClick"
        parameters["offerType"] = "subscription"
        parameters["monetizationModel"] = "SVOD"
        parameters["billingProductId"] = billingProductId.toString()
        parameters["position"] = position.toString()
        parameters["page"] = "payment_widget"
        parameters["path"] = path.eventValue
        parameters["title"] = title
        parameters["uuid"] = uuid
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(2, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", parameters)
    }
    
    /**
     * Переход к строке поиска
     * 
     */
    fun searchSearchEngineStarted() {
        val parameters = mutableMapOf<String, Any>()
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Search.SearchEngine.Started", parameters)
    }
    
    /**
     * Показ саджестов для текущего запроса
     * 
     * 0. query - Запрос в поиске
     * 1. no_titles - Не найден ни один тайтл
     * 2. no_persons - Не найдена ни одна персона
     * 3. no_cinemas - Не найден ни один кинотеатр
     */
    fun searchSearchEngineSuggestShowed(query: String, noTitles: Boolean, noPersons: Boolean, noCinemas: Boolean) {
        val parameters = mutableMapOf<String, Any>()
        parameters["query"] = query
        parameters["no_titles"] = noTitles.toString()
        parameters["no_persons"] = noPersons.toString()
        parameters["no_cinemas"] = noCinemas.toString()
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.Showed", parameters)
    }
    
    enum class SearchSearchEngineSuggestNavigatedTo(val eventValue: String) {
        PersonCard("person_card"),
        TitleCard("title_card"),
        CinemaCard("cinema_card"),
        GlobalSearchResult("global_search_result"),
        SearchList("search_list"),
    }
    
    /**
     * Переход к другому экрану
     * 
     * 0. to - тип экрана
     */
    fun searchSearchEngineSuggestNavigated(to: SearchSearchEngineSuggestNavigatedTo) {
        val parameters = mutableMapOf<String, Any>()
        parameters["to"] = to.eventValue
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.Navigated", parameters)
    }
    
    enum class SearchSearchEngineSuggestSelectedType(val eventValue: String) {
        AllResults("all_results"),
        OttResults("ott_results"),
    }
    
    /**
     * Выбор варианта отображения саджеста
     * 
     * 0. type - Типы отображения
     */
    fun searchSearchEngineSuggestSelected(type: SearchSearchEngineSuggestSelectedType) {
        val parameters = mutableMapOf<String, Any>()
        parameters["type"] = type.eventValue
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.Selected", parameters)
    }
    
    /**
     * Возникла ошибка при показе саджеста
     * 
     * 0. type - Тип ошибки
     * 1. code - Код ошибки
     * 2. text - Описание ошибки
     */
    fun searchSearchEngineSuggestErrorRaised(type: ErrorType, code: Int, text: String) {
        val parameters = mutableMapOf<String, Any>()
        parameters["type"] = type.eventValue
        parameters["code"] = code.toString()
        parameters["text"] = text
        val interfacesDict = HashMap<String, Any>();
        val _meta = makeMeta(1, interfacesDict);
        parameters["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.ErrorRaised", parameters)
    }
    
}
