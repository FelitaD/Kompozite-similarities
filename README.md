Provides a dataframe that shows 3 different similarities:
- similar_words: number of identical words (>0)
- levenshtein_ratio: > .65
- difflib_ratio: > .65

# Usage

```commandline
python3 main.py
```

# Improvements

- Errors: add tests
- Only compares elements of one list to the others. Should compare elements of 2nd list to the 1st.
- Not time efficient
- Code repeated accross function
- Add parameter to adjust ratios treshold
