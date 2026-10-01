<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kendi Yapay Zekam</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color: #0f172a; 
            color: #f8fafc; 
            display: flex; 
            flex-direction: column; 
            height: 100vh; 
            padding: 20px; 
        }
        .container {
            max-width: 800px;
            width: 100%;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        h1 { 
            text-align: center; 
            color: #38bdf8; 
            margin-bottom: 20px; 
            font-size: 24px; 
        }
        #chat-box { 
            flex: 1; 
            border: 1px solid #334155; 
            border-radius: 12px; 
            padding: 20px; 
            overflow-y: auto; 
            background-color: #1e293b; 
            display: flex; 
            flex-direction: column; 
            gap: 12px; 
        }
        .msg { 
            padding: 12px 16px; 
            border-radius: 10px; 
            max-width: 80%; 
            line-height: 1.5; 
            word-wrap: break-word; 
        }
        .user { 
            background-color: #0284c7; 
            color: #ffffff; 
            align-self: flex-end; 
        }
        .bot { 
            background-color: #334155; 
            color: #f8fafc; 
            align-self: flex-start; 
            white-space: pre-wrap; 
        }
        #input-container { 
            display: flex; 
            gap: 10px; 
            margin-top: 15px; 
        }
        input { 
            flex: 1; 
            padding: 14px; 
            border-radius: 8px; 
            border: 1px solid #334155; 
            background-color: #1e293b; 
            color: #fff; 
            font-size: 15px; 
            outline: none; 
        }
        input:focus {
            border-color: #38bdf8;
        }
        button { 
            padding: 14px 24px; 
            border-radius: 8px; 
            border: none; 
            background-color: #38bdf8; 
            color: #0f172a; 
            font-weight: bold; 
            cursor: pointer; 
            font-size: 15px; 
        }
        button:hover { 
            background-color: #0284c7; 
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Kendi Yapay Zekam</h1>
        <div id="chat-box"></div>
        <div id="input-container">
            <input type="text" id="user-input" placeholder="Yapay zekaya soru sor..." onkeydown="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()">Gönder</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value.trim();
            if (!message) return;

            const chatBox = document.getElementById('chat-box');
            chatBox.innerHTML += `<div class="msg user"><b>Sen:</b> ${message}</div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            const loadingId = 'loading-' + Date.now();
            chatBox.innerHTML += `<div class="msg bot" id="${loadingId}"><i>Düşünüyor...</i></div>`;
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });
                const data = await res.json();
                document.getElementById(loadingId).remove();
                chatBox.innerHTML += `<div class="msg bot"><b>Yapay Zeka:</b><br>${data.reply}</div>`;
            } catch (err) {
                document.getElementById(loadingId).innerText = 'Hata oluştu! Lütfen sunucuyu kontrol edin.';
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
