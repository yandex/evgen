class TrackerImpl: EvgenAnalyticsTracker {
	override fun trackIntEvent(event: String, param: Int) {
        println("Int")
        println(param)
        println("\n\n")
    }
    override fun trackDoubleEvent(event: String, param: Double) {
        println("Double")
        println(param)
        println("\n\n")
    }
    override fun trackBoolEvent(event: String, param: Boolean) {
        println("Bool")
        println(param)
        println("\n\n")
    }
    override fun trackTimeMillisecondsEvent(event: String, param: Double) {
        println("Bool")
        println(param)
        println("\n\n")
    }
}


fun main() {
    val analytics = EvgenAnalytics(TrackerImpl())
    analytics.myIntEvent1(1)
    analytics.myIntEvent2(2)
    analytics.myDoubleEvent(3.0)
    analytics.myBoolEvent(false)
    analytics.myTimeEvent(1000.0)
}

