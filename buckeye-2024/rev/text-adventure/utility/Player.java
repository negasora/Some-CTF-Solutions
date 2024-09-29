package utility;

import java.util.HashSet;
import java.util.Set;

public class Player {
   public static Player instance = new Player();
   private static Set<String> Inventory;

   private Player() {
      Inventory = new HashSet();
   }

   public void equipItem(String item) {
      if (Inventory.contains(item)) {
         System.out.println("Already have one of those!");
      } else {
         System.out.println("You picked up the " + item + ".");
         Inventory.add(item);
      }

   }

   public boolean hasItem(String item) {
      return Inventory.contains(item);
   }
}
