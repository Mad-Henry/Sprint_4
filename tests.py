from data import books_lst
from data import wrong_names_lst
import pytest


class TestBooksCollecto:


    def test_add_new_book_add_one_book(self, empty_collector):
        empty_collector.add_new_book(books_lst[1])
        assert len(empty_collector.get_books_genre()) == 1, f'Словарь содержит: {empty_collector.get_books_genre()}'

    @pytest.mark.parametrize('wrong_name', wrong_names_lst)
    def test_add_new_book_not_applicable_names(self, empty_collector, wrong_name):
        empty_collector.add_new_book('same name')
        empty_collector.add_new_book(wrong_name)
        assert len(empty_collector.get_books_genre()) == 1, f'Словарь содержит: {empty_collector.get_books_genre()}'


    def test_set_book_genre_set_coorect_name_and_genre(self, empty_collector):
        empty_collector.add_new_book(books_lst[1])
        empty_collector.set_book_genre(books_lst[1], 'Ужасы')
        assert empty_collector.get_book_genre(books_lst[1]) == 'Ужасы', f'Словарь содержит: {empty_collector.get_books_genre()}'

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби 2','Ужасы'],[books_lst[1],'Хоррор']])
    def test_set_book_genre_apsent_book_or_genre(self, empty_collector, name, genre):
        empty_collector.add_new_book(books_lst[1])
        empty_collector.set_book_genre(name, genre)
        assert empty_collector.get_books_genre().get(genre) == None, f'Словарь содержит: {empty_collector.get_books_genre()}'


    def test_get_book_genre_show_genre_list(self, empty_collector):
        empty_collector.add_new_book(books_lst[1])
        empty_collector.set_book_genre(books_lst[1], 'Ужасы')
        assert empty_collector.get_book_genre(books_lst[1]) == 'Ужасы', f'Словарь содержит: {empty_collector.get_books_genre()}'


    def test_get_books_genre_show_dict_w_one_book(self, empty_collector):
        empty_collector.add_new_book(books_lst[1])
        empty_collector.set_book_genre(books_lst[1], 'Ужасы')
        asert_dict = {books_lst[1]: 'Ужасы'}
        assert empty_collector.get_books_genre() == asert_dict, f'Словарь содержит: {empty_collector.get_books_genre()}'


    def test_get_books_for_children_show_buratino(self, empty_collector):
        empty_collector.add_new_book(books_lst[1])
        empty_collector.set_book_genre(books_lst[1], 'Ужасы')
        empty_collector.add_new_book(books_lst[3])
        empty_collector.set_book_genre(books_lst[3], 'Мультфильмы')
        assert empty_collector.get_books_for_children() == ['Буратино'], f'Список содержит: {empty_collector.get_books_for_children()}'


    def test_add_book_in_favorites_add_to_favorite(self, empty_collector):
        empty_collector.add_new_book(books_lst[1])
        empty_collector.add_book_in_favorites(books_lst[1])
        assert empty_collector.get_list_of_favorites_books() == [books_lst[1]], f'Список содержит: {empty_collector.get_list_of_favorites_books()}'

    @pytest.mark.parametrize('name', [books_lst[4], 'Отсутствующая книга'] )
    def test_add_book_in_favorites_double_add_or_empty_collecttion(self, empty_collector, name):
        empty_collector.add_new_book(books_lst[4])
        empty_collector.add_book_in_favorites(books_lst[4])
        empty_collector.add_book_in_favorites(name)
        assert len(empty_collector.get_list_of_favorites_books()) == 1, f'Список содержит: {empty_collector.get_list_of_favorites_books()}'


    def test_delete_book_from_favorites_add_two_books_and_then_delete_one(self, empty_collector):
        empty_collector.add_new_book(books_lst[1])
        empty_collector.add_new_book(books_lst[3])
        empty_collector.add_book_in_favorites(books_lst[1])
        empty_collector.add_book_in_favorites(books_lst[3])
        empty_collector.delete_book_from_favorites(books_lst[3])
        assert len(empty_collector.get_list_of_favorites_books()) == 1, f'Список содержит: {empty_collector.get_list_of_favorites_books()}'


    def test_get_list_of_favorites_books_add_one_book_to_favorites(self, empty_collector):
        empty_collector.add_new_book(books_lst[3])
        empty_collector.add_book_in_favorites(books_lst[3])
        assert empty_collector.get_list_of_favorites_books() == [books_lst[3]], f'Список содержит: {empty_collector.get_list_of_favorites_books()}'
