import pandas as pd
from similarities.individual_similarities import similar_words, calculate_levenshtein_ratio, difflib_ratio


def combine_similarities(compared_brand, series_of_brands):
    """Returns a dataframe where similar words > 0 and ratios > .5"""

    combined_similarities = pd.DataFrame(
        columns=['compared_brand', 'other_brand', 'similar_words', 'levenshtein_ratio', 'difflib_ratio'])

    similar_words_df = similar_words(compared_brand, series_of_brands)
    levenshtein_ratio_df = calculate_levenshtein_ratio(compared_brand, series_of_brands)
    difflib_ratio_df = difflib_ratio(compared_brand, series_of_brands)

    combined_similarities = pd.merge(similar_words_df, levenshtein_ratio_df, on=['compared_brand', 'other_brand'],
                                     how='outer')
    combined_similarities = pd.merge(combined_similarities, difflib_ratio_df, on=['compared_brand', 'other_brand'],
                                     how='outer')

    return combined_similarities