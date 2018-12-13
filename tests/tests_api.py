import pytest
import requests
import json

class TestApi():

##### Success request - 1 url
    @pytest.mark.parametrize(
        ('URL'),
        (
                ("https://djangowordcounter.herokuapp.com/v1/counter?word=python&url=https://en.wikipedia.org/wiki/Monty_Python"),
        )
    )

    def test_success_status_code_1word(self, URL):
        """Check if we are able to reach the API"""
        page = requests.get(URL)
        assert page.status_code == 200

##### Success request - 2 urls
    @pytest.mark.parametrize(
        ('URL'),
        (
                ("https://djangowordcounter.herokuapp.com/v1/counter?word=python&url1=https://en.wikipedia.org/wiki/Monty_Python&url2=https://en.wikipedia.org/wiki/Monty_Python_and_the_Holy_Grail"),
        )
    )

    def test_success_status_code_2word(self, URL):
        """Check if we are able to reach the API"""
        page = requests.get(URL)
        assert page.status_code == 200

##### Failed request - 1 url
    @pytest.mark.parametrize(
        ('URL'),
        (
                ("https://djangowordcounter.herokuapp.com/v1/counter?word=teste&url=https://antedeguemon.co"),
        )
    )

    def test_failure_status_code_1word(self, URL):
        """Check if specific parameters are causing intentional errors"""
        page = requests.get(URL)
        assert page.status_code == 400

##### Failed request - 2 urls
    @pytest.mark.parametrize(

        ('URL'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=teste&url1=https://antedeguemon.co&url2=https://exemploaqui.net"),
        )
    )

    def test_failure_status_code_2word(self, URL):
        """Check if specific parameters are causing intentional errors"""
        page = requests.get(URL)
        assert page.status_code == 400


    @pytest.mark.parametrize(

        ('URL'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=teste&url=https://antedeguemon.co"),
        )
    )

    def test_invalid_url_1word(self, URL):
        """Check if invalid URL validation is working"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert "Page unavailable" in result['url']

    @pytest.mark.parametrize(
        ('URL', 'word'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=rucula&url=https://en.wikipedia.org/wiki/Monty_Python", "rucula"),
        )
    )

    def test_no_occurrences_1word(self, URL, word):
        """Check if no occurrences result is correct"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word] == 0 or [0]

    @pytest.mark.parametrize(
        ('URL', 'word','occurrences'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=python&url=https://en.wikipedia.org/wiki/Monty_Python", "python", 324),
        )
    )

    def test_occurrences(self, URL, word, occurrences):
        """Check if the correct amount of occurrences is being returned"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word] == occurrences or [occurrences]