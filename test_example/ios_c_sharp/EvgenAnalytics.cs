/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

using System.Collections.Generic;


public class EvgenAnalytics {
    public EvgenAnalytics(EvgenAnalytics.Tracker eventTracker, EvgenAnalytics.GlobalParamsProvider globalParamsProvider, EvgenAnalytics.PlatformParamsProvider platformParamsProvider) {
        this.eventTracker = eventTracker;
        this.globalParamsProvider = globalParamsProvider;
        this.platformParamsProvider = platformParamsProvider;
    }
    
    private EvgenAnalytics.Tracker eventTracker ;
    private EvgenAnalytics.GlobalParamsProvider globalParamsProvider ;
    private EvgenAnalytics.PlatformParamsProvider platformParamsProvider ;
    
    private void trackEvent(string eventName, Dictionary<string, object> parameters) {
        var mergedParams = new Dictionary<string, object>(parameters);
        mergedParams.putAll(globalParamsProvider.getGlobalParams().makeParams());
        mergedParams.putAll(platformParamsProvider.getPlatformParams().makeParams());
        this.eventTracker.trackEvent(eventName, mergedParams);
    }
    
    private Dictionary<string, object>  makeMeta(int event_version, Dictionary<string, object> interfaces) {
        Dictionary<string, object>  metaDict = new Dictionary<string, object>();
        Dictionary<string, object> eventDict = new Dictionary<string, object>();
        eventDict.Add("version", event_version);
        metaDict.Add("event", eventDict);
        metaDict.Add("interfaces", interfaces);
        return metaDict;
    }
    
    public interface Tracker {
        void trackEvent(string eventName, Dictionary<string, object> parameters);
    }
    
    public interface GlobalParamsProvider {
        GlobalParams getGlobalParams();
    }
    public interface PlatformParamsProvider {
        PlatformParams getPlatformParams();
    }
    
    public class subService {
        private subService(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static subService AFISHA  { get { return new subService("afisha"); } }
        public static subService DRIVE  { get { return new subService("drive"); } }
        public static subService EATS  { get { return new subService("eats"); } }
        public static subService KINOPOISK_WEB  { get { return new subService("kinopoisk_web"); } }
        public static subService KINOPOISK_YASERP  { get { return new subService("kinopoisk_yaserp"); } }
        public static subService KINOPOISK_YAEFIR  { get { return new subService("kinopoisk_yaefir"); } }
        public static subService KINOPOISK_YAVIDEO  { get { return new subService("kinopoisk_yavideo"); } }
        public static subService KINOPOISK_YASPORT  { get { return new subService("kinopoisk_yasport"); } }
        public static subService KINOPOISK_APP  { get { return new subService("kinopoisk_app"); } }
        public static subService KINOPOISK_ANDROIDTV  { get { return new subService("kinopoisk_androidtv"); } }
        public static subService KINOPOISK_APPLETV  { get { return new subService("kinopoisk_appletv"); } }
        public static subService KINOPOISK_YANDEXTV_LAUNCHER  { get { return new subService("kinopoisk_yandextv_launcher"); } }
        public static subService KINOPOISK_YANDEXTV  { get { return new subService("kinopoisk_yandextv"); } }
        public static subService KINOPOISK_SMARTTV  { get { return new subService("kinopoisk_smarttv"); } }
        public static subService KINOPOISK_GIFT  { get { return new subService("kinopoisk_gift"); } }
        public static subService LAVKA  { get { return new subService("lavka"); } }
        public static subService MARKET  { get { return new subService("market"); } }
        public static subService MUSIC_WEB  { get { return new subService("music_web"); } }
        public static subService MUSIC_APP  { get { return new subService("music_app"); } }
        public static subService MUSIC_YASTATION  { get { return new subService("music_yastation"); } }
        public static subService MUSIC_MTSRU  { get { return new subService("music_mtsru"); } }
        public static subService MUSIC_WINDOWS  { get { return new subService("music_windows"); } }
        public static subService MUSIC_RADIO  { get { return new subService("music_radio"); } }
        public static subService MUSIC_NAVI  { get { return new subService("music_navi"); } }
        public static subService MUSIC_YAAUTO  { get { return new subService("music_yaauto"); } }
        public static subService MUSIC_MUSICKP  { get { return new subService("music_musickp"); } }
        public static subService MUSIC_PP  { get { return new subService("music_pp"); } }
        public static subService MUSIC_MTSBW  { get { return new subService("music_mtsbw"); } }
        public static subService NAVI  { get { return new subService("navi"); } }
        public static subService PLUS  { get { return new subService("plus"); } }
        public static subService PLUS_GIFT  { get { return new subService("plus_gift"); } }
        public static subService TAXI  { get { return new subService("taxi"); } }
        public static subService ZAPRAVKI  { get { return new subService("zapravki"); } }
        public static subService DEVICE  { get { return new subService("device"); } }
        public static subService FINTECH  { get { return new subService("fintech"); } }
        public static subService AON  { get { return new subService("aon"); } }
    }
    
    public class GlobalParams {
        public string testIds;
        public bool childMode;
        public Dictionary<string, object> experiment;
        public subService subService;
        
        public Dictionary<string, object> makeParams() {
            var parameters = new Dictionary<string, object>();
            parameters.Add("testIds", testIds);
            if (childMode) {
                parameters.Add("childMode", "true");
            } else {
                parameters.Add("childMode", "false");
            }
            parameters.Add("experiment", experiment);
            parameters.Add("subService", subService.RawValue);
            parameters.Add("serviceName", "ott-mobile-ios_swift");
            return parameters;
        }
        
        public GlobalParams(string testIds, bool childMode, Dictionary<string, object> experiment, subService subService) {
            this.testIds = testIds;
            this.childMode = childMode;
            this.experiment = experiment;
            this.subService = subService;
        }
    }
    public class PlatformParams {
        
        public Dictionary<string, object> makeParams() {
            var parameters = new Dictionary<string, object>();
            parameters.Add("iosParam", "ios_swift");
            return parameters;
        }
        
        public PlatformParams() {
        }
    }
    public class SubscriptionPage {
        private SubscriptionPage(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static SubscriptionPage MY_MOVIES_SCREEN  { get { return new SubscriptionPage("my_movies_screen"); } }
        public static SubscriptionPage SHOP_SCREEN  { get { return new SubscriptionPage("shop_screen"); } }
        public static SubscriptionPage PROFILE_SCREEN  { get { return new SubscriptionPage("profile_screen"); } }
        public static SubscriptionPage PAYMENT_WIDGET  { get { return new SubscriptionPage("payment_widget"); } }
        public static SubscriptionPage ONBOARDING_SCREEN  { get { return new SubscriptionPage("onboarding_screen"); } }
        public static SubscriptionPage LOCKED_SUBSCRIPTION_SCREEN  { get { return new SubscriptionPage("locked_subscription_screen"); } }
    }
    
    public class ErrorType {
        private ErrorType(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static ErrorType BACKEND_ERROR  { get { return new ErrorType("backend_error"); } }
        public static ErrorType PARSER_ERROR  { get { return new ErrorType("parser_error"); } }
        public static ErrorType NETWORK_ERROR  { get { return new ErrorType("network_error"); } }
    }
    
    /**
        Успешное оформление подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
        2. extraParams - Доп параметры
    */
    public void marketingSubscriptionSucceed(string subscriptionType, SubscriptionPage page, Dictionary<string, object> extraParams) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        parameters.Add("page", page.RawValue);
        parameters.Add("extraParams", extraParams);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Marketing.Subscription.Succeed", parameters);
    }
    
    /**
        Успешное оформление подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    */
    public void marketingSubscriptionSucceedV2(string subscriptionType) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(2, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Marketing.Subscription.Succeed", parameters);
    }
    
    /**
        Успешное оформление триальной подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
    */
    public void marketingSubscriptionTrialSubsSucceed(string subscriptionType, SubscriptionPage page) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        parameters.Add("page", page.RawValue);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Marketing.Subscription.TrialSubs.Succeed", parameters);
    }
    
    /**
        Успешное оформление регулярной подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
    */
    public void marketingSubscriptionRegularSubsSucceed(string subscriptionType, SubscriptionPage page) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        parameters.Add("page", page.RawValue);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Marketing.Subscription.RegularSubs.Succeed", parameters);
    }
    
    /**
        Показ предложения оформления подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. offerTitle - Текст кнопки
        2. offerText - Текст оффера
    */
    public void paymentWidgetSubscriptionOfferShowed(string subscriptionType, string offerText, string offerTitle = "Offer Title") {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        parameters.Add("offerTitle", offerTitle);
        parameters.Add("offerText", offerText);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("PaymentWidget.SubscriptionOffer.Showed", parameters);
    }
    
    public class PaymentWidgetSubscriptionOfferShowedV2Path {
        private PaymentWidgetSubscriptionOfferShowedV2Path(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static PaymentWidgetSubscriptionOfferShowedV2Path PAYMENT_WIDGET  { get { return new PaymentWidgetSubscriptionOfferShowedV2Path("payment_widget"); } }
        public static PaymentWidgetSubscriptionOfferShowedV2Path PURCHASE_OPTION  { get { return new PaymentWidgetSubscriptionOfferShowedV2Path("purchase_option"); } }
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
    public void paymentWidgetSubscriptionOfferShowedV2(string subscriptionType, string offerText, int billingProductId, PaymentWidgetSubscriptionOfferShowedV2Path path, string title, string uuid, string offerTitle = "Offer Title", int position = -1) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        parameters.Add("offerTitle", offerTitle);
        parameters.Add("offerText", offerText);
        parameters.Add("eventType", "offerShow");
        parameters.Add("offerType", "subscription");
        parameters.Add("monetizationModel", "SVOD");
        parameters.Add("billingProductId", billingProductId);
        parameters.Add("position", position);
        parameters.Add("page", "payment_widget");
        parameters.Add("path", path.RawValue);
        parameters.Add("title", title);
        parameters.Add("uuid", uuid);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(2, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("PaymentWidget.SubscriptionOffer.Showed", parameters);
    }
    
    /**
        Переход на оплату подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. offerTitle - Текст кнопки
        2. offerText - Текст оффера
        3. eventType - Константа для единообразной обработки кросссервисных событий.
    */
    public void paymentWidgetSubscriptionOfferNavigated(string subscriptionType, string offerText, string offerTitle = "Offer Title") {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        parameters.Add("offerTitle", offerTitle);
        parameters.Add("offerText", offerText);
        parameters.Add("eventType", "offerClick");
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", parameters);
    }
    
    public class PaymentWidgetSubscriptionOfferNavigatedV2Path {
        private PaymentWidgetSubscriptionOfferNavigatedV2Path(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static PaymentWidgetSubscriptionOfferNavigatedV2Path PAYMENT_WIDGET  { get { return new PaymentWidgetSubscriptionOfferNavigatedV2Path("payment_widget"); } }
        public static PaymentWidgetSubscriptionOfferNavigatedV2Path PURCHASE_OPTION  { get { return new PaymentWidgetSubscriptionOfferNavigatedV2Path("purchase_option"); } }
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
    public void paymentWidgetSubscriptionOfferNavigatedV2(string subscriptionType, string offerText, int billingProductId, PaymentWidgetSubscriptionOfferNavigatedV2Path path, string title, string uuid, string offerTitle = "Offer Title", int position = -1) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("subscriptionType", subscriptionType);
        parameters.Add("offerTitle", offerTitle);
        parameters.Add("offerText", offerText);
        parameters.Add("eventType", "offerClick");
        parameters.Add("offerType", "subscription");
        parameters.Add("monetizationModel", "SVOD");
        parameters.Add("billingProductId", billingProductId);
        parameters.Add("position", position);
        parameters.Add("page", "payment_widget");
        parameters.Add("path", path.RawValue);
        parameters.Add("title", title);
        parameters.Add("uuid", uuid);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(2, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", parameters);
    }
    
    /**
        Показ экрана поиска
        
    */
    public void searchShowed() {
        var parameters = new Dictionary<string, object>();
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.Showed", parameters);
    }
    
    /**
        Переход к строке поиска
        
    */
    public void searchSearchEngineStarted() {
        var parameters = new Dictionary<string, object>();
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.SearchEngine.Started", parameters);
    }
    
    public class SearchSearchEngineNavigatedTo {
        private SearchSearchEngineNavigatedTo(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static SearchSearchEngineNavigatedTo GLOBAL_SEARCH_RESULT  { get { return new SearchSearchEngineNavigatedTo("global_search_result"); } }
        public static SearchSearchEngineNavigatedTo SEARCH_LIST  { get { return new SearchSearchEngineNavigatedTo("search_list"); } }
        public static SearchSearchEngineNavigatedTo BEST_MOVIES_FILTER  { get { return new SearchSearchEngineNavigatedTo("best_movies_filter"); } }
    }
    
    /**
        Переход к другому экрану
        
        0. to - тип экрана
    */
    public void searchSearchEngineNavigated(SearchSearchEngineNavigatedTo to) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("to", to.RawValue);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.SearchEngine.Navigated", parameters);
    }
    
    /**
        Выход из строки поиска
        
    */
    public void searchSearchEngineFinished() {
        var parameters = new Dictionary<string, object>();
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.SearchEngine.Finished", parameters);
    }
    
    /**
        Показ саджестов для текущего запроса
        
        0. query - Запрос в поиске
        1. no_titles - Не найден ни один тайтл
        2. no_persons - Не найдена ни одна персона
        3. no_cinemas - Не найден ни один кинотеатр
    */
    public void searchSearchEngineSuggestShowed(string query, bool noTitles, bool noPersons, bool noCinemas) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("query", query);
        if (noTitles) {
            parameters.Add("no_titles", "true");
        } else {
            parameters.Add("no_titles", "false");
        }
        if (noPersons) {
            parameters.Add("no_persons", "true");
        } else {
            parameters.Add("no_persons", "false");
        }
        if (noCinemas) {
            parameters.Add("no_cinemas", "true");
        } else {
            parameters.Add("no_cinemas", "false");
        }
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.Showed", parameters);
    }
    
    public class SearchSearchEngineSuggestNavigatedTo {
        private SearchSearchEngineSuggestNavigatedTo(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static SearchSearchEngineSuggestNavigatedTo PERSON_CARD  { get { return new SearchSearchEngineSuggestNavigatedTo("person_card"); } }
        public static SearchSearchEngineSuggestNavigatedTo TITLE_CARD  { get { return new SearchSearchEngineSuggestNavigatedTo("title_card"); } }
        public static SearchSearchEngineSuggestNavigatedTo CINEMA_CARD  { get { return new SearchSearchEngineSuggestNavigatedTo("cinema_card"); } }
        public static SearchSearchEngineSuggestNavigatedTo GLOBAL_SEARCH_RESULT  { get { return new SearchSearchEngineSuggestNavigatedTo("global_search_result"); } }
        public static SearchSearchEngineSuggestNavigatedTo SEARCH_LIST  { get { return new SearchSearchEngineSuggestNavigatedTo("search_list"); } }
    }
    
    /**
        Переход к другому экрану
        
        0. to - тип экрана
    */
    public void searchSearchEngineSuggestNavigated(SearchSearchEngineSuggestNavigatedTo to) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("to", to.RawValue);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.Navigated", parameters);
    }
    
    public class SearchSearchEngineSuggestSelectedType {
        private SearchSearchEngineSuggestSelectedType(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static SearchSearchEngineSuggestSelectedType ALL_RESULTS  { get { return new SearchSearchEngineSuggestSelectedType("all_results"); } }
        public static SearchSearchEngineSuggestSelectedType OTT_RESULTS  { get { return new SearchSearchEngineSuggestSelectedType("ott_results"); } }
    }
    
    /**
        Выбор варианта отображения саджеста
        
        0. type - Типы отображения
    */
    public void searchSearchEngineSuggestSelected(SearchSearchEngineSuggestSelectedType type) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("type", type.RawValue);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.Selected", parameters);
    }
    
    /**
        Возникла ошибка при показе саджеста
        
        0. type - Тип ошибки
        1. code - Код ошибки
        2. text - Описание ошибки
    */
    public void searchSearchEngineSuggestErrorRaised(ErrorType type, int code, string text) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("type", type.RawValue);
        parameters.Add("code", code);
        parameters.Add("text", text);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.ErrorRaised", parameters);
    }
    
}
