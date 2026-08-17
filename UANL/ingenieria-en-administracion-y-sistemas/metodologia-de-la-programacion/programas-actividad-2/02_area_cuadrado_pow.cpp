#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double lado;
    cout << "AREA DE UN CUADRADO CON POW\n";
    cout << "Ingresa la medida del lado: ";
    cin >> lado;
    if (lado <= 0) {
        cerr << "Error: el lado debe ser mayor que cero.\n";
        return 1;
    }
    double area = pow(lado, 2.0);
    cout << fixed << setprecision(2)
         << "Area = " << area << " unidades cuadradas\n";
    return 0;
}
