# Функции test_books_genre_get_value_books_genre,
# test_favorites_get_value_favorites, test_genre_get_value_genre,
# test_genre_age_rating_get_value_genre_age_rating проверяет метод _init_ и его значения

# test_add_new_book_input_valid_name_book_new_book_added_to_the_books_genre
# проверяет метод добавления книги в словарь books_genre и получение словаря books_genre

# test_add_new_book_input_invalid_name_book_new_book_not_added_to_the_books_genre
# проверяет невозможность добавления в словарь books_genre невалидных названий книг

# test_add_new_book_input_repeat_book_added_one_book_to_the_books_genre
# проверяет невозможность добавления одной и той-же книги

# test_set_book_genre_input_existing_genre_book_set_genre
# проверяет метод присвоения книге в словаре допустимого жанра (список допустимых жанров хранится в  genre) 

# test_set_book_genre_input_non_existent_genre_book_not_set_genere
# проверяет невозможность присвоения книге в словаре недопустимого жанра 


# test_get_books_with_specific_genre_input_valid_genre_get_books_by_genre
# проверяет вывод списка книг по существующему в  списке genre жанру

# test_get_books_with_specific_genre_input_invalid_genre_get_empty_books_by_genre
# проверяет невозможность вывода списка книг по несуществующему в  списке genre жанру

# test_get_books_for_children_input_books_all_genre_get_books_except_genre_age_rating
# проверяет, что возвращаются книги подходящие детям, исключая жанры genre_age_rating не проходящие по возрастному рейтингу

# test_add_book_in_favorites_add_books_show_books_in_favorite_list
# проверяет добавление книги в список избранных и метод получения списка избранных книг

# test_delete_book_from_favorites_books_deleted_on_favorite_list
# проверяет удаление книги из списка избранных
