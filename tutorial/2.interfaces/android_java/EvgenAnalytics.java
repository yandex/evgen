/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

package ru.yandex.kinopoisk;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public final class EvgenAnalytics {
    public static final class GlobalParams {
        public Map<String, Object> paramsMap;
        public GlobalParams() {
            Map<String, Object> params = new HashMap<>();
            this.paramsMap = params;
        }
    }
    
    public static final class PlatformParams {
        public Map<String, Object> paramsMap;
        public PlatformParams() {
            Map<String, Object> params = new HashMap<>();
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
    
    public EvgenAnalytics(Tracker tracker, GlobalParamsProvider globalParamsProvider, PlatformParamsProvider platformParamsProvider) {
        this.tracker = tracker;
        this.globalParamsProvider = globalParamsProvider;
        this.platformParamsProvider = platformParamsProvider;
    }
    
    private void trackEvent(String eventName, Map<String, ?> parameters) {
        Map<String, Object> mergedParams = new HashMap<>(parameters);
        mergedParams.putAll(this.globalParamsProvider.getGlobalParams().paramsMap);
        mergedParams.putAll(this.platformParamsProvider.getPlatformParams().paramsMap);
        this.tracker.trackEvent(eventName, mergedParams);
    }
    
    private Map<String, Object>  makeMeta(int event_version, Map<String, ?> interfaces ) {
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
        ?????????? ???????????? ????????????????
        
        0. page - ???????????????? ????????????????
        1. pageId - ?????????????????????????? ????????????????
    */
    public void shopShowed(String page, int pageId) {
        Map<String, Object> params = new HashMap<>();
        params.put("page", page);
        params.put("pageId", String.valueOf(pageId));
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> myInterfacesPage = new HashMap<>();
        myInterfacesPage.put("version", 1);
        interfacesDict.put("MyInterfaces.Page", myInterfacesPage);
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Shop.Showed", params);
    }
    
    /**
        ?????????? ???????????? ????????????????
        
        0. page - ???????????????? ????????????????
        1. movieName - ???????????????? ????????????
        2. movieId - ?????????????????????????? ????????????
        3. pageId - ?????????????????????????? ????????????????
    */
    public void showcaseMovieShowed(String page, String movieName, int movieId, int pageId) {
        Map<String, Object> params = new HashMap<>();
        params.put("page", page);
        params.put("movieName", movieName);
        params.put("movieId", String.valueOf(movieId));
        params.put("pageId", String.valueOf(pageId));
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> myInterfacesPage = new HashMap<>();
        myInterfacesPage.put("version", 1);
        interfacesDict.put("MyInterfaces.Page", myInterfacesPage);
        Map<String, Object> myInterfacesMovie = new HashMap<>();
        myInterfacesMovie.put("version", 2);
        interfacesDict.put("MyInterfaces.Movie", myInterfacesMovie);
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Showcase.Movie.Showed", params);
    }
    
    /**
        ?????????? ???????????? ????????????????
        
        0. page - ???????????????? ????????????????
        1. movieName - ???????????????? ????????????
        2. pageId - ?????????????????????????? ????????????????
    */
    public void showcaseTVShowShowed(String page, String movieName, int pageId) {
        Map<String, Object> params = new HashMap<>();
        params.put("page", page);
        params.put("movieName", movieName);
        params.put("pageId", String.valueOf(pageId));
        Map<String, Object> interfacesDict = new HashMap<>();
        Map<String, Object> myInterfacesPage = new HashMap<>();
        myInterfacesPage.put("version", 1);
        interfacesDict.put("MyInterfaces.Page", myInterfacesPage);
        Map<String, Object> myInterfacesMovie = new HashMap<>();
        myInterfacesMovie.put("version", 1);
        interfacesDict.put("MyInterfaces.Movie", myInterfacesMovie);
        Map<String, Object> _meta = makeMeta(1, interfacesDict);
        params.put("_meta", _meta);
        trackEvent("Showcase.TVShow.Showed", params);
    }
    
}
