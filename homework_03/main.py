"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
import models
from jsonplaceholder_requests import get_users_data_from_url, get_posts_data_from_url


async def async_main():
    await models.create_tables()
    users, posts = await asyncio.gather(get_users_data_from_url(), get_posts_data_from_url())


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
