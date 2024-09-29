package rooms;

public class StairwayBottom extends Room {
   private Room sealedDoor = new SealedDoor(this);
   private Room river = new River(this);

   public StairwayBottom(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      System.out.println("You are at the base of the stairway. Two paths lay before you, one left and one right.\nYou hear the sound of rushing water coming from the right passageway.");

      while(true) {
         label48:
         while(true) {
            label46:
            while(true) {
               label44:
               while(true) {
                  String input = getInput();
                  String var2;
                  switch((var2 = input.toLowerCase()).hashCode()) {
                  case -1654690961:
                     if (var2.equals("up stairs")) {
                        break label44;
                     }
                     break;
                  case -1408684854:
                     if (var2.equals("ascend")) {
                        break label44;
                     }
                     break;
                  case -125856540:
                     if (var2.equals("go right")) {
                        break label46;
                     }
                     break;
                  case 3317767:
                     if (var2.equals("left")) {
                        break label48;
                     }
                     break;
                  case 98463955:
                     if (var2.equals("go up")) {
                        break label44;
                     }
                     break;
                  case 102846135:
                     if (var2.equals("leave")) {
                        break label44;
                     }
                     break;
                  case 108511772:
                     if (var2.equals("right")) {
                        break label46;
                     }
                     break;
                  case 134002975:
                     if (var2.equals("go back")) {
                        break label44;
                     }
                     break;
                  case 134304831:
                     if (var2.equals("go left")) {
                        break label48;
                     }
                  }

                  System.out.println("Can't do that.");
               }

               System.out.println("You go up the steps...");
               this.previousRoom.enter();
            }

            System.out.println("You head into the right passageway...");
            this.river.enter();
         }

         System.out.println("You head into the left passageway...");
         this.sealedDoor.enter();
      }
   }
}
