package tf.irisc.chal.webwebhookhook.controller

import org.springframework.http.MediaType
import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.*
import tf.irisc.chal.webwebhookhook.State
import tf.irisc.chal.webwebhookhook.StateType
import java.net.HttpURLConnection
import java.net.URI

@Controller
class MainController {

    @GetMapping("/")
    fun home(model: Model): String {
        return "home.html"
    }

    @PostMapping("/webhook")
    @ResponseBody
    fun webhook(@RequestParam("hook") hook_str: String, @RequestBody body: String, @RequestHeader("Content-Type") contentType: String, model: Model): String {
        var hook = URI.create(hook_str).toURL(); // we control this
        for (h in State.arr) {
            if(h.hook == hook) {
                var newBody = h.template.replace("_DATA_", body); // we control this
                var conn = hook.openConnection() as? HttpURLConnection;
                if(conn === null)
                {
                    println("CONNECTION IS NULL")
                    break;
                }
                conn.requestMethod = "POST";
                conn.doOutput = true;
                conn.setFixedLengthStreamingMode(newBody.length);
                conn.setRequestProperty("Content-Type", contentType); // we control this
                conn.connect()
                conn.outputStream.use { os ->
                    os.write(newBody.toByteArray())
                }
                print("Sent: ")
                println(newBody)
                println("Returning")
                return h.response
            }
        }
        return "{\"result\": \"fail\"}"
    }

    @PostMapping("/create", consumes = [MediaType.APPLICATION_JSON_VALUE])
    @ResponseBody
    fun create(@RequestBody body: StateType): String {
        for(h in State.arr) {
            if(body.hook == h.hook) // maybe different dns entry here idk
                return "{\"result\": \"fail\"}"
        }
        State.arr.add(body)
        return "{\"result\": \"ok\"}"
    }
}
