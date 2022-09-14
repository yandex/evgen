package ru.yandex.kinopoisk;

import ru.yandex.kinopoisk.EvgenAnalytics;

import java.util.Map;
import java.util.HashMap;

class TrackerImpl implements EvgenAnalytics.Tracker {
    @Override
    public void trackIntEvent(String eventId, int param) {
        System.out.println(eventId);
        System.out.println(param);
        System.out.println();
    }

    @Override
    public void trackDoubleEvent(String eventId, double param) {
        System.out.println(eventId);
        System.out.println(param);
        System.out.println();
    }

    @Override
    public void trackBoolEvent(String eventId, boolean param) {
        System.out.println(eventId);
        System.out.println(param);
        System.out.println();
    }

    @Override
    public void trackTimeMillisecondsEvent(String eventId, double param) {
        System.out.println(eventId);
        System.out.println(param);
        System.out.println();
    }
}


public class Main {

    public static void main(String[] args) {
        EvgenAnalytics analytics = new EvgenAnalytics(new TrackerImpl());

        analytics.myIntEvent1(1);
        analytics.myIntEvent2(2);
        analytics.myDoubleEvent(3.0);
        analytics.myBoolEvent(true);
        analytics.myTimeEvent(1000.1);
    }
}
