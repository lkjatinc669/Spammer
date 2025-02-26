# Message Spammer 🚀

This script automates sending messages repeatedly using PyAutoGUI. It's useful for testing, pranking (ethically), or automating repetitive messages.

## ⚠️ Disclaimer
**Use this script responsibly!** Spamming can violate platform policies and lead to bans. Ensure you have permission before using it.

## 📌 Features
- Sends a specified message multiple times.
- Allows a delay before starting.
- Includes random delays between messages to simulate human behavior.
- Simple and easy-to-use command-line interface.

## 🛠 Installation
### **1️⃣ Install Dependencies**
Ensure you have Python installed, then install the required package:
```sh
pip install pyautogui
```

## 🚀 Usage
### **Basic Command**
Send a message **10 times** with a **5-second delay** before execution:
```sh
python spammer.py --message "Hello, world!" --times 10 --ttw 5
```

### **Arguments**
| Argument     | Type   | Default | Description |
|-------------|--------|---------|-------------|
| `--message` | String | Required | The message to be spammed. |
| `--times`   | Integer | `10` | Number of times to send the message. |
| `--ttw`     | Integer | `5` | Time (in seconds) to wait before spamming starts. |

### **Example Commands**
#### ✅ **Spam "Hey!" 5 times with a 3-second delay:**
```sh
python spammer.py --message "Hey!" --times 5 --ttw 3
```
#### ✅ **Spam "LOL 😂" 20 times immediately:**
```sh
python spammer.py --message "LOL 😂" --times 20 --ttw 0
```

## ⚙️ How It Works
1. **Countdown Timer** → Before execution, a countdown is shown.
2. **Typing Simulation** → PyAutoGUI types and sends the message.
3. **Random Delay** → Adds a natural delay between messages.

## ❗ Warnings
- **Avoid excessive spamming** to prevent being flagged.
- **Use responsibly** and ensure compliance with platform policies.
- **Run it in the correct chat window** (It sends messages wherever your cursor is focused!).

## 📝 Notes
- The script assumes the chat input field is **active** before execution.
- If messages appear incorrectly, try adding a small typing delay inside `p.write()`:
  ```python
  p.write(message, interval=0.05)
  ```
- Tested on **Windows & macOS**.

## 📜 License
This script is provided for **educational purposes only**. The author is not responsible for misuse.

**Happy Spamming! 🚀**
