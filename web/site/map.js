var currLocation;
locs = {};

function init() {
    navigator.geolocation.getCurrentPosition(showPosition)
};

function showPosition(position) {
    if (position) {
        currLocation = {lat: position.coords.latitude, long: position.coords.latitude};
        init_map();
    }
};

function advertiseSlot() {
// TODO: advertiseSlot
};

var balance = 2000;


function donate(address) {
    fetch("/donate?address=" + address)
        .then(function (data) {
            window.alert("Thanks!")
        })
        .catch(function (error) {
            console.log("error donating")
        });
};

function show_station_details() {
    var station = locs[$("#station-button").attr("data-address")];
    $("#map-container").hide();
    $("#station-container").show();
    $("#balance").text(balance);
    $("#price").text(station.price);
    $("#payment-address").text(station.owner);

    $("#charing-btn").click(function () {
            $("#charing-btn").hide();
            $("#progress-bar").show();

            for(i = 0; i <= 100; i+=1){

                $("#progress-bar").css("width", i + "%");
                $("#progress-bar").text(i + "%");
            }
        }
    )
}

function init_map() {
    console.log(currLocation.lat, currLocation.long);

    locs = [{
        availability: "free",
        price: 0.01, // Given in milli iota
        long: -0.119562,
        lat: 51.503454,
        owner: "GFDSAHOFDSHAUFSAZFSAHFFHDSIAHDISAHIDJFDSKAJDSA",
        address: "TIZODOIHIDSHAUGIDSGAIDSAHODSGIDSAIUDSADSAOI",
        txid: "DHWSGSFB9MKZZCJCYGAOXMKFCUXQYSI9DZTUTIBPNCN9DMFRHDXEFOQRIESSOFSIMTUYICABUYWJWZ999",
        id: "asjkdasd"
    },
        {
            availability: "occupied",
            price: 0.01, // Given in milli iota
            long: -0.119580,
            lat: 51.503474,
            owner: "GFDSAHOFDSHAUFSAZFSAHFFHDSIAHDISAHIDJFDSKAJDSA",
            address: "TIZODOIHIDSHAUGIDSGAIDSAHODSGIDSAIUDSADSAOI",
            txid: "DHWSGSFB9MKZZCJCYGAOXMKFCUXQYSI9DZTUTIBPNCN9DMFRHDXEFOQRIESSOFSIMTUYICABUYWJWZ999",
            id: "asjkdasd"
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
            + lat.toString()
            + '+'
            + long.toString()
            + '\/\">'
            + 'Get Directions'
            + '</a>';
    }

    function show_price(price) {
        return '<p>'
            + price
            + ' mi/min'
            + '</p>'
    }

    function show_testnet_link(txid) {
        return '<p><a target="_blank" href=\"https://testnet.thetangle.org/transaction/'
            + txid
            + '\/\">'
            + "View in Tangle Explorer"
            + '</a></p>'
    }

    for (j = 0; j < locs.length; j++) {
        var price = locs[j].price;
        var lat = locs[j].lat;
        var long = locs[j].long;
        var status = locs[j].availability;
        var txid = locs[j].txid;
        infoWindowContent.push([
            '<div class="info_content">'
            + show_price(price)
            + show_directions_link(lat, long)
            + show_testnet_link(txid)
            + '    <div class="div-center col-md-2 col-sm-2">\n' +
            '      <button id="station-button" data-address="' + j + '" onclick="show_station_details()" class="btn btn-success btn-md">I\'m There!</button>\n' +
            '    </div>'
            // + '<a href = "/updateStation?id=stationID&status=FREE">  Claim </a>'
            + '</div>\n'
        ])
        markers.push([locs[j].lat, locs[j].long, price, status]);
    }

    // Loop through our array of markers & place each one on the map
    for (i = 0; i < markers.length; i++) {
        if (markers[i][3] === "free") {
            icon_url = "http://mt.google.com/vt/icon?psize=25&font=fonts/Roboto-Bold.ttf&color=ff135C13&name=icons/spotlight/spotlight-waypoint-a.png&ax=44&ay=50&text=%E2%80%A2"
        } else {
            icon_url = "http://mt.google.com/vt/icon?psize=25&font=fonts/Roboto-Bold.ttf&color=ff135C13&name=icons/spotlight/spotlight-waypoint-b.png&ax=44&ay=50&text=%E2%80%A2"
        }
        var position = new google.maps.LatLng(markers[i][0], markers[i][1]);
        bounds.extend(position);
        marker = new google.maps.Marker({
            position: position,
            map: map,
            icon: {url: icon_url,},
        });

        // Allow each marker to have an info window
        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
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
        function (event) {
            google.maps.event.removeListener(boundsListener);
        });
}
