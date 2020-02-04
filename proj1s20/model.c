#include <stdio.h>

int main (int argc, char** argv)
{
 int val;

 /* prompt the user for input */
 printf ("Enter in a list of numbers ito be stored in a dynamic array.\n");
 printf ("End the list with the terminal value of -999\n");
 
 /* loop until the user enters -999 */
 scanf ("%d", &val);
 while (val != -999)
   {
    /* store the value into an array */

    /* get next value */
    scanf("%d", &val);
   }

 /* call function to make a copy of the array of values */

 /* call function to sort one of the arrays */

 /* loop until the user enters -999 */
 printf ("Enter in a list of numbers to use for searching.  \n");
 printf ("End the list with a terminal value of -999\n");
 scanf ("%d", &val);
 while (val != -999)
   {
    /* call function to perform target sum operation */

    /* print out info about the target sum results  */

   

    /* get next value */
    scanf("%d", &val);
   }


 printf ("Good bye\n");
 return 0;
} 
