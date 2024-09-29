package rooms;

import java.util.Scanner;

public abstract class Room {
   static Scanner scan;
   protected Room previousRoom;

   static {
      scan = new Scanner(System.in);
   }

   public abstract void enter();

   protected static String getInput() {
      System.out.print("\n> ");
      String in = scan.nextLine();
      System.out.print("\n");
      if (in.equals("exit")) {
         System.out.println("Okay, goodbye!");
         scan.close();
         System.exit(0);
      }

      return in;
   }

   protected void darkRoom() {
      System.out.println("It's too dark to see anything!");

      while(true) {
         label19:
         while(true) {
            String input = getInput();
            String var2;
            switch((var2 = input.toLowerCase()).hashCode()) {
            case 102846135:
               if (var2.equals("leave")) {
                  break label19;
               }
               break;
            case 134002975:
               if (var2.equals("go back")) {
                  break label19;
               }
            }

            System.out.println("Can't do that.");
         }

         System.out.println("You exit back into the hall you came through.");
         this.previousRoom.enter();
      }
   }
}
