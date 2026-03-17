#include <iostream>
using namespace std;

int main() {
    // === Оператор switch ===
    // switch (значение) {
    //      case вариант_1:
    //          действия, сработают если значение и вариант_1 совпали
    //          break;
    //      case вариант_2:
    //          действия, сработают если значение и вариант_2 совпали
    //          break;
    //      case вариант_3:
    //          действия, сработают если значение и вариант_3 совпали
    //          break;
    //      case вариант_4:
    //          действия, сработают если значение и вариант_4 совпали
    //          break;
    //      default:
    //          действия, сработают если значение не совпало ни с одним вариантом
    //          break;
    //  }

    float num1, num2;
    char operation;

    cin >> num1 >> num2 >> operation;

    switch (operation) {
        case '+':
            cout << "Сумма: " << num1 << " + " << num2 << " = " << num1 + num2 << "\n";
            break;
        case '-':
            cout << "Разность: " << num1 << " - " << num2 << " = " << num1 - num2 << "\n";
            break;
        case '*':
            cout << "Произведение: " << num1 << " * " << num2 << " = " << num1 * num2 << "\n";
            break;
        case '/':
            cout << "Частное: " << num1 << " / " << num2 << " = " << num1 / num2 << "\n";
            break;
        default:
            cout << "Непонятный символ, нужно вводить (+, -, *, /)\n";
    }

    return 0;
}
