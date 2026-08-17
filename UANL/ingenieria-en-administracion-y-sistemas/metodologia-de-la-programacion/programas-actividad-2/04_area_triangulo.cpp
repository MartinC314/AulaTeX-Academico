#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double base, altura;
    cout << "AREA DE UN TRIANGULO\n";
    cout << "Ingresa la base: ";
    cin >> base;
    cout << "Ingresa la altura: ";
    cin >> altura;
    if (base <= 0 || altura <= 0) {
        cerr << "Error: base y altura deben ser mayores que cero.\n";
        return 1;
    }
    double area = base * altura / 2.0;
    cout << fixed << setprecision(2)
         << "Area = " << area << " unidades cuadradas\n";
    return 0;
}
