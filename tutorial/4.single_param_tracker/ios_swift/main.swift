import Foundation

class TrackerImpl: EvgenAnalyticsTracker {
	func trackIntEvent(_ event: String, param: Int) {
        print("\(event)\n\(param)\n\n")
    }
    func trackDoubleEvent(_ event: String, param: Double) {
        print("\(event)\n\(param)\n\n")
    }
    func trackBoolEvent(_ event: String, param: Bool) {
        print("\(event)\n\(param)\n\n")
    }
    func trackTimeMillisecondsEvent(_ event: String, param: Double) {
        print("\(event)\n\(param)\n\n")
    }
}

let analytics = EvgenAnalytics(eventTracker: TrackerImpl())

analytics.myIntEvent1(intParam1: 1)
analytics.myIntEvent2(intParam2: 2)
analytics.myDoubleEvent(doubleParam: 3.0)
analytics.myBoolEvent(boolParam: true)
analytics.myTimeEvent(timeParam: 10000.1)
