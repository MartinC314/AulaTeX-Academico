#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double a, b, c;
    cout << "AREA DE UN TRIANGULO: FORMULA DE HERON\n";
    cout << "Ingresa el lado a: ";
    cin >> a;
    cout << "Ingresa el lado b: ";
    cin >> b;
    cout << "Ingresa el lado c: ";
    cin >> c;
    if (a <= 0 || b <= 0 || c <= 0 ||
        a + b <= c || a + c <= b || b + c <= a) {
        cerr << "Error: los valores no forman un triangulo valido.\n";
        return 1;
    }
    double semiperimetro = (a + b + c) / 2.0;
    double area = sqrt(semiperimetro * (semiperimetro - a)
                     * (semiperimetro - b) * (semiperimetro - c));
    cout << fixed << setprecision(2)
         << "Area = " << area << " unidades cuadradas\n";
    return 0;
}
