/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/

export interface EvgenAnalyticsTracker {
    trackIntEvent(event: string, param: number): void;
    trackDoubleEvent(event: string, param: number): void;
    trackBoolEvent(event: string, param: boolean): void;
    trackTimeMillisecondsEvent(event: string, param: number): void;
}

export class EvgenAnalytics {
    private eventTracker: EvgenAnalyticsTracker;
    
    constructor(eventTracker: EvgenAnalyticsTracker) {
        this.eventTracker = eventTracker;
    }
    
    /**
        Event description
        
        0. intParam1 - Интовый параметр
    */
    myIntEvent1(intParam1: number) {
        this.eventTracker.trackIntEvent("MyIntEvent1", intParam1)
    }
    
    /**
        Event description
        
        0. intParam2 - Интовый параметр
    */
    myIntEvent2(intParam2: number) {
        this.eventTracker.trackIntEvent("MyIntEvent2", intParam2)
    }
    
    /**
        Event description
        
        0. doubleParam - Параметр типа double
    */
    myDoubleEvent(doubleParam: number) {
        this.eventTracker.trackDoubleEvent("MyDoubleEvent", doubleParam)
    }
    
    /**
        Event description
        
        0. boolParam - Параметр для логирования времени
    */
    myBoolEvent(boolParam: boolean) {
        this.eventTracker.trackBoolEvent("MyBoolEvent", boolParam)
    }
    
    /**
        Event description
        
        0. timeParam - Параметр типа double
    */
    myTimeEvent(timeParam: number) {
        this.eventTracker.trackTimeMillisecondsEvent("MyTimeEvent", timeParam)
    }
    
}
