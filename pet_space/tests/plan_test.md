Будем тестировать:

В файле test_routes.py:
Главная страница доступна анонимному пользователю.
Страница отдельного тарифа доступна анонимному пользователю.
Страницы удаления и редактирования тарифа доступны автору записки и только если он обладает правами админа.
Страница удаления и редактирования новости доступны пользователям - уровня модератора и выше
При попытке перейти на страницу редактирования или удаления записки анонимный пользователь перенаправляется на страницу авторизации.
Страницы регистрации пользователей, входа в учётную запись и выхода из неё доступны анонимным пользователям.

В файле test_content.py:

Тарифы отсортированы от самого дешевого к самому дорогому. Дешевые тарифы в начале списка.
Новости отсортированы от самой новой к самой старой. Новые новости в начале списка.
Комментарии на странице отдельной новости отсортированы от новых к старым: новые в начале списка, старые — в конце.


В файле test_logic.py:
Анонимный пользователь не может отправить комментарий.
Авторизованный пользователь может отправить комментарий.
Если комментарий содержит запрещённые слова, он не будет опубликован, а форма вернёт ошибку.
Авторизованный пользователь может редактировать или удалять свои комментарии.
Авторизованный пользователь не может редактировать или удалять чужие комментарии.

Не будем тестировать:
Непосредственно регистрацию пользователей, процесс входа в учетную запись и выхода из неё.
Всё, что связано с админ-зоной проекта.
Абсолютные url-адреса; обращаться к адресам будем при помощи функции reverse('name').
Какие шаблоны используются, и насколько корректно шаблон обрабатывает полученную от Django информацию. Например, если в шаблон передается список объектов, мы будем считать, что они выводятся все, а их сортировка не меняется.
Всё то, что не попало в список «будем тестировать».