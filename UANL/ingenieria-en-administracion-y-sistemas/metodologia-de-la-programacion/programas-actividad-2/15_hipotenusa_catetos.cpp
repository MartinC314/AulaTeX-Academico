#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double cateto1, cateto2;
    cout << "HIPOTENUSA A PARTIR DE LOS CATETOS\n";
    cout << "Ingresa el cateto 1: ";
    cin >> cateto1;
    cout << "Ingresa el cateto 2: ";
    cin >> cateto2;
    if (cateto1 <= 0 || cateto2 <= 0) {
        cerr << "Error: los catetos deben ser mayores que cero.\n";
        return 1;
    }
    double hipotenusa = hypot(cateto1, cateto2);
    cout << fixed << setprecision(2)
         << "Hipotenusa = " << hipotenusa << '\n';
    return 0;
}
