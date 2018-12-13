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

    def test_success_status_code_1url(self, URL):
        """Check if we are able to reach the API with 1 url parameter"""
        page = requests.get(URL)
        assert page.status_code == 200

##### Success request - 2 urls
    @pytest.mark.parametrize(
        ('URL'),
        (
                ("https://djangowordcounter.herokuapp.com/v1/counter?word=python&url1=https://en.wikipedia.org/wiki/Monty_Python&url2=https://en.wikipedia.org/wiki/Monty_Python_and_the_Holy_Grail"),
        )
    )

    def test_success_status_code_2url(self, URL):
        """Check if we are able to reach the API with 2 urls parameter"""
        page = requests.get(URL)
        assert page.status_code == 200

##### Failed request - 1 url
    @pytest.mark.parametrize(
        ('URL'),
        (
                ("https://djangowordcounter.herokuapp.com/v1/counter?word=teste&url=https://antedeguemon.co"),
        )
    )

    def test_failure_status_code_1url(self, URL):
        """Check if using invalid word and url returns an error"""
        page = requests.get(URL)
        assert page.status_code == 400

##### Failed request - 2 urls
    @pytest.mark.parametrize(

        ('URL'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=teste&url1=https://antedeguemon.co&url2=https://exemploaqui.net"),
        )
    )

    def test_failure_status_code_2url(self, URL):
        """Check if using invalid word and url returns an error"""
        page = requests.get(URL)
        assert page.status_code == 400

##### Invalid URL - 1 url
    @pytest.mark.parametrize(

        ('URL'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=teste&url=https://antedeguemon.co"),
        )
    )

    def test_invalid_url_1url(self, URL):
        """Check if invalid URL validation is working for one url"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert "Page unavailable" in result['url']

##### Invalid URL - 2 urls - Both invalid
    @pytest.mark.parametrize(

        ('URL'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=teste&url1=https://antedeguemon.co&url2=https://teste123.co"),
        )
    )

    def test_invalid_url_2url_both(self, URL):
        """Check if invalid URL validation is working for both urls"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert "Page unavailable" in result['url']

##### Invalid URL - 2 urls - First invalid
    @pytest.mark.parametrize(

        ('URL'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=test&url1=https://antedeguemon.co&url2=https://en.wikipedia.org/wiki/Test"),
        )
    )

    def test_invalid_url_2url_first(self, URL):
        """Check if invalid URL validation is working for first url"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert "Page unavailable" in result['url']

##### Invalid URL - 2 urls - Second invalid
    @pytest.mark.parametrize(

        ('URL'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=test&url1=https://en.wikipedia.org/wiki/Test&url2=https://antedeguemon.co"),
        )
    )

    def test_invalid_url_2url_second(self, URL):
        """Check if invalid URL validation is working for second url"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert "Page unavailable" in result['url']

##### No occurrences - 1 url
    @pytest.mark.parametrize(
        ('URL', 'word'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=rucula&url=https://en.wikipedia.org/wiki/Monty_Python", "rucula"),
        )
    )

    def test_no_occurrences_1url(self, URL, word):
        """Check if no occurrences result in one url is correct"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word] == 0 or [0]


##### No occurrences - 2 urls - Both zero
    @pytest.mark.parametrize(
        ('URL', 'word', 'url1', 'url2'),
        (
                (
                "https://djangowordcounter.herokuapp.com/v1/counter?word=rucula&url1=https://en.wikipedia.org/wiki/Monty_Python&url2=https://en.wikipedia.org/wiki/Test",
                "rucula", "https://en.wikipedia.org/wiki/Monty_Python", "https://en.wikipedia.org/wiki/Test"),
        )
    )
    def test_no_occurrences_2url_both(self, URL, word, url1, url2):
        """Check if no occurrences result in both urls is correct"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word][url1] == 0 or [0]
        assert result[word][url2] == 0 or [0]

##### No occurrences - 2 urls - First zero
    @pytest.mark.parametrize(
        ('URL', 'word', 'url1', 'url2'),
        (
                (
                "https://djangowordcounter.herokuapp.com/v1/counter?word=especiaria&url1=https://en.wikipedia.org/wiki/Monty_Python&url2=https://pt.wikipedia.org/wiki/Mostarda_(planta)",
                "especiaria", "https://en.wikipedia.org/wiki/Monty_Python", "https://pt.wikipedia.org/wiki/Mostarda_(planta)"),
        )
    )
    def test_no_occurrences_2url_first(self, URL, word, url1, url2):
        """Check if no occurrences result is correct in first url"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word][url1] == 0 or [0]
        assert not result[word][url2] == 0 or [0]

##### No occurrences - 2 urls - Second zero
    @pytest.mark.parametrize(
        ('URL', 'word','url1','url2'),
        (
                (
                "https://djangowordcounter.herokuapp.com/v1/counter?word=especiaria&url1=https://pt.wikipedia.org/wiki/Mostarda_(planta)&url2=https://en.wikipedia.org/wiki/Monty_Python",
                "especiaria", "https://pt.wikipedia.org/wiki/Mostarda_(planta)", "https://en.wikipedia.org/wiki/Monty_Python"),
        )
    )
    def test_no_occurrences_2url_second(self, URL, word, url1, url2):
        """Check if no occurrences result is correct in second url"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word][url1] == 0 or [0]
        assert not result[word][url2] == 0 or [0]

##### Test occurrences - 1 url
    @pytest.mark.parametrize(
        ('URL', 'word','occurrences'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=python&url=https://en.wikipedia.org/wiki/Monty_Python", "python", 324),
        )
    )

    def test_occurrences_1url(self, URL, word, occurrences):
        """Check if the correct amount of occurrences is being returned"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word] == occurrences or [occurrences]

##### Test occurrences - 2 urls
    @pytest.mark.parametrize(
        ('URL', 'word','url1','url2','occurrences1','occurrences2'),
        (
            ("https://djangowordcounter.herokuapp.com/v1/counter?word=python&url1=https://en.wikipedia.org/wiki/Monty_Python&url2=https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus", "python", "https://en.wikipedia.org/wiki/Monty_Python","https://en.wikipedia.org/wiki/Monty_Python's_Flying_Circus", 324, 8),
        )
    )

    def test_occurrences_2url(self, URL, word, url1, url2, occurrences1, occurrences2):
        """Check if the correct occurrences on two pages are being returned"""
        page = requests.get(URL)
        result = json.loads(page.text)
        assert result[word][url1] == occurrences1 or [occurrences1]
        assert result[word][url2] == occurrences2 or [occurrences2]