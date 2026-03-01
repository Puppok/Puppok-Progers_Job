#include <iostream> // библиотека ввода вывода
using namespace std;

int main() { // главная функция программы

    // === 1. Переменные ===
    // тип_данных имя = значение;
    int x = 124;

    // --- Типы данных ---
    // 1. int - целые числа
    int num = 8;

    // 2. float - дроби
    float shell = 36.8194;

    // 3. double - дроби, больший диапазон чисел
    double shell_2 = 2363234.569857684;

    // 4. char - символьный тип (в одинарных кавычках)
    char symb = 'K';

    // 5. string - строка (в двойных кавычках)
    string str = "Black hole";

    // 6. bool - логический тип (true / false (да / нет))
    bool is_weekend = true;

    // Способы именования
    // 1. Camel Case
    // takeInfoFromTable

    // 2. Underscore case
    // take_info_from_table

    // cout << - вывод информации в консоль
    cout << str << endl; // вывести значение str в консоль

    // endl - перенос строки
    // '\n' - перенос строки

    cout << "Сегодня выходной? " << is_weekend << '\n';

// **Создать переменные для персонажа игры:**
// - имя _(string)_
// - уровень _(int)_
// - здоровье _(float)_
// - активен ли _(bool)_
// - класс персонажа одним символом _(char)_
//
// Вывести все данные красиво на экран

// Задача 1.
    string name = "Hero";
    int level = 80;
    float health = 53.8;
    bool is_active = false;
    char char_class = 'A';

    cout << "Character info:\n";
    cout << "--------------------\n";
    cout << "Name: " << name << '\n';
    cout << "Level: " << level << '\n';
    cout << "Health: " << health << '\n';
    cout << "Is active: " << is_active << '\n';
    cout << "Class: " << char_class << '\n';
    cout << "--------------------\n";

    return 0; // успешное завершение программы
}
