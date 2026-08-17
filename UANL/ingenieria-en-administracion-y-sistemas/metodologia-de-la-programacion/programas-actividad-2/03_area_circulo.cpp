#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    const double PI = acos(-1.0);
    double radio;
    cout << "AREA DE UN CIRCULO\n";
    cout << "Ingresa el radio: ";
    cin >> radio;
    if (radio <= 0) {
        cerr << "Error: el radio debe ser mayor que cero.\n";
        return 1;
    }
    double area = PI * pow(radio, 2.0);
    cout << fixed << setprecision(2)
         << "Area = " << area << " unidades cuadradas\n";
    return 0;
}
