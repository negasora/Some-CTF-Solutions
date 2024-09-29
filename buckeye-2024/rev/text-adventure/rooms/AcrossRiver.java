package rooms;

import utility.Player;

public class AcrossRiver extends Room {
   private boolean hasSword = true;

   public AcrossRiver(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      if (this.hasSword) {
         System.out.println("It looks like there was once a battle here, long ago. You see the remains of a knight, still clothed in armor. A slightly-rusted sword lies across his lap.");
      } else {
         System.out.println("It looks like there was once a battle here, long ago. You still the remains of the knight whose sword you took.");
      }

      while(true) {
         label82:
         while(true) {
            label80:
            while(true) {
               label78:
               while(true) {
                  label76:
                  while(true) {
                     String input = getInput();
                     String var2;
                     switch((var2 = input.toLowerCase()).hashCode()) {
                     case -1906921030:
                        if (var2.equals("use the rope")) {
                           break label76;
                        }
                        break;
                     case -1817454439:
                        if (var2.equals("pick up armor")) {
                           break label78;
                        }
                        break;
                     case -1800680105:
                        if (var2.equals("pick up sword")) {
                           break label80;
                        }
                        break;
                     case -1506632735:
                        if (var2.equals("swing across")) {
                           break label76;
                        }
                        break;
                     case -1328913207:
                        if (var2.equals("swing back")) {
                           break label76;
                        }
                        break;
                     case -341309461:
                        if (var2.equals("use rope")) {
                           break label76;
                        }
                        break;
                     case 3083764:
                        if (var2.equals("dive")) {
                           break label82;
                        }
                        break;
                     case 3543688:
                        if (var2.equals("swim")) {
                           break label82;
                        }
                        break;
                     case 102846135:
                        if (var2.equals("leave")) {
                           break label76;
                        }
                        break;
                     case 109854462:
                        if (var2.equals("swing")) {
                           break label76;
                        }
                        break;
                     case 134002975:
                        if (var2.equals("go back")) {
                           break label76;
                        }
                        break;
                     case 681711211:
                        if (var2.equals("grab armor")) {
                           break label78;
                        }
                        break;
                     case 698485545:
                        if (var2.equals("grab sword")) {
                           break label80;
                        }
                        break;
                     case 1378416975:
                        if (var2.equals("equip armor")) {
                           break label78;
                        }
                        break;
                     case 1395191309:
                        if (var2.equals("equip sword")) {
                           break label80;
                        }
                        break;
                     case 1699735654:
                        if (var2.equals("take armor")) {
                           break label78;
                        }
                        break;
                     case 1716509988:
                        if (var2.equals("take sword")) {
                           break label80;
                        }
                     }

                     System.out.println("Can't do that.");
                  }

                  System.out.println("You throw the rope again, and swing back to the other side.");
                  this.previousRoom.enter();
               }

               System.out.println("You probably won't need that.");
            }

            if (this.hasSword) {
               System.out.println("Seems a shame to leave a fine sword to rust like that... It would be better off with you.");
               Player.instance.equipItem("sword");
               this.hasSword = false;
            } else {
               System.out.println("You already did that.");
            }
         }

         System.out.println("The water's moving too fast for you to swim across.");
      }
   }
}
