# Departure Board
The departure board is available at this address: https://cdt.hafas.de/opendata/apiserver/departureBoard?<br>
The xml definition here: https://cdt.hafas.de/opendata/apiserver/departureBoard?wadl<br>

It provides you with information about the different bus lines like the operator etc. for a given stop/station.<br>
So you have to pass it the id of a station and then it will return you which busses arrive/depart from that station.<br>
If in realtime mode, you will also get realtime information like how late a bus is.<br>

To get the id of a station have a look at "[Location Search by Coordinate](Location_Search_by_Coordinate.md)".<br>

Table of contents:

1) [Requesting data](#Requesting-data)
2) [API response](#API-response)
    1. [XML](#XML)
    2. [JSON](#JSON)
    3. [Response values meaning](#response-values-meaning)
3) [Detailed information about response values](#detailed-information-about-response-values)
    1. [ref](#ref)


<br>
<br>
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
| extId         | False     | str   | \[Deprecated] The station/stop id from which you want to retrieve data |
| direction     | False     | str   | If only vehicles departing or arriving from a certain direction shall be returned, specify the direction by giving the station/stop ID of the last stop on the journey. |
| date          | False     | str   | Sets the start date for which the departures shall be retrieved. Represented in the format YYYY-MM-DD. |
| time          | False     | str   | Sets the start time for which the departures shall be retrieved. Represented in the format hh:mm[:ss] in 24h nomenclature. Seconds will be ignored for requests. |
| dur           | False     | int   | ??? Range from 0 to 1439 |
| duration      | False     | int   | ??? Set the interval size in minutes. Range from 0 to 1439. Default is 60 |
| maxJourneys   | False     | int   | Maximum number of journeys to be returned. If no value is defined or -1, all departing/arriving services within the duration sized period are returned. Default is -1 |
| products      | False     | int   | ??? Decimal value defining the product classes to be included in the search. It represents a bitmask combining bit number of a product as defined in the HAFAS raw data file zugart. |
| operators     | False     | str   | \[CHECK OPERATORS] Only journeys provided by the given operators are part of the result. To filter multiple operators, separate the codes by comma. If the operator should not be part of the be trip, negate it by putting ! in front of it. Available operators are: RGTR, AVL, CFL |
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

<br>
<br>

### JSON
```json
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

<br>
<br>
<br>

### Response values meaning
Here is a table explaining all those values you get from a request to the API: <br>
(If there is "???" then information is missing) <br>
(If there is "->" in front of a key, it means that it is a child of the key above the first key with "->" in front of it) <br>


| Key                     | Always present | Value type | Meaning                                                                             |
| ---                     | -------------- | ---------- | -------                                                                             |
| JourneyDetailRef        | True           | dict       | Contains [ref](#key-ref)                                                            |
| <p id="key-ref">ref</p> | True           | str        | Contains detailed information like wheelchair access or country of origin in encoded form (each number stands for smth) and the last number is always the current date. <br>For detailed information see [ref](#ref)|
| JourneyStatus           | True           | str        | ??? (Always "P"?)                                                                   |
| Product                 | True           | dict       | Contains: [icon](#key-icon), [res](#key-res), [name](#key-Pname), [num](#key-num), [line](#key-line), [catOut](#key-catOut), [catIn](#key-catIn), [catCode](#key-catCode), [cls](#key-cls), [catOutS](#key-catOutS), [catOutL](#key-catOutL), [operatorCode](#key-operatorCode), [operator](#key-operator), [admin](#key-admin), [matchId](#key-matchId) |
| <p id="key-icon">icon</p> | True         | dict       | The icon representation of the stop. Contains: [foregroundColor](#key-fgColor), [backgroundColor](#key-bgColor)|
| <p id="key-fgColor">foregroundColor</p> | True | dict | Foreground color of the station icon {"r": int, "g": int, "b": int, "hex": str}     |
| <p id="key-bgColor">backgroundColor</p> | True | dict | Background color of the station icon {"r": int, "g": int, "b": int, "hex": str}     |
| <p id="key-res">res</p> | True           | str        | ??? Bus = "prod_bus_t", Tram = "prod_tram_t", Train = "prod_reg" |
| <p id="key-Pname">Product - name</p> | True         | str        | The name of the vehicle: Bus: "Bus XXX", Tram: "TXXX", Train: \["RB XXX": Regionalbahn???, "TERXXX": ???, "IC XXX": ICE???] \| where XXX is the [number](#key-number) of the line |
| <p id="key-num">num</p>   | True         | str        | Each Bus has a unique identifier number which is stored in the "num" value          |
| <p id="key-line">line</p> | True         | str        | The line number which is displayed in the name, if it's a tram it is equal to the [name](#key-Pname)  |
| <p id="key-catOut">catOut</p> | True     | str        | The vehicle type. Available: Bus, Train, Tram                                       |
| <p id="key-catIn">catIn</p> | True       | str        | ??? (For busses its usually a number, for tram "CAF")                               |   
| <p id="key-catCode">catCode</p> | True   | str        | ??? (Usually "5" for busses and "8" for tram)                                       |
| <p id="key-cls">cls</p> | True           | str        | ??? (Usually a number in a string)                                                  |
| <p id="key-catOutS">catOutS</p> | True   | str        | ??? (Seems to be the same as [catIn](#key-catIn)                                    |
| <p id="key-catOutL">catOutL</p> | True   | str        | ??? (Seems to be the same as [catOut](#key-catOut)                                  |
| <p id="key-operatorCode">operatorCode</p>| True | str | The abbreviation code for the [operator](#key-operator): RGT = Régime Général des Transports Routiers (was RGTR before), TRA = Luxtram, AVL = Ville de Luxembourg - Service Autobus, CFL = Chemins de Fer Luxembourgeois |
| <p id="key-operator">operator</p> | True | str        | The long name of the operator (see [operatorCode](#key-operatorCode) for full names)|                 
| <p id="key-admin">admin</p> | True       | str        | ??? Probably the administrative unit: Bus: RGTR/AVL, Tram: LUTRAM, Train: "C82--"?  |
| <p id="key-matchId">matchId</p> | True   | str        | ??? Seems to be the same as the [line](#key-line)                                   |
| Notes                   | True           | dict       | Contains [Note](#key-Note)                                                          |
| <p id="key-Note">Note</p>| True          | list       | Contains multiple dicts which each represent a [note](#key-notedict) telling us for example the operator or that you can charge you phone on this bus/tram/train (but not always complete, neraly only complete for trains) |
| <p id="key-notedict">note (Not a key but a dict inside the list [Note](#key-Note))</p>| False | dict | Contains values that describe a note: [value](#key-value), [key](#key-key), [type](#key-Ntype), [routeIdxFrom](#key-routeIdxFrom), [routeIdxTo](#key-routeIdxTo), [textN](#key-textN), [textL](#key-textL), [textS](#key-textS) |
| <p id="key-value">value</p> | False     | str         | The text/value that will be displayed to travellers like "RB XXX: This train is cancelled"|
| <p id="key-key">key</p>| False          | str         | ??? (Missing keys) The key matching the [value](#key-value): \[if the note is about the operator, key="OPERATOR", line cancelled: "text.realtime.stop.cancelled", Bicycles can be taken with you: "71"] |
| <p id="key-Ntype">Note - type</p> | False | str       | ??? ("A" for note like "You can charge your phone here" and "R" for "line cancelled"?)|
| <p id="key-routeIdxFrom">routeIdxFrom</p> | False | int | ??? (Not the id of a stop)                                                        |
| <p id="key-routeIdxTo">routeIdxTo</p> | False | int   | ??? (Not the id of a stop)                                                          |
| <p id="key-textN">textN</p> | False     | str         | ??? (Maybe the normal text version of the [value](#key-value)(ex.: if value="TRAM", textN="TRAM")|
| <p id="key-textL">textL</p> | False     | str         | ??? (Maybe the long text version of the [value](#key-value)(ex.: if value="TRAM", textL="Luxtram")|
| <p id="key-textS">textS</p> | False     | str         | ??? (Maybe the short text version of the [value](#key-value)(ex.: if value="TRAM", textS="TRA")|
| name                   | True           | str         | The name of the line like [Product - name](#key-Pname)                              |
| type                   | True           | str         | ??? (Always "ST"?)                                                                  |
| stop                   | True           | str         | The current station/stop (= the station/stop you asked the data from in your API request) gives the full name of the stop |
| stopid                 | True           | str         | ??? Gives you the name of the stop and its coordinates?                             |
| stopExtId              | True           | str         | Gives you the id of the station/stop (= the id you entered in your request to the API)|
| prognosisType          | False          | str         | ??? Either it is missing or it is "PROGNOSED", maybe it means that a bus/tram/train has started its tour and the arrival time could be prognosed |
| time                   | True           | str         | The planned arrival time (= the time at which the line is scheduled to arrive at this stop)|
| date                   | True           | str         | The date at which the line will arrive at that stop (if in realtime mode, it is always today)|
| rtTime                 | False          | str         | The actual (real time) time at which the line will arrive at that stop (maybe it is late)(only available when line has started its tour)|
| rtDate                 | False          | str         | The actual date at which the line will arrive at that stop (only available when line has started its tour)|
| cancelled              | False          | bool        | Only in the request answer if line is cancelled and then it is set to true         |
| reachable              | True           | bool        | ??? If a line is reachable, always "true", except if line is cancelled (and maybe when it won't stop at that stop? but then its often missing)|
| direction              | True           | str         | The final destination of the line, full name of the station/stop                   |
| trainNumber            | True           | str         | The number of the line (ex.: 812 for the Bus 812)                                  |
| trainCategory          | True           | str         | ??? "064" for busses, "CAF" for tram, \["CRB", "CE", "CTE", "CIC", ?] for trains   |





## Detailed information about response values
Here is some information more in detail about some of the values you receive


### ref
This is an example of a "ref" value you could get in a response: <br>
```json
"JourneyDetailRef": {
    "ref": "1|3078|7|82|29012023"
}
```

As you can see, "ref" is "1|3078|7|82|29012023". <br>
Each number, separated by a | stands for something. <br>
The first number ("1" here) stands for: ??? <br>
The second number ("3078" here) stands for: ??? <br>
The third number ("7" here) stands for: ??? <br>
The fourth number ("82" here) stands for the country of origin.<br>
Each country has a unique identifier and Luxembourg has the code "82" as identifier.<br>
Here a list of identifiers:<br>
(Not all numbers are used, 0-9 are for local authorities)<br>

* 10 Finland
* 20 Russia
* 21 Belorussia
* 22 Ukraine
* 23 Moldova
* 24 Lithuania
* 25 Latvia
* 26 Estonia
* 27 Kazakhstan
* 28 Georgia
* 29 Uzbekistan
- 30 North Korea
- 31 Mongolia
- 32 Vietnam
- 33 China
- 40 Cuba
- 41 Albania
- 42 Japan
- 44 Bosnia-Herzegovina (Serbian part)
- 50 Bosnia-Herzegovina (Bosnian-Croatian part)
- 51 Poland
- 52 Bulgaria
- 53 Rumania
- 54 Czech Republic
- 55 Hungary
- 56 Slovakia
- 57 Azerbaijan
- 58 Armenia
- 59 Kyrgyzstan
- 60 Ireland
- 61 South Korea
- 62 Montenegro
- 65 Macedonia
- 66 Tadzhikistan
- 67 Turkmenistan
- 70 Great Britain
- 71 Spain
- 72 Serbia
- 73 Greece
- 74 Sweden
- 75 Turkey
- 76 Norway
- 78 Croatia
- 79 Slovenia
- 80 Germany
- 81 Austria
- ***82 Luxembourg***
- 83 Italy
- 84 Netherlands
- 85 Switzerland
- 86 Denmark
- 87 France
- 88 Belgium
- 89 Bosnia
- 90 Egypt
- 91 Tunisia
- 92 Algeria
- 93 Morocco
- 94 Protugal
- 95 Israel
- 96 Iran
- 97 Syria
- 98 Lebanon
- 99 Iraq
