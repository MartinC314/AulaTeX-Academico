#include <iostream>
#include <string>
using namespace std;

int main() {
    string nombre;
    int semestre;
    cout << "DATOS DEL ESTUDIANTE\n";
    cout << "Ingresa tu nombre completo: ";
    getline(cin, nombre);
    cout << "Ingresa el semestre que cursaras: ";
    cin >> semestre;
    if (nombre.empty() || semestre <= 0) {
        cerr << "Error: proporciona un nombre y un semestre valido.\n";
        return 1;
    }
    cout << "Nombre: " << nombre << '\n'
         << "Semestre a cursar: " << semestre << '\n';
    return 0;
}
