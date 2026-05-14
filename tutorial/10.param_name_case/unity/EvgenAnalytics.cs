/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

using System.Collections.Generic;

public class EvgenAnalytics {
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

    public class PlatformParams {
        
        public Dictionary<string, object> MakeParams() {
            var parameters = new Dictionary<string, object>();
            return parameters;
        }
        
        public PlatformParams() {
        }
    }

    /**
        Демонстрация param_name_case: одинаковое событие для Android, iOS, Flutter, WebSmartTV, Unity.
        
    
        1. user_session_id - Ключ в YAML в snake_case
        2. screenTitle - Ключ в YAML в camelCase (без подчёркиваний)
    */
    public void CaseDemoSampleEvent(
        string userSessionId = "guest",
        string screenTitle
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("USER_SESSION_ID", userSessionId);
        parameters.Add("SCREEN_TITLE", screenTitle);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("CaseDemo.SampleEvent", parameters);
    }

}
