## Описание
Проект по генерации вопросов по тексту. Генератор основан на модели `t5`. Модель обучена на данных `SberQUAD`.
## Требования
Python 3.11+

## Установка
```console
$ pip install -r requirements.txt
```
## Запуск
В директории `app` :
```console
$  uvicorn main:app --reload
```
## Попробовать
После запуска сервера станет доступна страница `openapi` по адресу `http://localhost:port/`. На данной странице доступен запрос серверу, с помощью которого можно протестировать генерацию вопроса по тексту. Для этого нажмите кнопку `Try it out`, введите в поле `text` контекст, по которому необходимо сгенерировать вопрос, и нажмите кнопку `Execute`. В ответ на данный запрос получите сгенерированный вопрос.