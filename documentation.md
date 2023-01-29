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

This key has a limit of requests you can make to the API, for small projects this is enough, but if you really want to track all busses around Luxembourg, you will have to ask them to increase your limit.<br>

Default limits are:<br>
    Hourly: 500 requests<br>
    Daily: 5000 requests<br>
<br>
There also exists a monthly and yearly quota, but the defined request amount is quite generous.<br>

Once you have your key you can go ahead and make requests to the API.<br>


## Getting data from the API
There are 2 data access points the API provides.<br>


1. [Location Search by Coordinate (nearbystops)](Location_Search_by_Coordinate.md)
2. [Departure Board](Departure_Board.md)







