var map = null;

$(document).ready(function() {
// window resize event
	resizeWindowHandler();
	$(window).resize(resizeWindowHandler);
	function resizeWindowHandler() {
		// when resizing window, adjust map height to current viewport
		$('#map_canvas').height(getMapHeight());
	}
	function getMapHeight() {
		return $(window).height()-$('#navbar').height();
	}
//

// map
	// initialize map container
    initializeMap();
    // get current Lat and Lng of user and set new map center
	getLatLng(updateMapCenter);

	function updateMapCenter(pos) {
	// function run after finding current position
		if (pos.lat && pos.lng) {
			pos = new google.maps.LatLng(pos.lat, pos.lng);
			map.setZoom(10);	
			map.panTo(pos);
		}
	}
//
});

function initializeMap() {
	var mapOptions = {
		streetViewControl : false,
		center: new google.maps.LatLng(0, 0),
		zoom: 5,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
}

function getLatLng(callback) {
	// apart from anything
	// localize through GeoIP
	getLatLngGeoIP(callback);

	// try to use HTML5 geolocation - it's better than GeoIP
	if (navigator && navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function(pos) {
			// if user click Yes to 'allow this site my location'
			callback({
				'lat' : pos.coords.latitude,
				'lng' : pos.coords.longitude
			});
		}, function(error) {
			// if user clicked No to 'allow this site my location'
			// do nothing because we are already GeoIP'ed
		});
	}
	
	function getLatLngGeoIP(callback) {
	// helper function, loading MaxMind JS GeoIP and returning lat/lng ...
		callback({
			// need MaxMind GeoIP js library!
			'lat' : geoip_latitude(),
			'lng' : geoip_longitude()
		});
	}
}

function modal(iframe_src) {
	$('#modal-iframe').attr('src', iframe_src);
	$('#modal').modal();
}
