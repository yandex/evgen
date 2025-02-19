public final class ApplicationAnalytics {
  
  public struct CustomCommonParams {
      let timeSinceLastAppLaunch: Int
      let isColdLaunch: Bool
  
      public init(timeSinceLastAppLaunch: Int, isColdLaunch: Bool) {
          self.timeSinceLastAppLaunch = timeSinceLastAppLaunch
          self.isColdLaunch = isColdLaunch
      }
  
      func makeDictionary() -> [String: Any] {
          var options: [String: Any] = [:]
          options["time_since_last_app_launch"] = timeSinceLastAppLaunch
          options["is_cold_launch"] = isColdLaunch
          return options
      }
  }
  
  public struct CustomStartupInfo {
      
      public struct DeeplinkInfo {
          let url: String
      
          public init(url: String) {
              self.url = url
          }
      
          func makeDictionary() -> [String: Any] {
              var options: [String: Any] = [:]
              options["url"] = url
              return options
          }
      }
      let commonParams: CustomCommonParams
  
      public init(deeplinkInfo: DeeplinkInfo, commonParams: CustomCommonParams) {
          self.deeplinkInfo = deeplinkInfo
          self.commonParams = commonParams
      }
  
      func makeDictionary() -> [String: Any] {
          var options: [String: Any] = [:]
          options["deeplink_info"] = deeplinkInfo
          options["common_params"] = commonParams
          return options
      }
  }

  public func applicationResumed(startupInfo: CustomStartupInfo, startupInfoDuplicate: CustomStartupInfo) {
    var options: [String: Any] = [:]
    options[startup_info] = startupInfo.makeDictionary()
    options[startup_info_duplicate] = startupInfoDuplicate.makeDictionary()
    trackEvent("Application.Resumed", withOptions: options)
  }

  public func applicationResumedV2(startupInfoV2: CustomStartupInfo, listUnnamedProperty: [ListUnnamedProperty], listNamedProperty: [CustomStartupInfo]) {
    var options: [String: Any] = [:]
    options[startup_info_v2] = startupInfoV2.makeDictionary()
    options[list_unnamed_property] = listUnnamedProperty
    options[list_named_property] = listNamedProperty
    trackEvent("Application.Resumed", withOptions: options)
  }
}
