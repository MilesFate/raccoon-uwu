#include<iostream>
using namespace std;

// this is c+++ version of def
// these are functions
void raccoon(){
    string one = " |~-~-~-~-~-~-~|\n"; // pattern one
    string two = " |-~-~-~-~-~-~-|\n"; // pattern two

    cout<<" Cheese Grater\n";
    cout<<" _______________\n";
    cout<<one; 
    cout<<two; 
    cout<<one;
    cout<<two;
    cout<<one;
    cout<<two;
    cout<<" ^~^~^~^~^~^~^~^\n ";
    cout<<"for a raccoon boi\n";
    return ;
}

void adeptus(){
    cout<<"From the moment I understood the weakness of my flesh,\n";
    cout<<"it disgusted me.\n";
    cout<<"craved the strength and certainty of steel.\n";
    cout<<"I aspired to the purity of the Blessed Machine.\n";
    cout<<"Your kind cling to your flesh, as if it will not decay and fail you.\n";
    cout<<"One day the crude biomass that you call a temple will wither,\n";
    cout<<"and you will beg my kind to save you.\n";
    cout<<"But I am already saved, for the Machine is immortal...\n";
    cout<<"...even in death I serve the Omnissiah.\n";
    return;
}

int main(){
    string input;
    cout<<"raccoon or adeptus\n";
    cin>>input;
    if (input == "raccoon") {
        raccoon();
    } else if (input == "adeptus") {
        adeptus();
    }else{
        cout<<"invalid input\n";
    }
}

