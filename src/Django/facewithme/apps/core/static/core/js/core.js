var map;

$(document).ready(function() {
	// window resize event
	resizeWindowHandler();
	$(window).resize(resizeWindowHandler);
    
    // map and geolocation
    initializeMap();    

	var resizeWindowHandlerActive = false;
	var resizeWindowHandlerMaxHeight = getMapHeight();
	function resizeWindowHandler() {
		// when resizing window, adjust map height to current viewport
		$('#map').height(getMapHeight());
		google.maps.event.trigger(map, 'resize');
	}
	function getMapHeight() {
		return $(window).height()-$('#navbar').height();
	}
	function initializeMap() {
		var mapOptions = {
			zoom: 18,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			center: new google.maps.LatLng(50.20, 19.50)
		};
	
		map = new google.maps.Map(document.getElementById('map'), mapOptions);
		getLatLng(getLatLngHandler);
	}
	
	function getLatLngHandler(pos) {
		if (pos.lat && pos.lng) {
			pos = new google.maps.LatLng(pos.lat, pos.lng);	
			map.setCenter(pos);
		}
	}
});

function modal(modal_id, iframe_id, iframe_src) {
	$(iframe_id).attr('src', iframe_src);
	$(modal_id).modal();
}
