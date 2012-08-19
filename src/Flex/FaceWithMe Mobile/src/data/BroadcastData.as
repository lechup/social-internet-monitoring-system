package data {
	public class BroadcastData  {
		public var URL:String = "";
		public var netGroupName:String = "";
		public var RMFPServerURL:String = "";
		public var deleteToken:String = "";
		public function BroadcastData() {
		}
		public function get(title:String, category:Array, is_private:Boolean, user:String = null, password:String = null):void {
			// get broadcast data from server
			// fake request
			URL = "http://facewithme.com/lechup/457asdhasd68jasdhgk/";
			netGroupName = "fancyname123";
			RMFPServerURL = "rtmfp://108.59.252.39/2ad53ba05ab0437da544-8adb73046434";
			deleteToken = "56s7f89sd0fsd89ftoken234710ksd"
		}
	}
}