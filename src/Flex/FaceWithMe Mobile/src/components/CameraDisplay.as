//
// Source from: http://cookbooks.adobe.com/post_Using_Camera_with_a_MediaContainer_instead_of_Vide-19618.html
//
package components {
	import flash.events.Event;
	import flash.media.Camera;
	import mx.core.UIComponent;
	import org.osmf.containers.MediaContainer;
	
	public class CameraDisplay extends UIComponent {
		private var mediaContainer:MediaContainer;
		private var cameraMediaElement:CameraElement;

		public function set camera(camera:Camera):void{
			mediaContainer = new MediaContainer();
			cameraMediaElement = new CameraElement();
			mediaContainer.width = width;
			mediaContainer.height = height;
			addChild(mediaContainer);
			mediaContainer.addMediaElement(cameraMediaElement);
			cameraMediaElement.camera = camera;  //You have to wait until after adding the media element to the mediaContainer before setting the camera property as that will trigger the mediaContainers layout routines.
		}

		public function get camera():Camera {
			return cameraMediaElement.camera;
		}

		override protected function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void {
			super.updateDisplayList(unscaledWidth, unscaledHeight);
			if(mediaContainer){
				mediaContainer.width = unscaledWidth;
				mediaContainer.height = unscaledHeight;
			}
		}
	}
}