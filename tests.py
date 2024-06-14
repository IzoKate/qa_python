import pytest

from main import BooksCollector


class TestBooksCollector:

    #Тестируем метод _init_ и все его значения
    def test_books_genre_get_value_books_genre(self):
        book = BooksCollector()
        assert book.books_genre == {}

    def test_favorites_get_value_favorites(self):
        book = BooksCollector()
        assert book.favorites == []

    def test_genre_get_value_genre(self):
        book = BooksCollector()
        assert book.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_get_value_genre_age_rating(self):
        book = BooksCollector()
        assert book.genre_age_rating == ['Ужасы', 'Детективы']


   #Тестируем добавление книг с валидным названием
    valid_books = ['Я','Общая теория занятости, процента и денег', 'Путешествия Гулливера']

    @pytest.mark.parametrize('book_name', valid_books)
    def test_add_new_book_input_valid_name_book_new_book_added_to_the_books_genre(self, book_name):
        book_collection = BooksCollector()
        book_collection.add_new_book(book_name)
        assert 'Общая теория занятости, процента и денег' in book_collection.get_books_genre() or 'Путешествия Гулливера' in book_collection.get_books_genre() or 'Я' in book_collection.get_books_genre()



   # Тестируем добавление книг с невалидным названием
    invalid_book = ['', 'Безобразная герцогиня Маргарита  Маульташ', 'Жизнь и мнения Тристрама Шенди джентльмена', 'Клуб любителей книг и пирогов из картофельных очистков']

    @pytest.mark.parametrize('book_name', invalid_book)
    def test_add_new_book_input_invalid_name_book_new_book_not_added_to_the_books_genre(self, book_name):
        book_collection = BooksCollector()
        book_collection.add_new_book(book_name)
        assert book_collection.get_books_genre() == {}



    #Тестируем повторное добавление книги
    double_book = ['Путешествия Гулливера', 'Путешествия Гулливера']

    @pytest.mark.parametrize('book_name', double_book)
    def test_add_new_book_input_repeat_book_added_one_book_to_the_books_genre(self, book_name):
        book_collection = BooksCollector()
        book_collection.add_new_book(book_name)
        assert book_collection.get_books_genre() == {'Путешествия Гулливера': ''}



    #1 Проверка по жанрам
    # Установим книге существующий жанр
    existing_book_genre = [
        ('Дюна', 'Фантастика'),
        ('Кладбище домашних животных', 'Ужасы'),
        ('Книга жизни', 'Мультфильмы'),
        ('Горе от ума', 'Комедии')
    ]

    @pytest.mark.parametrize('book1, genre1', existing_book_genre)
    def test_set_book_genre_input_existing_genre_book_set_genre(self, book1, genre1):
        book_collection = BooksCollector()
        book_collection.add_new_book(book1)
        book_collection.set_book_genre(book1, genre1)
        assert book_collection.get_book_genre(book1) in ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']



    #2 Проверка по жанрам
   # Установим книге несуществующий жанр
    non_existing_book_genre = [
     ('Дюна', 'Криминал'),
     ('Кладбище домашних животных', 'Поэзия')
    ]
    @pytest.mark.parametrize('book2, genre2', non_existing_book_genre)
    def test_set_book_genre_input_non_existent_genre_book_not_set_genere(self,book2,genre2):
        book_collection = BooksCollector()
        book_collection.add_new_book(book2)
        book_collection.set_book_genre(book2,genre2)
        assert book_collection.get_book_genre('Дюна') == '' or book_collection.get_book_genre('Кладбище домашних животных') == ''

    # 3 Проверка по жанрам
    # Проверяем вывод списка книг по существующему в списке жанру
    @pytest.mark.parametrize('book3, genre3', existing_book_genre)
    def test_get_books_with_specific_genre_input_valid_genre_get_books_by_genre(self, book3, genre3):
        book_collection = BooksCollector()
        book_collection.add_new_book(book3)
        book_collection.set_book_genre(book3, genre3)
        assert book_collection.get_books_with_specific_genre('Фантастика') == ['Дюна'] or book_collection.get_books_with_specific_genre('Ужасы') == ['Кладбище домашних животных'] or book_collection.get_books_with_specific_genre('Мультфильмы') == ['Книга жизни'] or book_collection.get_books_with_specific_genre('Комедии') == ['Горе от ума']


    #4 Проверка по жанрам
   # Проверяем вывод списка книг по несуществующему в списке жанру

    @pytest.mark.parametrize('book4, genre4', existing_book_genre)
    def test_get_books_with_specific_genre_input_invalid_genre_get_empty_books_by_genre(self, book4, genre4):
        book_collection = BooksCollector()
        book_collection.add_new_book(book4)
        book_collection.set_book_genre(book4, genre4)
        assert book_collection.get_books_with_specific_genre('Криминал') == []



    #Проверяем что возвращаются книги подходящие детям

    collection_book_for_children = [
        ('Дюна', 'Фантастика'),
        ('Кладбище домашних животных', 'Ужасы'),
        ('Книга жизни', 'Мультфильмы'),
        ('Горе от ума', 'Комедии'),
        ('Внутри убийцы', 'Детективы')
    ]

    @pytest.mark.parametrize('book5, genre5', collection_book_for_children)
    def test_get_books_for_children_input_books_all_genre_get_books_except_genre_age_rating(self, book5, genre5):
        book_collection = BooksCollector()
        book_collection.add_new_book(book5)
        book_collection.set_book_genre(book5, genre5)
        assert book_collection.get_books_for_children() != ['Кладбище домашних животных'] or book_collection.get_books_for_children() != ['Внутри убийцы']


    #Проверяем Добавление книги в избранное
    collection_book_for_favorite = [
        ('Дюна', 'Фантастика'),
        ('Кладбище домашних животных', 'Ужасы'),
    ]
    @pytest.mark.parametrize('book6, genre6', collection_book_for_favorite)
    def test_add_book_in_favorites_add_books_show_books_in_favorite_list(self, book6, genre6):
        book_collection = BooksCollector()
        book_collection.add_new_book(book6)
        book_collection.set_book_genre(book6, genre6)
        book_collection.add_book_in_favorites(book6)
        assert book_collection.get_list_of_favorites_books() == ['Дюна'] or book_collection.get_list_of_favorites_books() == ['Кладбище домашних животных']


    #Проверяем Удаление книги из избранного

    def test_delete_book_from_favorites_books_deleted_on_favorite_list(self):
        book_collection = BooksCollector()
        book_collection.add_new_book('Дюна')
        book_collection.add_new_book('Кладбище домашних животных')
        book_collection.set_book_genre('Дюна', 'Фантастика')
        book_collection.set_book_genre('Кладбище домашних животных', 'Ужасы')
        book_collection.add_book_in_favorites('Дюна')
        book_collection.add_book_in_favorites('Кладбище домашних животных')
        book_collection.delete_book_from_favorites('Дюна')
        assert book_collection.get_list_of_favorites_books() == ['Кладбище домашних животных']


