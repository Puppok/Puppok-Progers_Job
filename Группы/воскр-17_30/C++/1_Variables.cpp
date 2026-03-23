#include <iostream> // библиотека ввода вывода
using namespace std; // используем набор стандартных команд

int main() { // главная программа
    // === Переменные ===
    // тип_данных имя = значение;
    int number = 12;

    // --- Типы данных ---
    // int - целые числа
    int celoe = 658;

    // float - дробные числа
    float drob = 2.5;

    // bool - логический тип (true / false)
    bool isAlive = true;

    // char - символьный тип
    char letter = 'f';

    // string - строковый тип
    string word = "Hello World!";

    // --- Вывод в консоль ---
    // cout << значение;
    // \n - перенос строки (либо команда endl)
    cout << "Пончик\n";

    cout << "Пример целого числа: " << number << '\n';

    return 0; // успешное завершение программы
}