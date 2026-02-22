#include <iostream> // библиотека ввода вывода
using namespace std; // использование стандартных команд c++

int main() { // главная функция программы
    // === 1. Переменные ===
    // тип имя = значение;
    int number = 124; // числовая переменная
    cout << number << '\n'; // cout << - команда вывода в консоль

    // --- Типы данных ---
    // int - целые числа
    int num = 12;

    // float - дроби
    float shell = 34.167;

    // double - дроби (большего размера)
    double shell_2 = 12415.645;

    // char - символы
    char symb = 'H';

    // string - строки
    string str = "Hello picun!@#$%^& Bugaga";

    // bool - логический тип (true / false (да / нет))
    bool is_open = false;


    // Способы именования переменных
    // camel case - bigDataFromTable
    // underscore - big_data_from_table


    // Задача 1.
    string name = "Hero";
    int level = 80;
    float health = 95.5;
    bool is_active = false;
    char char_class = 'W';

    cout << "Game character:\n";
    cout << "-----------------\n";
    cout << "Name: " << name << "\n";
    cout << "Level: " << level << "\n";
    cout << "Health: " << health << "\n";
    cout << "IsActive: " << is_active << "\n";
    cout << "Char class: " << char_class << "\n";
    cout << "-----------------\n";

    return 0; // команда успешного завершения программы
}

// **Создать переменные для описания товара в магазине:**
// - название
// - цена
// - количество на складе
// - есть ли в наличии
//
// Вывести все на экран


// Создать переменную `score` со значением `0`,
// затем присвоить ей значение `150`,
// затем `300`
// Вывести значение после каждого изменения
