#include <iostream>
using namespace std;

int main() {
    // === Оператор switch ===
    // switch (значение) {
    //      case вариант_1:
    //          действия, работают если значение и вариант_1 совпали
    //          break;
    //      case вариант_2:
    //          действия, работают если значение и вариант_2 совпали
    //          break;
    //      case вариант_3:
    //          действия, работают если значение и вариант_3 совпали
    //          break;
    //      default:
    //          действия, работают если значение не совпало ни с чем
    //          break;
    // }

    // Пример - калькулятор
    float num1, num2; // два числа
    char operation; // операция (+, -, *, /)

    cin >> num1 >> num2 >> operation; // ввод всех значений

    switch (operation) {
        case '+':
            cout << "Сумма: " << num1 << " + " << num2 << " = " << num1 + num2 << '\n';
            break;
        case '-':
            cout << "Разность: " << num1 << " - " << num2 << " = " << num1 - num2 << '\n';
            break;
        case '*':
            cout << "Произведение: " << num1 << " * " << num2 << " = " << num1 * num2 << '\n';
            break;
        case '/':
            cout << "Частное: " << num1 << " / " << num2 << " = " << num1 / num2 << '\n';
            break;
        default:
            cout << "Неизвестная команда\n";
    }

    return 0;
}