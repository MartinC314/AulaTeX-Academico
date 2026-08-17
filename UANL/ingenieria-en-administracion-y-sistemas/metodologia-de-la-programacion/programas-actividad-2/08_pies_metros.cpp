#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double METROS_POR_PIE = 0.3048;
    double pies;
    cout << "CONVERSION DE PIES A METROS\n";
    cout << "Ingresa la longitud en pies: ";
    cin >> pies;
    if (pies < 0) {
        cerr << "Error: la longitud no puede ser negativa.\n";
        return 1;
    }
    cout << fixed << setprecision(4)
         << pies << " pies = " << pies * METROS_POR_PIE << " metros\n";
    return 0;
}
