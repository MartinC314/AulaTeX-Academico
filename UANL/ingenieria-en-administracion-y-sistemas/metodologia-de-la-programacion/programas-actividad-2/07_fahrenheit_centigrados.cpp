#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double fahrenheit;
    cout << "CONVERSION DE FAHRENHEIT A CENTIGRADOS\n";
    cout << "Ingresa la temperatura en grados Fahrenheit: ";
    cin >> fahrenheit;
    double centigrados = (fahrenheit - 32.0) * 5.0 / 9.0;
    cout << fixed << setprecision(2)
         << fahrenheit << " F = " << centigrados << " C\n";
    return 0;
}
