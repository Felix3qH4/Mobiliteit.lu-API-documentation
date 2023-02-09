# Location Search by Coordinate

- [Location Search by Coordinate](#location-search-by-coordinate-1)
- [Output](#output)
    1. [XML](#xml)
    2. [JSON](#json)
- [Output Meaning](#output-meaning)
    1. [Id](#id)
    2. [ExtId](#extid)
    3. [Name](#name)
    4. [Lon](#lon)
    5. [Lat](#lat)
    6. [Weight](#weight)
    7. [Dist](#dist)
    8. [Products](#products)
- [Error codes](#error-codes)
<br>

## Location Search by Coordinate
As the name says it, you can search for a location (= stop/station) based on coordinates you pass.<br>
This allows you to get the id of a station to be used in the [Departure Board](Departure_Board.md) request.<br>

<br>
The nearbystops URL is available via https://cdt.hafas.de/opendata/apiserver/location.nearbystops?<br>
The xml definition here: https://cdt.hafas.de/opendata/apiserver/location.nearbystops?wadl<br>
<br>
Available arguments for the nearby stops:<br>

| Argument Name | Mandatory | Value | Description                                         |
| ------------- | --------- | ----- | -----------                                         |
| accessId      | true      | str   | Access ID for identifying the requesting client. (= your API-key)|
| requestId     | false     | str   | Request ID for identifying the request. The field "requestId" will be returned with your request so it probably only serves you in seeing which request i was (you can pass anything)|
| format        | false     | str   | Requested response format. If not set, the Accept-Header is used. If both are missing application/xml is used. Available are: json, xml|
| jsonpCallback | false     | str   | Requests the JSON response data is wrapped into a JavaScript function with that name. |
| lang          | false     | str   | The language of the journey planer.                  |
| originCoordLat| true      | str   | Latitude of centre coordinate.                        |
| originCoordLong | true    | str   | Longitude of centre coordinate.                       |
| r             | false     | int   | Search radius in meter around the given coordinate if any. |
| maxNo         | false     | int   | Maximum number of returned stops. Range from 1 to 5000. |
| type          | false     | str   | ??? Type filter for location types. (Which types can you filter? Are there actually some?) |
| locationSelectionMode | false     | str   | ??? Selection mode for locations. |
| products      | false     | str   | Decimal value defining the product classes to be included in the search. It represents a bitmask combining bit number of a product as defined in the HAFAS raw data file Zugart. |
| meta          | false     | str   | Filter by a predefined meta filter. If the rules of the predefined filter should not be negated, put ! in front of it. |
| sattributes   | false     | str   | Filter trips by one or more station attribute codes of a journey. Multiple attribute codes are separated by comma. If the attribute should not be part of the be trip, negate it by putting ! in front of it. |
| sinfotexts    | false     | str   | Filter locations by one or more station infotext codes and values. Multiple attribute codes are separated by comma the value by pipe |
<br>

Example request:<br>
(replace //YOUR_API_KEY// with your API-Key) <br>
https://cdt.hafas.de/opendata/apiserver/location.nearbystops?accessId=//YOUR_API_KEY//&originCoordLat=49.557852&originCoordLong=5.924272&maxNo=1000&r=100&format=json

To get all stops in Luxembourg: <br>
(replace //YOUR_API_KEY// with your API-Key) <br>
https://cdt.hafas.de/opendata/apiserver/location.nearbystops?accessId=//API-KEY//&originCoordLong=6.09528&originCoordLat=49.77723&maxNo=5000&r=100000&format=json
<br><br>



## Output
The request will output something similar to the following: <br>

### XML
Shortened for better visualization.<br>

```xml
<StopLocation id="A=1@O=Rouscht@X=6092924@Y=49786459@u=0@U=82@L=160102002@" extId="160102002" name="Rouscht" lon="6.092924" lat="49.786459" weight="5374" dist="1040" products="32">
    <productAtStop name="Bus K10" line="K10" lineId="K10" catOut="Bus" cls="32" catOutS="050" catOutL="Bus">
        <icon res="prod_bus_t">
            <foregroundColor r="255" g="255" b="255" hex="#FFFFFF"/>
            <backgroundColor r="117" g="40" b="100" hex="#752864"/>
        </icon>
    </productAtStop>
    <productAtStop name="Bus M05" line="M05" lineId="M05" catOut="Bus" cls="32" catOutS="070" catOutL="Bus">
        <icon res="prod_bus_t">
            <foregroundColor r="255" g="255" b="255" hex="#FFFFFF"/>
            <backgroundColor r="117" g="40" b="100" hex="#752864"/>
        </icon>
    </productAtStop>
</StopLocation>
```

### JSON
Shortened for better visualization.<br>
```json
{
    "StopLocation": {
        "productAtStop": [
            {
                "icon": {
                    "foregroundColor": {
                        "r": 255,
                        "g": 255,
                        "b": 255,
                        "hex": "#FFFFFF"
                    },
                    "backgroundColor": {
                        "r": 117,
                        "g": 40,
                        "b": 100,
                        "hex": "#752864"
                    },
                    "res": "prod_bus_t"
                },
                "name": "Bus 941",
                "line": "941",
                "lineId": "941",
                "catOut": "Bus",
                "cls": "32",
                "catOutS": "064",
                "catOutL": "Bus"
            },
            {
                "icon": {
                    "foregroundColor": {
                        "r": 255,
                        "g": 255,
                        "b": 255,
                        "hex": "#FFFFFF"
                    },
                    "backgroundColor": {
                        "r": 117,
                        "g": 40,
                        "b": 100,
                        "hex": "#752864"
                    },
                    "res": "prod_bus_t"
                },
                "name": "Bus H01",
                "line": "H01",
                "lineId": "H01",
                "catOut": "Bus",
                "cls": "32",
                "catOutS": "063",
                "catOutL": "Bus"
            }            
        ],
        "id": "A=1@O=Rouscht@X=6092924@Y=49786459@u=0@U=82@L=160102002@",
        "extId": "160102002",
        "name": "Rouscht",
        "lon": 6.092924,
        "lat": 49.786459,
        "weight": 5374,
        "dist": 1040,
        "products": 32
    }
}
```


## Output Meaning

## ID
See [DepartureBoard -> stopId](Departure_Board.md#stopid) for detailed information. <br>

## ExtId
Is the same as the 'L' in the '[stopId](Departure_Board.md#stopid)'. <br>
Was used to get departures from the [DepartureBoard](Departure_Board.md), now 'id' is used.

## Name
The name of the station. <br>

## lon
The longitude of the stop.<br>
See [DepartureBoard -> stopId](Departure_Board.md#x) for detailed information. <br>

## lat
The latitude of the stop. <br>
See [DepartureBoard -> stopId](Departure_Board.md#y) for detailed information. <br>

## Weight
??? Probably the weight when you draw the station on a map like Leaflet.

## Dist
???

## Products
Which vehicle types stop here. <br>
See [DepartureBoard -> cls](Departure_Board.md#cls) for all available products and their respective codes.<br>
<br>

## Error codes
Refer to the [error codes in DepartureBoard.md](Departure_Board.md#error-codes)