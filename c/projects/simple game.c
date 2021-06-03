#include <stdio.h>

// simple text adventure
// this is the pinnacle of "with enough if statements anything is possible"
// looking at this makes me cringe really hard ngl
void story(){
    int door;
    int person;
    int food; 
    printf("welcome to a text adventure game\n");
    printf("You wake up in a room, you see 3 doors infront of you.\n");
    printf("Each door has a number above it from 1-3.\n");
    printf("Which door do you go through.\n");
    scanf("%d", &door);
    if (door == 1){
        printf("Enter the first door.\n");
        printf("In the room you see 3 people.\n");
        printf("Each has a letter on them ranging from a-c.\n");
        printf("Who do you talk to?:A-1,B-2,C-3\n");
        scanf("%d", &person);
       if(person == 1){
            printf("You walk up to person a.\n");
            printf("They tell you to follow them.\n");
            printf("After a long walk, they show you a table with two foods on it.\n");
            printf("The foods are an apple and an orange, each on one end of the table sitting on a plate.\n");
            printf("They say that one will save you, the other will not.\n");
            printf("Which food do you choice?:Orange-1, Apple-2\n");
            scanf("%d", &food);
            if(food == 1){
                printf("you win\n");
            }else if(food == 2){
                printf("you eat the apple and die.\n");
                printf("You Lose\n");
            }else{
                printf("You walk in circles for the rest of time.\n");
                printf("You Lose\n");
            }
        }else if(person == 2){
            printf("You walk up to person b.\n");
            printf("They tell you to follow them.\n");
            printf("After a long walk, they show you a table with two foods on it.\n");
            printf("The foods are an apple and an orange, each on one end of the table sitting on a plate.\n");
            printf("They say that one will save you, the other will not.\n");
            printf("Which food do you choice?:Orange-1, Apple-2\n");
            scanf("%d", &food);
            if(food == 1){
                printf("you win\n");
            }else if(food == 2){
                printf("you eat the apple and die.\n");
                printf("you lose\n");
            }else{
                printf("You walk in circles for the rest of time.\n");
                printf("You Lose\n");
            }
        }else if(person == 3){
            printf("you lose\n");
        }else{
            printf("You walk in circles for the rest of time.\n");
            printf("You Lose\n");
        }
    }else if (door == 2){
        printf("Enter the second door.\n");
        printf("In the room you see 3 people.\n");
        printf("Each has a letter on them ranging from A-C.\n");
        printf("Who do you talk to?:A-1,B-2,C-3\n");
        scanf("%d", &person);
        if(person == 1){
            printf("You walk up to person a.\n");
            printf("They tell you to follow them.\n");
            printf("After a long walk, they show you a table with two foods on it.\n");
            printf("The foods are an apple and an orange, each on one end of the table sitting on a plate.\n");
            printf("They say that one will save you, the other will not.\n");
            printf("Which food do you choice?:Orange-1, Apple-2\n");
            scanf("%d", &food);
            if(food == 1){
                printf("you win\n");
            }else if(food == 2){
                printf("you eat the apple and die.\n");
                printf("you lose\n");
            }else{
                printf("You walk in circles for the rest of time.\n");
                printf("You Lose\n");
            }
        }else if(person == 2){
            printf("You walk up to person b.\n");
            printf("They tell you to follow them.\n");
            printf("After a long walk, they show you a table with two foods on it.\n");
            printf("The foods are an apple and an orange, each on one end of the table sitting on a plate.\n");
            printf("They say that one will save you, the other will not.\n");
            printf("Which food do you choice?:Orange-1, Apple-2\n");
            scanf("%d", &food);
            if(food == 1){
                printf("you win\n");
            }else if(food == 2){
                printf("you eat the apple and die.\n");
                printf("you lose\n");
            }else{
                printf("You walk in circles for the rest of time.\n");
                printf("You Lose\n");
            }
        }else if(person == 3){
            printf("you lose\n");
        }else{
            printf("You walk in circles for the rest of time.\n");
            printf("You Lose\n");
        }
    }else if (door == 3){
        printf("Enter the third door.\n");
        printf("In the room you see 3 people.\n");
        printf("Each has a letter on them ranging from A-C.\n");
        printf("Who do you talk to?:A-1,B-2,C-3\n");
        scanf("%d", &person);
        if(person == 1){
            printf("You walk up to person a.\n");
            printf("They tell you to follow them.\n");
            printf("After a long walk, they show you a table with two foods on it.\n");
            printf("The foods are an apple and an orange, each on one end of the table sitting on a plate.\n");
            printf("They say that one will save you, the other will not.\n");
            printf("Which food do you choice?:Orange-1, Apple-2\n");
            scanf("%d", &food);
            if(food == 1){
                printf("you win\n");
            }else if(food == 2){
                printf("you eat the apple and die.\n");
                printf("you lose\n");
            }else{
                printf("You walk in circles for the rest of time.\n");
                printf("You Lose\n");
            }
        }else if(person == 2){
            printf("You walk up to person b.\n");
            printf("They tell you to follow them.\n");
            printf("After a long walk, they show you a table with two foods on it.\n");
            printf("The foods are an apple and an orange, each on one end of the table sitting on a plate.\n");
            printf("They say that one will save you, the other will not.\n");
            printf("Which food do you choice?:Orange-1, Apple-2\n");
            scanf("%d", &food);
            if(food == 1){
                printf("you win\n");
            }else if(food == 2){
                printf("you eat the apple and die.\n");
                printf("you lose\n");
            }else{
                printf("You walk in circles for the rest of time.\n");
                printf("You Lose\n");
            }
        }else if(person == 3){
            printf("you lose\n");
        }
    }else{
                printf("You walk in circles for the rest of time.\n");
                printf("You Lose\n");
            }
}

// mad libs, old but fun
// honestly, mad libs is my favorite thing to make in any language
void mad(){
    // declaring all the vars i need
    char name[20];
    int age;
    char adjective[20];
    char color[20];
    char animal[20];
    // getting all the required information
    printf("welcome to mad libs\n");
    printf("Enter a name: ");
    scanf("%s", &name);
    printf("Enter a number: ");
    scanf("%d", &age);
    printf("Enter a adjective: ");
    scanf("%s", &adjective);
    printf("Enter a color: ");
    scanf("%s", &color);
    printf("Type of animal: ");
    scanf("%s", &animal);

    // this is the result
    printf("\nHello, my name is %s and I am %d years old.\n",name, age);
    printf("I am a %s.\n",adjective);
    printf("My favorite animal is %s.\n",animal);
    printf("My Favore color is %s.\n",color);

}

// main duh
int main(){
    // the opening decision as to what the user wishes to play
    char choice;
    printf("hello friend\n");
    printf("Which game do you want to play\n");
    printf("Mad Libs='a', Text Adventure='b'\n");
    scanf("%s", &choice);
    
    // here is where their decision decideds the game
    if (choice == 'a'){
        mad();
    } else if (choice == 'b'){
        story();
    }
}