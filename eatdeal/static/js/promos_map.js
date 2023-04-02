function initMap() {
  var city = JSON.parse(document.getElementById('city').textContent);
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14
  });
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({'address': city}, function(results, status) {
    if (status === 'OK') {
      map.setCenter(results[0].geometry.location);
    } else {
      console.log('Geocode was not successful for the following reason: ' + status);
    }
  });
  var promos = JSON.parse(document.getElementById('markers').textContent);
  promos.forEach(function(promo) {
    var address = promo.cafe + ', ' + promo.city;
    geocoder.geocode({'address': address}, function(results, status) {
      if (status === 'OK') {
        var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location,
          title: promo.title,
          description: promo.description,
          cafe: promo.cafe
        });
        marker.addListener('click', function() {
          var contentStr = '<h3>' + promo.cafe + '</h3><h4>' + promo.title + '</h4><p>' + promo.description + '</p>';
          var infowindow = new google.maps.InfoWindow({
            content: contentStr
          });
          infowindow.open(map, marker);
        });
      } else {
        console.log('Geocode was not successful for the following reason: ' + status);
      }
    });
  });
}
