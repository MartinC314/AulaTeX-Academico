#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double masa, velocidad;
    cout << "ENERGIA CINETICA\n";
    cout << "Ingresa la masa en kilogramos: ";
    cin >> masa;
    cout << "Ingresa la velocidad en m/s: ";
    cin >> velocidad;
    if (masa < 0) {
        cerr << "Error: la masa no puede ser negativa.\n";
        return 1;
    }
    double energia = masa * pow(velocidad, 2.0) / 2.0;
    cout << fixed << setprecision(2)
         << "Energia cinetica = " << energia << " joules\n";
    return 0;
}
