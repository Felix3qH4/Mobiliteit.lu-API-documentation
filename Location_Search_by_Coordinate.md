# Location Search by Coordinate
## Location Search by Coordinate
As the name says it, you can search for a location (= stop/station) based on coordinates you pass.<br>
This allows you to get the id of a station to be used in the [Departure Board](Departure_Board.md) request.<br>

<br>
The nearbystops URL is available via https://cdt.hafas.de/opendata/apiserver/location.nearbystops?<br>
The xml definition here: https://cdt.hafas.de/opendata/apiserver/location.nearbystops?wadl
<br>
Available arguments for the nearby stops:<br>

| Argument Name | Mandatory | Value | Description                                         |
| ------------- | --------- | ----- | -----------                                         |
| accessId      | true      | str   | Access ID for identifying the requesting client.    |
| requestId     | false     | str   | Request ID for identifying the request.             |
| format        | false     | str   | Requested response format. If not set, the Accept-Header is used. If both are missing application/xml is used |
| jsonpCallback | false     | str   | Requests the JSON response data is wrapped into a JavaScript function with that name. |
| lang          | false     | str   | The language of the journey planer.                  |
| originCoordLat| true      | str   | Latitude of centre coordinate.                        |
| originCoordLong | true    | str   | Longitude of centre coordinate.                       |
| r             | false     | int   | Search radius in meter around the given coordinate if any. |
| maxNo         | false     | int   | Maximum number of returned stops. Range from 1 to 5000. |
| type          | false     | str   | Type filter for location types. |
| locationSelectionMode | false     | str   | Selection mode for locations. |
| products      | false     | str   | Decimal value defining the product classes to be included in the search. It represents a bitmask combining bit number of a product as defined in the HAFAS raw data file zugart. |
| meta          | false     | str   | Filter by a predefined meta filter. If the rules of the predefined filter should not be negated, put ! in front of it. |
| sattributes   | false     | str   | Filter trips by one or more station attribute codes of a journey. Multiple attribute codes are separated by comma. If the attribute should not be part of the be trip, negate it by putting ! in front of it. |
| sinfotexts    | false     | str   | Filter locations by one or more station infotext codes and values. Multiple attribute codes are separated by comma the value by pipe |
<br>

Example request:<br>
https://cdt.hafas.de/opendata/apiserver/location.nearbystops?accessId="YOUR_API_KEY"&originCoordLat=49.557852&originCoordLong=5.924272&maxNo=1000&r=100&format=json

<br><br>
