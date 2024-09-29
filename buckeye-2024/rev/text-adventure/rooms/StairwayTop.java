package rooms;

import utility.Player;

public class StairwayTop extends Room {
   private Room stairwayBottom = new StairwayBottom(this);

   public StairwayTop(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      if (Player.instance.hasItem("torch")) {
         System.out.println("You find yourself at the top of a long stair descending downward. You cannot make out the bottom.");
         System.out.println("Behind you lies the great hall you first entered through.");

         while(true) {
            label39:
            while(true) {
               label37:
               while(true) {
                  String input = getInput();
                  String var2;
                  switch((var2 = input.toLowerCase()).hashCode()) {
                  case 102846135:
                     if (var2.equals("leave")) {
                        break label37;
                     }
                     break;
                  case 134002975:
                     if (var2.equals("go back")) {
                        break label37;
                     }
                     break;
                  case 134076634:
                     if (var2.equals("go down")) {
                        break label39;
                     }
                     break;
                  case 134182001:
                     if (var2.equals("go hall")) {
                        break label37;
                     }
                     break;
                  case 1556853930:
                     if (var2.equals("descend")) {
                        break label39;
                     }
                     break;
                  case 1797592917:
                     if (var2.equals("go to the hall")) {
                        break label37;
                     }
                  }

                  System.out.println("Can't do that.");
               }

               System.out.println("You exit back into the hall you came through.");
               this.previousRoom.enter();
            }

            System.out.println("You muster all of your courage and wander down into the depths...");
            this.stairwayBottom.enter();
         }
      }

      this.darkRoom();
   }
}
