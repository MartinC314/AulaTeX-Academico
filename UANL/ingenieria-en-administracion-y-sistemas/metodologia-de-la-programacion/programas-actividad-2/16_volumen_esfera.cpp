#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    const double PI = acos(-1.0);
    double radio;
    cout << "VOLUMEN DE UNA ESFERA\n";
    cout << "Ingresa el radio: ";
    cin >> radio;
    if (radio <= 0) {
        cerr << "Error: el radio debe ser mayor que cero.\n";
        return 1;
    }
    double volumen = (4.0 / 3.0) * PI * pow(radio, 3.0);
    cout << fixed << setprecision(2)
         << "Volumen = " << volumen << " unidades cubicas\n";
    return 0;
}
