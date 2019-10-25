#include <stdio.h>
#include <stdlib.h>

/* 
 * a simple game of tic-tac-toe
 */
#define SPACE ' '

char matrix[3][3] = {
    SPACE,SPACE,SPACE,
    SPACE,SPACE,SPACE,
    SPACE,SPACE,SPACE
};

void get_computer_move(void);
void get_player_void(void);
void disp_matrix(void);
int check(void);

int main()
{
    char done;
    
    printf("This is the game of Tic-Tac-Toe.\n");
    printf("You will be playing against the computer.\n");
    
    done = SPACE
    do {
        disp_matrix();
    }
}
