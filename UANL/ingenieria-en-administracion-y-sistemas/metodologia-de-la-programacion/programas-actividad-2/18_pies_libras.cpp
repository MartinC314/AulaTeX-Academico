#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double METROS_POR_PIE = 0.3048;
    const double KILOGRAMOS_POR_LIBRA = 0.45359237;
    double pies, libras;
    cout << "CONVERSION DE LONGITUD Y PESO\n";
    cout << "Ingresa la longitud en pies: ";
    cin >> pies;
    cout << "Ingresa el peso en libras: ";
    cin >> libras;
    if (pies < 0 || libras < 0) {
        cerr << "Error: los valores no pueden ser negativos.\n";
        return 1;
    }
    cout << fixed << setprecision(4)
         << "Longitud: " << pies * METROS_POR_PIE << " metros\n"
         << "Peso: " << libras * KILOGRAMOS_POR_LIBRA << " kilogramos\n";
    return 0;
}
