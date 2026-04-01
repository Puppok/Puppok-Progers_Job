#include <iostream>
using namespace std;

// === Функции ===
// тип имя_функции(аргументы) {
//      действия, которые выполняет функция во время вызова
// }
//
// имя_функции(параметры); - вызов функции

// --- 1. Функция информационная ---
// void - пустая функция, указывается когда результат функции уходит в консоль
void sayHello() {
    cout << "Hello dude, fucking nigger suka bitch yopta bombastik\n";
}

// --- 2. Функция с аргументами ---
// пример - функция суммы двух чисел
void sum(int num1, int num2) {
    cout << "Сумма " << num1 << " + " << num2 << " = " << num1 + num2 << '\n';
}

// пример - функция сравнения двух чисел
void compare(int num1, int num2) {
    if (num1 > num2) {
        cout << num1 << " больше\n";
    }
    else if (num2 > num1) {
        cout << num2 << " больше\n";
    }
    else {
        cout << "Числа равны\n";
    }
}


int main() {
    sayHello(); // вызов функции

    // Примеры работы функций с аргументами
    sum(23, 70); // сумма двух чисел
    sum(345, 8);
    sum(796, 38);

    compare(12, 7); // сравнение двух чисел
    compare(176, 325);
    compare(9, 9);


    return 0;
}