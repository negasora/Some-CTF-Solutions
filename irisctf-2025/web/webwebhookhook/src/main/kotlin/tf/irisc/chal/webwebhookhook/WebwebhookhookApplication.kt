package tf.irisc.chal.webwebhookhook

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class WebwebhookhookApplication

const val FLAG = "irisctf{test_flag}";

fun main(args: Array<String>) {
    State.arr.add(StateType(
            "http://example.com/admin", // hook
            "{\"data\": _DATA_, \"flag\": \"" + FLAG + "\"}", // template
            "{\"response\": \"ok\"}")) // response
    runApplication<WebwebhookhookApplication>(*args)
}
