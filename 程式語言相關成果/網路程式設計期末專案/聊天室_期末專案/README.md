# Python_聊天室期末專案
## 專案目標
通過 Socket 建立與伺服器的連接，並允許使用者在客戶端與伺服器之間進行文字訊息的傳遞。

## 函式庫及功能
### 函式庫 :
#### socket：用於建立網路連接、通訊和監聽連接請求的底層函式庫。
#### threading：用於創建和管理多執行緒的函式庫，用於同時處理多個客戶端的訊息。
#### time：用於時間相關的操作，例如暫停執行緒的執行。
#### os：用於與操作系統進行交互
### 函式功能 :
#### socket.socket()：建立一個 Socket 物件，用於網路通訊。
#### socket.gethostbyname()：獲取本機主機的 IP 地址。
#### input()：接收使用者的輸入。
#### socket.connect()：與指定的 IP 地址和端口建立連接。
#### socket.send()：將資料發送到連接的對等方。
#### socket.recv()：接收從對等方發送過來的資料。
#### socket.bind()：綁定 IP 地址和埠號，以監聽連接請求。
#### socket.listen()：開始監聽連接請求。
#### socket.accept()：接受連接請求，返回連接物件和客戶端地址。
#### socket.close()：關閉連接。
#### threading.Thread()：創建一個新的執行緒，用於並行執行多個任務。
#### threading.Thread.start()：啟動執行緒。
#### threading.Thread.join()：等待執行緒結束。
#### time.sleep()：暫停執行緒的執行一段時間。
