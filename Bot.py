import requests
import os
import re
import time
import sys
import http.server
import socketserver
import threading
from requests.exceptions import RequestException

class MyHandler(http.server.SimpleHTTPRequestHandler):
def do_GET(self):
self.send_response(200)
self.send_header('Content-type', 'text/plain')
self.end_headers()
self.wfile.write(b"TH3 UNB3T34BL3 L3G3ND FYT3R JAY X VEERU HERE")

class FacebookCommenter:
def init(self):
self.comment_count = 0

def comment_on_post(self, cookies, post_id, comment, delay):  
    with requests.Session() as r:  
        r.headers.update({  
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',  
            'sec-fetch-site': 'none',  
            'accept-language': 'id,en;q=0.9',  
            'Host': 'mbasic.facebook.com',  
            'sec-fetch-user': '?1',  
            'sec-fetch-dest': 'document',  
            'accept-encoding': 'gzip, deflate',  
            'sec-fetch-mode': 'navigate',  
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36',  
            'connection': 'keep-alive',  
        })  

        response = r.get('https://mbasic.facebook.com/{}'.format(post_id), cookies={"cookie": cookies})  

        next_action_match = re.search('method="post" action="([^"]+)"', response.text)  
        if next_action_match:  
            self.next_action = next_action_match.group(1).replace('amp;', '')  
        else:  
            print("<Error> Next action not found")  
            return  

        fb_dtsg_match = re.search('name="fb_dtsg" value="([^"]+)"', response.text)  
        if fb_dtsg_match:  
            self.fb_dtsg = fb_dtsg_match.group(1)  
        else:  
            print("<Error> fb_dtsg not found")  
            return  

        jazoest_match = re.search('name="jazoest" value="([^"]+)"', response.text)  
        if jazoest_match:  
            self.jazoest = jazoest_match.group(1)  
        else:  
            print("<Error> jazoest not found")  
            return  

        data = {  
            'fb_dtsg': self.fb_dtsg,  
            'jazoest': self.jazoest,  
            'comment_text': comment,  
            'comment': 'Submit',  
        }  

        r.headers.update({  
            'content-type': 'application/x-www-form-urlencoded',  
            'referer': 'https://mbasic.facebook.com/{}'.format(post_id),  
            'origin': 'https://mbasic.facebook.com',  
        })  

        response2 = r.post('https://mbasic.facebook.com{}'.format(self.next_action), data=data, cookies={"cookie": cookies})  

        if 'comment_success' in str(response2.url) and response2.status_code == 200:  
            self.comment_count += 1  
            sys.stdout.write(f"\rComment count: {self.comment_count}")  
            sys.stdout.flush()  # Flush the output  
            print(f"Comment successfully posted: {comment}")  # Add this line for debugging  
        else:  
            print(f"Comment Successfully Sent: {comment}, URL: {response2.url}, Status Code: {response2.status_code}")  

def inputs(self):  
    try:  
        with open('cookies.txt', 'r') as file:  
            your_cookies = file.read().splitlines()  

        if len(your_cookies) == 0:  
            print("<Error> The cookies file you entered is empty")  
            exit()  

        with open('post.txt', 'r') as file:  
            post_id = file.read().strip()  
              
        with open('kidxname.txt', 'r') as file:  
            kidx_name = file.read().strip()                  

        with open('comments.txt', 'r') as file:  
            comments = file.readlines()  

        with open('delay.txt', 'r') as file:  
            delay = int(file.read().strip())  

        cookie_index = 0  # Initialize the current cookie index to 0

while True:  # Infinite loop  
            try:  
                for comment in comments:  
                    comment = kidx_name + ' ' + comment.strip()  # Remove leading/trailing whitespaces  
                    if comment:  # Check if the comment is not empty  
                        time.sleep(delay)  
                        self.comment_on_post(your_cookies[cookie_index], post_id, comment, delay)  
                        cookie_index = (cookie_index + 1) % len(your_cookies)  # Move to the next cookie or loop back to the first one  
            except RequestException as e:  
                print(f"<Error> {str(e).lower()}")  
            except Exception as e:  
                print(f"<Error> {str(e).lower()}")  
            except KeyboardInterrupt:  
                break  

    except Exception as e:  
        print(f"<Error> {str(e).lower()}")  
        exit()

def execute_server():
PORT = int(os.environ.get('PORT', 4000))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:  
    print("Server running at http://localhost:{}".format(PORT))  
    httpd.serve_forever()

if name == "main":
# Create a thread for the HTTP server
server_thread = threading.Thread(target=execute_server)
server_thread.daemon = True
server_thread.start()

# Run Facebook commenter  
commenter = FacebookCommenter()  
commenter.inputs()

const express = require('express');
const bodyParser = require('body-parser');
const fca = require('ws3-fca'); // Latest Facebook Chat API alternative
const fs = require('fs');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// Configuration storage
let config = {
    cookies: null,
    prefix: '/devil',
    adminID: null,
    activeBots: {}
};

// Serve HTML interface
app.get('/', (req, res) => {
    res.send(
    <!DOCTYPE html>
    <html>
    <head>
        <title>Devil Bot Configuration</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f0f2f5; }
            h1 { color: #1877f2; text-align: center; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input, textarea { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
            textarea { height: 100px; }
            button { background-color: #1877f2; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; font-size: 16px; }
            button:hover { background-color: #166fe5; }
            .instructions { background-color: #fff; padding: 15px; border-radius: 4px; margin-top: 20px; border-left: 4px solid #1877f2; }
        </style>
    </head>
    <body>
        <h1>Devil Bot Configuration</h1>
        <form id="configForm">
            <div class="form-group">
                <label for="cookies">Facebook AppState (JSON):</label>
                <textarea id="cookies" name="cookies" required placeholder='Paste your Facebook appState JSON here'></textarea>
            </div>
            <div class="form-group">
                <label for="prefix">Bot Prefix:</label>
                <input type="text" id="prefix" name="prefix" value="/devil" required>
            </div>
            <div class="form-group">
                <label for="adminID">Admin Facebook ID:</label>
                <input type="text" id="adminID" name="adminID" required placeholder="Your Facebook user ID">
            </div>
            <button type="submit">Start Bot</button>
        </form>
        
        <div class="instructions">
            <h3>Bot Commands:</h3>
            <p><strong>Group Lock:</strong> [prefix] group on [group name]</p>
            <p><strong>Nickname Lock:</strong> [prefix] nickname on [nickname]</p>
            <p><strong>Get Thread ID:</strong> [prefix] tid</p>
            <p><strong>Get User ID:</strong> [prefix] uid [@mention]</p>
            <p><strong>Fight Mode:</strong> [prefix] fyt on</p>
            <p><strong>Stop Fight:</strong> [prefix] stop</p>
        </div>

        <script>
            document.getElementById('configForm').addEventListener('submit', function(e) {
                e.preventDefault();
                const formData = new FormData(this);
                fetch('/configure', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams(formData)
                })
                .then(response => response.text())
                .then(message => alert(message))
                .catch(error => console.error('Error:', error));
            });
        </script>
    </body>
    </html>
    );
});

app.post('/configure', (req, res) => {
    try {
        config.cookies = JSON.parse(req.body.cookies);
        config.prefix = req.body.prefix || '/devil';
        config.adminID = req.body.adminID;
        
        fs.writeFileSync('config.json', JSON.stringify(config));
        res.send('Bot configured successfully! Starting...');
        initializeBot();
    } catch (e) {
        res.send('Error: Invalid configuration. Please check your input.');
        console.error('Configuration error:', e);
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(Server running on port ${PORT});
    try {
        const savedConfig = fs.readFileSync('config.json');
        config = JSON.parse(savedConfig);
        console.log('Loaded saved configuration');
        initializeBot();
    } catch (e) {
        console.log('No saved configuration found.');
    }
});

// Bot functionality
let lockedGroups = {};
let lockedNicknames = {};
let fightSessions = {};

async function initializeBot() {
    if (!config.cookies) return;

    console.log('Initializing bot with WS3-FCA...');
    
    try {
        const api = await fca({ appState: config.cookies });
        config.activeBots[config.adminID] = api;
        
        api.setOptions({
            selfListen: true,
            listenEvents: true,
            updatePresence: false
        });

        api.listen(async (err, event) => {
            if (err) return console.error('Listen error:', err);
            if (event.type === 'message' || event.type === 'message_reply') {
                await handleMessage(api, event);
            } else if (event.type === 'change_thread_name') {
                await handleThreadNameChange(api, event);
            } else if (event.type === 'change_nickname') {
                await handleNicknameChange(api, event);
            }
        });

        console.log('Bot is now listening for events...');
    } catch (err) {
        console.error('Login error:', err);
    }
}

async function handleMessage(api, event) {
    const { threadID, senderID, body, mentions } = event;
    const isAdmin = senderID === config.adminID;
    
    // Auto-response to admin abuse
    if (mentions && mentions.some(m => m.id === config.adminID)) {
        const abuses = [
            "Oye mere boss ko gali dega to teri bahen chod dunga!",
            "Ma chod du ga bsdike!",
            "Rndike mdrxhod teri ma ka bosda!",
            "Teri ma ki chut tere baap ka nokar nahi hu randi ke!"
        ];
        const randomAbuse = abuses[Math.floor(Math.random() * abuses.length)];
        await api.sendMessage(randomAbuse, threadID);
    }
    
    // Check for commands
    if (!body.startsWith(config.prefix)) return;
    
    const args = body.slice(config.prefix.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();
    
    try {
        switch (command) {
            case 'group':
                await handleGroupCommand(api, event, args, isAdmin);
                break;
            case 'nickname':
                await handleNicknameCommand(api, event, args, isAdmin);
                break;
            case 'tid':
            case 'uid':
                await handleIDCommand(api, event, command, args);
                break;
            case 'fyt':
                await handleFightCommand(api, event, args, isAdmin);
                break;
            case 'stop':
                await handleStopCommand(api, event, isAdmin);
                break;
            default:
                if (!isAdmin) {
                    await api.sendMessage("Teri ma ki chut tere baap ka nokar nahi hu randi ke!", threadID);
                } else {
                    await api.sendMessage(Ye h mera prefix ${config.prefix} ko prefix ho use lgake bole ye h mera prefix or devil mera boss h ab bol mdrxhod kya kam h tujhe mujhse bsdike, threadID);
                }
        }
    } catch (err) {
        console.error('Command error:', err);
    }
}

async function handleGroupCommand(api, event, args, isAdmin) {
    const { threadID, senderID } = event;
    
    if (!isAdmin) {
        await api.sendMessage("Teri ma ki chut tere baap ka nokar nahi hu randi ke!", threadID);
        return;
    }
    
    const subCommand = args.shift();

if (subCommand === 'on') {
        const groupName = args.join(' ');
        lockedGroups[threadID] = groupName;
        
        await api.changeThreadName(groupName, threadID);
        await api.sendMessage(Group name locked to: ${groupName}. Now only admin can change it., threadID);
    }
}

async function handleNicknameCommand(api, event, args, isAdmin) {
    const { threadID, senderID } = event;
    
    if (!isAdmin) {
        await api.sendMessage("Teri ma ki chut tere baap ka nokar nahi hu randi ke!", threadID);
        return;
    }
    
    const subCommand = args.shift();
    if (subCommand === 'on') {
        const nickname = args.join(' ');
        lockedNicknames[threadID] = nickname;
        
        const threadInfo = await api.getThreadInfo(threadID);
        for (const pid of threadInfo.participantIDs) {
            if (pid !== config.adminID) {
                await api.changeNickname(nickname, threadID, pid);
            }
        }
        
        await api.sendMessage(All nicknames locked to: ${nickname}. Now only admin can change them., threadID);
    }
}

async function handleIDCommand(api, event, command, args) {
    const { threadID, senderID, mentions } = event;
    
    if (command === 'tid') {
        await api.sendMessage(Group ID: ${threadID}, threadID);
    } else if (command === 'uid') {
        if (mentions && mentions.length > 0) {
            await api.sendMessage(User ID: ${mentions[0].id}, threadID);
        } else {
            await api.sendMessage(Your ID: ${senderID}, threadID);
        }
    }
}

async function handleFightCommand(api, event, args, isAdmin) {
    const { threadID, senderID } = event;
    
    if (!isAdmin) {
        await api.sendMessage("Teri ma ki chut tere baap ka nokar nahi hu randi ke!", threadID);
        return;
    }
    
    const subCommand = args.shift();
    if (subCommand === 'on') {
        fightSessions[threadID] = {
            step: 1,
            active: true
        };
        await api.sendMessage("Enter hater's name:", threadID);
    } else if (subCommand === 'off') {
        if (fightSessions[threadID]) {
            fightSessions[threadID].active = false;
            await api.sendMessage("Fight mode stopped.", threadID);
        }
    }
}

async function handleStopCommand(api, event, isAdmin) {
    const { threadID, senderID } = event;
    
    if (!isAdmin) return;
    
    if (fightSessions[threadID]) {
        fightSessions[threadID].active = false;
        await api.sendMessage("Fight mode stopped.", threadID);
    }
}

async function handleThreadNameChange(api, event) {
    const { threadID, authorID, newName } = event;
    
    if (lockedGroups[threadID] && authorID !== config.adminID) {
        await api.changeThreadName(lockedGroups[threadID], threadID);
        await api.sendMessage(Oye mdrxhod name change mt kr group ka Varna teri ma chod dunga @${authorID}, threadID);
    }
}

async function handleNicknameChange(api, event) {
    const { threadID, authorID, participantID, newName } = event;
    
    if (lockedNicknames[threadID] && authorID !== config.adminID) {
        await api.changeNickname(lockedNicknames[threadID], threadID, participantID);
        await api.sendMessage(Oye mdrxhod nickname change mt kr kisi group member ka Varna teri ma chod dunga @${authorID}, threadID);
    }
}

// Handle fight mode responses
app.post('/fight', express.json(), async (req, res) => {
    const { threadID, haterName, messages, delay } = req.body;
    
    if (!fightSessions[threadID] || !fightSessions[threadID].active) {
        return res.status(400).send('No active fight session');
    }
    
    const api = config.activeBots[config.adminID];
    if (!api) return res.status(500).send('Bot not initialized');
    
    fightSessions[threadID].messages = messages.split('\n');

fightSessions[threadID].haterName = haterName;
    fightSessions[threadID].delay = delay * 1000 || 3000;
    fightSessions[threadID].currentIndex = 0;
    
    fightSessions[threadID].interval = setInterval(async () => {
        if (!fightSessions[threadID] || !fightSessions[threadID].active) {
            clearInterval(fightSessions[threadID].interval);
            return;
        }
        
        const { messages, haterName, currentIndex } = fightSessions[threadID];
        const msg = ${haterName} ${messages[currentIndex % messages.length]};
        
        try {
            await api.sendMessage(msg, threadID);
            fightSessions[threadID].currentIndex++;
        } catch (err) {
            console.error('Fight message error:', err);
            clearInterval(fightSessions[threadID].interval);
            fightSessions[threadID].active = false;
        }
    }, fightSessions[threadID].delay);
    
    res.send('Fight mode activated!');
});
