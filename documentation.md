# Documentation #

The Mobiliteit.lu API is available at "https://cdt.hafas.de/opendata/apiserver", but only with a valid API-Key.
With this API you can track the busses and trains which you can see in the mobiliteit app and on their website.
You can see how late they are, if they are cancelled and much more.
Unfortunately there is no real documentation for the API and the meaning of the different keys in the output, so here is an effort to make it more understandable.


## Get an API-Key
First you will need an API-Key to be able to make calls to the API.
Without a valid key the API will reject any calls and return no information.
To get an API-Key, you have to contact the "Verkéiersbond" (basically Mobiliteit.lu) by email: opendata-api@verkeiersverbond.lu
They will then give you an API-Key which looks like this:
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

where x is either a number or a lowercase letter

This key has a limit of requests you can make to the API (per hour?) and for small projects this is enough, but if you really want to track all busses around Luxembourg, you will have to ask them to increase your limit.
Once you have your key you can go ahead and make requests to the API.


## Getting data from the API


