package rooms;

import utility.MagicOrb;

public class DeadEnd extends Room {
   private MagicOrb flag = new MagicOrb();

   public DeadEnd(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      System.out.println("It appears to be a dead end.");

      while(true) {
         label32:
         while(true) {
            String input = getInput();
            String var2;
            switch((var2 = input.toLowerCase()).hashCode()) {
            case -1388976959:
               if (var2.equals("reach through the crack in the rocks")) {
                  System.out.println("What? What crack in the rocks?");
                  input = getInput();
                  if (input.equals("the crack in the rocks concealing the magical orb with the flag")) {
                     System.out.println("There's a crack in the --? Well, it seems you know more about this world than I do. Happy hacking!");

                     try {
                        this.flag.printFlag();
                     } catch (Exception var4) {
                        System.out.println("Hmm.... it seems the magical orb has decided to give you nothing. How strange.");
                     }
                  }
                  continue;
               }
               break;
            case 102846135:
               if (var2.equals("leave")) {
                  break label32;
               }
               break;
            case 134002975:
               if (var2.equals("go back")) {
                  break label32;
               }
            }

            System.out.println("Can't do that.");
         }

         System.out.println("You return back to the room you came through.");
         this.previousRoom.enter();
      }
   }
}
