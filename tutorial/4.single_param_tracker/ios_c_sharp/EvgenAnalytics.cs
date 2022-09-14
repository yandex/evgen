/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

using System.Collections.Generic;

public class EvgenAnalytics {
    public interface Tracker {
        void trackIntEvent(string event_name, int param);
        void trackDoubleEvent(string event_name, double param);
        void trackBoolEvent(string event_name, bool param);
        void trackTimeMillisecondsEvent(string event_name, double param);
    }
    
    public EvgenAnalytics(Tracker eventTracker) {
        this.eventTracker = eventTracker;
    }
    
    private Tracker eventTracker ;
    
    /**
        Event description
        
        0. intParam1 - Интовый параметр
    */
    public void myIntEvent1(int intParam1) {
        eventTracker.trackIntEvent("MyIntEvent1", param: intParam1);
    }
    
    /**
        Event description
        
        0. intParam2 - Интовый параметр
    */
    public void myIntEvent2(int intParam2) {
        eventTracker.trackIntEvent("MyIntEvent2", param: intParam2);
    }
    
    /**
        Event description
        
        0. doubleParam - Параметр типа double
    */
    public void myDoubleEvent(double doubleParam) {
        eventTracker.trackDoubleEvent("MyDoubleEvent", param: doubleParam);
    }
    
    /**
        Event description
        
        0. boolParam - Параметр для логирования времени
    */
    public void myBoolEvent(bool boolParam) {
        eventTracker.trackBoolEvent("MyBoolEvent", param: boolParam);
    }
    
    /**
        Event description
        
        0. timeParam - Параметр типа double
    */
    public void myTimeEvent(double timeParam) {
        eventTracker.trackTimeMillisecondsEvent("MyTimeEvent", param: timeParam);
    }
    
}
