#!/usr/bin/env python3


def return_evens(num_list):
    """Returns a list of even numbers from num_list"""
    evens = []  # Initialize an empty list to store the even numbers

    for num in num_list:  # Iterate over each number in num_list
        if num % 2 == 0:  # If the number is even (remainder of division by 2 is 0)
            evens.append(num)  # Add the number to the evens list

    return evens  # Return the list of even numbers


def make_exclamation(sentence_list):
    """Adds exclamation marks to the end of each sentence in sentence_list"""
    exclaimed_sentences = []

    for sentence in sentence_list:
        exclaimed_sentence = sentence + "!"
        exclaimed_sentences.append(exclaimed_sentence)

    return exclaimed_sentences
