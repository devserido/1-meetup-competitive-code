#include <iostream>
using namespace std;

#define u_l_l unsigned long long


u_l_l Fib(u_l_l n, u_l_l c, u_l_l b) {    
    if (n == 0)
        return 0;
    if (n == 1)
        return c;
    return Fib(n-1, c+b, c);
}

int main() {
    u_l_l T, N; 

    cin>>T;
 
    for (int i = 0; i < T; i++){
        cin>>N;
        cout << "Fib(" << N << ") = " << Fib(N, 1, 0) << endl;
    }
    
    return 0;
}