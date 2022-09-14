/**
 * AUTO-GENERATED FILE. DO NOT MODIFY
 * This class was automatically generated.
 */
/* ktlint-disable */

interface EvgenAnalyticsTracker {
    fun trackBoolEvent(event: String, param: Boolean)
    fun trackIntEvent(event: String, param: Int)
    fun trackDoubleEvent(event: String, param: Double)
    fun trackTimeMillisecondsEvent(event: String, param: Long)
}

class EvgenAnalytics(private val eventTracker: EvgenAnalyticsTracker) {
    
    /**
     * Event description
     * 
     * 0. intParam1 - Интовый параметр
     */
    fun myIntEvent1(intParam1: Int) {
        eventTracker.trackIntEvent("MyIntEvent1", intParam1)
    }
    
    /**
     * Event description
     * 
     * 0. intParam2 - Интовый параметр
     */
    fun myIntEvent2(intParam2: Int) {
        eventTracker.trackIntEvent("MyIntEvent2", intParam2)
    }
    
    /**
     * Event description
     * 
     * 0. doubleParam - Параметр типа double
     */
    fun myDoubleEvent(doubleParam: Double) {
        eventTracker.trackDoubleEvent("MyDoubleEvent", doubleParam)
    }
    
    /**
     * Event description
     * 
     * 0. boolParam - Параметр для логирования времени
     */
    fun myBoolEvent(boolParam: Boolean) {
        eventTracker.trackBoolEvent("MyBoolEvent", boolParam)
    }
    
    /**
     * Event description
     * 
     * 0. timeParam - Параметр типа double
     */
    fun myTimeEvent(timeParam: Long) {
        eventTracker.trackTimeMillisecondsEvent("MyTimeEvent", timeParam)
    }
    
}
