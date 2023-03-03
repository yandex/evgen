/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
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

public enum subService: String {
    case `afisha` = "afisha"
    case `drive` = "drive"
    case `eats` = "eats"
    case `kinopoiskWeb` = "kinopoisk_web"
    case `kinopoiskYaserp` = "kinopoisk_yaserp"
    case `kinopoiskYaefir` = "kinopoisk_yaefir"
    case `kinopoiskYavideo` = "kinopoisk_yavideo"
    case `kinopoiskYasport` = "kinopoisk_yasport"
    case `kinopoiskApp` = "kinopoisk_app"
    case `kinopoiskAndroidtv` = "kinopoisk_androidtv"
    case `kinopoiskAppletv` = "kinopoisk_appletv"
    case `kinopoiskYandextvLauncher` = "kinopoisk_yandextv_launcher"
    case `kinopoiskYandextv` = "kinopoisk_yandextv"
    case `kinopoiskSmarttv` = "kinopoisk_smarttv"
    case `kinopoiskGift` = "kinopoisk_gift"
    case `lavka` = "lavka"
    case `market` = "market"
    case `musicWeb` = "music_web"
    case `musicApp` = "music_app"
    case `musicYastation` = "music_yastation"
    case `musicMtsru` = "music_mtsru"
    case `musicWindows` = "music_windows"
    case `musicRadio` = "music_radio"
    case `musicNavi` = "music_navi"
    case `musicYaauto` = "music_yaauto"
    case `musicMusickp` = "music_musickp"
    case `musicPp` = "music_pp"
    case `musicMtsbw` = "music_mtsbw"
    case `navi` = "navi"
    case `plus` = "plus"
    case `plusGift` = "plus_gift"
    case `taxi` = "taxi"
    case `zapravki` = "zapravki"
    case `device` = "device"
    case `fintech` = "fintech"
    case `aon` = "aon"
}

public struct EvgenAnalyticsGlobalParams {
    public var testIds: String
    public var childMode: Bool
    public var experiment: [String: Any]
    public var subService: subService
    
    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["testIds"] = testIds
        if childMode {
            options["childMode"] = "true"
        } else {
            options["childMode"] = "false"
        }
        options["experiment"] = experiment
        options["subService"] = subService.rawValue
        options["serviceName"] = "ott-mobile-ios_swift"
        return options
    }
    
    public init(testIds: String, childMode: Bool, experiment: [String: Any], subService: subService) {
        self.testIds = testIds
        self.childMode = childMode
        self.experiment = experiment
        self.subService = subService
    }
}

public struct EvgenAnalyticsPlatformParams {
    
    public func makeOptions() -> [String: Any] {
        var options: [String: Any] = [:]
        options["iosParam"] = "ios_swift"
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
    
    public enum SubscriptionPage: String {
        case `myMoviesScreen` = "my_movies_screen"
        case `shopScreen` = "shop_screen"
        case `profileScreen` = "profile_screen"
        case `paymentWidget` = "payment_widget"
        case `onboardingScreen` = "onboarding_screen"
        case `lockedSubscriptionScreen` = "locked_subscription_screen"
    }
    
    public enum ErrorType: String {
        case `backendError` = "backend_error"
        case `parserError` = "parser_error"
        case `networkError` = "network_error"
    }
    
    /**
        Успешное оформление подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
        2. extraParams - Доп параметры
    */
    public func marketingSubscriptionSucceed(subscriptionType: String, page: SubscriptionPage, extraParams: [String: Any]) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        options["page"] = page.rawValue
        options["extraParams"] = extraParams
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Marketing.Subscription.Succeed", withOptions: options)
    }
    
    /**
        Успешное оформление подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    */
    public func marketingSubscriptionSucceedV2(subscriptionType: String) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(2, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Marketing.Subscription.Succeed", withOptions: options)
    }
    
    /**
        Успешное оформление триальной подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
    */
    public func marketingSubscriptionTrialSubsSucceed(subscriptionType: String, page: SubscriptionPage) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        options["page"] = page.rawValue
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Marketing.Subscription.TrialSubs.Succeed", withOptions: options)
    }
    
    /**
        Успешное оформление регулярной подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
    */
    public func marketingSubscriptionRegularSubsSucceed(subscriptionType: String, page: SubscriptionPage) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        options["page"] = page.rawValue
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Marketing.Subscription.RegularSubs.Succeed", withOptions: options)
    }
    
    /**
        Показ предложения оформления подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. offerTitle - Текст кнопки
        2. offerText - Текст оффера
    */
    public func paymentWidgetSubscriptionOfferShowed(subscriptionType: String, offerTitle: String = "Offer Title", offerText: String) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        options["offerTitle"] = offerTitle
        options["offerText"] = offerText
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("PaymentWidget.SubscriptionOffer.Showed", withOptions: options)
    }
    
    public enum PaymentWidgetSubscriptionOfferShowedV2Path: String {
        case `paymentWidget` = "payment_widget"
        case `purchaseOption` = "purchase_option"
    }
    
    /**
        Показ предложения оформления подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. offerTitle - Текст кнопки
        2. offerText - Текст оффера
        3. eventType - Константа для единообразной обработки кросссервисных событий.
        4. offerType - Константа для единообразной обработки кросс платформенных логов.
        5. monetizationModel - Константа для единообразной обработки кросссервисных событий.
        6. billingProductId - id продукта в биллинге
        7. position - Порядковый номер оффера одного типа. Считаютсясвехру вниз, слева направо. Например, если этобаннеры (upsale) на витрине Магазина, тосчитаются сверху вниз от экрана.
        8. page - название экрана, где находится оффер
        9. path - Путь до оффера.
        10. title - Название контента, для которого вызван виджет оплаты,если виджет вызван для контретного контента. Иначе пустая строка
        11. uuid - Universally unique identifier контента, для которого вызван виджет оплаты, если виджет вызван для контретного контента. Иначе -1
    */
    public func paymentWidgetSubscriptionOfferShowedV2(subscriptionType: String, offerTitle: String = "Offer Title", offerText: String, billingProductId: Int, position: Int = -1, path: PaymentWidgetSubscriptionOfferShowedV2Path = .paymentWidget, title: String, uuid: String) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        options["offerTitle"] = offerTitle
        options["offerText"] = offerText
        options["eventType"] = "offerShow"
        options["offerType"] = "subscription"
        options["monetizationModel"] = "SVOD"
        options["billingProductId"] = "\(billingProductId)"
        options["position"] = "\(position)"
        options["page"] = "payment_widget"
        options["path"] = path.rawValue
        options["title"] = title
        options["uuid"] = uuid
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(2, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("PaymentWidget.SubscriptionOffer.Showed", withOptions: options)
    }
    
    /**
        Переход на оплату подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. offerTitle - Текст кнопки
        2. offerText - Текст оффера
        3. eventType - Константа для единообразной обработки кросссервисных событий.
    */
    public func paymentWidgetSubscriptionOfferNavigated(subscriptionType: String, offerTitle: String = "Offer Title", offerText: String) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        options["offerTitle"] = offerTitle
        options["offerText"] = offerText
        options["eventType"] = "offerClick"
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", withOptions: options)
    }
    
    public enum PaymentWidgetSubscriptionOfferNavigatedV2Path: String {
        case `paymentWidget` = "payment_widget"
        case `purchaseOption` = "purchase_option"
    }
    
    /**
        Переход на оплату подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. offerTitle - Текст кнопки
        2. offerText - Текст оффера
        3. eventType - Константа для единообразной обработки кросссервисных событий.
        4. offerType - Константа для единообразной обработки кросс платформенных логов.
        5. monetizationModel - Константа для единообразной обработки кросссервисных событий.
        6. billingProductId - id продукта в биллинге
        7. position - Порядковый номер оффера одного типа. Считаютсясвехру вниз, слева направо. Например, если этобаннеры (upsale) на витрине Магазина, тосчитаются сверху вниз от экрана.
        8. page - название экрана, где находится оффер
        9. path - Путь до оффера.
        10. title - Название контента, для которого вызван виджет оплаты,если виджет вызван для контретного контента. Иначе пустая строка
        11. uuid - Universally unique identifier контента, для которого вызван виджет оплаты, если виджет вызван для контретного контента. Иначе -1
    */
    public func paymentWidgetSubscriptionOfferNavigatedV2(subscriptionType: String, offerTitle: String = "Offer Title", offerText: String, billingProductId: Int, position: Int = -1, path: PaymentWidgetSubscriptionOfferNavigatedV2Path = .paymentWidget, title: String, uuid: String) {
        var options: [String: Any] = [:]
        options["subscriptionType"] = subscriptionType
        options["offerTitle"] = offerTitle
        options["offerText"] = offerText
        options["eventType"] = "offerClick"
        options["offerType"] = "subscription"
        options["monetizationModel"] = "SVOD"
        options["billingProductId"] = "\(billingProductId)"
        options["position"] = "\(position)"
        options["page"] = "payment_widget"
        options["path"] = path.rawValue
        options["title"] = title
        options["uuid"] = uuid
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(2, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", withOptions: options)
    }
    
    /**
        Показ экрана поиска
        
    */
    public func searchShowed() {
        var options: [String: Any] = [:]
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.Showed", withOptions: options)
    }
    
    /**
        Переход к строке поиска
        
    */
    public func searchSearchEngineStarted() {
        var options: [String: Any] = [:]
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.SearchEngine.Started", withOptions: options)
    }
    
    public enum SearchSearchEngineNavigatedTo: String {
        case `globalSearchResult` = "global_search_result"
        case `searchList` = "search_list"
        case `bestMoviesFilter` = "best_movies_filter"
    }
    
    /**
        Переход к другому экрану
        
        0. to - тип экрана
    */
    public func searchSearchEngineNavigated(to: SearchSearchEngineNavigatedTo) {
        var options: [String: Any] = [:]
        options["to"] = to.rawValue
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.SearchEngine.Navigated", withOptions: options)
    }
    
    /**
        Выход из строки поиска
        
    */
    public func searchSearchEngineFinished() {
        var options: [String: Any] = [:]
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.SearchEngine.Finished", withOptions: options)
    }
    
    /**
        Показ саджестов для текущего запроса
        
        0. query - Запрос в поиске
        1. no_titles - Не найден ни один тайтл
        2. no_persons - Не найдена ни одна персона
        3. no_cinemas - Не найден ни один кинотеатр
    */
    public func searchSearchEngineSuggestShowed(query: String, noTitles: Bool, noPersons: Bool, noCinemas: Bool) {
        var options: [String: Any] = [:]
        options["query"] = query
        if noTitles {
            options["no_titles"] = "true"
        } else {
            options["no_titles"] = "false"
        }
        if noPersons {
            options["no_persons"] = "true"
        } else {
            options["no_persons"] = "false"
        }
        if noCinemas {
            options["no_cinemas"] = "true"
        } else {
            options["no_cinemas"] = "false"
        }
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.Showed", withOptions: options)
    }
    
    public enum SearchSearchEngineSuggestNavigatedTo: String {
        case `personCard` = "person_card"
        case `titleCard` = "title_card"
        case `cinemaCard` = "cinema_card"
        case `globalSearchResult` = "global_search_result"
        case `searchList` = "search_list"
    }
    
    /**
        Переход к другому экрану
        
        0. to - тип экрана
    */
    public func searchSearchEngineSuggestNavigated(to: SearchSearchEngineSuggestNavigatedTo) {
        var options: [String: Any] = [:]
        options["to"] = to.rawValue
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.Navigated", withOptions: options)
    }
    
    public enum SearchSearchEngineSuggestSelectedType: String {
        case `allResults` = "all_results"
        case `ottResults` = "ott_results"
    }
    
    /**
        Выбор варианта отображения саджеста
        
        0. type - Типы отображения
    */
    public func searchSearchEngineSuggestSelected(type: SearchSearchEngineSuggestSelectedType) {
        var options: [String: Any] = [:]
        options["type"] = type.rawValue
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.Selected", withOptions: options)
    }
    
    /**
        Возникла ошибка при показе саджеста
        
        0. type - Тип ошибки
        1. code - Код ошибки
        2. text - Описание ошибки
    */
    public func searchSearchEngineSuggestErrorRaised(type: ErrorType, code: Int, text: String) {
        var options: [String: Any] = [:]
        options["type"] = type.rawValue
        options["code"] = "\(code)"
        options["text"] = text
        let interfacesDict: [String: Any] = [:]
        let _meta = makeMeta(1, interfaces: interfacesDict)
        options["_meta"] = _meta
        trackEvent("Search.SearchEngine.Suggest.ErrorRaised", withOptions: options)
    }
    
}
