import socket
import threading
import tkinter as tk
from tkinter import scrolledtext



def start_server(host = "127.0.0.1", port = 65432, text_callback  = None):
    def handle_client(conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if text_callback:
                text_callback(data.decode())


    def server_thread():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Server listening on {host}:{port}") 
            while True:
                conn,addr = s.accept()
                threading.Thread(target=handle_client, args = (conn, ), daemon = True).start()

    server_thread_instance = threading.Thread(target=server_thread, daemon=True)
    server_thread_instance.start()


   
def main():
    root = tk.Tk()
    root.title("TCP output")
    txt = scrolledtext.ScrolledText(root, width= 40, height = 10 , state = "disabled")
    txt.pack(padx = 10, pady = 10)
    

    def append_text(msg):
        txt.config(state = "normal")
        txt.insert("end" , msg + "\n")
        txt.config(state = "disabled")


    root.after(500, lambda: start_server(text_callback=append_text))
   
    root.mainloop()

if __name__ == "__main__":
    main()    