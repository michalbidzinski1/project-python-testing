import unittest
from src.sample.Morse import  Morse
from assertpy import assert_that
class TestMorse(unittest.TestCase):
    def setUp(self):
        self.temp = Morse()
    def test_morse_single_letter(self):
        morse=".- "
        inputed_data = "A"
        self.assertEqual(morse, self.temp.coding(inputed_data))
    def test_morse_word(self):
        morse=".-- --- -.. .- "
        inputed_data = "woda"
        self.assertEqual(morse, self.temp.coding(inputed_data))
    def test_morse_numbers(self):
        inputed_data = "12345 67890"
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- "
        self.assertEqual(morse,self.temp.coding(inputed_data))
    def test_morse_sentence(self):
        morse=".- .-.. .- -- .- -.- --- - .- "
        inputed_data = "ala ma kota"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_empty(self):
        morse = ""
        inputed_data = ""
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_punctuation_marks(self):
        morse = "--..-- "
        inputed_data = ","
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_punctuation_marks_2(self):
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-. "
        inputed_data = "&'@)(:,=!.-+\"?/"
        self.assertEqual(morse, self.temp.coding(inputed_data))
    def test_morse_with_polish_marks(self):
        morse = '.-.- -.-.. ..-.. .-..- --.-- ---. ...-... '
        inputed_data = "ĄĆĘŁŃÓŚ"
        self.assertEqual(morse, self.temp.coding(inputed_data))

    def test_morse_coding_arr(self):
        inputed_data = []
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)
    def test_morse_coding_obj(self):
        inputed_data = {}
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)
    def test_morse_coding_float(self):
        inputed_data = 3.14
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)
    def test_morse_coding_False(self):
        inputed_data = False
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)
    def test_morse_coding_True(self):
        inputed_data = True
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)
    def test_morse_coding_None(self):
        inputed_data = None
        assert_that(self.temp.coding).raises(Exception).when_called_with(inputed_data)

    # -------
    # DECODING
    # ----
    def test_morse_decoding_single_letter(self):
        expected_output = "A"
        morse = ".-"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)

    def test_morse_decoding_single_word(self):
        expected_output = "ALIBABA"
        morse = ".- .-.. .. -... .- -... .-"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)
    def test_morse_decoding_sentence(self):
        expected_output = "ALA MA KOTA"
        morse = ".- .-.. .-   -- .-   -.-  --- - .-"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)
    def test_morse_decoding_punctuation(self):
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        expected_output = "&'@)(:, ,=!.-+\"?/"
        self.assertEqual(self.temp.decoding(morse), expected_output)
    def test_morse_decoding_numbers(self):
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        assert_that(self.temp.decoding(morse)).is_equal_to(expected_output)

    def test_morse_decoding_empty_morse(self):
        morse = ""
        assert_that(self.temp.decoding).raises(Exception).when_called_with(morse)
    def test_morse_decoding_too_many_spaces(self):
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        assert_that(self.temp.decoding).raises(Exception).when_called_with(morse)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
