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
exports.anotherNamespaceEvent2 = exports.anotherNamespaceEvent1 = void 0;
var evgen_analytics_1 = require("./evgen_analytics");
/**
    Первое событие с переиспользуемым параметром
    
    0. reusedParam - Параметр, который переиспользуется в нескольких событиях
*/
function anotherNamespaceEvent1(evgen_analytics, parameters) {
    var _meta = evgen_analytics_1.makeMetaParams(1);
    var enhancedParams = __assign(__assign({}, parameters), { _meta: _meta });
    evgen_analytics.trackEvent("AnotherNamespace.Event1", enhancedParams);
}
exports.anotherNamespaceEvent1 = anotherNamespaceEvent1;
/**
    Второе событие с переиспользуемым параметром
    
    0. reusedParam - Параметр, который переиспользуется в нескольких событиях
*/
function anotherNamespaceEvent2(evgen_analytics, parameters) {
    var _meta = evgen_analytics_1.makeMetaParams(1);
    var enhancedParams = __assign(__assign({}, parameters), { _meta: _meta });
    evgen_analytics.trackEvent("AnotherNamespace.Event2", enhancedParams);
}
exports.anotherNamespaceEvent2 = anotherNamespaceEvent2;
