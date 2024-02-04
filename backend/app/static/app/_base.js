console.log("Welcome to Django JWT Authentication app :)")



class Socket {
    constructor() {
        this.urls = "ws://localhost:8000/chat/";
        this.sock = undefined;
    }

    connect() {
        if (this.sock === undefined) {
            this.sock = new WebSocket(this.urls);
        } else {
            console.log("Connection already exists :(")
        }
    }

    close() {
        if (this.sock !== undefined) {
            this.sock.close()
        } else {
            console.log("No connection found :)")
        }

    }
}


let sock = undefined


async function connect() {
    document.querySelector("#ws-connect").onclick = () => {
        // if (sock === undefined) {

        sock = new WebSocket(`ws://${location.host}/chat/`)
        sock.onmessage = (e) => {
            console.log(`Received: ${e.data} :)`)
        }

        // } else {
        //     console.log("Error on connections :(")
        // }

    }
}

async function disconnect() {
    document.querySelector("#ws-disconnect").onclick = () => {
        // if (sock !== undefined) {

        sock.close();

        // } 

    }
}

const selectInputFromUser = async () => {
    document.querySelector("#send-message").onclick = () => {
        // console.log(document.querySelector('#write-message').value);
        sock.send(JSON.stringify({"message": document.querySelector('#write-message').value}))
    }
}
async function send() {
    await selectInputFromUser();
}


async function sendOnEnter() {
    document.addEventListener(
        "keydown",
        async (event) => {
            const keyName = event.key;
            if (keyName === "Enter") {
                console.log(keyName);
                await selectInputFromUser();
            }
        },
        false,
    );
    
}

async function main() {
    await sendOnEnter();
    await connect();
    await send();
    await disconnect();

}

main();