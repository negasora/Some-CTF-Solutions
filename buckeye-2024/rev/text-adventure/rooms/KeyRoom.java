package rooms;

import utility.Player;

public class KeyRoom extends Room {
   private boolean hasKey = true;

   public KeyRoom(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      if (this.hasKey) {
         System.out.println("You come in to a small room with a glowing pedestal in the center.\nThe light is dazzling, and upon the pedestal lies an ornate key. Neat!");
      } else {
         System.out.println("You come in to a small room with a glowing pedestal in the center.\nYou already picked up the ornate key, but the light is still beautiful.");
      }

      while(true) {
         label41:
         while(true) {
            label39:
            while(true) {
               String input = getInput();
               String var2;
               switch((var2 = input.toLowerCase()).hashCode()) {
               case -2106907591:
                  if (!var2.equals("pick up key")) {
                     break label39;
                  }
                  break;
               case -646266042:
                  if (!var2.equals("take key")) {
                     break label39;
                  }
                  break;
               case 85634699:
                  if (!var2.equals("grab key")) {
                     break label39;
                  }
                  break;
               case 102846135:
                  if (var2.equals("leave")) {
                     break label41;
                  }
                  break label39;
               case 134002975:
                  if (var2.equals("go back")) {
                     break label41;
                  }
                  break label39;
               case 1074068079:
                  if (!var2.equals("equip key")) {
                     break label39;
                  }
                  break;
               default:
                  break label39;
               }

               if (this.hasKey) {
                  System.out.println("You slowly reach out your hand, wary of any traps you might spring, or eyes that might be watching...");
                  System.out.println("...but there aren't any. Easy, right?");
                  Player.instance.equipItem("key");
                  this.hasKey = false;
               } else {
                  System.out.println("You already did that.");
               }
            }

            System.out.println("Can't do that.");
         }

         System.out.println("You exit back into the hall of spiders.");
         this.previousRoom.enter();
      }
   }
}
