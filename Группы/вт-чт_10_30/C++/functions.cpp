#include <iostream>
using namespace std;

// === Функции ===
// тип имя_функции(аргументы) {
//      набор действий, которые делает функция
// }
//
// имя_функции(параметры) - вызов функции

// --- 1. Информационная функция ---
// void - пустая функция (используется если ответ уходит в консоль через cout)
void sayHello() {
    cout << "Hello world, fucking nigger bitch yopta\n";
}

// --- 2. Функция с аргументами ---
// аргументы - псевдозначения, с которыми работает функция (существуют только внутри функции)
void sum(int num1, int num2) {
    cout << "Сумма " << num1 << " + " << num2 << " = " << num1 + num2 << "\n";
}

void compare(int num1, int num2) {
    if (num1 > num2) {
        cout << num1 << " больше\n";
    }
    else if (num1 < num2) {
        cout << num2 << " больше\n";
    }
    else {
        cout << "Числа равны\n";
    }
}


int main() {
    sayHello(); // вызов функции sayHello (можно вызвать сколько угодно раз)

    // примеры вызовов функций с аргументами
    sum(12, 546);
    sum(1, 6);
    sum(46, 90);

    compare(12, 76);
    compare(62, 8);
    compare(12, 8);
    compare(23, 567);


    return 0;
}