# Departure Board
The departure board is available at this address: https://cdt.hafas.de/opendata/apiserver/departureBoard?<br>
The xml definition here: https://cdt.hafas.de/opendata/apiserver/departureBoard?wadl<br>

It provides you with information about the different bus lines like the operator etc. for a given stop/station.<br>
So you have to pass it the id of a station and then it will return you which busses arrive/depart from that station.<br>
If in realtime mode, you will also get realtime information like how late a bus is.<br>

To get the id of a station have a look at "[Location Search by Coordinate](Location_Search_by_Coordinate.md)".<br>

Table of contents:

1) [Requesting data](#Requesting-data)
2) [Common questions](#common-questions)
3) [API response](#API-response)
    1. [XML](#XML)
    2. [JSON](#JSON)
    3. [Response values meaning](#response-values-meaning)
4) [Detailed information about response values](#detailed-information-about-response-values)
    1. [ref](#ref)
5) [Error codes](#error-codes)


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
| requestId     | False     | str   | Request ID for identifying the request. For each request a requestId is generated. Used for debugging on server side. You can set your own requestId by passing this parameter. |
| format        | False     | str   | The format you want your response in. Availables are: json, xml <br>If not set, xml is used.|
| jsonpCallback | False     | str   | The json response will be wrapped in a javascript function with the name you passed |
| lang          | False     | str   | Language of the journey planner. <br>You can basically put anything in here as the keys in the response will always be in english and the data in french. |
| extId         | False     | str   | \[Deprecated] The station/stop id from which you want to retrieve data |
| direction     | False     | str   | If only vehicles departing or arriving from a certain direction shall be returned, specify the direction by giving the station/stop ID of the last stop on the journey. |
| date          | False     | str   | Sets the start date for which the departures shall be retrieved. Represented in the format YYYY-MM-DD. |
| time          | False     | str   | Sets the start time for which the departures shall be retrieved. Represented in the format hh:mm[:ss] in 24h nomenclature. Seconds will be ignored for requests. |
| dur           | False     | int   | \[Deprecated -> use 'duration'] Range from 0 to 1439 |
| duration      | False     | int   | The the time period from the request time on until when departures/arrivals should be returned. Range from 0 to 1439. Default is 60 (= 60 minutes) |
| maxJourneys   | False     | int   | Maximum number of journeys to be returned. If no value is defined or -1, all departing/arriving services within the duration sized period are returned. Default is -1 |
| products      | False     | int   | Decimal value defining the product classes to be included in the search. It represents a bitmask combining bit number of a product as defined in the HAFAS raw data file zugart. See [products](#products) for the bitmasks. |
| operators     | False     | str   | \[CHECK OPERATORS] Only journeys provided by the given operators are part of the result. To filter multiple operators, separate the codes by comma. If the operator should not be part of the be trip, negate it by putting ! in front of it. Available operators are: RGTR, AVL, CFL |
| lines         | False     | str   | Only journeys running the given line are part of the result. To filter multiple lines, separate the codes by comma. If the line should not be part of the be trip, negate it by putting ! in front of it. |
| filterEquiv   | False     | int   | \[Unused] Enables/disables the filtering of equivalent marked stops. There are no equal stops in Luxembourg so this parameter won't do anything.|
| attributes    | False     | str   | ??? Filter boards by one or more attribute codes of a journey. Multiple attribute codes are separated by comma. If the attribute should not be part of the result, negate it by putting ! in front of it. |
| platforms     | False     | str   | Filter boards by platform. Multiple platforms are separated by comma. Platforms are used for example at train stations. A train station is one single stop but has multiple platforms so the busses stopping there all stop at the same stop (= the train station) but at different platforms. (Depends on the station how many platforms there are.) |
| rtMode        | False     | bool   | Set the realtime mode to be used if enabled. Available are: FULL and OFF. By default it is set to FULL and returns the real-time arrival time of the journey if set to FULL. |
| <p id="key-passlist">passlist</p>| False| int| Include a list of all stops for this journey. 0 = Disabled->returns no stops (Default) and 1 = All stops |



## Common questions

**Can you search for a specific bus/train/tram line?**
When I asked mobiliteit.lu the last time (24. February 2023) the answer was no and I don't think anything has changed about that.<br>
The only 'way' to search for a line is to pass the 'line' parameter when making a request, that way you only get this line at the station, but you cannot search for this line on all the stations without making a request for all stations. <br>
ex.: https://cdt.hafas.de/opendata/apiserver/departureBoard?accessId=XXXXX&lang=fr&id=200403015&format=json&lines=802

<br>

**I get the error "QuotaExceeded"**
This means that you have used all your available request tokens (as your API-Key is limited to a certain amount).<br>
Either wait an hour or so until your tokens are reset or ask for your limit to be made higher. <br>

**Some stations don't return any lines**
Yes that happens, but usually only when the lines can't stop at that station for some reason.<br>
Then they are not shown on that station, thats why you don't get any results.<br>

**What API services are available**
Only the DepartureBoard service and the [Location Search by Coordinate](Location_Search_by_Coordinate.md) are available for now.<br>
On my question from the 24. February 2023 they mentionned that maybe they would offer some more API services in the future.<br>

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
  <Product name="Bus 812" num="3398" line="812" catOut="Bus" catIn="064" catCode="5" cls="32" catOutS="064" catOutL="Bus" operatorCode="RGT" operator="R??gime G??n??ral des Transports Routiers" admin="RGTR--" matchId="812">
    <icon res="prod_bus_t">
      <foregroundColor r="255" g="255" b="255" hex="#FFFFFF"/>
      <backgroundColor r="117" g="40" b="100" hex="#752864"/>
    </icon>
  </Product>
  <Notes>
    <Note key="OPERATOR" type="A" routeIdxFrom="34" routeIdxTo="41" txtN="RGTR" txtL="R??gime G??n??ral des Transports Routiers" txtS="RGT">RGTR</Note>
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
        "operator":"R??gime G??n??ral des Transports Routiers",
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
                "txtL":"R??gime G??n??ral des Transports Routiers",
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


| Key                     | Always present | Value type | Meaning                                                                             |
| ---                     | -------------- | ---------- | -------                                                                             |
| JourneyDetailRef        | True           | dict       | Contains [ref](#key-ref)                                                            |
| <p id="key-ref">ref</p> | True           | str        | Contains detailed information like wheelchair access or country of origin in encoded form (each number stands for smth) and the last number is always the current date. <br>For detailed information see [ref](#ref)|
| JourneyStatus           | True           | str        | Shows the status of the journey. For detailed information see [JourneyStatus](#journeystatus)|
| Product                 | True           | dict       | Contains: [icon](#key-icon), [res](#key-res), [name](#key-Pname), [num](#key-num), [line](#key-line), [catOut](#key-catOut), [catIn](#key-catIn), [catCode](#key-catCode), [cls](#key-cls), [catOutS](#key-catOutS), [catOutL](#key-catOutL), [operatorCode](#key-operatorCode), [operator](#key-operator), [admin](#key-admin), [matchId](#key-matchId) |
| <p id="key-icon">icon</p> | True         | dict       | The icon representation of the stop. Contains: [foregroundColor](#key-fgColor), [backgroundColor](#key-bgColor)|
| <p id="key-fgColor">foregroundColor</p> | True | dict | Foreground color of the station icon {"r": int, "g": int, "b": int, "hex": str}     |
| <p id="key-bgColor">backgroundColor</p> | True | dict | Background color of the station icon {"r": int, "g": int, "b": int, "hex": str}     |
| <p id="key-res">res</p> | True           | str        | Description of the icons for the different vehicle types in the mobiliteit app. For more details see [res](#res)|
| <p id="key-Pname">name</p> | True         | str        | The name of the vehicle: Bus: "Bus XXX", Tram: "TXXX", Train: \["RB XXX": Regionalbahn?, "TERXXX": ?, "IC XXX": ICE?, "RE XXX": Regionalexpress?] \| where XXX is the [number](#key-number) of the line |
| <p id="key-num">num</p>   | True         | str        | Each Bus has an internal unique identifier number which is stored in the "num" value|
| <p id="key-line">line</p> | True         | str        | The line number which is displayed in the name, if it's a tram it is equal to the [name](#key-Pname)  |
| <p id="key-catOut">catOut</p> | True     | str        | The vehicle type. Available: Bus, Train, Tram                                       |
| <p id="key-catIn">catIn</p> | True       | str        | Encoding for the Bus or train category. For details see [catIn](#catIn)             |   
| <p id="key-catCode">catCode</p> | True   | str        | A code telling you which vehicle type it is (Bus/Intercity/...). For more details see [catCode](#catCode) |
| <p id="key-cls">cls</p> | True           | str        | A number telling you which product it is. (Bus, Tram, ...) See [cls](#cls) for more details. |
| <p id="key-catOutS">catOutS</p> | True   | str        | Stands for the short form of [catOut](#key-catOut). Is the same as [catIn](#key-catIn)|
| <p id="key-catOutL">catOutL</p> | True   | str        | Stands for the **long** form of [catOut](#key-catOut). Is the same as [catOut](#key-catOut)|
| <p id="key-operatorCode">operatorCode</p>| True | str | The abbreviation code for the [operator](#key-operator). See [operator codes](#operator-codes) for abbreviations.|
| <p id="key-operator">operator</p> | True | str        | The long name of the operator (see [operator codes](#operator-codes) for full names)|                 
| <p id="key-admin">admin</p> | True       | str        | The administrator or operator of the different lines. For more details see [admin](#admin)|
| <p id="key-matchId">matchId</p> | True   | str        | ??? Seems to be the same as the [line](#key-line)                                   |
| Notes                   | True           | dict       | Contains [Note](#key-Note)                                                          |
| <p id="key-Note">Note</p>| True          | list       | Contains multiple dicts which each represent a [note](#key-notedict) telling us for example the operator or that you can charge you phone on this bus/tram/train (but not always complete, neraly only complete for trains) |
| <p id="key-notedict">note (Not a key but a dict inside the list [Note](#key-Note))</p>| False | dict | Contains values that describe a note: [value](#key-value), [key](#key-key), [type](#key-Ntype), [routeIdxFrom](#key-routeIdxFrom), [routeIdxTo](#key-routeIdxTo), [textN](#key-textN), [textL](#key-textL), [textS](#key-textS). For more details see [note](#note)|
| <p id="key-value">value</p> | False     | str         | The text/value that will be displayed to travellers like "RB XXX: This train is cancelled"|
| <p id="key-key">key</p>| False          | str         | The key matching the [value](#key-value). For more detailed information see [key](#key)|
| <p id="key-Ntype">type</p>| False       | str         | Displays the type of message contained in a note. For more details see [type](#type-note)|
| <p id="key-routeIdxFrom">routeIdxFrom</p> | False | int | Indicates for which stops of the journey the note is valid. For more details see [Stop](#Stop)|
| <p id="key-routeIdxTo">routeIdxTo</p> | False | int   | ??? (Not the id of a stop)                                                          |
| <p id="key-priority">priority</p>| False | str        | The priority of the note between 0 and 999, the lower the number = the higher the priority. Every note is displayed, but this might affect the order in which they are displayed. ([Source 1 p.89](#Source-1)|
| <p id="key-textN">textN</p> | False     | str         | The normal text version of the [value](#key-value)(ex.: if value="TRAM", textN="TRAM")|
| <p id="key-textL">textL</p> | False     | str         | The long text version of the [value](#key-value)(ex.: if value="TRAM", textL="Luxtram")|
| <p id="key-textS">textS</p> | False     | str         | The short text version of the [value](#key-value)(ex.: if value="TRAM", textS="TRA")|
| name                   | True           | str         | The name of the line like [Product - name](#key-Pname)                              |
| type                   | True           | str         | The type of stop. See [type](#type) for more details.                               |
| stop                   | True           | str         | The current station/stop (= the station/stop you asked the data from in your API request) gives the full name of the stop |
| stopid                 | True           | str         | Gives you the name of the stop and its coordinates. See [stopid](#stopid) for detailed information |
| stopExtId              | True           | str         | Gives you the id of the station/stop (= the id you entered in your request to the API)|
| prognosisType          | False          | str         | In combination with [rtTime](#key-rtTime) it says that the rtTime=arrival time is prognosed so in real-time prognosed|
| time                   | True           | str         | The planned arrival time (= the time at which the line is scheduled to arrive at this stop)|
| date                   | True           | str         | The date at which the line will arrive at that stop (if in realtime mode, it is always today)|
| <p id="key-rtTime">rtTime</p>| False    | str         | The actual (real time) time at which the line will arrive at that stop (maybe it is late)(only available when line has started its tour)|
| rtDate                 | False          | str         | The actual date at which the line will arrive at that stop (only available when line has started its tour)|
| cancelled              | False          | bool        | Only in the request answer if line is cancelled and then it is set to true         |
| reachable              | True           | bool        | If the journey can be accomplished (ex.: if the bus can drive), always on 'True' as it doesn't show if you can reach that journey. (Only 'False' if journey is [cancelled](#key).)|
| direction              | True           | str         | The final destination of the line, full name of the station/stop                   |
| trainNumber            | True           | str         | The number of the line (ex.: 812 for the Bus 812)                                  |
| trainCategory          | True           | str         | Equals [catIn](#key-catIn), no public list of codes. ("064" for busses, "CAF" for tram, \["CRB", "CE", "CTE", "CIC", ?] for trains)   |
| Stops                  | False          | dict        | Contains [Stop](#key-stop)                                                         |
| Stop                   | False          | list        | Contains the stops of a journey. For more details see [Stop](#Stop)                |


<br>
<br>
<br>

## Detailed information about response values
Here is some information more in detail about some of the values you receive


## ref
This is an example of a "ref" value you could get in a response: <br>
```json
"JourneyDetailRef": {
    "ref": "1|3078|7|82|29012023"
}
```
The "ref" value is an internal ID with which one can identify every single journey.<br>
That way one can check if the journey is the same after another request to the API or if it is already a new journey.<br>
As you can see, "ref" is "[1](#first-number)|[3078](#second-number)|[7](#third-number)|[82](#fourth-number)|[29012023](#fifth-number)". <br>
Each number, separated by a | stands for something. <br>
(By clicking on a number you can quickly get to the description of what it stands for without having to scroll down.) <br>

### first number
The first number ("**1**" here) stands for: ??? (Always one for bus, train, tram)<br>

### second number
The second number ("**3078**" here) stands for: ??? <br>

### third number
The third number ("**7**" here) stands for: ??? <br>

### fourth number
The fourth number ("**82**" here) stands for the country of origin.<br>
Each country has a unique identifier and Luxembourg has the code "82" as identifier.<br>
Here a list of identifiers:<br>
(Not all numbers are used, 0-9 are for local authorities)<br>

- 10 Finland
- 20 Russia
- 21 Belorussia
- 22 Ukraine
- 23 Moldova
- 24 Lithuania
- 25 Latvia
- 26 Estonia
- 27 Kazakhstan
- 28 Georgia
- 29 Uzbekistan
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

source: ([Source 1 page 16](#source-1))
<br>

### Fifth number
The fifth number ("**29012023**" here) stands for the current date, so here it would be the 29th of January 2023.<br>

<br>
<br>

## JourneyStatus
Shows the status of the journey:
- P = Planned -> A planned journey. This is also the default value
- R = Replacement -> The journey was added as a replacement for a planned journey.
- A = Additional -> The journey is an additional journey to the planned journeys.
- S = Special -> This is a special journey. The exact definition which journeys are considered special is up to the customer.
<br>
<br>

## res
The description/name for the icons of the different vehicle types in the mobiliteit.lu app.<br>
Pretty irrelevant and no exact list available as they are created by another society.
The descriptions might change if new icons are used in the mobiliteit.lu app.
These are the known icon names:
- Bus : prod_bus_t
- Tram : prod_tram_t
- Train : ["prod_reg" for "RB" and "RE" trains, "prod_ic" for "IC" trains]
<br>
<img src="./images/vehicle_types_icons_in_app.png" alt="Image of the different vehicle types icons in the app." />
<br>
<br>

## catIn
An internal encoding of the bus or train category.<br>
For busses its usually 064, but it can also be values like 063 or 034.<br>
Therefore [catOut](#catOut) is way more interesting as it contains the value which is also used for displaying the category and transportation vehicle.<br>
<br>

## catCode
The 'catCode' allows identifying the type of vehicle that operates this line. <br>
(From the file 'zugart') <br>
Here a list of all known codes: <br>
- 00 : ICE-Trains
- 01 : Intercity- and Eurocitytrains
- 02 : Interregio- and Fast trains
- 03 : Regional and other trains
- 04 : S-Bahn
- 05 : Busses
- 06 : Boats
- 07 : Underground
- 08 : Tram
- 09 : Services requiring tel. registration for passengers

*The above codes are complete and correct as of 24. February 2023 .*
<br>
<br>

## cls
Tells you which product category is serving the line: <br>
- 1 = [express-train = TGV](#express-train)
- 2 = [national-train = IC](#national-train)
- 4 = [local-train = RB, RE, TER](#local-train)
- 32 = [bus](#bus)
- 256 = [tram](#tram)

Information from [Source 5](#Source-5) and verified by the API service people.<br>
*Above codes are complete and correct as of 24. February 2023 .*<br><br>


## operator codes
There are 6 operators in Luxembourg: <br>
See [Source 1](#source-1) point 6.18. page 132 for details. <br>

```json
{
    "id": "00001",
    "K": "AVL", //= 'operatorCode' in the API response
    "L": "AVL",
    "V": "Ville de Luxembourg - Service Autobus", //= 'operator' in the API response
    "administrator": "AVL---" //= 'admin' in the API response
}
```
<br>

```json
{
    "id": "00002",
    "K": "CFL", //= 'operatorCode' in the API response
    "L": "CFL",
    "V": "Chemins de Fer Luxembourgeois", //= 'operator' in the API response
    "administrator": [
        "c80---",
        "c82---",
        "c85---",
        "c87---",
        "c88---"
    ] //= 'admin' in the API response
}
```
<br>

```json
{
    "id": "00003",
    "K": "CFL", //= 'operatorCode' in the API response
    "L": "CFLBus",
    "V": "Soci??t?? Nationale des Chemins de Fer Luxembourgeois", //= 'operator' in the API response
    "administrator": "CFLBUS" //= 'admin' in the API response
}
```
<br>

```json
{
    "id": "00004",
    "K": "RGT", //= 'operatorCode' in the API response
    "L": "RGTR",
    "V": "R??gime G??n??ral des Transports Routiers", //= 'operator' in the API response
    "administrator": "RGTR---" //= 'admin' in the API response
}
```
<br>

```json
{
    "id": "00005",
    "K": "TIC", //= 'operatorCode' in the API response
    "L": "TICE",
    "V": "Syndicat des Tramways Intercommunaux dans le Canton d'Esch", //= 'operator' in the API response
    "administrator": "TIC---" //= 'admin' in the API response
}
```
<br>

```json
{
    "id": "00006",
    "K": "TRA", //= 'operatorCode' in the API response
    "L": "TRAM",
    "V": "Luxtram", //= 'operator' in the API response
    "administrator": "LUTRAM" //= 'admin' in the API response
}
```

<br>

*The above codes and names are complete and correct as of 24. February 2023*
<br>
<br>

## admin
The value of 'admin' shows the administrator/operator of the different lines.<br>
The values can be found at [operatorCodes](#operator-codes) under the 'administrator' keys.<br>
(AVL---, c80---, c82---, c85---, c87---, c88---, CFLBUS, RGTR---, TIC---, LUTRAM)<br>
<br>
<br>

## note
The different notes are given by the different data providers (ex.: Deutsche Bahn, SNCF, ...).<br>
This means that there are no standardized values for a note.<br>
Each provider provides their own pair of [keys](#key) and the respective value.<br>
The API will then take them as they are and display them that way.<br>
If a journey is cancelled it will be displayed as [cancelled](#key).<br>
The '[type](#type-note)' value displays the type of message contained in the note.<br>
<img src="images/note_in_app.png" alt="Image of 2 notes in the mobiliteit.lu app" />
<br>
<br>

## key
**There are keys missing/some keys are incorrect**<br>
The key of a [note](#note) is text and often an abbreviation. <br>
If the key is an abbreviation the long text can be found under "[textN](#key-textN)". <br>
Here is a list of known abbreviations:<br>
- EH = Einstiegshilfe   ([priority 350](#key-priority))
- KL = Klimaanlage  ([priority 350](#key-priority))
- LS = Laptop-Steckplatz    ([priority 350](#key-priority))
- 71 = bicylce transport / service pour bicyclettes / Fahrradmitnahme ([priority 1](#key-priority))
- text.realtime.journey.cancelled = The entire line is cancelled and won't drive
- text.realtime.stop.cancelled = The line will not stop at this station/stop
- OPERATOR = The note tells us who the operator is for this line

Depending from which country the bus/train comes from the priorities may have different numbers. <br>

<br>
<br>

## type-Note
Displays the type of message contained in a [note](#note).<br>
- A = Attribute
- R = Realtime
- I = Infotext
<br>
There should not be any other types in the API (as of 24. February 2023).
<br>
<br>

## type
Displays the type of stop:<br>
- ST = Stop
- ADR = Address
- POI = Point of Interest
As the API is being called with [stop ids](#stopid), it should always be 'ST'.<br>
<br>
<br>

## stopid
```json
"stopid": "A=1@O=Steinfort, Gemeng@X=5913410@Y=49659424@U=82@L=191104004@"
```
This is an example of a stopid value. <br>
Now each of the components means something.<br>

### A
A is unknown, even to the people from the API, but is always 1.<br>
<br>

### O
The name of the station/stop (long version).<br>
<br>

### X
The X coordinate of the station/stop (missing decimal point).
The X/Y coordinates are indicated by degrees of longitude and latitude in a
geographical coordinate system. Units: degrees with decimal places. For accurancy in meters it has to have 6 right-of-comma positions. The preferred
coordinate system is UTM32.


### Y
The Y coordinate of the station/stop (missing decimal point).
The X/Y coordinates are indicated by degrees of longitude and latitude in a
geographical coordinate system. Units: degrees with decimal places. For accurancy in meters it has to have 6 right-of-comma positions. The preferred
coordinate system is UTM32.


### U
Country code for Luxembourg.<br>
For a list of codes see [ref](#ref).<br>
<br>

### L
The id of the station/stop.<br>
<br>
<br>


## trainCategory
The category of vehicle that is being used for the transport. (For general Hafas API: [Source 1 p. 65](#source-1))<br>
- 064 : Bus
- CAF : Tram (named  like that because of the society that made the tram [Source 2](#source-2))
- CRB : Regional train? (only used for "RB" trains)
- CIC : Intercity train (Deutsche Bahn trains)(only used for "IC" trains)
- CTE : trains from the SNCF (France)(only used for "TER" trains)

Also see [Products](#Products) for detailed information about each product. <br><br>

## Stop
```json
"Stop":[
    {"name":"Luxembourg, Gare Centrale","id":"A=1@O=Luxembourg, Gare Centrale@X=6134239@Y=49599969@U=82@L=200405060@","extId":"200405060","routeIdx":0,"lon":6.134239,"lat":49.599969,"depTime":"18:32:00","depDate":"2023-02-24"},
    {"name":"Howald, Gare","id":"A=1@O=Howald, Gare@X=6132459@Y=49581083@U=82@L=200304014@","extId":"200304014","routeIdx":1,"lon":6.132459,"lat":49.581083,"arrTime":"18:35:00","arrDate":"2023-02-24"},
    {"name":"Berchem, Gare","id":"A=1@O=Berchem, Gare@X=6133753@Y=49542663@U=82@L=221101001@","extId":"221101001","routeIdx":2,"lon":6.133753,"lat":49.542663,"arrTime":"18:40:00","arrDate":"2023-02-24"},
    {"name":"Bettembourg, Gare","id":"A=1@O=Bettembourg, Gare@X=6101680@Y=49516513@U=82@L=220102018@","extId":"220102018","routeIdx":3,"lon":6.10168,"lat":49.516513,"arrTime":"18:45:00","arrDate":"2023-02-24"},
    {"name":"Noertzange, Gare","id":"A=1@O=Noertzange, Gare@X=6050882@Y=49508009@U=82@L=220105006@","extId":"220105006","routeIdx":4,"lon":6.050882,"lat":49.508009,"arrTime":"18:49:00","arrDate":"2023-02-24"},
    {"name":"Schifflange, Gare","id":"A=1@O=Schifflange, Gare@X=6009783@Y=49506301@U=82@L=221401002@","extId":"221401002","routeIdx":5,"lon":6.009783,"lat":49.506301,"arrTime":"18:53:00","arrDate":"2023-02-24"},
    {"name":"Esch-sur-Alzette, Gare","id":"A=1@O=Esch-sur-Alzette, Gare@X=5985090@Y=49493914@U=82@L=220402046@","extId":"220402046","routeIdx":6,"lon":5.98509,"lat":49.493914,"arrTime":"18:57:00","arrDate":"2023-02-24"}]
```
Contains all stops of a journey.<br>
Only present if you passed the [passlist](#key-passlist) argument!<br>
'routeIdxTo' and 'routeIdxFrom' from a [note](#note) point to the stop at the given index in the 'Stop' list.<br>
So if a note has the attributes:<br>
```json
"routeIdxFrom": 0,
"routeIdxTo": 4
```
This means that the note is valid from stop '0' to stop '4' in the 'Stop' list.<br>
We start counting at '0', so the first stop is stop number '0'.<br>
The note would be valid from stop 'Luxembourg, Gare Centrale' to stop 'Noertzange, Gare' in this example.<br>
<br>
<br>

## Error codes
Sample of an error message containing an error code:<br>
```json
{"serverVersion":"2.7.6","dialectVersion":"1.29","errorCode":"API_PARAM","errorText":"id or extId missing (IllegalArgumentException)","requestId":"default-request-id"}
```
As you can see the error code here is "API_PARAM".<br><br>
List of all known codes as of 24. February 2023:<br>
|        Code         | HTTP status code |                       Text                       |
|---------------------|------------------|--------------------------------------------------|
| API_AUTH            | 403              | access                                           |
| API_QUOTA 	      | 400	             | quota exceeded for 'key' on 'service'            |
| API_PARAM	          | 400	             | required parameter <<name>> is missing           |
| API_PARAM	          | 400	             | numB wrong, only number in range [0,6] al-lowed  |
| API_PARAM	          | 400	             | numF wrong, only number in range [0,6] al-lowed  |
| API_PARAM	          | 400	             | numF + numB not greater than [6] allowed         |
| API_FORMAT	      | 400	             | response format not supported                    |
| SVC_PARAM	          | 400	             | request parameter missing or invalid             |
| SVC_LOC	          | 400	             | location missing or invalid                      |
| SVC_LOC_ARR	      | 400	             | arrival location missing or invalid              |
| SVC_LOC_DEP	      | 400	             | departure location missing or invalid            |
| SVC_LOC_VIA	      | 400	             | unknown change stop                              |
| SVC_LOC_EQUAL	      | 400	             | start/destination or vias are equal              |
| SVC_LOC_NEAR	      | 400	             | start and destination to close                   |
| SVC_DATATIME	      | 400	             | date/time missing or invalid                     |
| SVC_DATATIME_PERIOD |	400	             | date/time not in timetable or allowed period     |
| SVC_PROD	          | 400	             | product field missing or invalid                 |
| SVC_CTX	          | 400	             | context invalid                                  |
| SVC_MAIL_ADR	      | 400	             | sender/receiver mail address invalid or miss-ing |
| SVC_MAIL	          | 500	             | fail to send mail                                |
| SVC_SMS_NUM	      | 400	             | receiver sms phone number invalid or missing     |
| SVC_SMS	          | 500	             | fail to send sms                                 |
| SVC_FAILED_SEARCH	  | 500	             | unsuccessful search                              |
| SVC_NO_RESULT	      | 500	             | no result found                                  |
| SVC_NO_MATCH	      | 500	             | no match found                                   |
| INT_ERR	          | 500	             | internal error                                   |


<br>
<br>


# Products
Following product information is from [Source 5](#source-5). <br>
But bitmasks vary from the ones in the [cfl version](http://github.com/public-transport/hafas-client/tree/master/p/cfl)<br>

## Express train
```json
{
    "id": "express-train",
    "mode": "train",
    "bitmasks": [1],
    "name": "local train (TGV/ICE)",
    "short": "TGV/ICE"
}
```

## National train
```json
{
    "id": "national-train",
    "mode": "train",
    "bitmasks": [2],
    "name": "national train (IC/RE/IRE)",
    "short": "IC/RE/IRE"
}
```

## Local train
```json
{
    "id": "local-train",
    "mode": "train",
    "bitmasks": [4],
    "name": "local train (RB/TER)",
    "short": "RB/TER"
}
```

## Bus
```json
{
    "id": "bus",
    "mode": "bus",
    "bitmasks": [32],
    "name": "Bus",
    "short": "Bus"
}
```

## Tram
```json
{
    "id": "tram",
    "mode": "train",
    "bitmasks": [256],
    "name": "Tram",
    "short": "Tram"
}
```


## Source 1
https://transportdatamanagement.ch/content/uploads/2020/04/HRDF.5.20.39-Guidelines-e.pdf


## Source 2
https://www.caf.net/de/soluciones/proyectos/proyecto-detalle.php?p=278


## Source 3
https://download-data.deutschebahn.com/static/apis/fahrplan/Fpl-API-Doku-Open-Data-BETA-0_81_2.pdf

## Source 4
https://gtfs.org

## Source 5
https://github.com/public-transport/hafas-client/blob/master/p/mobiliteit-lu/products.js