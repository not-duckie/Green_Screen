#include<iostream>
#include<stdio.h>
using namespace std;

void naming(int a)
{ int x,y,z;
   z=a%10;
   x=(a%100)-z;
   y=(a%1000)-(x+z);
int temp=1;
 switch (y)
 {
  case 100 : cout<<"one hundred ";
  break;
  case 200 : cout<<"two hundreds ";
break;
  case 300 : cout<<"three hundreds ";
break;
  case 400 : cout<<"four hundreds ";
break;
  case 500 : cout<<"five hundreds ";
break;
  case 600 : cout<<"six hundreds ";
break;
  case 700 : cout<<"seven hundreds ";
break;
  case 800 : cout<<"eight hundreds ";
break;
  case 900 : cout<<"nine hundreds ";
  }
  switch (x)
  {
   case 10 :  temp=0;

               switch(z)
            {
              case 10: cout<<"ten ";
              break;
              case 1 : cout<<"eleven ";
              break;
              case 2 : cout<<"twelve ";
              break;
              case 3 : cout<<"thirteen ";
              break;
              case 4 : cout<<"fourteen ";
              break;
              case 5 : cout<<"fifteen ";
              break;
              case 6 : cout<<"sixteen ";
              break;
              case 7 : cout<<"seventeen ";
              break;
              case 8 : cout<<"eighteen ";
              break;
              case 9 : cout<<"nineteen ";
            }
   break;
   case 20 : cout<<"twenty ";
   break;
   case 30 : cout<<"thrity ";
   break;
   case 40 : cout<<"forty ";
   break;
   case 50 : cout<<"fifty ";
   break;
   case 60 : cout<<"sixty ";
   break;
   case 70 : cout<<"sevety ";
   break;
   case 80 : cout<<"eighty ";
   break;
   case 90 : cout<<"ninety ";
   break;
  }

if(temp==1)
{  switch (z)
  {
   case 1 : cout<<"one ";

break;
   case 2 : cout<<"two ";

break;
   case 3 : cout<<"three ";

break;
   case 4 : cout<<"four ";

break;
   case 5 : cout<<"five ";
break;
   case 6 : cout<<"six ";
break;
   case 7 : cout<<"seven ";
break;
   case 8 : cout<<"eight ";
break;
   case 9 : cout<<"nine "; }
   }
}


int main()
{  int a;
   char ch;
do{
   cout<<"enter the number"<<"\n";
   cin>>a;
    naming(a);
        cout<<"\n";
         cin.get();
        cout<<"do you wish to contiue(y/n)?"<<"\n";
        cin>>ch;
      system("clear");
}while(ch=='y');
    cout<<"Thank you for using"<<"\n";
    exit(0);
 return(0);

}
