#include <iostream>
using namespace std;
int main()
{
    int tab[5][5];
    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            tab[i][j] = 0;
        }
    }
    tab[0][0]=1;
    tab[0][1]=1;
    tab[0][2]=1;
    tab[1][1]=1;
    tab[2][0]=1;
    tab[2][1]=1;
    tab[2][2]=1;
    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            cout << tab[i][j];
        }
        cout << endl;
    }
    return 0;
}
