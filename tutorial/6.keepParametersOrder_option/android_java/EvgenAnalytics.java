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
        public Map<String, Object> paramsMap;
        public GlobalParams() {
            Map<String, Object> params = new HashMap<>();
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
     *  1. firstParam - Первый параметр
     *  2. paramFromAnotherFile - Параметр, описанный в отдельным файле.
     *  3. reusedParam - Description
     *  4. batchParam1 - Параметр, описанный в отдельным файле.
     *  5. batchParam2 - Параметр, описанный в отдельным файле.
     *  6. lastParam - Последний параметр
     */
    public void namespaceEvent(int firstParam, String paramFromAnotherFile, String reusedParam, String batchParam1, String batchParam2, String lastParam) {
        Map<String, Object> params = new HashMap<>();
        params.put("firstParam", String.valueOf(firstParam));
        params.put("paramFromAnotherFile", paramFromAnotherFile);
        params.put("reusedParam", reusedParam);
        params.put("batchParam1", batchParam1);
        params.put("batchParam2", batchParam2);
        params.put("lastParam", lastParam);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Namespace.Event", params);
    }

}
