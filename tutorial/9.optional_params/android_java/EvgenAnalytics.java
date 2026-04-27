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
     * 0. optionalGlobal - Необязательный глобальный параметр
     */
    public static final class GlobalParams {
        public String optionalGlobal;
        public Map<String, Object> paramsMap;
        public GlobalParams(String optionalGlobal) {
            this.optionalGlobal = optionalGlobal;
            Map<String, Object> params = new HashMap<>();
            params.put("optionalGlobal", optionalGlobal);
            this.paramsMap = params;
        }
    }
    
    /**
     * 0. optionalPlatformHint - Необязательная подсказка с платформы
     */
    public static final class PlatformParams {
        public String optionalPlatformHint;
        public Map<String, Object> paramsMap;
        public PlatformParams(String optionalPlatformHint) {
            this.optionalPlatformHint = optionalPlatformHint;
            Map<String, Object> params = new HashMap<>();
            params.put("optionalPlatformHint", optionalPlatformHint);
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
        mergedParams.entrySet().removeIf(entry -> entry.getValue() == null);
        this.tracker.trackEvent(eventName, mergedParams);
    }
    
    private Map<String, Object> makeMeta(int event_version, Map<String, ?> interfaces) {
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
     *  Событие с optional-параметрами; клиент может не передавать их, тогда при merge null-ключи отфильтровываются
     *
     *  1. requiredId - Обязательный идентификатор
     *  2. optionalContext - Необязательный контекст
     *  3. optionalScore - Необязательное числовое значение
     *  4. androidOnlyLocal - Локальный параметр только для Android (не в общем списке и не на других платформах)
     */
    public void optionalNamespaceDemoEvent(String requiredId, String optionalContext, int optionalScore, String androidOnlyLocal) {
        Map<String, Object> params = new HashMap<>();
        params.put("requiredId", requiredId);
        params.put("optionalContext", optionalContext);
        params.put("optionalScore", String.valueOf(optionalScore));
        params.put("androidOnlyLocal", androidOnlyLocal);
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("OptionalNamespace.DemoEvent", params);
    }

}
