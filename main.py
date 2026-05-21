# main.py
import time
import mouse
import keyboard
import config    # Nhập các thông số tọa độ chuột
import hardware  # Nhập dữ liệu đèn từ Arduino

print("\nHỆ THỐNG SẴN SÀNG! Vui lòng quét mã Barcode...")

while True:
    ma_lot_quet_duoc = input("\n[INPUT] Nhận dữ liệu từ máy quét: ")
    if not ma_lot_quet_duoc:
        continue

    # KIỂM TRA KHÓA AN TOÀN TRƯỚC KHI CHẠY (Lấy dữ liệu từ file hardware)
    
    # Trường hợp 1: Máy lỗi (Đèn đỏ sáng)
    if hardware.den_do_sang == True:
        print(" [CẢNH BÁO ĐỎ] Không thể nạp mã! Máy đang bị lỗi sự cố.")
        
    # Trường hợp 2: Máy rảnh (Đèn vàng sáng, đỏ tắt) -> THỎA MÃN CHẠY
    elif hardware.den_vang_sang == True and hardware.den_do_sang == False:
        print(f" [MÁY RẢNH] Hợp lệ! Đang tự động nạp mã: {ma_lot_quet_duoc}")
        
        # --- BẮT ĐẦU ĐIỀU KHIỂN CHUỘT/BÀN PHÍM (Lấy tọa độ từ file config) ---
        mouse.move(config.TOA_DO_X, config.TOA_DO_Y, absolute=True, duration=0.2)
        mouse.click(button='left')
        time.sleep(config.DELAY_CLICK)
        
        keyboard.send('ctrl+a')
        keyboard.send('backspace')
        time.sleep(0.05)
        
        keyboard.write(ma_lot_quet_duoc, delay=config.DELAY_GO_PHIM)
        time.sleep(0.1)
        
        keyboard.send('tab')
        time.sleep(0.1)
        
        keyboard.send('enter')
        print("-> Đã hoàn thành tự động nhập và kích hoạt Recipe!")

    # Trường hợp 3: Máy đang bận chạy (Cả vàng và đỏ đều tắt)
    else:
        print(" [CẢNH BÁO VÀNG] Không thể nạp mã! Máy đang bận chạy sản phẩm cũ.")