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

## Location Search by Coordinate
As the name says it, you can search for a location (= stop/station) based on coordinates you pass.<br>
This allows you to get the id of a station for example which you need for the Departure Board.<br>

radius, range, lat, lon, max_res
