"use strict";
/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/
/**
    eslint-disable
*/
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
exports.__esModule = true;
exports.createEvgenAnalytics = exports.makeMetaParams = void 0;
function makeMetaParams(eventVersion, interfaces) {
    if (interfaces === void 0) { interfaces = {}; }
    return {
        event: {
            version: eventVersion
        },
        interfaces: interfaces
    };
}
exports.makeMetaParams = makeMetaParams;
function createEvgenAnalytics(eventTracker, globalParamsProvider, platformParamsProvider) {
    var trackEvent = function (event, parameters) {
        var mergedParameters = __assign(__assign(__assign({}, parameters), globalParamsProvider.getGlobalParams()), platformParamsProvider.getPlatformParams());
        eventTracker.trackEvent(event, mergedParameters);
    };
    return { trackEvent: trackEvent };
}
exports.createEvgenAnalytics = createEvgenAnalytics;
