+ test_add_new_books_valid_title_length: проверка на валидность названия книги, проверяет, что книга добавлена в список книг.

+ test_add_new_books_invalid_title_length:проверка на невалидность названия книги. Отрицательный сценарий (сценарий подразумевающий несработку правила — корректное неотнесение рассматриваемого кейса).

+ test_set_book_genre_is_set: проверка на установку жанра книги, проверяет, что жанр книги установлен.

+ test_set_book_genre_not_valid_genre: проверка на установку невалидного жанра книги. Отрицательный сценарий.

+ test_get_book_genre_for_existing_book: проверка на получение жанра книги, проверяет, что жанр книги получен.

+ test_get_books_genre_for_book_not_genre: проверка на получение жанра у книги без жанра проверяет, что у книги без жанра возвращается пустая строка.

+ test_get_books_with_specific_genre_two_books_one_genre: проверка на получение списка книг с определенным жанром проверяет, что список книг с определенным жанром состоит из двух книг.

+ test_get_books_genre_with_book_return_books_genre: возвращает список с книгами и жанром.

+ test_get_books_for_children_with_age_rating: проверяем что книги с возрастным рейтингом не попадут в список детских книг.

+ test_add_book_in_favorites_add_one_book: добавляем в список избранного одну книгу.

+ test_delete_book_from_favorites_deletes_book_successfully: успешное удаление книги из избранного.

+ test_get_list_of_favorites_books_some_books:  в список избранного добавлено несколько книг.