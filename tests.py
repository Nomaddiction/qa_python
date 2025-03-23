import pytest
from main import BooksCollector


@pytest.mark.parametrize("book_name", ["Гарри Поттер", "Властелин Колец"])
def test_add_new_book_valid_input_added(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre()

@pytest.mark.parametrize("book_name, genre", [("Гарри Поттер", "Фантастика"), ("Оно", "Ужасы")])
def test_set_book_genre_valid_input_genre_set(book_name, genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == genre

def test_get_book_genre_no_genre_empty_string():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    assert collector.get_book_genre("Гарри Поттер") == ""

def test_get_books_with_specific_genre_valid_genre_books_listed():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert "Гарри Поттер" in collector.get_books_with_specific_genre("Фантастика")

def test_get_books_for_children_excludes_restricted_books():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    collector.add_new_book("Оно")
    collector.set_book_genre("Оно", "Ужасы")
    assert "Гарри Поттер" in collector.get_books_for_children()
    assert "Оно" not in collector.get_books_for_children()

def test_add_book_in_favorites_valid_book_added_to_favorites():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites_existing_book_removed():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.delete_book_from_favorites("Гарри Поттер")
    assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

def test_add_nonexistent_book_to_favorites_not_added():
    collector = BooksCollector()
    collector.add_book_in_favorites("Несуществующая книга")
    assert "Несуществующая книга" not in collector.get_list_of_favorites_books()
