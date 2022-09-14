/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

import Foundation

public protocol EvgenAnalyticsTracker {
    func trackIntEvent(_ event: String, param: Int)
    func trackDoubleEvent(_ event: String, param: Double)
    func trackBoolEvent(_ event: String, param: Bool)
    func trackTimeMillisecondsEvent(_ event: String, param: Double)
}

public final class EvgenAnalytics {
    public init(eventTracker: EvgenAnalyticsTracker) {
        self.eventTracker = eventTracker
    }
    
    private let eventTracker: EvgenAnalyticsTracker
    
    /**
        Event description
        
        0. intParam1 - Интовый параметр
    */
    public func myIntEvent1(intParam1: Int) {
        eventTracker.trackIntEvent("MyIntEvent1", param: intParam1)
    }
    
    /**
        Event description
        
        0. intParam2 - Интовый параметр
    */
    public func myIntEvent2(intParam2: Int) {
        eventTracker.trackIntEvent("MyIntEvent2", param: intParam2)
    }
    
    /**
        Event description
        
        0. doubleParam - Параметр типа double
    */
    public func myDoubleEvent(doubleParam: Double) {
        eventTracker.trackDoubleEvent("MyDoubleEvent", param: doubleParam)
    }
    
    /**
        Event description
        
        0. boolParam - Параметр для логирования времени
    */
    public func myBoolEvent(boolParam: Bool) {
        eventTracker.trackBoolEvent("MyBoolEvent", param: boolParam)
    }
    
    /**
        Event description
        
        0. timeParam - Параметр типа double
    */
    public func myTimeEvent(timeParam: Double) {
        eventTracker.trackTimeMillisecondsEvent("MyTimeEvent", param: timeParam)
    }
    
}
