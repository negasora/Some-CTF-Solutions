package rooms;

import utility.Player;

public class River extends Room {
   private Room acrossRiver = new AcrossRiver(this);

   public River(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      System.out.println("You find yourself alongside a great rushing underground river!\nThe remains of a broken bridge lie torn and rotted. You'll have to find some other way to cross.\nThere's a great root of some tree sticking out from the ceiling, but it's too high for you to reach.\nThe base of the steps lie behind you.");

      while(true) {
         while(true) {
            label65:
            while(true) {
               label63:
               while(true) {
                  label61:
                  while(true) {
                     String input = getInput();
                     String var2;
                     switch((var2 = input.toLowerCase()).hashCode()) {
                     case -1906921030:
                        if (!var2.equals("use the rope")) {
                           break label61;
                        }
                        break;
                     case -1902974149:
                        if (!var2.equals("throw the rope")) {
                           break label61;
                        }
                        break;
                     case -1506632735:
                        if (!var2.equals("swing across")) {
                           break label61;
                        }
                        break;
                     case -341309461:
                        if (!var2.equals("use rope")) {
                           break label61;
                        }
                        break;
                     case -331929108:
                        if (!var2.equals("throw rope")) {
                           break label61;
                        }
                        break;
                     case -124606993:
                        if (var2.equals("go steps")) {
                           break label63;
                        }
                        break label61;
                     case -98476149:
                        if (var2.equals("go to the steps")) {
                           break label63;
                        }
                        break label61;
                     case 3083764:
                        if (var2.equals("dive")) {
                           break label65;
                        }
                        break label61;
                     case 3273774:
                        if (var2.equals("jump")) {
                           System.out.println("Too far to jump.");
                           continue;
                        }
                        break label61;
                     case 3543688:
                        if (var2.equals("swim")) {
                           break label65;
                        }
                        break label61;
                     case 102846135:
                        if (var2.equals("leave")) {
                           break label63;
                        }
                        break label61;
                     case 109854462:
                        if (!var2.equals("swing")) {
                           break label61;
                        }
                        break;
                     case 134002975:
                        if (var2.equals("go back")) {
                           break label63;
                        }
                     default:
                        break label61;
                     }

                     if (Player.instance.hasItem("rope")) {
                        System.out.println("You throw with all your might, and the rope catches on the root! You swing across safely.");
                        this.acrossRiver.enter();
                     } else {
                        System.out.println("Hmm, that root might hold your weight... if only you had some rope.");
                     }
                  }

                  System.out.println("Can't do that.");
               }

               System.out.println("You return to the base of the steps.");
               this.previousRoom.enter();
            }

            System.out.println("The water's moving too fast for you to swim across.");
         }
      }
   }
}
