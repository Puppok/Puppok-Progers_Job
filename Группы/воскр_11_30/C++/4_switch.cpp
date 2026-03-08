#include <iostream>
using namespace std;

int main() {
    // === Оператор switch ===
    // switch (значение) {
    //      case вариант_1:
    //          действия, выполнятся если значение совпадет с вариант_1
    //          break;
    //      case вариант_2:
    //          действия, выполнятся если значение совпадет с вариант_2
    //          break;
    //      case вариант_3:
    //          действия, выполнятся если значение совпадет с вариант_3
    //          break;
    //      case вариант_4:
    //          действия, выполнятся если значение совпадет с вариант_4
    //          break;
    //      default:
    //          действия, выполнятся если значение не совпало ни с одним вариантом
    //          break;
    // }

    // Задача про транспорт
    int vehicle;

    cout << "Выберите тип транспорта:\n";
    cout << "1 - Автобус\n";
    cout << "2 - Троллейбус\n";
    cout << "3 - Метро\n";
    cout << "4 - Трамвай\n";
    cin >> vehicle;

    switch (vehicle) {
        case 1:
            cout << "На автобусе проезд стоит 40р\n";
            break;
        case 2:
            cout << "На троллейбусе проезд стоит 50р\n";
            break;
        case 3:
            cout << "На метро проезд стоит 70р\n";
            break;
        case 4:
            cout << "На трамвае проезд стоит 35р\n";
            break;
        default:
            cout << "Неизвестный тип транспорта\n";
            break;
    }

    float a, b;
    char oper;

    cin >> a >> b >> oper;

    switch (oper) {
        case '+':
            cout << a << " + " << b << " = " << a + b << '\n';
            break;
        case '-':
            cout << a << " - " << b << " = " << a - b << '\n';
            break;
        case '*':
            cout << a << " * " << b << " = " << a * b << '\n';
            break;
        case '/':
            if (b == 0) {
                cout << "На ноль делить нельзя\n";
            }
            else {
                cout << a << " / " << b << " = " << a / b << '\n';
            }
            break;
        default:
            cout << "Неизвестный символ\n";
            break;
    }

    return 0;
}