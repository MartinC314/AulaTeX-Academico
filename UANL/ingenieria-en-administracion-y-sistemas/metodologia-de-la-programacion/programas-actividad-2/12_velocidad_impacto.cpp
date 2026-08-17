#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    const double GRAVEDAD = 9.81;
    double altura;
    cout << "VELOCIDAD FINAL DE IMPACTO EN CAIDA LIBRE\n";
    cout << "Ingresa la altura en metros: ";
    cin >> altura;
    if (altura < 0) {
        cerr << "Error: la altura no puede ser negativa.\n";
        return 1;
    }
    double velocidad = sqrt(2.0 * GRAVEDAD * altura);
    cout << fixed << setprecision(2)
         << "Velocidad final = " << velocidad << " m/s\n";
    return 0;
}
