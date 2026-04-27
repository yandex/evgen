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
        var keysToRemove = new List<string>();
        foreach (var kvp in mergedParams) {
            if (kvp.Value == null) {
                keysToRemove.Add(kvp.Key);
            }
        }
        foreach (var key in keysToRemove) {
            mergedParams.Remove(key);
        }
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

    /**
        0. optionalGlobal - Необязательный глобальный параметр
    */
    public class GlobalParams {
        public string? optionalGlobal;

        public Dictionary<string, object> MakeParams() {
            var parameters = new Dictionary<string, object>();
            parameters.Add("optionalGlobal", optionalGlobal)
            return parameters;
        }

        public GlobalParams(optionalGlobal: string? = null) {
            this.optionalGlobal = optionalGlobal
        }
    }

    /**
        0. optionalPlatformHint - Необязательная подсказка с платформы
    */
    public class PlatformParams {
        public string? optionalPlatformHint;
        
        public Dictionary<string, object> MakeParams() {
            var parameters = new Dictionary<string, object>();
            parameters.Add("optionalPlatformHint", optionalPlatformHint)
            return parameters;
        }
        
        public PlatformParams(optionalPlatformHint: string? = null) {
            this.optionalPlatformHint = optionalPlatformHint
        }
    }

    /**
        Событие с optional-параметрами; клиент может не передавать их, тогда при merge null-ключи отфильтровываются
    
        1. requiredId - Обязательный идентификатор
        2. optionalContext - Необязательный контекст
        3. optionalScore - Необязательное числовое значение
    */
    public void OptionalNamespaceDemoEvent(
        string requiredId,
        string? optionalContext = null,
        int? optionalScore = null
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("requiredId", requiredId);
        parameters.Add("optionalContext", optionalContext);
        parameters.Add("optionalScore", optionalScore);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("OptionalNamespace.DemoEvent", parameters);
    }

}
