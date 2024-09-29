package rooms;

public class CaveEnterance extends Room {
   Room entryHall = new EntryHall(this);

   public void enter() {
      System.out.println("You find yourself standing at the opening of a vast, mysterious cave. The entrance looms before you, awaiting.");

      while(true) {
         label29:
         while(true) {
            label27:
            while(true) {
               String input = getInput();
               String var2;
               switch((var2 = input.toLowerCase()).hashCode()) {
               case 96667352:
                  if (var2.equals("enter")) {
                     break label27;
                  }
                  break;
               case 98463581:
                  if (var2.equals("go in")) {
                     break label27;
                  }
                  break;
               case 102846135:
                  if (var2.equals("leave")) {
                     break label29;
                  }
                  break;
               case 134002975:
                  if (var2.equals("go back")) {
                     break label29;
                  }
               }

               System.out.println("Can't do that.");
            }

            System.out.println("You feel the air grow cool as you pass through the threshold into the depths...");
            this.entryHall.enter();
         }

         System.out.println("Go back? GO BACK? You cannot go back. Your fate is fixed; you have no choice.");
      }
   }
}
