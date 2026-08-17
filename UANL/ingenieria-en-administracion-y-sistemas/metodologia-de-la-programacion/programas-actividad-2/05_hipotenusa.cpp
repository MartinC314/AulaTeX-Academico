#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double catetoA, catetoB;
    cout << "HIPOTENUSA DE UN TRIANGULO RECTANGULO\n";
    cout << "Ingresa el primer cateto: ";
    cin >> catetoA;
    cout << "Ingresa el segundo cateto: ";
    cin >> catetoB;
    if (catetoA <= 0 || catetoB <= 0) {
        cerr << "Error: los catetos deben ser mayores que cero.\n";
        return 1;
    }
    double hipotenusa = sqrt(pow(catetoA, 2.0) + pow(catetoB, 2.0));
    cout << fixed << setprecision(2)
         << "Hipotenusa = " << hipotenusa << '\n';
    return 0;
}
