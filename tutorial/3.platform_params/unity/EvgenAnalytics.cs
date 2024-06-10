/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

using System.Collections.Generic;

class EvgenAnalytics {
    public EvgenAnalytics(
        ITracker eventTracker,
        IGlobalParamsProvider globalParamsProvider,
        IPlatformParamsProvider platformParamsProvider
    ) {
        _eventTracker = eventTracker;
        _globalParamsProvider = globalParamsProvider;
        _platformParamsProvider = platformParamsProvider;
    }

    private readonly ITracker _eventTracker;
    private readonly IGlobalParamsProvider _globalParamsProvider;
    private readonly IPlatformParamsProvider _platformParamsProvider;

    private void TrackEvent(string eventName, Dictionary<string, object> parameters) {
        var mergedParams = new Dictionary<string, object>(parameters);
        mergedParams.PutAll(_globalParamsProvider.GetGlobalParams().MakeParams());
        mergedParams.PutAll(_platformParamsProvider.GetPlatformParams().MakeParams());
        _eventTracker.TrackEvent(eventName, mergedParams);
    }

    private Dictionary<string, object> MakeMeta(int event_version, Dictionary<string, object> interfaces) {
        Dictionary<string, object>  metaDict = new Dictionary<string, object>();
        Dictionary<string, object> eventDict = new Dictionary<string, object>();
        eventDict.Add("version", event_version);
        metaDict.Add("event", eventDict);
        metaDict.Add("interfaces", interfaces);
        return metaDict;
    }

    public interface ITracker {
        void TrackEvent(string eventName, Dictionary<string, object> parameters);
    }

    public interface IGlobalParamsProvider {
        GlobalParams GetGlobalParams();
    }

    public interface IPlatformParamsProvider {
        PlatformParams GetPlatformParams();
    }

    public class GlobalParams {

        public Dictionary<string, object> MakeParams() {
            var parameters = new Dictionary<string, object>();
            return parameters;
        }

        public GlobalParams() {
        }
    }

    /**
        0. unityVersion - Версия Unity
    */
    public class PlatformParams {
        public string unityVersion;
        
        public Dictionary<string, object> MakeParams() {
            var parameters = new Dictionary<string, object>();
            parameters.Add("unityVersion", unityVersion)
            return parameters;
        }
        
        public PlatformParams(unityVersion: string) {
            this.unityVersion = unityVersion
        }
    }

    /**
        Also event description
    
    */
    public void AlsoMyEventLogged(
    ) {
        var parameters = new Dictionary<string, object>();
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("AlsoMyEvent.Logged", parameters);
    }

    /**
        Event description
    
    */
    public void MyEvent(
    ) {
        var parameters = new Dictionary<string, object>();
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("MyEvent", parameters);
    }

}
