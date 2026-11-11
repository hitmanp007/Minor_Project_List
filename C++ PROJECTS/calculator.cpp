
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <iomanip>
#include <limits>

using namespace std;

// Read and validate numerical input
double getNumber(string message) {
    double number;
    string input;

    while (true) {
        cout << message;
        getline(cin, input);

        stringstream ss(input);

        if (ss >> number) {
            ss >> ws;

            if (ss.eof() && isfinite(number)) {
                return number;
            }
        }

        cout << "Invalid input! Please enter a valid number.\n";
    }
}

// Display calculator menu
void showMenu() {
    cout << "\n";
    cout << "====================================\n";
    cout << "         SMART CALCULATOR\n";
    cout << "====================================\n";
    cout << " 1. Addition (+)\n";
    cout << " 2. Subtraction (-)\n";
    cout << " 3. Multiplication (*)\n";
    cout << " 4. Division (/)\n";
    cout << " 5. Modulo (%)\n";
    cout << " 6. Power (x^y)\n";
    cout << " 7. Square Root\n";
    cout << " 8. Percentage\n";
    cout << " 9. Average of Two Numbers\n";
    cout << "10. Clear Screen\n";
    cout << " 0. Exit\n";
    cout << "====================================\n";
}

// Print result safely
void showResult(double result) {
    if (!isfinite(result)) {
        cout << "Error: Result is outside the supported range.\n";
        return;
    }

    cout << "\nResult: "
         << setprecision(12) << result << "\n";
}

// Main function
int main() {

    int choice;

    cout << fixed;

    cout << "Welcome to Smart Calculator!\n";

    while (true) {

        showMenu();

        string input;
        cout << "Enter your choice: ";
        getline(cin, input);

        stringstream ss(input);

        if (!(ss >> choice) || (ss >> ws, !ss.eof())) {
            cout << "Invalid choice! Enter a menu number.\n";
            continue;
        }

        if (choice == 0) {
            cout << "\nThank you for using Smart Calculator!\n";
            break;
        }

        if (choice == 10) {
            cout << "\nCalculator menu refreshed.\n";
            continue;
        }

        if (choice < 1 || choice > 9) {
            cout << "Invalid choice! Select between 0 and 10.\n";
            continue;
        }

        double num1, num2, result = 0;

        switch (choice) {

            case 1:
                num1 = getNumber("Enter first number: ");
                num2 = getNumber("Enter second number: ");

                result = num1 + num2;
                showResult(result);
                break;

            case 2:
                num1 = getNumber("Enter first number: ");
                num2 = getNumber("Enter second number: ");

                result = num1 - num2;
                showResult(result);
                break;

            case 3:
                num1 = getNumber("Enter first number: ");
                num2 = getNumber("Enter second number: ");

                result = num1 * num2;
                showResult(result);
                break;

            case 4:
                num1 = getNumber("Enter numerator: ");
                num2 = getNumber("Enter denominator: ");

                if (num2 == 0) {
                    cout << "Error: Division by zero is not allowed.\n";
                } else {
                    result = num1 / num2;
                    showResult(result);
                }
                break;

            case 5:
                num1 = getNumber("Enter first number: ");
                num2 = getNumber("Enter second number: ");

                if (num2 == 0) {
                    cout << "Error: Modulo by zero is not allowed.\n";
                } else {
                    result = fmod(num1, num2);
                    showResult(result);
                }
                break;

            case 6:
                num1 = getNumber("Enter base: ");
                num2 = getNumber("Enter exponent: ");

                result = pow(num1, num2);

                showResult(result);
                break;

            case 7:
                num1 = getNumber("Enter number: ");

                if (num1 < 0) {
                    cout << "Error: Cannot calculate real square root of a negative number.\n";
                } else {
                    result = sqrt(num1);
                    showResult(result);
                }
                break;

            case 8:
                num1 = getNumber("Enter total value: ");
                num2 = getNumber("Enter percentage: ");

                result = (num1 * num2) / 100.0;
                showResult(result);
                break;

            case 9:
                num1 = getNumber("Enter first number: ");
                num2 = getNumber("Enter second number: ");

                result = (num1 + num2) / 2.0;
                showResult(result);
                break;
        }

        cout << "\nPress Enter to continue...";
        getline(cin, input);
    }

    return 0;
}
