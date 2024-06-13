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

    /**
        0. globalParam - Глобальный параметр, который добавится к каждому событию
    */
    public class GlobalParams {
        public string globalParam;

        public Dictionary<string, object> MakeParams() {
            var parameters = new Dictionary<string, object>();
            options["globalParam"] = globalParam
            parameters.Add("globalParam", globalParam)
            return parameters;
        }

        public GlobalParams(globalParam: string) {
            this.globalParam = globalParam
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

    public class MyNamespaceMyEventEnumParam {
        private MyNamespaceMyEventEnumParam(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static MyNamespaceMyEventEnumParam OPTION_1 { get { return new MyNamespaceMyEventEnumParam("option1"); } }
        public static MyNamespaceMyEventEnumParam OPTION_2 { get { return new MyNamespaceMyEventEnumParam("option2"); } }
        public static MyNamespaceMyEventEnumParam OPTION_3 { get { return new MyNamespaceMyEventEnumParam("option3"); } }
    }
    
    public class Pages {
        private Pages(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static Pages SCREEN_1 { get { return new Pages("screen_1"); } }
        public static Pages SCREEN_2 { get { return new Pages("screen_2"); } }
        public static Pages SCREEN_3 { get { return new Pages("screen_3"); } }
    }
    
    /**
        Первое событие с переиспользуемым параметром
    
        0. reusedParam - Параметр, который переиспользуется в нескольких событиях
    */
    public void AnotherNamespaceEvent1(
        string reusedParam
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("reusedParam", reusedParam);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("AnotherNamespace.Event1", parameters);
    }

    /**
        Второе событие с переиспользуемым параметром
    
        0. reusedParam - Параметр, который переиспользуется в нескольких событиях
    */
    public void AnotherNamespaceKebabCaseEvent2(
        string reusedParam
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("reusedParam", reusedParam);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("AnotherNamespace.kebab-case-event-2", parameters);
    }

    public class MyNamespaceMyEventEnumParamInt {
        private MyNamespaceMyEventEnumParamInt(string value) { RawValue = value; }
        public string RawValue { get; private set; }
        public static MyNamespaceMyEventEnumParamInt Int1 { get { return new MyNamespaceMyEventEnumParamInt("1"); } }
        public static MyNamespaceMyEventEnumParamInt Int2 { get { return new MyNamespaceMyEventEnumParamInt("2"); } }
        public static MyNamespaceMyEventEnumParamInt Int3 { get { return new MyNamespaceMyEventEnumParamInt("3"); } }
    }
    
    /**
        События со всеми возможными типами параметров
    
        0. stringParam - Параметр типа String
        1. intParam - Параметр типа Int
        2. longIntParam - Параметр типа Long Int
        3. boolParam - Параметр типа Bool
        4. doubleParam - Параметр типа Double
        5. constParam - Параметр типа Const. Не участвует в сигнатуре функции, но логируется в при отправке в трекер
        6. enumParam - Параметр типа Enum. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
        7. enumParamInt - Параметр типа Enum Int. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
        8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages. Если какой-то enum используется больше одного раза, то лучше давать ему явное имя, разботчики смогут обращаться к нему однообразно
        9. dictParam - параметр типа Dict.
        10. dictElementType - параметр типа Dict енумов.
        11. typedDictParam - типизированный Dict.
        12. typedListParam - типизированный List.
        13. platformConst - Платформозависимая константа
        14. listOfInt - Список целочисленных параметров
        15. listOfDouble - Список флотовых параметров
        16. listOfString - Cписок строк
        17. listOfEnum - Cписок енумов
    */
    public void MyNamespaceMyEvent(
        string stringParam = "val",
        int intParam = 42,
        long longIntParam,
        bool boolParam = true,
        double doubleParam,
        MyNamespaceMyEventEnumParam enumParam = MyNamespaceMyEventEnumParam.Option1,
        MyNamespaceMyEventEnumParamInt enumParamInt = MyNamespaceMyEventEnumParamInt.Int1,
        Pages namedEnumParam,
        Dictionary<string, object> dictParam,
        Dictionary<string, MyNamespaceMyEventEnumParam> dictElementType,
        Dictionary<string, object> typedDictParam,
        List<object> typedListParam,
        List<int> listOfInt = [],
        List<double> listOfDouble = [],
        List<string> listOfString = [],
        List<MyNamespaceMyEventEnumParam> listOfEnum = []
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("stringParam", stringParam);
        parameters.Add("intParam", intParam);
        parameters.Add("longIntParam", longIntParam);
        parameters.Add("boolParam", boolParam);
        parameters.Add("doubleParam", doubleParam);
        parameters.Add("constParam", "ValueToLog");
        parameters.Add("enumParam", enumParam.RawValue);
        parameters.Add("enumParamInt", enumParamInt.RawValue);
        parameters.Add("namedEnumParam", namedEnumParam.RawValue);
        parameters.Add("dictParam", dictParam);
        parameters.Add("dictElementType", dictElementType);
        parameters.Add("typedDictParam", typedDictParam);
        parameters.Add("typedListParam", typedListParam);
        parameters.Add("platformConst", "UnityValue");
        parameters.Add("listOfInt", listOfInt);
        parameters.Add("listOfDouble", listOfDouble);
        parameters.Add("listOfString", listOfString);
        parameters.Add("listOfEnum", listOfEnum);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("MyNamespace.MyEvent", parameters);
    }

}
