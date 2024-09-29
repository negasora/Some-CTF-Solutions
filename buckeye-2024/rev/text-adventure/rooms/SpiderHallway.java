package rooms;

import utility.Player;

public class SpiderHallway extends Room {
   Room keyRoom = new KeyRoom(this);
   private boolean websCut = false;

   public SpiderHallway(Room prevRoom) {
      this.previousRoom = prevRoom;
   }

   public void enter() {
      if (Player.instance.hasItem("torch")) {
         if (!this.websCut) {
            System.out.println("You come upon a long hallway, the walls covered by thick webs. Thousands of little legs seem to scurry away from your torch's light.\nYou notice a door at the end of the hall, completely covered in webs. You'll need someting sharp to get cut through it.");
         } else {
            System.out.println("You return to the long hall, still covered in webs. The door is free, now, though. You feel like hundreds of tiny eyes are watching your every move.\nThe main hall lies behind you.");
         }

         while(true) {
            label73:
            while(true) {
               label71:
               while(true) {
                  label69:
                  while(true) {
                     String input = getInput();
                     String var2;
                     switch((var2 = input.toLowerCase()).hashCode()) {
                     case -2007890096:
                        if (var2.equals("burn webs")) {
                           break label71;
                        }
                        break label69;
                     case -567175905:
                        if (var2.equals("burn the webs")) {
                           break label71;
                        }
                        break label69;
                     case 98882:
                        if (!var2.equals("cut")) {
                           break label69;
                        }
                        break;
                     case 102846135:
                        if (var2.equals("leave")) {
                           break label73;
                        }
                        break label69;
                     case 134002975:
                        if (var2.equals("go back")) {
                           break label73;
                        }
                        break label69;
                     case 134182001:
                        if (var2.equals("go hall")) {
                           break label73;
                        }
                        break label69;
                     case 239250716:
                        if (var2.equals("burn it")) {
                           break label71;
                        }
                        break label69;
                     case 359614183:
                        if (!var2.equals("cut through")) {
                           break label69;
                        }
                        break;
                     case 556903116:
                        if (!var2.equals("cut door")) {
                           break label69;
                        }
                        break;
                     case 557459133:
                        if (!var2.equals("cut webs")) {
                           break label69;
                        }
                        break;
                     case 1797592917:
                        if (var2.equals("go to the hall")) {
                           break label73;
                        }
                        break label69;
                     case 2112469531:
                        if (!var2.equals("cut the door")) {
                           break label69;
                        }
                        break;
                     case 2113025548:
                        if (!var2.equals("cut the webs")) {
                           break label69;
                        }
                        break;
                     default:
                        break label69;
                     }

                     if (!this.websCut) {
                        if (Player.instance.hasItem("sword")) {
                           System.out.println("The sword slices right through the webs! You're able to cut away the door and get through.");
                           this.websCut = true;
                           this.keyRoom.enter();
                        } else {
                           System.out.println("With what, your hands?");
                        }
                     } else {
                        System.out.println("You already did that.");
                     }
                  }

                  System.out.println("Can't do that.");
               }

               System.out.println("You can't seem to get them to light. Must be some kind of magic...");
            }

            System.out.println("You exit back into the hall you first entered in.");
            this.previousRoom.enter();
         }
      }

      this.darkRoom();
   }
}
