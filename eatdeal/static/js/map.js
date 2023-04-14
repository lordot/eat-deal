function getCookie(name) {
  const value = "; " + document.cookie;
  const parts = value.split("; " + name + "=");
  if (parts.length === 2) {
    return parts.pop().split(";").shift();
  }
}

function toggleFavorite(event, id) {
  event.stopPropagation();
  const button = event.target;
  const isFavorited = button.textContent === "Unfavorite";

  const requestOptions = {
    method: isFavorited ? "DELETE" : "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  };

  if (isFavorited) {
    fetch(`/api/promos/${id}/favorite/`, { method: "DELETE", headers: {"X-CSRFToken": getCookie("csrftoken")} })
      .then(() => {
        button.textContent = "Favorite";
      })
      .catch((error) => console.error("Failed to unfavorite promo:", error));
  } else {
    fetch(`/api/promos/${id}/favorite/`, { method: "POST", headers: {"X-CSRFToken": getCookie("csrftoken")} })
      .then(() => {
        button.textContent = "Unfavorite";
      })
      .catch((error) => console.error("Failed to favorite promo:", error));
  }
}
// Fetch cities and add them to the select element
fetch('/api/cities/')
  .then(response => response.json())
  .then(cities => {
    const select = document.getElementById('city-select');
    cities.forEach(city => {
      const option = document.createElement('option');
      option.value = city.name;
      option.text = city.name;
      select.appendChild(option);
    });
  })
  .catch(error => console.error('Failed to load cities:', error));

// Initialize map with default options
function initMap() {
  const city = document.getElementById('city-select').value;
  const selection = document.getElementById('promo-select').value;
  const map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14
  });
  const geocoder = new google.maps.Geocoder();
  geocoder.geocode({ 'address': city }, function(results, status) {
    if (status === 'OK') {
      map.setCenter(results[0].geometry.location);
    } else {
      console.error('Geocode was not successful for the following reason:', status);
    }
  });
  fetch(`/api/promos/?city=${city}&selection=${selection}`)
    .then(response => response.json())
    .then(promos => {
      promos.forEach(promo => {
        const address = `${promo.cafe}, ${city}`;
        geocoder.geocode({ 'address': address }, function(results, status) {
          if (status === 'OK') {
            const iconColor = promo.is_favorited ? 'https://maps.google.com/mapfiles/ms/icons/pink-dot.png' : 'https://maps.google.com/mapfiles/ms/icons/red-dot.png';
            const marker = new google.maps.Marker({
              map: map,
              position: results[0].geometry.location,
              title: promo.title,
              description: promo.description,
              cafe: promo.cafe,
              icon: iconColor
            });
            marker.addListener('click', function() {
              const favoriteButtonText = promo.is_favorited ? "Unfavorite" : "Favorite";
              const contentStr = `
                <h3>${promo.cafe}</h3>
                <h4>${promo.title}</h4>
                <p>${promo.description}</p>
                <button onclick="toggleFavorite(event, ${promo.id})">${favoriteButtonText}</button>
              `;
              const infowindow = new google.maps.InfoWindow({
                content: contentStr
              });
              infowindow.open(map, marker);
            });
          } else {
            console.error('Geocode was not successful for the following reason:', status);
          }
        });
      });
    })
    .catch(error => console.error('Failed to load promos:', error));
}

// Add event listeners to the select elements
document.getElementById('city-select').addEventListener('change', () => {
  initMap();
});
document.getElementById('promo-select').addEventListener('change', () => {
  initMap();
});
