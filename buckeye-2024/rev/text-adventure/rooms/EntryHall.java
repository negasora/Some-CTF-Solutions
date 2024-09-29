package rooms;

import utility.Player;

public class EntryHall extends Room {
   Room spiderHall = new SpiderHallway(this);
   Room stairway = new StairwayTop(this);
   Room bridge = new Bridge(this);
   boolean hasTorch = true;

   public EntryHall(Room previousRoom) {
      this.previousRoom = previousRoom;
   }

   public void enter() {
      System.out.print("You find yourself in a central hall.");
      if (this.hasTorch) {
         System.out.print(" It is faintly lit by a torch on the leftmost wall.");
      }

      System.out.println("\nThrough the gloom you barely make out three arches to ongoing passages: one left, one middle, and one right.");

      while(true) {
         while(true) {
            label55:
            while(true) {
               label53:
               while(true) {
                  String input = getInput();
                  String var2;
                  switch((var2 = input.toLowerCase()).hashCode()) {
                  case -1799992490:
                     if (var2.equals("pick up torch")) {
                        break label55;
                     }
                     break;
                  case -125856540:
                     if (var2.equals("go right")) {
                        System.out.println("You pass through the right corridor...");
                        this.bridge.enter();
                        continue;
                     }
                     break;
                  case -39497075:
                     if (var2.equals("go center")) {
                        break label53;
                     }
                     break;
                  case 134002975:
                     if (var2.equals("go back")) {
                        System.out.println("You exit back into the light of day beyond the cave.");
                        this.previousRoom.enter();
                        continue;
                     }
                     break;
                  case 134304831:
                     if (var2.equals("go left")) {
                        System.out.println("You pass through the left corridor...");
                        this.spiderHall.enter();
                        continue;
                     }
                     break;
                  case 250175437:
                     if (var2.equals("go middle")) {
                        break label53;
                     }
                     break;
                  case 699173160:
                     if (var2.equals("grab torch")) {
                        break label55;
                     }
                     break;
                  case 1395878924:
                     if (var2.equals("equip torch")) {
                        break label55;
                     }
                     break;
                  case 1717197603:
                     if (var2.equals("take torch")) {
                        break label55;
                     }
                  }

                  System.out.println("Can't do that.");
               }

               System.out.println("You pass through the middle corridor...");
               this.stairway.enter();
            }

            if (this.hasTorch) {
               Player.instance.equipItem("torch");
               this.hasTorch = false;
            } else {
               System.out.println("You already picked that up.");
            }
         }
      }
   }
}
