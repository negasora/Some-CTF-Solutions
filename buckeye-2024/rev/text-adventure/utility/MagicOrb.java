package utility;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MagicOrb {
   public void printFlag() throws IOException {
      BufferedReader br = new BufferedReader(new FileReader("/flag"));

      String line;
      while((line = br.readLine()) != null) {
         System.out.println(line);
      }

      br.close();
   }
}
