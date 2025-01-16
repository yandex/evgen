/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */

package ru.yandex.kinopoisk;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public final class EvgenAnalytics {
    /**
     * 0. globalParam - Глобальный параметр, который добавится к каждомоу событию
     */
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
    
    /**
     *  Первое событие с переиспользуемым параметром
     *
     *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
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
     *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
     */
    public void anotherNamespaceEvent2(String reusedParam) {
        Map<String, Object> params = new HashMap<>();
        params.put("reusedParam", reusedParam);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("AnotherNamespace.Event2", params);
    }

    /**
     *  События со всеми возможными типами параметров
     *
     *  1. paramFromAnotherFile - Параметр, описанный в отдельным файле.
     *  2. batchParam1 - Параметр, описанный в отдельным файле.
     *  3. batchParam2 - Параметр, описанный в отдельным файле.
     *  4. stringParam - Парамтер типа String
     *  5. intParam - Параметр типа Int
     */
    public void myNamespaceMyEvent(String paramFromAnotherFile, String batchParam1, String batchParam2, String stringParam, int intParam) {
        Map<String, Object> params = new HashMap<>();
        params.put("paramFromAnotherFile", paramFromAnotherFile);
        params.put("batchParam1", batchParam1);
        params.put("batchParam2", batchParam2);
        params.put("stringParam", stringParam);
        params.put("intParam", String.valueOf(intParam));
        params.put("сonstParam", "shop_page");
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("MyNamespace.MyEvent", params);
    }

}
