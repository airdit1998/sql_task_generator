from pandas import concat
import string
from random import choice, randint

from generators.first_table_generator import FirstTableGenerator
from generators.second_table_generator import SecondTableGenerator


def main():
    try:
        input_length = int(input("Enter table length. Only positive integer numbers: "))

        assert input_length > 0

    except TypeError:
        raise TypeError("Mismatch type for table length. You need to enter positive value from 1 to 100")
    except AssertionError:
        raise AssertionError("You need to enter ONLY positive value")

    try:
        input_width = int(input("Enter table width. Only positive integer: "))

        assert input_width > 0

    except TypeError:
        raise TypeError("Mismatch type for table width. You need to enter positive value from 1 to 100")
    except AssertionError:
        raise AssertionError("You need to enter ONLY positive value")

    try:
        random_index = randint(1, 10000)
        table_index = [x for x in range(random_index, random_index + input_length)]

        first_table_dataframe = FirstTableGenerator(
            length=input_length,
            width=input_width,
            table_index=table_index,
        ).generate_table()

        second_table_dataframe = SecondTableGenerator(
            length=input_length,
            width=input_width,
            table_index=table_index,
        ).generate_table()

        user_df_name = input("Would you like to enter your file name? [y, n]: ")
        if user_df_name.lower() not in ['y', 'n']:
            raise ValueError("You need to write y or n")

        if user_df_name.lower() == 'y':
            custom_df_name = str(input("Enter you file name: "))
        else:
            custom_df_name = None

        exit_dataframe = concat([first_table_dataframe, second_table_dataframe], axis=1)

        if custom_df_name:
            exit_dataframe.to_excel(custom_df_name + '.xlsx', index=False)
        else:
            custom_df_name = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(10))
            exit_dataframe.to_excel(custom_df_name + '.xlsx', index=False)

    except TypeError as ex:
        raise TypeError("Mismatch type for talbe")

    except Exception as ex:
        raise ex


if __name__ == '__main__':
    main()
