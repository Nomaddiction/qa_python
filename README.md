<h1>Описание тестов для BooksCollector</h1>

<h3>В данном проекте реализованы тесты для класса BooksCollector. Они проверяют основные методы, обеспечивая корректную работу с книгами, жанрами и избранными книгами.</h3>

Реализованные тесты:

`test_add_new_book_valid_input_added` — проверяет, что новая книга добавляется в коллекцию.

`test_set_book_genre_valid_input_genre_set` — проверяет, что книге можно присвоить жанр.

`test_get_book_genre_no_genre_empty_string` — проверяет, что у новой книги жанр отсутствует по умолчанию.

`test_get_books_with_specific_genre_valid_genre_books_listed` — проверяет, что можно получить список книг определённого жанра.

`test_get_books_for_children_excludes_restricted_books` — проверяет, что книги с возрастными ограничениями не попадают в список детских книг.

`test_add_book_in_favorites_valid_book_added_to_favorites` — проверяет, что книгу можно добавить в избранное.

`test_delete_book_from_favorites_existing_book_removed` — проверяет, что книгу можно удалить из избранного.

`test_add_nonexistent_book_to_favorites_not_added` — проверяет, что нельзя добавить в избранное книгу, которой нет в коллекции.

<h3>Запуск тестов</h3>

Чтобы запустить тесты, выполните команду:

`pytest -v tests.py`

Флаг -v включает подробный вывод результатов тестирования.

<h4>Требования</h4>

 - Python 3.x
 - pytest

