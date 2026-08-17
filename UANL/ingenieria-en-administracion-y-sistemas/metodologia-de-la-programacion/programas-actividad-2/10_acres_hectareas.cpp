#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double METROS_CUADRADOS_POR_ACRE = 4047.0;
    const double METROS_CUADRADOS_POR_HECTAREA = 10000.0;
    double acres;
    cout << "CONVERSION DE ACRES A HECTAREAS\n";
    cout << "Ingresa la extension en acres: ";
    cin >> acres;
    if (acres < 0) {
        cerr << "Error: la extension no puede ser negativa.\n";
        return 1;
    }
    double hectareas = acres * METROS_CUADRADOS_POR_ACRE
                     / METROS_CUADRADOS_POR_HECTAREA;
    cout << fixed << setprecision(4)
         << acres << " acres = " << hectareas << " hectareas\n";
    return 0;
}
