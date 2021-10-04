#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Список маршрутов.
routes = []


def get_route():
    """
    Запросить данные о маршруте.
    """
    destination = input("Пункт назначения? ")
    number = input("Номер поезда? ")
    time = input("Время отправления?(формат чч:мм) ")

    return {
        'destination': destination,
        'number': number,
        'time': time
    }


def display_routes(way):
    """
    Отобразить список маршрутов.
    """
    if way:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 4,
            '-' * 20
        )
        print(line)
        print(
            '| {:^30} | {:^4} | {:^20} |'.format(
                "Пункт назначения",
                "№",
                "Время"
            )
        )
        print(line)

        for route in way:
            print(
                '| {:<30} | {:>4} | {:<20} |'.format(
                    route.get('destination', ''),
                    route.get('number', ''),
                    route.get('time', '')
                )
            )
        print(line)

    else:
        print("Маршруты не найдены")


def select_routes(way, period):
    """
    Выбрать маршруты после заданного времени.
    """
    result = []

    for route in way:
        time_route = tuple(route.get('time').split(':'))
        if period < time_route:
            result.append(route)

    # Возвратить список выбранных маршрутов.
    return result


def main():
    """
    Главная функция программы.
    """

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о маршруте.
            route = get_route()

            # Добавить словарь в список.
            routes.append(route)
            # Отсортировать список в случае необходимости.
            if len(routes) > 1:
                routes.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            # Отобразить все маршруты.
            display_routes(routes)

        elif command == 'select':
            time_select = tuple(input("Выберите время отправления"
                                      "(формат чч:мм): ").split(':'))
            selected = select_routes(routes, time_select)
            # Отобразить выбранные маршруты.
            display_routes(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select - нати маршруты по времени")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
