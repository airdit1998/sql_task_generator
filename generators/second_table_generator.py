from math import ceil
from pandas import DataFrame
from generators.table_generator import TableParameterGenerator
from random import choice


class SecondTableGenerator(TableParameterGenerator):

    def __init__(self, length: int, width: int, table_index: list[int]):

        super().__init__(length=length, width=width)
        self.table_index = table_index

    def generate_table(self) -> DataFrame:
        """
        Method generate dataframe from data from random_generator by given length and width
        :return: DataFrame
        """
        self._generate_random_table_length()
        self._generate_random_table_width()
        self.table_index = self._generate_new_index()

        df = DataFrame()
        # add index
        df['index_col'] = self.table_index

        for i in range(self.length):
            df['col_' + str(i) + '_st'] = self._get_random_data()

        return df.sort_index()

    def _generate_random_table_length(self) -> None:
        """
        Method generate length for second table by coefficient
        if table length is too low, you can only raise table length
        if table length > 4, you can get table length higher or lower for then given length
        :return: int
        """
        if self.length <= 4:

            start_ = self.length
            stop_ = self.length * choice([2, 3])
            step_ = 1

        elif 4 < self.length <= 10:

            start_ = ceil(self.length * choice([x / 100 for x in range(50, 125, 25)]))
            stop_ = ceil(self.length * choice([x / 100 for x in range(100, 175, 25)]))
            step_ = 1

        else:

            start_ = ceil(self.length * choice([x / 100 for x in range(25, 125, 25)]))
            stop_ = ceil(self.length * choice([x / 100 for x in range(100, 225, 25)]))
            step_ = 1

        if start_ != stop_:  # Exclude range method exception
            self.length = choice([x for x in range(start_, stop_, step_)])

    def _generate_random_table_width(self) -> None:
        """
        Method generate width for second table by coefficient
        :return: int
        """

        start_ = ceil(self.width * choice([x / 100 for x in range(50, 125, 25)]))
        stop_ = ceil(self.width * choice([x / 100 for x in range(100, 175, 25)]))
        step_ = 1

        if start_ != stop_:  # Exclude range method exception
            self.width = choice([x for x in range(start_, stop_, step_)])

    def _get_random_data(self) -> list[any]:
        """
        Method returns some random data from random_generator by random choice of supported generator data
        :return: list[parameter]
        """

        random_data_type = choice(self.supported_list)
        random_data = [self.random_generator.get_random_data(random_data_type) for _ in range(self.length)]

        if random_data_type == 'name':
            # Need to exclude generated name for pretty dataframe
            self.supported_list.remove(random_data_type)

        return random_data

    def _generate_new_index(self) -> list[int]:
        """
        Method generate random index for hard join first table ob second table
        :return: list[int]
        """
        df_index = [choice(self.table_index) for _ in range(self.length)]

        return df_index
