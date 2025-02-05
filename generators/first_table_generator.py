from random import choice
from pandas import DataFrame
from generators.table_generator import TableParameterGenerator


class FirstTableGenerator(TableParameterGenerator):

    def __init__(self, length: int, width: int, table_index: list[int]):

        super().__init__(length=length, width=width)
        self.table_index = table_index

    def generate_table(self):
        """
        Generate random dataset for given length and width
        """
        df = DataFrame()
        #add index
        df['index_col'] = self.table_index

        for i in range(self.length):
            df['col_' + str(i) + '_ft'] = self._get_random_data()

        # Empty string for merging dataframes
        df['ms'] = ''

        return df

    def _get_random_data(self):
        """
        :TODO add description
        :return:
        """

        random_data_type = choice(self.supported_list)
        random_data = [self.random_generator.get_random_data(random_data_type) for _ in range(self.length)]

        if random_data_type == 'name':
            # Need to exclude generated name for pretty dataframe
            self.supported_list.remove(random_data_type)

        return random_data
