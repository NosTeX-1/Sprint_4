import pytest

from te4 import BooksCollector

class TestBooksCollector:
    collector = BooksCollector()

    def test_add_new_books_valid_title_length(self): # проверка на валидность названия книги
        """Проверяет, что книга добавлена в список книг"""
        collector = BooksCollector()
        name = 'Гарри Поттер и философский камень'
        collector.add_new_book(name)
        print(collector.books_genre)
        assert name in collector.books_genre

    @pytest.mark.xfail
    @pytest.mark.parametrize('name', ['', 'A'*41])
    def test_add_new_books_invalid_title_length(self, name): # проверка на невалидность названия книги
        """Проверяет, что книга не добавлена в список книг"""
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name == collector.books_genre

    def test_set_book_genre_is_set(self): # проверка на установку жанра книги
        """Проверяет, что жанр книги установлен"""
        collector = BooksCollector()
        name = 'Гарри Поттер и философский камень'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    @pytest.mark.xfail
    def test_set_book_genre_not_valid_genre(self): # проверка на установку невалидного жанра книги
        collector = BooksCollector()
        name = 'Гарри Поттер и философский камень'
        genre = 'Исторические фильмы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_get_book_genre_for_existing_book(self): # проверка на получение жанра книги
        """Проверяет, что жанр книги получен"""
        collector = BooksCollector()
        name = 'Гарри Поттер и философский камень'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_genre_for_book_not_genre(self): # проверка на получение жанра у книги без жанра
        """Проверяет, что у книги без жанра возвращается пустая строка"""
        collector = BooksCollector()
        name = 'Гарри Поттер и философский камень'
        collector.add_new_book(name)
        assert collector.get_books_genre() == {'Гарри Поттер и философский камень':''}

    def test_get_books_with_specific_genre_two_books_one_genre(self): # проверка на получение списка книг с определенным жанром
        """Проверяет, что список книг с определенным жанром состоит из двух книг"""
        collector = BooksCollector()
        list_books = ['Гарри Поттер и философский камень', 'Семь', 'Хоббит']
        for i in range(len(list_books)):
            collector.add_new_book(list_books[i])
        collector.set_book_genre(list_books[0], 'Фантастика')
        collector.set_book_genre(list_books[1], 'Детективы')
        collector.set_book_genre(list_books[2], 'Фантастика')
        spec_genre = collector.get_books_with_specific_genre('Фантастика')
        assert len(spec_genre) == 2


    def test_get_books_genre_with_book_return_books_genre(self): # проверка списка
        collector = BooksCollector()
        collector.books_genre['Семь'] = 'Детективы'
        collector.books_genre['Хоббит'] = 'Фантастика'

        result = collector.get_books_genre()

        assert result == {'Семь': 'Детективы', 'Хоббит': 'Фантастика'}


    def test_get_books_for_children_with_age_rating(self): # детские книги
        collector = BooksCollector()
        list_books = ['Гарри Поттер', 'Астрал', 'Хоббит']
        for i in range(len(list_books)):
            collector.add_new_book(list_books[i])
        collector.set_book_genre(list_books[0], 'Фантастика')
        collector.set_book_genre(list_books[1], 'Ужасы')
        collector.set_book_genre(list_books[2], 'Фантастика')
        assert collector.get_books_for_children() == ['Гарри Поттер', 'Хоббит']

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        name = 'Белый Бим Черный хвост'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == [name]


    def test_delete_book_from_favorites_deletes_book_successfully(self):
        collector = BooksCollector()
        name = 'Белый Бим Черный хвост'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_some_books(self):
        collector = BooksCollector()
        books = ['Белый Бим Черный хвост', 'Отцы и дети', 'Война и мир', 'Мцыри', 'Мастер и Маргарита']
        for i in books:
            collector.add_new_book(i)
            collector.add_book_in_favorites(i)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == books
