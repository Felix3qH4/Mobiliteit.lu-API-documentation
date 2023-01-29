# Departure Board
The departure board is available at this address: https://cdt.hafas.de/opendata/apiserver/departureBoard?<br>
The xml definition here: https://cdt.hafas.de/opendata/apiserver/departureBoard?wadl<br>

It provides you with information about the different bus lines like the operator etc. for a given stop/station.<br>
So you have to pass it the id of a station and then it will return you which busses arrive/depart from that station.<br>
If in realtime mode, you will also get realtime information like how late a bus is.<br>

To get the id of a station have a look at "[Location Search by Coordinate](Location_Search_by_Coordinate.md)".<br>

## Requesting data
When making a request to the departure board, it has to look like this:<br>
https://cdt.hafas.de/opendata/apiserver/departureBoard?arg1=XX&arg2=XX&arg3=XX<br>

Where arg1, arg2 and arg3 are some arguments you can pass to the departure board.<br>
You can choose yourself which arguments to pass and which not altough there are 2 arguments that are mandatory.<br>
You always have to pass "accessId" so your API-Key and "id", the id of the stop/station you want the data from.<br>

Available arguments for the departure board:<br>
(When you see "???" it means that further information is needed)<br>

| Argument Name | Mandatory | Value | Description                                         |
| ------------- | --------- | ----- | -----------                                         |
| accessId      | ****True****      | str   | Your API-Key                                        |
| id            | ****True****      | int   | The station/stop id from which you want to retrieve data |
| requestId     | False     | str   | ??? Request ID for identifying the request. (You can pass any number. Probably for your own use as you can see it in the response?) |
| format        | False     | str   | The format you want your response in. Availables are: json, xml <br>If not set, xml is used.|
| jsonpCallback | False     | str   | The json response will be wrapped in a javascript function with the name you passed |
| lang          | False     | str   | Language of the journey planner. Available are: deu, fr <br>You can basically put anything in here as the keys in the response will always be in english and the data in french. Default is "deu" |
| extId         | False     | str   | [Deprecated] The station/stop id from which you want to retrieve data |
| direction     | False     | str   | If only vehicles departing or arriving from a certain direction shall be returned, specify the direction by giving the station/stop ID of the last stop on the journey. |
| date          | False     | str   | Sets the start date for which the departures shall be retrieved. Represented in the format YYYY-MM-DD. |
| time          | False     | str   | Sets the start time for which the departures shall be retrieved. Represented in the format hh:mm[:ss] in 24h nomenclature. Seconds will be ignored for requests. |
| dur           | False     | int   | ??? Range from 0 to 1439 |
| duration      | False     | int   | ??? Set the interval size in minutes. Range from 0 to 1439. Default is 60 |
| maxJourneys   | False     | int   | Maximum number of journeys to be returned. If no value is defined or -1, all departing/arriving services within the duration sized period are returned. Default is -1 |
| products      | False     | int   | ??? Decimal value defining the product classes to be included in the search. It represents a bitmask combining bit number of a product as defined in the HAFAS raw data file zugart. |
| operators     | False     | str   | [CHECK OPERATORS] Only journeys provided by the given operators are part of the result. To filter multiple operators, separate the codes by comma. If the operator should not be part of the be trip, negate it by putting ! in front of it. Available operators are: RGT, AVL, CFL |
| lines         | False     | str   | Only journeys running the given line are part of the result. To filter multiple lines, separate the codes by comma. If the line should not be part of the be trip, negate it by putting ! in front of it. |
| filterEquiv   | False     | int   | ??? Enables/disables the filtering of equivalent marked stops. |
| attributes    | False     | str   | ??? Filter boards by one or more attribute codes of a journey. Multiple attribute codes are separated by comma. If the attribute should not be part of the result, negate it by putting ! in front of it. |
| platforms     | False     | str   | Filter boards by platform. Multiple platforms are separated by comma. Platforms are used for example at train stations. A train station is one single stop but has multiple platforms so the busses stopping there all stop at the same stop (= the train station) but at different platforms. (Depends on the station how many platforms there are.) |
| rtMode        | False     | bool   | ??? Set the realtime mode to be used if enabled. Available are: FULL <br>For Luxembourg it seems to always return realtime information no matter what you set rtMode to. |
| passlist      | False     | int    | ??? Include a list of all passed waystops? (Is -1 for all waystops and all other numbers for the amount of stops you want?) |


## API response
Depending on what you passed as argument for the format you want the response in, you will either get a response in json or xml format. <br>
Both responses carry the same values. <br>
Here are 2 examples of one busline from a request to the departure board. <br>
(You usually get more than one busline from a request but to simplify it we only show you one busline.) <br>

### XML
```xml
<Departure name="Bus 812" type="ST" stop="Steinfort, Gemeng" stopid="A=1@O=Steinfort, Gemeng@X=5913410@Y=49659424@U=82@L=191104004@" stopExtId="191104004" prognosisType="PROGNOSED" time="15:33:00" date="2023-01-29" rtTime="15:35:00" rtDate="2023-01-29" reachable="true" direction="Eischen, Denn Mairie" trainNumber="812" trainCategory="064">
  <JourneyDetailRef ref="1|3078|7|82|29012023"/>
  <JourneyStatus>P</JourneyStatus>
  <Product name="Bus 812" num="3398" line="812" catOut="Bus" catIn="064" catCode="5" cls="32" catOutS="064" catOutL="Bus" operatorCode="RGT" operator="Régime Général des Transports Routiers" admin="RGTR--" matchId="812">
    <icon res="prod_bus_t">
      <foregroundColor r="255" g="255" b="255" hex="#FFFFFF"/>
      <backgroundColor r="117" g="40" b="100" hex="#752864"/>
    </icon>
  </Product>
  <Notes>
    <Note key="OPERATOR" type="A" routeIdxFrom="34" routeIdxTo="41" txtN="RGTR" txtL="Régime Général des Transports Routiers" txtS="RGT">RGTR</Note>
  </Notes>
</Departure>
```

### JSON
```
{
    "JourneyDetailRef":{
        "ref":"1|3078|7|82|29012023"
    },
    "JourneyStatus":"P",
    "Product":{
        "icon":{
            "foregroundColor":{
                "r":255,
                "g":255,
                "b":255,
                "hex":"#FFFFFF"
            },
            "backgroundColor":{
                "r":117,
                "g":40,
                "b":100,
                "hex":"#752864"
            },
            "res":"prod_bus_t"
        },
        "name":"Bus 812",
        "num":"3398",
        "line":"812",
        "catOut":"Bus",
        "catIn":"064",
        "catCode":"5",
        "cls":"32",
        "catOutS":"064",
        "catOutL":"Bus",
        "operatorCode":"RGT",
        "operator":"Régime Général des Transports Routiers",
        "admin":"RGTR--",
        "matchId":"812"
    },
    "Notes":{
        "Note":[
            {
                "value":"RGTR",
                "key":"OPERATOR",
                "type":"A",
                "routeIdxFrom":34,
                "routeIdxTo":41,
                "txtN":"RGTR",
                "txtL":"Régime Général des Transports Routiers",
                "txtS":"RGT"
            }
        ]
    },
    "name":"Bus 812",
    "type":"ST",
    "stop":"Steinfort, Gemeng",
    "stopid":"A=1@O=Steinfort, Gemeng@X=5913410@Y=49659424@U=82@L=191104004@",
    "stopExtId":"191104004",
    "prognosisType":"PROGNOSED",
    "time":"15:33:00",
    "date":"2023-01-29",
    "rtTime":"15:33:00",
    "rtDate":"2023-01-29",
    "reachable":true,
    "direction":"Eischen, Denn Mairie",
    "trainNumber":"812",
    "trainCategory":"064"
}
```
