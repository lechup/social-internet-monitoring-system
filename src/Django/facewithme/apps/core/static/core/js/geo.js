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
			__getGeoIPLatLng(callback);
		});
	}
	else {		
	// if no HTML5 gelolocation available,
	// fallback to MaxMind GeoIP
		__getGeoIPLatLng(callback);
	}
	
	function __getGeoIPLatLng(callback) {
	// helper function, loading MaxMind JS GeoIP and returning lat/lng ...
		callback({
			'lat' : geoip_latitude(),
			'lng' : geoip_longitude()
		});
	}
}