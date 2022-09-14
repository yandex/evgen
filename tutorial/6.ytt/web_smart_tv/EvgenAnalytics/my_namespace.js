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
exports.myNamespaceMyEvent = void 0;
var evgen_analytics_1 = require("./evgen_analytics");
/**
    События со всеми возможными типами параметров
    
    0. stringParam - Парамтер типа String
    1. intParam - Параметр типа Int
    2. paramFromAnotherFile - Параметр, описанный в отдельным файле.
    3. batchParam1 - Параметр, описанный в отдельным файле.
    4. batchParam2 - Параметр, описанный в отдельным файле.
*/
function myNamespaceMyEvent(evgen_analytics, parameters) {
    var _a = parameters.stringParam, stringParam = _a === void 0 ? "val1" : _a, _b = parameters.intParam, intParam = _b === void 0 ? 42 : _b;
    var _meta = evgen_analytics_1.makeMetaParams(1);
    var enhancedParams = __assign(__assign({}, parameters), { stringParam: stringParam, intParam: intParam, _meta: _meta });
    evgen_analytics.trackEvent("MyNamespace.MyEvent", enhancedParams);
}
exports.myNamespaceMyEvent = myNamespaceMyEvent;
