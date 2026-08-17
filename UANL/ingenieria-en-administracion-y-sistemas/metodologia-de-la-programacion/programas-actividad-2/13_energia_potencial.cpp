#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double GRAVEDAD = 9.81;
    double masa, altura;
    cout << "ENERGIA POTENCIAL GRAVITATORIA\n";
    cout << "Ingresa la masa en kilogramos: ";
    cin >> masa;
    cout << "Ingresa la altura en metros: ";
    cin >> altura;
    if (masa < 0 || altura < 0) {
        cerr << "Error: masa y altura no pueden ser negativas.\n";
        return 1;
    }
    double energia = masa * GRAVEDAD * altura;
    cout << fixed << setprecision(2)
         << "Energia potencial = " << energia << " joules\n";
    return 0;
}
