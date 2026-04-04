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

// Пример: функция подсчета суммы двух чисел
void sum(int num1, int num2) {
    cout << "Сумма " << num1 << " + " << num2 << " = " << num1 + num2 << "\n";
}

// Пример: функция сравнения двух чисел
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

// Пример: функция вывода в консоль четных чисел от 1 до finish
void showEven(int finish) {
    for (int i = 1; i <= finish; i++) { // перебираем все числа от 1 до finish
        if (i % 2 == 0) {               // если число в остатке от деления на 2 даст 0, значит число четное
            cout << i << " ";           // вывод данного числа в консоль
        }
    }
    cout << '\n';
}

// --- 3. Возврат значения ---
// Пример: умножение двух чисел
int multi(int num1, int num2) {
    return num1 * num2;
}

// Большой пример: калькулятор
int calcSum(int num1, int num2) { // сумма
    return num1 + num2;
}

int calcSub(int num1, int num2) { // разность
    return num1 - num2;
}

int calcmMulti(int num1, int num2) { // умножение
    return num1 * num2;
}

float calcDiv(float num1, float num2) { // деление
    return num1 / num2;
}

void calculator(int x, int y, char oper) {
    switch (oper) {
        case '+':
            cout << calcSum(x, y) << '\n';
            break;
        case '-':
            cout << calcSub(x, y) << '\n';
            break;
        case '*':
            cout << calcmMulti(x, y) << '\n';
            break;
        case '/':
            cout << calcDiv(float(x), float(y)) << '\n';
            break;
        default:
            cout << "Неизвестный оператор\n";
    }
}



int main() {
    sayHello(); // вызов функции sayHello (можно вызвать сколько угодно раз)

    // примеры вызовов функций с аргументами
    sum(12, 546); // сумма чисел
    sum(1, 6);
    sum(46, 90);

    compare(12, 76); // сравнение чисел
    compare(62, 8);
    compare(12, 8);
    compare(23, 567);

    showEven(7); // список четных чисел
    showEven(9);
    showEven(25);

    cout << multi(2, 6) << '\n';
    int result = multi(2, 6);
    cout << result << '\n';

    sum(10, result);

    calculator(12, 53, '*');
    calculator(12, 53, '+');
    calculator(12, 53, '-');
    calculator(12, 53, '/');



    return 0;
}