import pandas as pd

def import_dataframes_by_url(url):
    tables = pd.read_html(url)

    print(f'На странице найдено таблиц: {len(tables)}\n')

    df_currency = tables[0]

    print("Содержимое таблицы 'Курсы валют к рублю':")
    print(df_currency.head())
    print("\n" + "=" * 50 + "\n")

    if len(tables) > 1:
        df_raw_materials = tables[1]
        print("Содержимое таблицы 'Цены на сырьё':")
        print(df_raw_materials.head())

def power_usage_data(file_address):
    df = pd.read_csv(file_address)

    baltic_countries = ['Latvia', 'Lithuania', 'Estonia']

    categories = [4, 12, 21]

    filtered_df = df[
        (df['country'].isin(baltic_countries)) &
        (df['category'].isin(categories)) &
        (df['year'] >= 2005) &
        (df['year'] <= 2010) &
        (df['quantity'] > 0)
        ]

    total_consumption = filtered_df['quantity'].sum()

    print(f"Суммарное потребление стран Прибалтики: {total_consumption}")

def film_with_highest_rating():
    ratings = pd.read_csv('data/pandas_dataset/task_1/ratings.csv')
    movies = pd.read_csv('data/pandas_dataset/task_1/movies.csv',
                         header=None,
                         names=['movieId', 'title', 'genres'])

    ratings_5 = ratings[ratings['rating'] == 5.0]

    if not ratings_5.empty:
        movie_counts = ratings_5['movieId'].value_counts()
        top_movie_id = movie_counts.idxmax()
        top_count = movie_counts.max()

        movie_title = movies[movies['movieId'] == top_movie_id]['title']

        if not movie_title.empty:
            title = movie_title.iloc[0]
        else:
            title = f"Фильм с ID {top_movie_id}"

        print(f"   Фильм с наибольшим количеством оценок 5.0:")
        print(f"   Название: {title}")
        print(f"   ID: {top_movie_id}")
        print(f"   Количество оценок 5.0: {top_count}")

    else:
        print("Нет оценок 5.0 в данных")

def main():
    film_with_highest_rating()
    power_usage_data('data/pandas_dataset/task_2/power.csv')
    import_dataframes_by_url('http://fortrader.org/quotes')
if __name__ == '__main__':
    main()