import uuid
from random import randint, choice, random
import string


class RandomDataGenerator:
    """
    This class generate random data by mapping
    You need co call class method get_random_data witch returns some random data by mapping:
    'string': random string with ascii symbols
    'uuid': random uuid
    'integer': random digit
    'float': random float
    'bool': random bool
    'name': random first name and last name
    """

    def __init__(self):
        self.supported_data = [
            'string',
            'uuid',
            'integer',
            'float',
            'bool',
            'name',
        ]

    def get_random_data(self, digit: str = 'string'):
        """
        Returns random class methood depends on given digit
        :param digit - digint for mapper to get random data
        """
        _method_mapping = {
            'string': self._generate_random_string(),
            'uuid': self._generate_random_uuid(),
            'integer': self._generate_random_int_digit(),
            'float': self._generate_random_float_range(),
            'bool': self._generate_random_bool(),
            'name': self._generate_random_name(),
        }

        try:
            return _method_mapping[digit]

        except KeyError:
            raise KeyError("""
            Invalid data where given for input. 
            Supporter data: 
            'string',
            'uuid',
            'integer',
            'float',
            'bool',
            'name'
            """)

        except Exception as ex:
            raise ex

    def _generate_random_uuid(self) -> uuid:
        """
        Generate random uuid in hex view
        """
        random_uuid = uuid.uuid4().hex

        return random_uuid

    def _generate_random_string(self) -> str:
        """
        Generate random string of digits and
        """
        random_digit = randint(5, 15)

        return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(random_digit))

    def _generate_random_int_digit(self) -> int:
        """
        Generate random integer digit
        """
        random_integer = randint(1, 1000000)

        return random_integer

    def _generate_random_float_range(self) -> float:
        """
        Generate random float digit
        """
        random_float = random()

        return random_float

    def _generate_random_bool(self) -> bool:
        """
        Choice random float digit
        """
        random_bool = choice([True, False])

        return random_bool

    def _generate_random_name(self) -> str:
        """
        Generate random first + last name
        """
        first_names = ['John', 'Will', 'Cade', 'Dax', 'Hue', 'Fynn', 'Gia', 'Hugo', 'Ivy', 'Jax']
        last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']

        random_name = choice(first_names) + ' ' + choice(last_names)

        return random_name
