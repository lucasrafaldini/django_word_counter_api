# Django Word Counter API
A simple word counter API made with Django Rest Framework.

If you want to know how many times a word is written on a page, just use this API and you will receive the data as JSON.

Getting Started

**See the Swagger documentation here**

https://app.swaggerhub.com/apis-docs/lucasrafaldini/Word-Counter-API/1.0.0

You can access the API directly on heroku:

https://djangowordcounter.herokuapp.com/v1/

**Here's some requests exemples to use:**

**Counting 1 word from 1 url:**
https://djangowordcounter.herokuapp.com/v1/counter?word=python&url=https://en.wikipedia.org/wiki/Monty_Python

**Counting 1 word from 2 urls:**
https://djangowordcounter.herokuapp.com/v1/counter?word=python&url1=https://en.wikipedia.org/wiki/Monty_Python&url2=https://en.wikipedia.org/wiki/Monty_Python_and_the_Holy_Grail

Prerequisites

This API was made using Python 3.7.0, Django, Django REST Framework, Beaultiful Soup, Requests and the good old RegEX.

Installing

All the required packages are listed on `requirements.txt`.

Contributing

Feel free to contribute.
The API still needs some adjustments that will be made soon. 
Here's a list of what it requires to be better:

`Tests` 

`A new index page with the documentation (figure out how to use 'restframework-swagger' properly`

`A new class to return all words in a page and each occurrence`

Authors

    Lucas Rafaldini



Acknowledgments

    If someone can do something, so do you.
