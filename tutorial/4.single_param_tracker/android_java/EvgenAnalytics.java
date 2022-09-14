/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

package ru.yandex.kinopoisk;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public final class EvgenAnalytics {
    public interface Tracker {
        void trackIntEvent(final String eventName, final int param);
        void trackDoubleEvent(final String eventName, final double param);
        void trackBoolEvent(final String eventName, final boolean param);
        void trackTimeMillisecondsEvent(final String eventName, final long param);
    }
    
    public EvgenAnalytics(Tracker tracker) {
        this.tracker = tracker;
    }
    
    private Tracker tracker;
    
    /**
        Event description
        
        0. intParam1 - Интовый параметр
    */
    public void myIntEvent1(int intParam1) {
        this.tracker.trackIntEvent("MyIntEvent1", intParam1);
    }
    
    /**
        Event description
        
        0. intParam2 - Интовый параметр
    */
    public void myIntEvent2(int intParam2) {
        this.tracker.trackIntEvent("MyIntEvent2", intParam2);
    }
    
    /**
        Event description
        
        0. doubleParam - Параметр типа double
    */
    public void myDoubleEvent(double doubleParam) {
        this.tracker.trackDoubleEvent("MyDoubleEvent", doubleParam);
    }
    
    /**
        Event description
        
        0. boolParam - Параметр для логирования времени
    */
    public void myBoolEvent(boolean boolParam) {
        this.tracker.trackBoolEvent("MyBoolEvent", boolParam);
    }
    
    /**
        Event description
        
        0. timeParam - Параметр типа double
    */
    public void myTimeEvent(long timeParam) {
        this.tracker.trackTimeMillisecondsEvent("MyTimeEvent", timeParam);
    }
    
}
