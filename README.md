# Number-game-
#include <stdio.h>
#include <stdio.h>
#include <time.h>
int main ()
//initialize radom number generator
{srand(time(0));
//generate random number bet 1 to 100
int random_number = (rand()%100)+1;
int no_of_guesses =0 ;
int guessed =0 ;

do {
printf("\nguess the number");
scanf("%d",&guessed);
if(guessed > random_number)
{   
printf("\nlower no. please");
}
else if ( random_number > guessed)
{
printf("\nhigher no. please");
}
else 
printf("\nyou got it!!");
no_of_guesses++;
} while ( guessed != random_number);
printf("\nyou guessedthe number in %d guesses", no_of_guesses);
return 0;
}