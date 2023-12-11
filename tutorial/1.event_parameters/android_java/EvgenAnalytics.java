/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */

package ru.yandex.kinopoisk;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public final class EvgenAnalytics {
    public static final class GlobalParams {
        public String globalParam;
        public Map<String, Object> paramsMap;
        public GlobalParams(String globalParam) {
            this.globalParam = globalParam;
            Map<String, Object> params = new HashMap<>();
            params.put("globalParam", globalParam);
            this.paramsMap = params;
        }
    }
    
    public static final class PlatformParams {
        public Map<String, Object> paramsMap;
        public PlatformParams() {
            Map<String, Object> params = new HashMap<>();
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
    
    public EvgenAppAnalytics(Tracker tracker, GlobalParamsProvider globalParamsProvider, PlatformParamsProvider platformParamsProvider) {
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
    
    public enum Pages {
        SCREEN_1("screen_1"),
        SCREEN_2("screen_2"),
        SCREEN_3("screen_3");
        public final String eventValue;
        Pages(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    /**
     *  Первое событие с переиспользуемым параметром
     *
     *  0. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    public void anotherNamespaceEvent1(String reusedParam) {
        Map<String, Object> params = new HashMap<>();
        params.put("reusedParam", reusedParam);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("AnotherNamespace.Event1", params);
    }

    /**
     *  Второе событие с переиспользуемым параметром
     *
     *  0. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    public void anotherNamespaceEvent2(String reusedParam) {
        Map<String, Object> params = new HashMap<>();
        params.put("reusedParam", reusedParam);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("AnotherNamespace.Event2", params);
    }

    public enum MyNamespaceMyEventEnumParam {
        OPTION1("option1"),
        OPTION2("option2"),
        OPTION3("option3");
        public final String eventValue;
        MyNamespaceMyEventEnumParam(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    public enum MyNamespaceMyEventEnumParamInt {
        INT_1("1"),
        INT_2("2"),
        INT_3("3"),
        public final String eventValue;
        MyNamespaceMyEventEnumParamInt(String eventValue) {
            this.eventValue = eventValue;
        }
    }
    
    /**
     *  События со всеми возможными типами параметров
     *
     *  0. stringParam - Параметр типа String
     *  1. intParam - Параметр типа Int
     *  2. longIntParam - Параметр типа Long Int
     *  3. boolParam - Параметр типа Bool
     *  4. doubleParam - Параметр типа Double
     *  5. constParam - Параметр типа Const. Не участвует в сигнатуре функции, но логируется в при отправке в трекер
     *  6. enumParam - Параметр типа Enum. При логировании можновыбрать только один вариант. В коде имееттип MyNamespaceMyEventEnumparam
     *  7. enumParamInt - Параметр типа Enum Int. При логировании можновыбрать только один вариант. В коде имееттип MyNamespaceMyEventEnumparam
     *  8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages.Если какой-то enum используется больше одного раза,то лучше давать ему явное имя, разботчики смогутобращаться к нему однообразно
     *  9. dictParam - параметр типа Dict.
     *  10. platformConst - Платформозависимая константа
     *  11. listOfInt - Список целочисленных параметров
     *  12. listOfDouble - Список флотовых параметров
     *  13. listOfString - Cписок строк
     */
    public void myNamespaceMyEvent(String stringParam, int intParam, long longIntParam, boolean boolParam, double doubleParam, MyNamespaceMyEventEnumParam enumParam, MyNamespaceMyEventEnumParamInt enumParamInt, Pages namedEnumParam, Map<String, ?> dictParam, List<int> listOfInt, List<double> listOfDouble, List<String> listOfString) {
        Map<String, Object> params = new HashMap<>();
        params.put("stringParam", stringParam);
        params.put("intParam", String.valueOf(intParam));
        params.put("longIntParam", String.valueOf(longIntParam));
        params.put("boolParam", String.valueOf(boolParam));
        params.put("doubleParam", String.valueOf(doubleParam));
        params.put("constParam", "ValueToLog");
        params.put("enumParam", enumParam.eventValue);
        params.put("enumParamInt", enumParamInt.eventValue);
        params.put("namedEnumParam", namedEnumParam.eventValue);
        params.put("dictParam", dictParam);
        params.put("platformConst", "AndroidValue");
        params.put("listOfInt", listOfInt);
        params.put("listOfDouble", listOfDouble);
        params.put("listOfString", listOfString);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("MyNamespace.MyEvent", params);
    }

}
