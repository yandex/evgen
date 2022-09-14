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
        
        public Dictionary<string, object> makeParams() {
            var parameters = new Dictionary<string, object>();
            return parameters;
        }
        
        public GlobalParams() {
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
        Also event description
        
    */
    public void alsoMyEventLogged() {
        var parameters = new Dictionary<string, object>();
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("AlsoMyEvent.Logged", parameters);
    }
    
    /**
        Event description
        
    */
    public void myEvent() {
        var parameters = new Dictionary<string, object>();
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("MyEvent", parameters);
    }
    
}
