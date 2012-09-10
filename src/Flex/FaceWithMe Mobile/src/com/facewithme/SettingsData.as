package com.facewithme {
	import flash.utils.ByteArray;
	import flash.data.EncryptedLocalStore;

	public class SettingsData {
		public function get(name:String, default_value:*=null):* {
			var storedValue:ByteArray = EncryptedLocalStore.getItem("settings."+name);
			if (storedValue != null)
				return storedValue.readObject();
			else
				return default_value;
		}

		public function set(name:String, value:*):void {
			if (name != null) {
				var toStoreValue:ByteArray = new ByteArray();
				toStoreValue.writeObject(value);
				EncryptedLocalStore.setItem("settings." + name, toStoreValue);
			}
		}
	}
}