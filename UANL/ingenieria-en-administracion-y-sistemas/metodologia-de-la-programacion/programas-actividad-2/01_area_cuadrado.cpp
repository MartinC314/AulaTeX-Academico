#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double lado;
    cout << "AREA DE UN CUADRADO\n";
    cout << "Ingresa la medida del lado: ";
    cin >> lado;
    if (lado <= 0) {
        cerr << "Error: el lado debe ser mayor que cero.\n";
        return 1;
    }
    cout << fixed << setprecision(2)
         << "Area = " << lado * lado << " unidades cuadradas\n";
    return 0;
}
