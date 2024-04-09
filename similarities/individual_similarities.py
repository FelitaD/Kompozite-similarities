import pandas as pd
from Levenshtein import matching_blocks, editops, ratio
import difflib


def similar_words(compared_brand, series_of_brand):
    """
    Compare one word with a series and find number of similar words.

    Parameters:
    - compared_brand (string): Compared brand.
    - series_of_brand (pd.Series): Series of other brands to compare to.

    Returns:
    A sorted dataframe where there is at least one similar word.
    """
    intersections = pd.DataFrame(columns=['compared_brand', 'other_brand', 'similar_words'])

    for i in range(len(series_of_brand)):
        other_brand = series_of_brand[i]
        intersections.loc[i, 'compared_brand'] = compared_brand
        intersections.loc[i, 'other_brand'] = other_brand
        similar_words = len(set(compared_brand.split()).intersection(set(other_brand.split())))
        intersections.loc[i, 'similar_words'] = similar_words

    return intersections[intersections.similar_words > 0].sort_values(by='similar_words', ascending=False)


def calculate_levenshtein_ratio(compared_brand, series_of_brand):
    """
    Calculates ratio between a word and a series.

    Parameters:
    - compared_brand (string): Compared brand.
    - series_of_brand (pd.Series): Series of other brands to compare to.

    Returns:
    A sorted dataframe where levenshtein_ratio is superior to 0.65.
    """
    levenshtein = pd.DataFrame(columns=['compared_brand', 'other_brand', 'levenshtein_ratio'])

    for i in range(len(series_of_brand)):
        levenshtein.loc[i, 'compared_brand'] = compared_brand
        levenshtein.loc[i, 'other_brand'] = series_of_brand[i]
        levenshtein.loc[i, 'levenshtein_ratio'] = ratio(compared_brand, series_of_brand[i])

    return levenshtein[levenshtein.levenshtein_ratio > .65].sort_values(by='levenshtein_ratio', ascending=False)


def difflib_ratio(compared_brand, series_of_brand):
    difflib_df = pd.DataFrame(columns=['compared_brand', 'other_brand', 'difflib_ratio'])

    for i in range(len(series_of_brand)):
        difflib_sq_matcher = difflib.SequenceMatcher(None, compared_brand, series_of_brand[i])

        difflib_df.loc[i, 'compared_brand'] = compared_brand
        difflib_df.loc[i, 'other_brand'] = series_of_brand[i]
        difflib_df.loc[i, 'difflib_ratio'] = difflib_sq_matcher.ratio()

    return difflib_df[difflib_df.difflib_ratio > .65].sort_values(by='difflib_ratio', ascending=False)