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
    
    public class GlobalParams {
        public string globalParam;
        
        public Dictionary<string, object> makeParams() {
            var parameters = new Dictionary<string, object>();
            parameters.Add("globalParam", globalParam);
            return parameters;
        }
        
        public GlobalParams(string globalParam) {
            this.globalParam = globalParam;
        }
    }
    public class PlatformParams {
        
        public Dictionary<string, object> makeParams() {
            var parameters = new Dictionary<string, object>();
            return parameters;
        }
        
        public PlatformParams() {
        }
    }
    /**
        Первое событие с переиспользуемым параметром
        
        0. reusedParam - Параметр, который переиспользуется в нескольких событиях
    */
    public void anotherNamespaceEvent1(string reusedParam) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("reusedParam", reusedParam);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("AnotherNamespace.Event1", parameters);
    }
    
    /**
        Второе событие с переиспользуемым параметром
        
        0. reusedParam - Параметр, который переиспользуется в нескольких событиях
    */
    public void anotherNamespaceEvent2(string reusedParam) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("reusedParam", reusedParam);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("AnotherNamespace.Event2", parameters);
    }
    
    /**
        События со всеми возможными типами параметров
        
        0. paramFromAnotherFile - Параметр, описанный в отдельным файле.
        1. batchParam1 - Параметр, описанный в отдельным файле.
        2. batchParam2 - Параметр, описанный в отдельным файле.
        3. stringParam - Парамтер типа String
        4. intParam - Параметр типа Int
        5. сonstParam - Constant parameter
    */
    public void myNamespaceMyEvent(string paramFromAnotherFile, string batchParam1, string batchParam2, string stringParam = "val1", int intParam = 42) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("paramFromAnotherFile", paramFromAnotherFile);
        parameters.Add("batchParam1", batchParam1);
        parameters.Add("batchParam2", batchParam2);
        parameters.Add("stringParam", stringParam);
        parameters.Add("intParam", intParam);
        parameters.Add("сonstParam", "shop_page");
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("MyNamespace.MyEvent", parameters);
    }
    
}
