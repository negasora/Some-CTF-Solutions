    package com.example.guess;

import android.os.Build;
import android.os.Bundle;
import android.view.View;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import java.util.Base64;

public class MainActivity extends AppCompatActivity {
    /* access modifiers changed from: protected */
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), new MainActivity$$ExternalSyntheticLambda0());
    }

    static /* synthetic */ WindowInsetsCompat lambda$onCreate$0(View v, WindowInsetsCompat insets) {
        Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
        v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
        return insets;
    }

    public static class flag {
        public static String end() {
            return whatTheFunction("cmpkdjNjYzE6MzUuU1R8aHY0dHR6YGd2b2R1MnBvfi46MTI0M3M6amcz");
        }

        private static String whatTheFunction(String evilString) {
            String fornameN = null;
            if (Build.VERSION.SDK_INT >= 26) {
                fornameN = new String(Base64.getDecoder().decode(evilString));
            }
            StringBuilder recursiveCharArray = new StringBuilder();
            String undecryptedencryptedString = "SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw==";
            char[] finalrray = undecryptedencryptedString.toCharArray();
            int kentucky = 0;
            for (int xortrad = finalrray.length - 1; kentucky < xortrad; xortrad--) {
                char glaf = finalrray[kentucky];
                finalrray[kentucky] = finalrray[xortrad];
                finalrray[xortrad] = glaf;
                kentucky++;
            }
            for (int everyOther = 0; everyOther < fornameN.length(); everyOther++) {
                recursiveCharArray.append((char) (fornameN.charAt(everyOther) - 1));
            }
            for (char c : finalrray) {
                if (Build.VERSION.SDK_INT >= 26) {
                    undecryptedencryptedString = new String(Base64.getEncoder().encode("SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw==".getBytes())) + c;
                }
            }
            return "SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw==" + recursiveCharArray + undecryptedencryptedString;
        }
    }
}
