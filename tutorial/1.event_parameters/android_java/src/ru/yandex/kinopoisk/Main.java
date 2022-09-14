package ru.yandex.kinopoisk;

import ru.yandex.kinopoisk.EvgenAnalytics;

import java.util.Map;
import java.util.HashMap;
import java.util.List;

class TrackerImpl implements EvgenAnalytics.Tracker {
    @Override
    public void trackEvent(String eventId, Map<String, ?> parameters) {
        System.out.println(eventId);
        System.out.println(parameters.toString());
        System.out.println();
    }
}

class GlobalParamsProviderImpl implements EvgenAnalytics.GlobalParamsProvider {
    @Override
    public EvgenAnalytics.GlobalParams getGlobalParams() {
        return new EvgenAnalytics.GlobalParams("global");
    }
}

class PlatformParamsProviderImpl implements EvgenAnalytics.PlatformParamsProvider {
    @Override
    public EvgenAnalytics.PlatformParams getPlatformParams() {
        return new EvgenAnalytics.PlatformParams();
    }
}

public class Main {

    public static void main(String[] args) {
        EvgenAnalytics analytics = new EvgenAnalytics(
                new TrackerImpl(),
                new GlobalParamsProviderImpl(),
                new PlatformParamsProviderImpl());

        HashMap<String, String> extraParams = new HashMap<String, String>();
        extraParams.put("Param1", "1");

        analytics.myNamespaceMyEvent("string",
                                     1,
                                     1333,
                                     true,
                                     42.3,
                                     EvgenAnalytics.MyNamespaceMyEventEnumParam.OPTION1,
                                     EvgenAnalytics.Pages.SCREEN_1,
                                     extraParams,
                                     List.of(1, 2, 3, 4, 5, 6),
                                     List.of(1.1, 2.2, 3.3, 4.4, 5.5, 6.6),
                                     List.of("STR1", "STR2"));
    }
}
