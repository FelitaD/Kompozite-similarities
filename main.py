import pandas as pd


from similarities.combined_similarities import combine_similarities


def load_data():
    brands_1_path = "data/brands_list_1_short.csv"
    brands_2_path = "data/brands_list_2_short.csv"

    brands_1 = pd.read_csv(brands_1_path, delimiter=';', header=None)[0]
    brands_2 = pd.read_csv(brands_2_path, delimiter=';', header=None)[0]

    return brands_1, brands_2


def all_brands_similarities(brands_1, brands_2):
    concatenated_df = pd.DataFrame()

    for i in range(len(brands_1)):
        brand_df = combine_similarities(brands_1[i], brands_2)

        concatenated_df = pd.concat([concatenated_df, brand_df], ignore_index=True)

    return concatenated_df


def export_to_csv(df):
    df.to_csv('brands_similarities.csv', index=False)


if __name__ == '__main__':
    brands_1, brands_2 = load_data()
    all_brands_df = all_brands_similarities(brands_1, brands_2)
    print('all_brands_df:\n', all_brands_df)
    export_to_csv(all_brands_df)

