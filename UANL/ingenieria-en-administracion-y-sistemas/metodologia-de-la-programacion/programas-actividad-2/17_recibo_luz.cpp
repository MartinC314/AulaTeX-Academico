#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    string nombre;
    double consumo, tarifa;
    cout << "RECIBO DE ENERGIA ELECTRICA\n";
    cout << "Ingresa el nombre del cliente: ";
    getline(cin, nombre);
    cout << "Ingresa el consumo en kilowatts: ";
    cin >> consumo;
    cout << "Ingresa la tarifa por kilowatt: $";
    cin >> tarifa;
    if (nombre.empty() || consumo < 0 || tarifa < 0) {
        cerr << "Error: revisa los datos proporcionados.\n";
        return 1;
    }
    double pago = consumo * tarifa;
    cout << "\n--- RECIBO ---\n"
         << "Cliente: " << nombre << '\n'
         << fixed << setprecision(2)
         << "Pago: $" << pago << '\n';
    return 0;
}
