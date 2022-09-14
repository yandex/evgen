package ru.yandex.kinopoisk;

import ru.yandex.kinopoisk.EvgenAnalytics;

import java.util.Map;
import java.util.HashMap;

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
        HashMap<String, String> experiments = new HashMap<String, String>();
        experiments.put("ExpName", "AB");
        return new EvgenAnalytics.GlobalParams(
                "2,4,55",
                true,
                experiments
                );
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

        analytics.searchSearchEngineSuggestNavigated(EvgenAnalytics.SearchSearchEngineSuggestNavigatedTo.PERSON_CARD);
        HashMap<String, String> extraParams = new HashMap<String, String>();
        extraParams.put("Param1", "1");
        analytics.marketingSubscriptionSucceed(
                "sub_type",
                EvgenAnalytics.SubscriptionPage.PAYMENT_WIDGET,
                extraParams
                );
    }
}
