{% load l10n %}
function geoip_country_code() { return '{{object.country_code}}'; }
function geoip_country_name() { return '{{object.country_name}}'; }
function geoip_city()         { return '{{object.city}}'; }
function geoip_region()       { return '{{object.region_name}}'; }
function geoip_region_name()  { return ''; }
function geoip_latitude()     {	
	return {% if object.latitude %}{{ object.latitude|unlocalize }}{% else %}50.205667{%endif%};
}
function geoip_longitude()    {
	return {% if object.longitude %}{{ object.longitude|unlocalize }}{% else %}19.123452{%endif%};
}
function geoip_postal_code()  { return ''; }
function geoip_area_code()    { return ''; }
function geoip_metro_code()   { return ''; }