public final class ApplicationAnalytics {
  
  public struct StartupInfo {
      
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
      
      public struct CommonParams {
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
  
      public init(deeplinkInfo: DeeplinkInfo, commonParams: CommonParams) {
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

  public func applicationResumed(startupInfo: StartupInfo) {
    var options: [String: Any] = [:]
    options[startup_info] = startupInfo.makeDictionary()
    trackEvent("Application.Resumed", withOptions: options)
  }
}
