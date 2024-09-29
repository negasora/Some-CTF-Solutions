package rooms;

import utility.Player;

public class CrystalRoom extends Room {
   private boolean hasRope = true;

   public CrystalRoom(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      System.out.println("On the other side of the bridge, you come upon a cavern covered in glistening pink crystals!\nSome are so large you can see your reflection in them as they glisten from your torchlight.\nSome of the crystals look mined away, but you don't see any sort of pickaxe. All that remains of the mining operation is a bundle of rope.");

      while(true) {
         label38:
         while(true) {
            label36:
            while(true) {
               String input = getInput();
               String var2;
               switch((var2 = input.toLowerCase()).hashCode()) {
               case -1640073658:
                  if (!var2.equals("grab rope")) {
                     break label36;
                  }
                  break;
               case -1063409950:
                  if (!var2.equals("equip rope")) {
                     break label36;
                  }
                  break;
               case -889407912:
                  if (!var2.equals("pick up rope")) {
                     break label36;
                  }
                  break;
               case 102846135:
                  if (var2.equals("leave")) {
                     break label38;
                  }
                  break label36;
               case 134002975:
                  if (var2.equals("go back")) {
                     break label38;
                  }
                  break label36;
               case 1440807147:
                  if (!var2.equals("take rope")) {
                     break label36;
                  }
                  break;
               default:
                  break label36;
               }

               if (this.hasRope) {
                  Player.instance.equipItem("rope");
                  this.hasRope = false;
               } else {
                  System.out.println("You already did that.");
               }
            }

            System.out.println("Can't do that.");
         }

         System.out.println("You brave the bridge once again...");
         System.out.println("...and again, safely make it across. Surefooted as they come.");
         this.previousRoom.enter();
      }
   }
}
