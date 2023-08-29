#include <bits/stdc++.h>
using namespace std;
 
int main() {
    std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    while(t--){
        int num_exams;
        int current_mark;
        int sum_mark = 0;
        bool scholarship_given = true;
 
        cin >> num_exams;
        for(int i = 0; i < num_exams; i++) {
            cin >> current_mark;
            scholarship_given = scholarship_given && (current_mark > 3);
            sum_mark += current_mark;
        }
 
        if(!scholarship_given)
            cout << "No"<<endl;
        else if (sum_mark / num_exams == 5)
            cout << "Personal"<<endl;
        else if ((float)(sum_mark) / num_exams >= 4.5)
            cout << "High"<<endl;
        else
            cout << "Common"<<endl;
    } 
    return 0;
}
