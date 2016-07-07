'''
Write a class that identifies the first and last name of a person in
unstructured text representing a person's name. You should strive to
have your model work universally with other names beyond the examples below.
Feel free to add any other tests or methods you feel are appropriate.

Please submit what you have by the deadline.

run the following to test:
$ pip install pytest
$ py.test -v test_name_parsing.py
'''
from name_parse_try import NameParse


class TestNameParsing:
    def setup_class(cls):
        cls.aaron = ('aaron', 'mangum')
        cls.naini = ('naini', 'mistry')
        cls.molly = ('molly', 'scott')
        cls.steven = ('steven', 'st. claire')

    def test_aaron_first_last(self):
        name = 'aaron mangum'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_first_middle_last(self):
        name = 'aaron david mangum'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_last_first(self):
        name = 'mangum aaron'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_last_comma_first_middle(self):
        name = 'mangum, aaron david'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_last_first_middle(self):
        name = 'mangum aaron david'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_title_first_last(self):
        name = 'data scientist, aaron mangum'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_first_last_title(self):
        name = 'aaron mangum, data scientist'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_evil_twin(self):
        name = 'aaron david von mangum'
        assert NameParse(name).parsed_name == self.aaron

    def test_aaron_evil_twin_last_first(self):
        name = 'von mangum, aaron david'
        assert NameParse(name).parsed_name == self.aaron

    def test_naini_first_last(self):
        name = 'naini mistry'
        assert NameParse(name).parsed_name == self.naini

    def test_naini_last_first(self):
        name = 'mistry naini'
        assert NameParse(name).parsed_name == self.naini

    def test_naini_last_comma_first(self):
        name = 'mistry, naini'
        assert NameParse(name).parsed_name == self.naini

    def test_naini_first_last_title(self):
        name = 'naini mistry, vice president of product'
        assert NameParse(name).parsed_name == self.naini

    def test_double_first(self):
        name = 'molly scott'
        assert NameParse(name).parsed_name == self.molly

    def test_double_first_last_first(self):
        name = 'scott molly'
        assert NameParse(name).parsed_name == self.molly

    def test_double_first_last_comma_first(self):
        name = 'scott, molly'
        assert NameParse(name).parsed_name == self.molly

    def test_double_first_title(self):
        name = 'molly scott account executive'
        assert NameParse(name).parsed_name == self.molly

    def test_punctuated_double(self):
        name = 'steven st. claire'
        assert NameParse(name).parsed_name == self.steven

    def test_title_puctuated_double(self):
        name = 'user interface designer steven st. claire'
        assert NameParse(name).parsed_name == self.steven


print dir(TestNameParsing)
