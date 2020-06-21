#include <bits/stdc++.h>

using namespace std;

int main() {
    long long int x, y, input, n;
    cin >> n;

    for (int k = 0; k < n; k++){
        x = 0, y = 1;

        cin >> input;

        if (input == 0) cout << "Fib(" << input << ") = 0\n";

        else{
            for (int i = 1; i < input; i++){
                y = y + x;
                x = y - x;
            }
            cout << "Fib(" << input << ") = "<< y << endl;
        }
    }

    return 0;
}
