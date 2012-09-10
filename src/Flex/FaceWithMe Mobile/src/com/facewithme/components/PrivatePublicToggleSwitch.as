package com.facewithme.components {
	import spark.skins.mobile.ToggleSwitchSkin;
	public class PrivatePublicToggleSwitch extends ToggleSwitchSkin {
		public function PrivatePublicToggleSwitch() {
			super();
            // Set properties to define the labels 
            // for the selected and unselected positions.
            selectedLabel="Publiczny";
            unselectedLabel="Prywatny"; 			
		}
	}
}