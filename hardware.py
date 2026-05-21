# # hardware.py
# import serial
# import time
# import threading
# import config  # Gọi file cài đặt để lấy cổng COM

# # Tạo 2 biến rơ-le số toàn cục để bên ngoài main.py có thể đọc được
# den_vang_sang = False
# den_do_sang = False

# def luong_doc_arduino():
#     global den_vang_sang, den_do_sang
#     try:
#         # Lấy thông số CONG_COM và TOC_DO từ file config ra dùng
#         arduino = serial.Serial(port=config.CONG_COM, baudrate=config.TOC_DO, timeout=1)
#         time.sleep(2)
#         print("-> Đã kết nối với Arduino thành công!")
        
#         while True:
#             if arduino.in_waiting > 0:
#                 dong_chu = arduino.readline().decode('utf-8').strip()
#                 mang_du_lieu = dong_chu.split(',')
#                 if len(mang_du_lieu) == 2:
#                     den_vang_sang = (mang_du_lieu[0] == "1")
#                     den_do_sang   = (mang_du_lieu[1] == "1")
#             time.sleep(0.05)
            
#     except Exception as e:
#         print(f"LỖI KẾT NỐI ARDUINO: {e}")

# # Tự động kích hoạt luồng chạy ngầm ngay khi file này được gọi
# threading.Thread(target=luong_doc_arduino, daemon=True).start()

# hardware.py (Bản mô phỏng không cần Arduino thật)
import time
import threading
import keyboard  # Dùng phím cơ trên máy tính để giả lập cảm biến

# 2 rơ-le số vẫn giữ nguyên để main.py đọc
den_vang_sang = False
den_do_sang = False

def luong_gia_lap_arduino():
    global den_vang_sang, den_do_sang
    print("\n=== CHẾ ĐỘ MÔ PHỎNG ARDUINO ===")
    print("Bấm phím [F1]: Giả lập Máy rảnh (Đèn Vàng bật, Đỏ tắt)")
    print("Bấm phím [F2]: Giả lập Máy lỗi   (Đèn Đỏ bật, Vàng tắt)")
    print("Bấm phím [F3]: Giả lập Máy bận   (Cả 2 đèn đều tắt)")
    print("===============================\n")
    
    while True:
        if keyboard.is_pressed('f1'):
            den_vang_sang = True
            den_do_sang = False
            print("\n-> [MÔ PHỎNG] Đã chuyển trạng thái: ĐÈN VÀNG SÁNG (Máy rảnh)")
            time.sleep(0.5) # Chống dội phím
            
        elif keyboard.is_pressed('f2'):
            den_vang_sang = False
            den_do_sang = True
            print("\n-> [MÔ PHỎNG] Đã chuyển trạng thái: ĐÈN ĐỎ SÁNG (Máy lỗi)")
            time.sleep(0.5)
            
        elif keyboard.is_pressed('f3'):
            den_vang_sang = False
            den_do_sang = False
            print("\n-> [MÔ PHỎNG] Đã chuyển trạng thái: CẢ 2 ĐÈN TẮT (Máy bận)")
            time.sleep(0.5)
            
        time.sleep(0.05)

# Kích hoạt luồng mô phỏng chạy ngầm
threading.Thread(target=luong_gia_lap_arduino, daemon=True).start()