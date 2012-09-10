package com.facewithme.components{
	import flash.media.Camera;
	import flash.media.Video;
	import org.osmf.media.MediaElement;
	import org.osmf.traits.DisplayObjectTrait;
	import org.osmf.traits.MediaTraitType;
	
	public class CameraElement extends MediaElement {
		private var _camera:Camera = null;
		private var video:Video = null;
		private var displayObjectTrait:DisplayObjectTrait = null;

		public function CameraElement (){
			video = new Video(160, 120);
			displayObjectTrait = new DisplayObjectTrait(video, video.width, video.height);
			addTrait(MediaTraitType.DISPLAY_OBJECT, displayObjectTrait);
		}
		
		public function set camera(camera:Camera):void {
			this._camera = camera;
			video.attachCamera(camera);
		}

		public function get camera():Camera {
			return this._camera;
		}
	}
}