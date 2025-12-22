/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

using System.Collections.Generic;
using UserId = string;
using ContentId = string;
using Timestamp = long;
using Price = double;
using ViewCount = int;
using MetadataV1 = Dictionary<string, object>;
using MetadataV2 = Dictionary<string, object>;
using ContentItems = List<object>;

public class PageId {
    private PageId(string value) { RawValue = value; }
    public string RawValue { get; private set; }
    public static PageId HOME { get { return new PageId("home"); } }
    public static PageId CATALOG { get { return new PageId("catalog"); } }
    public static PageId MOVIE_CARD { get { return new PageId("movie_card"); } }
    public static PageId SERIES_CARD { get { return new PageId("series_card"); } }
}


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
        0. globalParam - Глобальный параметр, который добавится к каждомоу событию
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

    /**
        Первое событие с переиспользуемым параметром
    
        1. reusedParam - Параметр, который переиспользуется в нескольких событиях
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
    
        1. reusedParam - Параметр, который переиспользуется в нескольких событиях
    */
    public void AnotherNamespaceEvent2(
        string reusedParam
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("reusedParam", reusedParam);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("AnotherNamespace.Event2", parameters);
    }

    /**
        Просмотр страницы (использует глобальный тип PageId)
    
        1. pageId - ID страницы
    */
    public void GlobalTypesDemoPageView(
        PageId pageId
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("pageId", pageId);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("GlobalTypesDemo.PageView", parameters);
    }

    /**
        Покупка контента (примитивные глобальные типы)
    
        1. userId - ID пользователя
        2. contentId - ID контента
        3. price - Цена покупки
        4. timestamp - Время покупки
    */
    public void GlobalTypesDemoPurchase(
        UserId userId,
        ContentId contentId,
        Price price,
        Timestamp timestamp
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("userId", userId);
        parameters.Add("contentId", contentId);
        parameters.Add("price", price);
        parameters.Add("timestamp", timestamp);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("GlobalTypesDemo.Purchase", parameters);
    }

    /**
        Просмотр списка контента (использует Metadata.v1)
    
        1. items - Элементы контента
        2. metadata - Метаданные запроса (базовая версия)
    */
    public void GlobalTypesDemoContentListView(
        ContentItems items,
        MetadataV1 metadata
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("items", items);
        parameters.Add("metadata", metadata);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("GlobalTypesDemo.ContentListView", parameters);
    }

    /**
        Просмотр списка контента (использует Metadata.v2 с тегами)
    
        1. items - Элементы контента
        2. metadata - Метаданные запроса (расширенная версия с тегами)
    */
    public void GlobalTypesDemoContentListViewV2(
        ContentItems items,
        MetadataV2 metadata
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("items", items);
        parameters.Add("metadata", metadata);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(2, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("GlobalTypesDemo.ContentListView", parameters);
    }

    /**
        События со всеми возможными типами параметров
    
        1. paramFromAnotherFile - Параметр, описанный в отдельным файле.
        2. batchParam1 - Параметр, описанный в отдельным файле.
        3. batchParam2 - Параметр, описанный в отдельным файле.
        4. stringParam - Парамтер типа String
        5. intParam - Параметр типа Int
    */
    public void MyNamespaceMyEvent(
        string paramFromAnotherFile,
        string batchParam1,
        string batchParam2,
        string stringParam = "val1",
        int intParam = 42
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("paramFromAnotherFile", paramFromAnotherFile);
        parameters.Add("batchParam1", batchParam1);
        parameters.Add("batchParam2", batchParam2);
        parameters.Add("stringParam", stringParam);
        parameters.Add("intParam", intParam);
        parameters.Add("сonstParam", "shop_page");
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("MyNamespace.MyEvent", parameters);
    }

}
