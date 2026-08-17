#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double KILOGRAMOS_POR_LIBRA = 0.45359237;
    double libras;
    cout << "CONVERSION DE LIBRAS A KILOGRAMOS\n";
    cout << "Ingresa el peso en libras: ";
    cin >> libras;
    if (libras < 0) {
        cerr << "Error: el peso no puede ser negativo.\n";
        return 1;
    }
    cout << fixed << setprecision(4)
         << libras << " lb = " << libras * KILOGRAMOS_POR_LIBRA << " kg\n";
    return 0;
}
