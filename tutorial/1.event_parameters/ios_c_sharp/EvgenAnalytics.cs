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
    public class Pages {
        private Pages(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static Pages SCREEN_1  { get { return new Pages("screen_1"); } }
        public static Pages SCREEN_2  { get { return new Pages("screen_2"); } }
        public static Pages SCREEN_3  { get { return new Pages("screen_3"); } }
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
    
    public class MyNamespaceMyEventEnumParam {
        private MyNamespaceMyEventEnumParam(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static MyNamespaceMyEventEnumParam OPTION1  { get { return new MyNamespaceMyEventEnumParam("option1"); } }
        public static MyNamespaceMyEventEnumParam OPTION2  { get { return new MyNamespaceMyEventEnumParam("option2"); } }
        public static MyNamespaceMyEventEnumParam OPTION3  { get { return new MyNamespaceMyEventEnumParam("option3"); } }
    }
    
    /**
        События со всеми возможными типами параметров
        
        0. stringParam - Параметр типа String
        1. intParam - Параметр типа Int
        2. longIntParam - Параметр типа Long Int
        3. boolParam - Параметр типа Bool
        4. doubleParam - Параметр типа Double
        5. constParam - Параметр типа Const. Не участвует в сигнатуре функции, но логируется в при отправке в трекер
        6. enumParam - Параметр типа Enum. При логировании можновыбрать только один вариант. В коде имееттип MyNamespaceMyEventEnumparam
        7. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages.Если какой-то enum используется больше одного раза,то лучше давать ему явное имя, разботчики смогутобращаться к нему однообразно
        8. dictParam - параметр типа Dict.
        9. platformConst - Платформозависимая константа
        10. listOfInt - Список целочисленных параметров
        11. listOfDouble - Список флотовых параметров
        12. listOfString - Cписок строк
    */
    public void myNamespaceMyEvent(long longIntParam, double doubleParam, MyNamespaceMyEventEnumParam enumParam, Pages namedEnumParam, Dictionary<string, object> dictParam, List<int> listOfInt, List<double> listOfDouble, List<string> listOfString, string stringParam = "val", int intParam = 42, bool boolParam = true) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("stringParam", stringParam);
        parameters.Add("intParam", intParam);
        parameters.Add("longIntParam", longIntParam);
        if (boolParam) {
            parameters.Add("boolParam", "true");
        } else {
            parameters.Add("boolParam", "false");
        }
        parameters.Add("doubleParam", doubleParam);
        parameters.Add("constParam", "ValueToLog");
        parameters.Add("enumParam", enumParam.RawValue);
        parameters.Add("namedEnumParam", namedEnumParam.RawValue);
        parameters.Add("dictParam", dictParam);
        parameters.Add("platformConst", "iOSValue");
        parameters.Add("listOfInt", listOfInt);
        parameters.Add("listOfDouble", listOfDouble);
        parameters.Add("listOfString", listOfString);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = makeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        trackEvent("MyNamespace.MyEvent", parameters);
    }
    
}
