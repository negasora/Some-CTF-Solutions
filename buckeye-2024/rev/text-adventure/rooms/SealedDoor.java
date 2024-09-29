package rooms;

import utility.Player;

public class SealedDoor extends Room {
   private Room deadEnd = new DeadEnd(this);
   private boolean locked = true;

   public SealedDoor(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      if (this.locked) {
         this.lockedRoom();
      } else {
         this.unlockedRoom();
      }

   }

   private void lockedRoom() {
      if (this.locked) {
         System.out.println("You enter a small room, with stone close all around you. Before you lies a door sealed with a large lock.\nBehind you lie the base of the steps.");
      } else {
         System.out.println("You return to the small room, with stone close all around you. Before you lies a great door, but it's unlocked now.\nBehind you lie the base of the steps.");
      }

      while(true) {
         label54:
         while(true) {
            label52:
            while(true) {
               label50:
               while(true) {
                  String input = getInput();
                  String var2;
                  switch((var2 = input.toLowerCase()).hashCode()) {
                  case -1989222567:
                     if (var2.equals("unlock the door")) {
                        break label52;
                     }
                     break;
                  case -920183030:
                     if (var2.equals("unlock door")) {
                        break label52;
                     }
                     break;
                  case -840442044:
                     if (var2.equals("unlock")) {
                        break label52;
                     }
                     break;
                  case -124606993:
                     if (var2.equals("go steps")) {
                        break label50;
                     }
                     break;
                  case -98476149:
                     if (var2.equals("go to the steps")) {
                        break label50;
                     }
                     break;
                  case 102846135:
                     if (var2.equals("leave")) {
                        break label50;
                     }
                     break;
                  case 134002975:
                     if (var2.equals("go back")) {
                        break label50;
                     }
                     break;
                  case 1153113875:
                     if (var2.equals("open the door")) {
                        break label54;
                     }
                     break;
                  case 1487686596:
                     if (var2.equals("open door")) {
                        break label54;
                     }
                  }

                  System.out.println("Can't do that.");
               }

               System.out.println("You return to the base of the steps.");
               this.previousRoom.enter();
            }

            if (Player.instance.hasItem("key")) {
               System.out.println("You fit the key into the lock, and slowly start to turn it...");
               System.out.println("It works! The lock falls away and you pass through the door.");
               this.locked = false;
               this.deadEnd.enter();
            } else {
               System.out.println("Looks like you'll have to find a key.");
            }
         }

         System.out.println("It's, uh, locked.");
      }
   }

   private void unlockedRoom() {
      System.out.println("You enter a small room with stone close all around. Before you lies the door you unlocked.");

      while(true) {
         label28: {
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
               case 102846135:
                  if (var2.equals("leave")) {
                     break label28;
                  }
                  break;
               case 134002975:
                  if (var2.equals("go back")) {
                     break label28;
                  }
                  break;
               case 1067699085:
                  if (var2.equals("go through")) {
                     break label27;
                  }
               }

               System.out.println("Can't do that.");
            }

            System.out.println("You enter back through the door...");
            this.deadEnd.enter();
         }

         System.out.println("You return back to the base of the steps.");
         this.previousRoom.enter();
      }
   }
}
