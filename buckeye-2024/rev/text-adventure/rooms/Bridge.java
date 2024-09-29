package rooms;

import utility.Player;

public class Bridge extends Room {
   private Room crystalRoom = new CrystalRoom(this);

   public Bridge(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      if (Player.instance.hasItem("torch")) {
         System.out.println("You find yourself standing at the edge of an unfathomable chasm! Far off, you can hear fast running water below.\nThere lies a stone bridge spanning the gap, but it's little more than a few feet wide. It arches away from you, and disappears into the darkness.\nThe main hall lies behind you.");

         while(true) {
            label65:
            while(true) {
               label63:
               while(true) {
                  label61:
                  while(true) {
                     label59:
                     while(true) {
                        String input = getInput();
                        String var2;
                        switch((var2 = input.toLowerCase()).hashCode()) {
                        case -1746062856:
                           if (!var2.equals("cross the bridge")) {
                              break label63;
                           }
                           break label61;
                        case -341309461:
                           if (!var2.equals("use rope")) {
                              break label63;
                           }
                           break;
                        case -256874883:
                           if (!var2.equals("jump off")) {
                              break label63;
                           }
                           break label59;
                        case -98487625:
                           if (!var2.equals("go across")) {
                              break label63;
                           }
                           break label61;
                        case 3273774:
                           if (!var2.equals("jump")) {
                              break label63;
                           }
                           break label59;
                        case 3506418:
                           if (!var2.equals("rope")) {
                              break label63;
                           }
                           break;
                        case 94935104:
                           if (!var2.equals("cross")) {
                              break label63;
                           }
                           break label61;
                        case 102080182:
                           if (!var2.equals("walk across")) {
                              break label63;
                           }
                           break label61;
                        case 102846135:
                           if (var2.equals("leave")) {
                              break label65;
                           }
                           break label63;
                        case 134002975:
                           if (var2.equals("go back")) {
                              break label65;
                           }
                           break label63;
                        case 134182001:
                           if (var2.equals("go hall")) {
                              break label65;
                           }
                           break label63;
                        case 1797592917:
                           if (var2.equals("go to the hall")) {
                              break label65;
                           }
                        default:
                           break label63;
                        }

                        System.out.println("The rope isn't long enough to get you to the bottom of the chasm.");
                     }

                     System.out.println("You wouldn't survive a fall from this height.");
                  }

                  System.out.println("You slowly edge out on to the bridge... holding your breath...");
                  System.out.println("...and eventually make it to the other side. Uh, good job.");
                  this.crystalRoom.enter();
               }

               System.out.println("Can't do that.");
            }

            System.out.println("You return to the hall you entered through.");
            this.previousRoom.enter();
         }
      }

      this.darkRoom();
   }
}
