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
			zoom: 5,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			center: new google.maps.LatLng(0, 0)
		};
	
		map = new google.maps.Map(document.getElementById('map'), mapOptions);
		getLatLng(getLatLngHandler);
	}
	
	function getLatLngHandler(pos) {
		if (pos.lat && pos.lng) {
			pos = new google.maps.LatLng(pos.lat, pos.lng);
			map.setZoom(10);	
			map.panTo(pos);
		}
	}
});

function modal(iframe_src) {
	$('#modal-iframe').attr('src', iframe_src);
	$('#modal').modal();
}

function getLatLng(callback) {
	if (navigator && navigator.geolocation) {
	// try to use HTML5 geolocation
		navigator.geolocation.getCurrentPosition(function(pos) {
		// suceess callback
			callback({
				'lat' : pos.coords.latitude,
				'lng' : pos.coords.longitude
			});
		}, function(error) {
		// error callback
		// eg. user forbids to get location by the browser
			getGeoIPLatLng(callback);
		});
	}
	else {		
	// if no HTML5 gelolocation available,
	// fallback to MaxMind GeoIP
		getGeoIPLatLng(callback);
	}
	
	function getGeoIPLatLng(callback) {
	// helper function, loading MaxMind JS GeoIP and returning lat/lng ...
		callback({
			'lat' : geoip_latitude(),
			'lng' : geoip_longitude()
		});
	}
}
