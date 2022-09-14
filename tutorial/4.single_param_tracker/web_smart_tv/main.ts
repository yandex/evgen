import { EvgenAnalytics } from './EvgenAnalytics';


class TrackerImpl {
	trackIntEvent(event: string, param: number): void {
        console.log(event);
        console.log(param);
    }
    trackDoubleEvent(event: string, param: number): void {
        console.log(event);
        console.log(param);
    }
    trackBoolEvent(event: string, param: boolean): void {
        console.log(event);
        console.log(param);
    }
    trackTimeMillisecondsEvent(event: string, param: number): void {
        console.log(event);
        console.log(param);
    }
}


const analytics = new EvgenAnalytics(new TrackerImpl());

analytics.myIntEvent1(1)
analytics.myIntEvent2(2)
analytics.myDoubleEvent(3.0)
analytics.myBoolEvent(false)
analytics.myTimeEvent(10000.1)