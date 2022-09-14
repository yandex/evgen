"use strict";
/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/
exports.__esModule = true;
exports.EvgenAnalytics = void 0;
var EvgenAnalytics = /** @class */ (function () {
    function EvgenAnalytics(eventTracker) {
        this.eventTracker = eventTracker;
    }
    /**
        Event description
        
        0. intParam1 - Интовый параметр
    */
    EvgenAnalytics.prototype.myIntEvent1 = function (intParam1) {
        this.eventTracker.trackIntEvent("MyIntEvent1", intParam1);
    };
    /**
        Event description
        
        0. intParam2 - Интовый параметр
    */
    EvgenAnalytics.prototype.myIntEvent2 = function (intParam2) {
        this.eventTracker.trackIntEvent("MyIntEvent2", intParam2);
    };
    /**
        Event description
        
        0. doubleParam - Параметр типа double
    */
    EvgenAnalytics.prototype.myDoubleEvent = function (doubleParam) {
        this.eventTracker.trackDoubleEvent("MyDoubleEvent", doubleParam);
    };
    /**
        Event description
        
        0. boolParam - Параметр для логирования времени
    */
    EvgenAnalytics.prototype.myBoolEvent = function (boolParam) {
        this.eventTracker.trackBoolEvent("MyBoolEvent", boolParam);
    };
    /**
        Event description
        
        0. timeParam - Параметр типа double
    */
    EvgenAnalytics.prototype.myTimeEvent = function (timeParam) {
        this.eventTracker.trackTimeMillisecondsEvent("MyTimeEvent", timeParam);
    };
    return EvgenAnalytics;
}());
exports.EvgenAnalytics = EvgenAnalytics;
