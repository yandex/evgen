/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

package ru.yandex.kinopoisk;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public final class EvgenAnalytics {
    public enum subService {
        AFISHA("afisha"),
        DRIVE("drive"),
        EATS("eats"),
        KINOPOISK_WEB("kinopoisk_web"),
        KINOPOISK_YASERP("kinopoisk_yaserp"),
        KINOPOISK_YAEFIR("kinopoisk_yaefir"),
        KINOPOISK_YAVIDEO("kinopoisk_yavideo"),
        KINOPOISK_YASPORT("kinopoisk_yasport"),
        KINOPOISK_APP("kinopoisk_app"),
        KINOPOISK_ANDROIDTV("kinopoisk_androidtv"),
        KINOPOISK_APPLETV("kinopoisk_appletv"),
        KINOPOISK_YANDEXTV_LAUNCHER("kinopoisk_yandextv_launcher"),
        KINOPOISK_YANDEXTV("kinopoisk_yandextv"),
        KINOPOISK_SMARTTV("kinopoisk_smarttv"),
        KINOPOISK_GIFT("kinopoisk_gift"),
        LAVKA("lavka"),
        MARKET("market"),
        MUSIC_WEB("music_web"),
        MUSIC_APP("music_app"),
        MUSIC_YASTATION("music_yastation"),
        MUSIC_MTSRU("music_mtsru"),
        MUSIC_WINDOWS("music_windows"),
        MUSIC_RADIO("music_radio"),
        MUSIC_NAVI("music_navi"),
        MUSIC_YAAUTO("music_yaauto"),
        MUSIC_MUSICKP("music_musickp"),
        MUSIC_PP("music_pp"),
        MUSIC_MTSBW("music_mtsbw"),
        NAVI("navi"),
        PLUS("plus"),
        PLUS_GIFT("plus_gift"),
        TAXI("taxi"),
        ZAPRAVKI("zapravki"),
        DEVICE("device"),
        FINTECH("fintech"),
        AON("aon");
        public final String eventValue;
        subService(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    public static final class GlobalParams {
        public String testIds;
        public boolean childMode;
        public Map<String, ?> experiment;
        public subService subService;
        public Map<String, Object> paramsMap;
        public GlobalParams(String testIds, boolean childMode, Map<String, ?> experiment, subService subService) {
            this.testIds = testIds;
            this.childMode = childMode;
            this.experiment = experiment;
            this.subService = subService;
            Map<String, Object> params = new HashMap<>();
            params.put("testIds", testIds);
            params.put("childMode", String.valueOf(childMode));
            params.put("experiment", experiment);
            params.put("subService", subService.eventValue);
            params.put("serviceName", "ott-mobile-android");
            this.paramsMap = params;
        }
    }
    
    public static final class PlatformParams {
        public Map<String, Object> paramsMap;
        public PlatformParams() {
            Map<String, Object> params = new HashMap<>();
            params.put("androidParam", "android");
            this.paramsMap = params;
        }
    }
    
    public interface GlobalParamsProvider {
        GlobalParams getGlobalParams();
    }
    
    public interface PlatformParamsProvider {
        PlatformParams getPlatformParams();
    }
    
    public interface Tracker {
        void trackEvent(final String eventName, final Map<String, ?> parameters);
    }
    
    public EvgenAnalytics(Tracker tracker, GlobalParamsProvider globalParamsProvider, PlatformParamsProvider platformParamsProvider) {
        this.tracker = tracker;
        this.globalParamsProvider = globalParamsProvider;
        this.platformParamsProvider = platformParamsProvider;
    }
    
    private void trackEvent(String eventName, Map<String, ?> parameters) {
        Map<String, Object> mergedParams = new HashMap<>(parameters);
        mergedParams.putAll(this.globalParamsProvider.getGlobalParams().paramsMap);
        mergedParams.putAll(this.platformParamsProvider.getPlatformParams().paramsMap);
        this.tracker.trackEvent(eventName, mergedParams);
    }
    
    private Map<String, Object>  makeMeta(int event_version, Map<String, ?> interfaces ) {
        Map<String, Object> metaDict = new HashMap<>();
        Map<String, Object> eventDict = new HashMap<>();
        eventDict.put("version", event_version);
        metaDict.put("event", eventDict);
        metaDict.put("interfaces", interfaces);
        return metaDict;
    }
    
    private Tracker tracker;
    private GlobalParamsProvider globalParamsProvider;
    private PlatformParamsProvider platformParamsProvider;
    
    public enum SubscriptionPage {
        MY_MOVIES_SCREEN("my_movies_screen"),
        SHOP_SCREEN("shop_screen"),
        PROFILE_SCREEN("profile_screen"),
        PAYMENT_WIDGET("payment_widget"),
        ONBOARDING_SCREEN("onboarding_screen"),
        LOCKED_SUBSCRIPTION_SCREEN("locked_subscription_screen");
        public final String eventValue;
        SubscriptionPage(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    public enum ErrorType {
        BACKEND_ERROR("backend_error"),
        PARSER_ERROR("parser_error"),
        NETWORK_ERROR("network_error");
        public final String eventValue;
        ErrorType(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    /**
        Успешное оформление подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
        2. extraParams - Доп параметры
    */
    public void marketingSubscriptionSucceed(String subscriptionType, SubscriptionPage page, Map<String, ?> extraParams) {
        Map<String, Object> params = new HashMap<>();
        params.put("subscriptionType", subscriptionType);
        params.put("page", page.eventValue);
        params.put("extraParams", extraParams);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Marketing.Subscription.Succeed", params);
    }
    
    /**
        Успешное оформление подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    */
    public void marketingSubscriptionSucceedV2(String subscriptionType) {
        Map<String, Object> params = new HashMap<>();
        params.put("subscriptionType", subscriptionType);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(2, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Marketing.Subscription.Succeed", params);
    }
    
    /**
        Успешное оформление триальной подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
    */
    public void marketingSubscriptionTrialSubsSucceed(String subscriptionType, SubscriptionPage page) {
        Map<String, Object> params = new HashMap<>();
        params.put("subscriptionType", subscriptionType);
        params.put("page", page.eventValue);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Marketing.Subscription.TrialSubs.Succeed", params);
    }
    
    /**
        Успешное оформление регулярной подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. page - Название экрана, где было предложение о подписке
    */
    public void marketingSubscriptionRegularSubsSucceed(String subscriptionType, SubscriptionPage page) {
        Map<String, Object> params = new HashMap<>();
        params.put("subscriptionType", subscriptionType);
        params.put("page", page.eventValue);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Marketing.Subscription.RegularSubs.Succeed", params);
    }
    
    public enum PaymentWidgetSubscriptionOfferShowedV2Path {
        PAYMENT_WIDGET("payment_widget"),
        PURCHASE_OPTION("purchase_option");
        public final String eventValue;
        PaymentWidgetSubscriptionOfferShowedV2Path(String eventValue) {
            this.eventValue = eventValue;
        }
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
    public void paymentWidgetSubscriptionOfferShowedV2(String subscriptionType, String offerTitle, String offerText, int billingProductId, int position, PaymentWidgetSubscriptionOfferShowedV2Path path, String title, String uuid) {
        Map<String, Object> params = new HashMap<>();
        params.put("subscriptionType", subscriptionType);
        params.put("offerTitle", offerTitle);
        params.put("offerText", offerText);
        params.put("eventType", "offerShow");
        params.put("offerType", "subscription");
        params.put("monetizationModel", "SVOD");
        params.put("billingProductId", String.valueOf(billingProductId));
        params.put("position", String.valueOf(position));
        params.put("page", "payment_widget");
        params.put("path", path.eventValue);
        params.put("title", title);
        params.put("uuid", uuid);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(2, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("PaymentWidget.SubscriptionOffer.Showed", params);
    }
    
    /**
        Переход на оплату подписки
        
        0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
        1. offerTitle - Текст кнопки
        2. offerText - Текст оффера
        3. eventType - Константа для единообразной обработки кросссервисных событий.
    */
    public void paymentWidgetSubscriptionOfferNavigated(String subscriptionType, String offerTitle, String offerText) {
        Map<String, Object> params = new HashMap<>();
        params.put("subscriptionType", subscriptionType);
        params.put("offerTitle", offerTitle);
        params.put("offerText", offerText);
        params.put("eventType", "offerClick");
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", params);
    }
    
    public enum PaymentWidgetSubscriptionOfferNavigatedV2Path {
        PAYMENT_WIDGET("payment_widget"),
        PURCHASE_OPTION("purchase_option");
        public final String eventValue;
        PaymentWidgetSubscriptionOfferNavigatedV2Path(String eventValue) {
            this.eventValue = eventValue;
        }
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
    public void paymentWidgetSubscriptionOfferNavigatedV2(String subscriptionType, String offerTitle, String offerText, int billingProductId, int position, PaymentWidgetSubscriptionOfferNavigatedV2Path path, String title, String uuid) {
        Map<String, Object> params = new HashMap<>();
        params.put("subscriptionType", subscriptionType);
        params.put("offerTitle", offerTitle);
        params.put("offerText", offerText);
        params.put("eventType", "offerClick");
        params.put("offerType", "subscription");
        params.put("monetizationModel", "SVOD");
        params.put("billingProductId", String.valueOf(billingProductId));
        params.put("position", String.valueOf(position));
        params.put("page", "payment_widget");
        params.put("path", path.eventValue);
        params.put("title", title);
        params.put("uuid", uuid);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(2, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("PaymentWidget.SubscriptionOffer.Navigated", params);
    }
    
    /**
        Переход к строке поиска
        
    */
    public void searchSearchEngineStarted() {
        Map<String, Object> params = new HashMap<>();
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Search.SearchEngine.Started", params);
    }
    
    /**
        Показ саджестов для текущего запроса
        
        0. query - Запрос в поиске
        1. no_titles - Не найден ни один тайтл
        2. no_persons - Не найдена ни одна персона
        3. no_cinemas - Не найден ни один кинотеатр
    */
    public void searchSearchEngineSuggestShowed(String query, boolean noTitles, boolean noPersons, boolean noCinemas) {
        Map<String, Object> params = new HashMap<>();
        params.put("query", query);
        params.put("no_titles", String.valueOf(noTitles));
        params.put("no_persons", String.valueOf(noPersons));
        params.put("no_cinemas", String.valueOf(noCinemas));
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.Showed", params);
    }
    
    public enum SearchSearchEngineSuggestNavigatedTo {
        PERSON_CARD("person_card"),
        TITLE_CARD("title_card"),
        CINEMA_CARD("cinema_card"),
        GLOBAL_SEARCH_RESULT("global_search_result"),
        SEARCH_LIST("search_list");
        public final String eventValue;
        SearchSearchEngineSuggestNavigatedTo(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    /**
        Переход к другому экрану
        
        0. to - тип экрана
    */
    public void searchSearchEngineSuggestNavigated(SearchSearchEngineSuggestNavigatedTo to) {
        Map<String, Object> params = new HashMap<>();
        params.put("to", to.eventValue);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.Navigated", params);
    }
    
    public enum SearchSearchEngineSuggestSelectedType {
        ALL_RESULTS("all_results"),
        OTT_RESULTS("ott_results");
        public final String eventValue;
        SearchSearchEngineSuggestSelectedType(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    /**
        Выбор варианта отображения саджеста
        
        0. type - Типы отображения
    */
    public void searchSearchEngineSuggestSelected(SearchSearchEngineSuggestSelectedType type) {
        Map<String, Object> params = new HashMap<>();
        params.put("type", type.eventValue);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.Selected", params);
    }
    
    /**
        Возникла ошибка при показе саджеста
        
        0. type - Тип ошибки
        1. code - Код ошибки
        2. text - Описание ошибки
    */
    public void searchSearchEngineSuggestErrorRaised(ErrorType type, int code, String text) {
        Map<String, Object> params = new HashMap<>();
        params.put("type", type.eventValue);
        params.put("code", String.valueOf(code));
        params.put("text", text);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Search.SearchEngine.Suggest.ErrorRaised", params);
    }
    
}
