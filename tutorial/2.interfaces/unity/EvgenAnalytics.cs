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
        Показ экрана магазина
    
        0. page - Название страницы
        1. pageId - Идентификатор страницы
    */
    public void ShopShowed(
        string page,
        int pageId
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("page", page);
        parameters.Add("pageId", pageId);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        Dictionary<string, object> myInterfacesPage = new Dictionary<string, object>();
        myInterfacesPage.Add("version", 1);
        interfacesDict.Add("MyInterfaces.Page", myInterfacesPage);
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("Shop.Showed", parameters);
    }

    /**
        Показ экрана магазина
    
        0. page - Название страницы
        1. movieName - Название фильма
        2. movieId - Идентификатор фильма
        3. pageId - Идентификатор страницы
    */
    public void ShowcaseMovieShowed(
        string page,
        string movieName,
        int movieId,
        int pageId
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("page", page);
        parameters.Add("movieName", movieName);
        parameters.Add("movieId", movieId);
        parameters.Add("pageId", pageId);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        Dictionary<string, object> myInterfacesPage = new Dictionary<string, object>();
        myInterfacesPage.Add("version", 1);
        interfacesDict.Add("MyInterfaces.Page", myInterfacesPage);
        Dictionary<string, object> myInterfacesMovie = new Dictionary<string, object>();
        myInterfacesMovie.Add("version", 2);
        interfacesDict.Add("MyInterfaces.Movie", myInterfacesMovie);
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("Showcase.Movie.Showed", parameters);
    }

    /**
        Показ экрана магазина
    
        0. page - Название страницы
        1. movieName - Название фильма
        2. pageId - Идентификатор страницы
    */
    public void ShowcaseTVShowShowed(
        string page,
        string movieName,
        int pageId
    ) {
        var parameters = new Dictionary<string, object>();
        parameters.Add("page", page);
        parameters.Add("movieName", movieName);
        parameters.Add("pageId", pageId);
        Dictionary<string, object> interfacesDict = new Dictionary<string, object>();
        Dictionary<string, object> myInterfacesPage = new Dictionary<string, object>();
        myInterfacesPage.Add("version", 1);
        interfacesDict.Add("MyInterfaces.Page", myInterfacesPage);
        Dictionary<string, object> myInterfacesMovie = new Dictionary<string, object>();
        myInterfacesMovie.Add("version", 1);
        interfacesDict.Add("MyInterfaces.Movie", myInterfacesMovie);
        var _meta = MakeMeta(1, interfacesDict);
        parameters.Add("_meta", _meta);
        TrackEvent("Showcase.TVShow.Showed", parameters);
    }

}
