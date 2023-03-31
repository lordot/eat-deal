function initMap() {
  var city = JSON.parse(document.getElementById('city').textContent);
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: {lat: -8.6478, lng: 115.1385}
  });
  var promos = JSON.parse(document.getElementById('promos-data').textContent);
  promos.forEach(function(promo) {
    var address = promo.cafe + ', ' + promo.city;
    var geocoder = new google.maps.Geocoder();
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
