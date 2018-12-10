from bs4 import BeautifulSoup
import re


class processing:

    def counter1(self, word, text):
        soup = BeautifulSoup(text, 'html.parser')
        body_txt = soup.body.extract()
        clean_txt = body_txt.get_text()

        # Pattern to filter the word with RegEx
        # \b - Matches a word boundary position between a word character and non-word character or position (start / end of string)
        pattern = r'\b{}\b'.format(word)
        matches = re.findall(pattern, clean_txt, re.IGNORECASE)

        occurrence = (len(matches) if matches else 0)

        return occurrence

    def counter2(self, word, text1, text2):
        soup = BeautifulSoup(text1, 'html.parser')
        body_txt = soup.body.extract()
        clean_txt = body_txt.get_text()

        # Pattern to filter the word with RegEx
        # \b - Matches a word boundary position between a word character and non-word character or position (start / end of string)
        pattern = r'\b{}\b'.format(word)
        matches = re.findall(pattern, clean_txt, re.IGNORECASE)

        occurrence1 = (len(matches) if matches else 0)

        soup = BeautifulSoup(text2, 'html.parser')
        body_txt = soup.body.extract()
        clean_txt = body_txt.get_text()

        pattern = r'\b{}\b'.format(word)
        matches = re.findall(pattern, clean_txt, re.IGNORECASE)

        occurrence2 = (len(matches) if matches else 0)

        return occurrence1, occurrence2