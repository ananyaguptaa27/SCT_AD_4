import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox
import qrcode
from PIL import Image, ImageTk

# Use OpenCV's built-in QRCodeDetector
def scan_qr():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if data:
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("QR Code Found", f"Data: {data}")
            return

        cv2.imshow("QR Scanner - Press Q to Quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Generate QR code
def generate_qr():
    text = simpledialog.askstring("Generate QR", "Enter text or URL:")
    if text:
        qr = qrcode.make(text)
        qr.save("generated_qr.png")

        img = Image.open("generated_qr.png")
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)

        qr_label.config(image=img)
        qr_label.image = img
        messagebox.showinfo("QR Code", "QR code saved as 'generated_qr.png'.")

# GUI setup
root = tk.Tk()
root.title("QR Scanner + Generator")

frame = tk.Frame(root)
frame.pack(pady=20)

scan_btn = tk.Button(frame, text="Scan QR Code", width=20, command=scan_qr)
scan_btn.grid(row=0, column=0, padx=10)

gen_btn = tk.Button(frame, text="Generate QR Code", width=20, command=generate_qr)
gen_btn.grid(row=0, column=1, padx=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
