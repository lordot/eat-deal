function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: {lat: -8.6478, lng: 115.1385}
  });

  promos.forEach(function(promo) {
    var address = promo.fields.cafe + ', Canggu';
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({'address': address}, function(results, status) {
      if (status === 'OK') {
        var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location,
          title: promo.fields.title,
          description: promo.fields.description,
          cafe: promo.fields.cafe
        });
        marker.addListener('click', function() {
          var contentStr = '<h3>' + promo.fields.cafe + '</h3><h4>' + promo.fields.title + '</h4><p>' + promo.fields.description + '</p>';
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
