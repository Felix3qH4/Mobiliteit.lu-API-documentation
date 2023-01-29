# Documentation #

The Mobiliteit.lu API is available at "https://cdt.hafas.de/opendata/apiserver", but only with a valid API-Key. <br>
With this API you can track the busses and trains which you can see in the mobiliteit app and on their website. <br>
You can see how late they are, if they are cancelled and much more. <br>
Unfortunately there is no real documentation for the API and the meaning of the different keys in the output, so here is an effort to make it more understandable. <br>


## Get an API-Key
First you will need an API-Key to be able to make calls to the API.<br>
Without a valid key the API will reject any calls and return no information.<br>
To get an API-Key, you have to contact the "Verkéiersbond" (basically Mobiliteit.lu) by email: opendata-api@verkeiersverbond.lu<br>
They will then give you an API-Key which looks like this:<br>
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx<br>

Where x is either a number or a lowercase letter.<br>

This key has a limit of requests you can make to the API (per hour?) and for small projects this is enough, but if you really want to track all busses around Luxembourg, you will have to ask them to increase your limit.<br>
Once you have your key you can go ahead and make requests to the API.<br>


## Getting data from the API
There are 2 data access points the API provides.<br>
1. Departure Board
2. Location Search by Coordinate

## Departure Board
The departure board is available at this address: https://cdt.hafas.de/opendata/apiserver/departureBoard?<br>
The xml definition here: https://cdt.hafas.de/opendata/apiserver/departureBoard?wadl<br>

It provides you with information about the different bus lines like the operator etc. for a given stop/station.<br>
So you have to pass it the id of a station and then it will return you which busses arrive/depart from that station.<br>
If in realtime mode, you will also get realtime information like how late a bus is.<br>

To get the id of a station have a look at "Location Search by Coordinate".<br>

When making a request to the departure board, it has to look like this:<br>
https://cdt.hafas.de/opendata/apiserver/departureBoard?arg1=XX&arg2=XX&arg3=XX<br>

Where arg1, arg2 and arg3 are some arguments you can pass to the departure board.<br>
You can choose yourself which arguments to pass and which not altough there are 2 arguments that are mandatory.
You always have to pass "accessId" so your API-Key and "id", the id of the stop/station you want the data from.

Available arguments for the departure board:

| Argument Name | Mandatory | Value | Description                                         |
| ------------- | --------- | ----- | -----------                                         |
| accessId      | True      | str   | Your API-Key                                        |
| id            | True      | int   | The station/stop id from which you want to retrieve data |
| requestId     | False     | str   | ??? |
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

## Location Search by Coordinate
As the name says it, you can search for a location (= stop/station) based on coordinates you pass.<br>
This allows you to get the id of a station for example which you need for the Departure Board.<br>

radius, range, lat, lon, max_res
