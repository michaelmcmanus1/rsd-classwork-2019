"""Computation of weighted average of squares."""


def average_of_squares(list_of_numbers, list_of_weights=None):
    """
    Return the weighted average of a list of values.
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.

    Example:
    -------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length
    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """
    Convert a list of strings into numbers, ignoring whitespace.

    Example:
    -------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]
    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]



from argparse import ArgumentParser
import numpy as np

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("numbers", help="user input for selected numbers file", type=str)
    parser.add_argument("--weights", help="user input for selected weights file", type=str)

    args = parser.parse_args()


    # TODO Can we make this optional, so that we don't need a weights file?
    if args.weights:
        with open(args.weights, "r") as weights_file:
            weight_strings = weights_file.readlines()
        numbers = convert_numbers(numbers_strings)
        weights = convert_numbers(weight_strings)
        # TODO Can we add the option of computing the square root of this result?
        result = average_of_squares(numbers, weights)
        # TODO Can we write the result in a file instead of printing it?
        print(result)


    #no weights file specified
    else:
        with open(args.numbers, "r") as numbers_file:
            numbers_strings = numbers_file.readlines()

        numbers = convert_numbers(numbers_strings)

        #if no weights file specified have all weights equal to 1
        weights = np.ones(len(numbers))

        result = average_of_squares(numbers, weights)
        result_sqrt = np.sqrt(average_of_squares(numbers, weights))

        #open file to write results to
        resultFile = open("resultFile_noWeights.txt", 'w')

        resultFile.write("%s\t" % "Original")
        resultFile.write("%s\n" % "Squre-root of Result")

        #write original result
        print(result, "Original Result")
        resultFile.write("%s\t\t" % result)

        #write squre rooted result
        print(result_sqrt, "Square-root of result")
        resultFile.write("%s\n" % result_sqrt)

