#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double masa, aceleracion;
    cout << "CALCULO DE FUERZA\n";
    cout << "Ingresa la masa en kilogramos: ";
    cin >> masa;
    cout << "Ingresa la aceleracion en m/s^2: ";
    cin >> aceleracion;
    if (masa < 0) {
        cerr << "Error: la masa no puede ser negativa.\n";
        return 1;
    }
    double fuerza = masa * aceleracion;
    cout << fixed << setprecision(2)
         << "Fuerza = " << fuerza << " newtons\n";
    return 0;
}
