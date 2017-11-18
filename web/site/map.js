var currLocation;
var locs;

function init() {
    navigator.geolocation.getCurrentPosition(showPosition)
};

function showPosition(position) {
    if (position) {
        currLocation = { lat: position.coords.latitude, long: position.coords.latitude};
        init_map();
    }
};

function advertiseSlot() {
// TODO: advertiseSlot
};

function donate(address) {
    fetch("/donate?address=" + address)
        .then(function(data) {
            window.alert("Thanks!")
        })
        .catch(function(error) {
            console.log("error donating")
        });
};

function init_map() {
    console.log(currLocation.lat, currLocation.long);

    locs = [{
        availability: "free",
        price: 0.01, // Given in milli iota
        long: -0.119562,
        lat: 51.503454,
        id: "GFDSAHOFDSHAUFSAZFSAHFFHDSIAHDISAHIDJFDSKAJDSA",
        address: "TIZODOIHIDSHAUGIDSGAIDSAHODSGIDSAIUDSADSAOI",
    },
    {
        availability: "occupied",
        price: 0.01, // Given in milli iota
        long: -0.119580,
        lat: 51.503474,
        id: "GFDSAHOFDSHAUFSAZFSAHFFHDSIAHDISAHIDJFDSKAJDSA",
        address: "TIZODOIHIDSHAUGIDSGAIDSAHODSGIDSAIUDSADSAOI",
    }];

    // fetch('/search?long=' + currLocation.long + '&lat=' + currLocation.lat)
    //     .then(function(data){
    //         locs = data
    //     })
    //     .catch(function(error) {})

    var map;
    var bounds = new google.maps.LatLngBounds();
    var mapOptions = {mapTypeId: 'roadmap'};

    // Display a map on the page
    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
    map.setTilt(45);

    // Multiple Markers
    var markers = [];

    // Info Window Content
    var infoWindowContent = [];

    // Display multiple markers on a map
    var infoWindow = new google.maps.InfoWindow(), marker, i;

    function show_directions_link(lat, long) {
        return '<a href=\"https://www.google.com/maps/place/'
            + lat.toString() + 'N'
            + '+'
            + long.toString() + 'W'
            + '\/\">'
            + 'Get Directions'
            + '</a>';
    }

    function show_price(price) {
        return '<p>'
            + price
            + ' mi / W'
            + '</p>'
    }

    for(j = 0; j < locs.length; j++) {
        var price = locs[j].price;
        var lat = locs[j].lat;
        var long = locs[j].long;
        var status = locs[j].availability;
        
        infoWindowContent.push([
            '<div class="info_content">'
            + show_price(price) 
            + show_directions_link(lat, long)
            // + '<a href = "/updateStation?id=stationID&status=FREE">  Claim </a>'
            + '</div>\n'
            ])
        markers.push([locs[j].lat, locs[j].long, price, status]);
    }

    // Loop through our array of markers & place each one on the map
    for(i = 0; i < markers.length; i++) {
        if (markers[i][3]==="free") {
            colour = "green"
        } else {
            colour = "red"
        }
        var position = new google.maps.LatLng(markers[i][0], markers[i][1]);
        bounds.extend(position);
        marker = new google.maps.Marker({
            position: position,
            map: map,
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                strokeColor: colour,
                scale: 10,
                },
        });

          // Allow each marker to have an info window
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infoWindow.setContent(infoWindowContent[i][0]);
                infoWindow.open(map, marker);
            }
        })(marker, i));

        // Automatically center the map fitting all markers on the screen
        map.fitBounds(bounds);
    }

    // Override our map zoom level once our fitBounds function runs (Make sure it only runs once)
    var boundsListener = google.maps.event.addListener((map),
                                                       'bounds_changed',
                                                       function(event)     {
        google.maps.event.removeListener(boundsListener);
    });
}
