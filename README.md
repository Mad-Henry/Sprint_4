# qa_python
Покрытие unit-тестами:
    Метод add_new_book, положительный test_add_new_book_add_one_book
    Метод add_new_book, отрицательный test_add_new_book_not_applicable_names: 
        1. Слишком длинное название кнгиги, 
        2. Название отсутствует (''), 
        3. Нзвание повторяется

    Метод set_book_genre, положительный test_set_book_genre_set_coorect_name_and_genre
    Метод set_book_genre, отрицательный test_set_book_genre_apsent_book_or_genre:
        1. Книга отсутствует в словаре
        2. Жанр отсутствует в списке

    Метод get_book_genre, положительный test_get_book_genre_show_genre_list

    Метод get_books_genre, положительный test_get_books_genre_show_dict_w_one_book

    Метод get_books_for_children, положительный test_get_books_for_children_show_buratino

    Метод add_book_in_favorites, положительный test_add_book_in_favorites_add_to_favorite
    Метод add_book_in_favorites, отрицательный test_add_book_in_favorites_double_add_or_empty_collecttion:
        1. Повторная попытка добавить книгу в избранное.
        2. Книга отсутствует в библиотеке

    Метод delete_book_from_favorites, положительный test_delete_book_from_favorites_add_two_books_and_then_delete_one

    Метод get_list_of_favorites_books, положительный test_get_list_of_favorites_books_add_one_book_to_favorites



TODO:
    Отрицательный тест get_book_genre, у книги отсутствует жанр
    Отрицательный тест get_books_for_children, может с пустой билиотекой?!?!?
    Отрицательный тест delete_book_from_favorites, удалить книгу из пустой библиотеки
