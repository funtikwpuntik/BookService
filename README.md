Для запуска (В IDE PyCharm) требуется в терминале перейти в категорию "app", далее запустить фласк командой "flask --app bookstore --debug run".
После запуска сервиса, можно проверить комманды:
Create:
  POST;  http://127.0.0.1:5000/books/; json = {"title":"thebook", "description": "a book", "publish_year": 2023, "pages_count": 100, "created_at": "2023-01-01"};
Read:
  GET; http://127.0.0.1:5000/books/;
Update:
  PATCH;  http://127.0.0.1:5000/books/1; {"title":"thebook1", "description": "a book 1", "publish_year": 2021, "pages_count": 101};
Delete:
  DEL;  http://127.0.0.1:5000/books/1;



При обновлении записи или ее удалении указывается id книги, к которой будет применена данная операция.
