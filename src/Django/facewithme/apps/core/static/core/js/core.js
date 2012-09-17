var map;

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
    
// map
    initializeMap();    

	function initializeMap() {
		var mapOptions = {
			streetViewControl : false,
			center: new google.maps.LatLng(0, 0),
			zoom: 5,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		};
	
		map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
		getLatLng(getLatLngHandler);
	}
	
	function getLatLngHandler(pos) {
	// function run after finding current position
		if (pos.lat && pos.lng) {
			pos = new google.maps.LatLng(pos.lat, pos.lng);
			map.setZoom(10);	
			map.panTo(pos);
		}
	}

	function getLatLng(callback) {
		getGeoIPLatLng(callback);
		// apart from anything
		// localize through GeoIP
		
		if (navigator && navigator.geolocation) {
		// try to use HTML5 geolocation - it's better than GeoIP
			navigator.geolocation.getCurrentPosition(function(pos) {
			// suceess callback
				callback({
					'lat' : pos.coords.latitude,
					'lng' : pos.coords.longitude
				});
			}, function(error) {
				// do nothing because we are already GeoIP'ed
			});
		}

		
		function getGeoIPLatLng(callback) {
		// helper function, loading MaxMind JS GeoIP and returning lat/lng ...
			callback({
				'lat' : geoip_latitude(),
				'lng' : geoip_longitude()
			});
		}
	}
});

function modal(iframe_src) {
	$('#modal-iframe').attr('src', iframe_src);
	$('#modal').modal();
}
