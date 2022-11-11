import java.util.Scanner;

/*
 * This version of the program is out of date
 * for a better version go to my dedicated repo 
 * https://github.com/MilesFate/LolMath
 * i will keep this just to remind myself how far i have come
 */
public class lolmath {

    public static void main(String[] args) {
        System.out.println("This program is made to make the Process of leveling easier");
        System.out.println("\" Assuming no xp earned in the entered level and the game is won with 20 min played\" ");
        System.out.println("-------------------------------------------------");
        LvlChecker();
    }

    private static int lolLevelCal(){
        Scanner in = new Scanner(System.in);
        do{
            System.out.print("Enter Current Level: ");
            var input = in.nextInt();
            if (input < 30) {
                in.close();
                return input;
            }
            System.out.println("Invalid Input, Enter a number under 30");
        } while (true);
    }
    // TODO : add proper game mode picker
    /*private static String ModeChecker(){
        Scanner in = new Scanner(System.in);
        do {
            System.out.print("pvp or pve: ");
            var input = in.nextLine();
            if (!input.isEmpty()) {
                in.close();
                return input;
            }
            System.out.println("Invalid Input");
        }while(true);
    }*/

    private static void LevelMath(int num) {
        int NeededGames = lo(num);
        int time = ( NeededGames * 20) / 60;
        System.out.printf("The number of games until Level 30 is about %d.\n",NeededGames);
        System.out.printf("Time required is %d hours.\n",time);
    }

    private static int lo(int num){
        var pve = 1200 * 0.08 + 4.95;
            return ((39382 - num)/ (int)pve);
    }

    private static void LvlChecker() {
        var input = lolLevelCal();
        do {
            switch (input) {
                case 1 ->  { LevelMath(0);     return; }
                case 2 ->  { LevelMath(144);   return; }
                case 3 ->  { LevelMath(288);   return; }
                case 4 ->  { LevelMath(480);   return; }
                case 5 ->  { LevelMath(720);   return; }
                case 6 ->  { LevelMath(1056);  return; }
                case 7 ->  { LevelMath(1488);  return; }
                case 8 ->  { LevelMath(2016);  return; }
                case 9 ->  { LevelMath(2640);  return; }
                case 10 -> { LevelMath(3360);  return; }
                case 11 -> { LevelMath(4176);  return; }
                case 12 -> { LevelMath(5088);  return; }
                case 13 -> { LevelMath(6072);  return; }
                case 14 -> { LevelMath(7128);  return; }
                case 15 -> { LevelMath(8256);  return; }
                case 16 -> { LevelMath(9600);  return; }
                case 17 -> { LevelMath(11040); return; }
                case 18 -> { LevelMath(12576); return; }
                case 19 -> { LevelMath(14256); return; }
                case 20 -> { LevelMath(16080); return; }
                case 21 -> { LevelMath(18048); return; }
                case 22 -> { LevelMath(20160); return; }
                case 23 -> { LevelMath(22368); return; }
                case 24 -> { LevelMath(24672); return; }
                case 25 -> { LevelMath(27120); return; }
                case 26 -> { LevelMath(29616); return; }
                case 27 -> { LevelMath(32112); return; }
                case 28 -> { LevelMath(34704); return; }
                case 29 -> { LevelMath(37392); return; }
            }
        } while (true);
    }
}
