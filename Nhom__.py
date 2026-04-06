import datetime
import json



# Danh sách lưu trữ học sinh
danh_sach_hoc_sinh = []

# Các môn học và hệ số
MON_HOC = {
    'Toán': 2,
    'Lý': 1,
    'Hóa': 1,
    'Anh': 1,
    'Sinh': 1,
    'Anh': 1,
    'Sử': 1
}

def kiem_tra_ngay_sinh(ngay_sinh):
    """Kiểm tra định dạng ngày sinh dd/mm/yyyy"""
    try:
        ngay, thang, nam = map(int, ngay_sinh.split('/'))
        datetime.datetime(nam, thang, ngay)
        if 1926 < nam < 2026:
            return True
    except:
        return False

def nhap_so_luong_hoc_sinh():
    """Nhập số lượng học sinh ban đầu"""
    while True:
        try:
            n = int(input("Nhập số lượng học sinh: "))
            if n > 0:
                return n
            else:
                print("Số lượng học sinh phải lớn hơn 0!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

def nhap_thong_tin_hoc_sinh():
    """Nhập thông tin cho một học sinh"""
    while True:
        ho_ten = input("Nhập họ và tên: ").strip()
        if "".join(ho_ten.split()).isalpha():
            break
        print("Tên không khả dụng, vui lòng nhập lại!")
    
    while True:
        gioi_tinh = input("Nhập giới tính (Nam/Nữ): ").strip()
        if gioi_tinh in ["Nam", "Nữ"]:
            break
        print("Giới tính chỉ nhận 'Nam' hoặc 'Nữ'!")
    
    while True:
        ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ").strip()
        if kiem_tra_ngay_sinh(ngay_sinh):
            break
        print("Ngày sinh không đúng định dạng, vui lòng nhập lại!")
    
    diem_mon = {}
    for mon in MON_HOC:
        print(f"\nNhập điểm môn {mon}:")
        while True:
            try:
                diem_hk1 = float(input("Điểm HK1: "))
                if 0 <= diem_hk1 <= 10:
                    break
                print("Điểm phải từ 0 đến 10!")
            except ValueError:
                print("Vui lòng nhập số!")
        
        while True:
            try:
                diem_hk2 = float(input("Điểm HK2: "))
                if 0 <= diem_hk2 <= 10:
                    break
                print("Điểm phải từ 0 đến 10!")
            except ValueError:
                print("Vui lòng nhập số!")
        
        diem_mon[mon] = (diem_hk1, diem_hk2)
    
    return {
        'ho_ten': ho_ten,
        'gioi_tinh': gioi_tinh,
        'ngay_sinh': ngay_sinh,
        'diem_mon': diem_mon
    }

def tinh_diem_trung_binh_hk(diem_mon, hoc_ky):
    """Tính điểm trung bình học kỳ"""
    tong_diem = 0
    tong_he_so = 0
    
    for mon, he_so in MON_HOC.items():
        diem = diem_mon[mon][0] if hoc_ky == 1 else diem_mon[mon][1]
        tong_diem += diem * he_so
        tong_he_so += he_so
    
    return tong_diem / tong_he_so if tong_he_so > 0 else 0

def tinh_diem_trung_binh_ca_nam(diem_mon):
    """Tính điểm trung bình cả năm"""
    diem_tb_hk1 = tinh_diem_trung_binh_hk(diem_mon, 1)
    diem_tb_hk2 = tinh_diem_trung_binh_hk(diem_mon, 2)
    return (diem_tb_hk1 + diem_tb_hk2 * 2) / 3

def xep_loai_hoc_sinh(diem_tb_ca_nam):
    """Xếp loại học sinh dựa trên điểm trung bình cả năm"""
    if diem_tb_ca_nam >= 8.0:
        return "Giỏi"
    elif diem_tb_ca_nam >= 6.5:
        return "Khá"
    elif diem_tb_ca_nam >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def tinh_tuoi(ngay_sinh):
    """Tính tuổi đến năm 2026"""
    ngay, thang, nam = map(int, ngay_sinh.split('/'))
    return 2026 - nam

def them_hoc_sinh():
    """Thêm học sinh mới"""
    hoc_sinh = nhap_thong_tin_hoc_sinh()
    danh_sach_hoc_sinh.append(hoc_sinh)
    print("Thêm học sinh thành công!")

def xoa_hoc_sinh():
    """Xóa học sinh theo tên"""
    ten = input("Nhập tên học sinh cần xóa: ").strip()
    found = False
    
    for i, hs in enumerate(danh_sach_hoc_sinh):
        if hs['ho_ten'].lower() == ten.lower():
            del danh_sach_hoc_sinh[i]
            print(f"Đã xóa học sinh {ten}")
            found = True
            break
    
    if not found:
        print(f"Không tìm thấy học sinh {ten}")

def sua_thong_tin_hoc_sinh():
    """Sửa thông tin học sinh"""
    ten = input("Nhập tên học sinh cần sửa: ").strip()
    found = False
    
    for i, hs in enumerate(danh_sach_hoc_sinh):
        if hs['ho_ten'].lower() == ten.lower():
            print("Nhập thông tin mới (ấn Enter để giữ nguyên):")
            
            # Sửa họ tên
            ho_ten_moi = input(f"Họ tên hiện tại: {hs['ho_ten']} -> Mới: ").strip()
            if ho_ten_moi:
                hs['ho_ten'] = ho_ten_moi
            
            # Sửa giới tính
            while True:
                gioi_tinh_moi = input(f"Giới tính hiện tại: {hs['gioi_tinh']} -> Mới (Nam/Nữ): ").strip()
                if not gioi_tinh_moi:
                    break
                if gioi_tinh_moi in ["Nam", "Nữ"]:
                    hs['gioi_tinh'] = gioi_tinh_moi
                    break
                print("Giới tính chỉ nhận 'Nam' hoặc 'Nữ'!")
            
            # Sửa ngày sinh
            while True:
                ngay_sinh_moi = input(f"Ngày sinh hiện tại: {hs['ngay_sinh']} -> Mới (dd/mm/yyyy): ").strip()
                if not ngay_sinh_moi:
                    break
                if kiem_tra_ngay_sinh(ngay_sinh_moi):
                    hs['ngay_sinh'] = ngay_sinh_moi
                    break
                print("Ngày sinh không đúng định dạng!")
            
            # Sửa điểm
            for mon in MON_HOC:
                print(f"\nSửa điểm môn {mon}:")
                print(f"Điểm hiện tại: HK1={hs['diem_mon'][mon][0]}, HK2={hs['diem_mon'][mon][1]}")
                
                # Sửa điểm HK1
                while True:
                    diem_hk1_moi = input("Điểm HK1 mới (Enter để giữ nguyên): ").strip()
                    if not diem_hk1_moi:
                        break
                    try:
                        diem = float(diem_hk1_moi)
                        if 0 <= diem <= 10:
                            hs['diem_mon'][mon] = (diem, hs['diem_mon'][mon][1])
                            break
                        print("Điểm phải từ 0 đến 10!")
                    except ValueError:
                        print("Vui lòng nhập số!")
                
                # Sửa điểm HK2
                while True:
                    diem_hk2_moi = input("Điểm HK2 mới (Enter để giữ nguyên): ").strip()
                    if not diem_hk2_moi:
                        break
                    try:
                        diem = float(diem_hk2_moi)
                        if 0 <= diem <= 10:
                            hs['diem_mon'][mon] = (hs['diem_mon'][mon][0], diem)
                            break
                        print("Điểm phải từ 0 đến 10!")
                    except ValueError:
                        print("Vui lòng nhập số!")
            
            print("Sửa thông tin thành công!")
            found = True
            break
    
    if not found:
        print(f"Không tìm thấy học sinh {ten}")

def hien_thi_danh_sach():
    """Hiển thị danh sách học sinh"""
    if not danh_sach_hoc_sinh:
        print("Danh sách học sinh trống!")
        return
    
    print("\n" + "="*100)
    print(f"{'STT':<5}{'Họ tên':<20}{'Giới tính':<10}{'Ngày sinh':<12}{'ĐTB HK1':<8}{'ĐTB HK2':<8}{'ĐTB CN':<8}{'Xếp loại':<12}{'Tuổi 2026':<10}")
    print("="*100)
    
    for i, hs in enumerate(danh_sach_hoc_sinh, 1):
        diem_tb_hk1 = tinh_diem_trung_binh_hk(hs['diem_mon'], 1)
        diem_tb_hk2 = tinh_diem_trung_binh_hk(hs['diem_mon'], 2)
        diem_tb_ca_nam = tinh_diem_trung_binh_ca_nam(hs['diem_mon'])
        xep_loai = xep_loai_hoc_sinh(diem_tb_ca_nam)
        tuoi = tinh_tuoi(hs['ngay_sinh'])
        
        print(f"{i:<5}{hs['ho_ten']:<20}{hs['gioi_tinh']:<10}{hs['ngay_sinh']:<12}"
              f"{diem_tb_hk1:<8.2f}{diem_tb_hk2:<8.2f}{diem_tb_ca_nam:<8.2f}"
              f"{xep_loai:<12}{tuoi:<10}")

def tinh_diem_va_xep_loai():
    """Tính điểm và xếp loại cho tất cả học sinh"""
    if not danh_sach_hoc_sinh:
        print("Danh sách học sinh trống!")
        return
    
    print("\nKết quả học tập:")
    print("="*80)
    print(f"{'Họ tên':<20}{'ĐTB HK1':<8}{'ĐTB HK2':<8}{'ĐTB CN':<8}{'Xếp loại':<12}")
    print("="*80)
    
    for hs in danh_sach_hoc_sinh:
        diem_tb_hk1 = tinh_diem_trung_binh_hk(hs['diem_mon'], 1)
        diem_tb_hk2 = tinh_diem_trung_binh_hk(hs['diem_mon'], 2)
        diem_tb_ca_nam = tinh_diem_trung_binh_ca_nam(hs['diem_mon'])
        xep_loai = xep_loai_hoc_sinh(diem_tb_ca_nam)
        
        print(f"{hs['ho_ten']:<20}{diem_tb_hk1:<8.2f}{diem_tb_hk2:<8.2f}"
              f"{diem_tb_ca_nam:<8.2f}{xep_loai:<12}")

def tinh_tuoi_hoc_sinh():
    """Tính tuổi của tất cả học sinh đến năm 2026"""
    if not danh_sach_hoc_sinh:
        print("Danh sách học sinh trống!")
        return
    
    print("\nTuổi học sinh đến năm 2026:")
    print("="*40)
    print(f"{'Họ tên':<20}{'Ngày sinh':<12}{'Tuổi':<8}")
    print("="*40)
    
    for hs in danh_sach_hoc_sinh:
        tuoi = tinh_tuoi(hs['ngay_sinh'])
        print(f"{hs['ho_ten']:<20}{hs['ngay_sinh']:<12}{tuoi:<8}")

def thong_ke_xep_loai():
    """Thống kê số lượng học sinh theo xếp loại"""
    if not danh_sach_hoc_sinh:
        print("Danh sách học sinh trống!")
        return
    
    thong_ke = {'Giỏi': 0, 'Khá': 0, 'Trung bình': 0, 'Yếu': 0}
    
    for hs in danh_sach_hoc_sinh:
        diem_tb_ca_nam = tinh_diem_trung_binh_ca_nam(hs['diem_mon'])
        xep_loai = xep_loai_hoc_sinh(diem_tb_ca_nam)
        thong_ke[xep_loai] += 1
    
    print("\nThống kê xếp loại học sinh:")
    print("="*30)
    for loai, so_luong in thong_ke.items():
        print(f"{loai}: {so_luong} học sinh")

def sap_xep_theo_diem():
    """Sắp xếp học sinh theo điểm trung bình cả năm (giảm dần)"""
    if not danh_sach_hoc_sinh:
        print("Danh sách học sinh trống!")
        return
    
    danh_sach_sap_xep = sorted(danh_sach_hoc_sinh, 
                              key=lambda hs: tinh_diem_trung_binh_ca_nam(hs['diem_mon']), 
                              reverse=True)
    
    print("\nDanh sách học sinh theo điểm (cao đến thấp):")
    print("="*80)
    print(f"{'STT':<5}{'Họ tên':<20}{'ĐTB CN':<8}{'Xếp loại':<12}")
    print("="*80)
    
    for i, hs in enumerate(danh_sach_sap_xep, 1):
        diem_tb_ca_nam = tinh_diem_trung_binh_ca_nam(hs['diem_mon'])
        xep_loai = xep_loai_hoc_sinh(diem_tb_ca_nam)
        print(f"{i:<5}{hs['ho_ten']:<20}{diem_tb_ca_nam:<8.2f}{xep_loai:<12}")

def tim_hoc_sinh_cao_diem_nhat():
    """Tìm học sinh có điểm trung bình cao nhất"""
    if not danh_sach_hoc_sinh:
        print("Danh sách học sinh trống!")
        return
    
    hs_cao_nhat = max(danh_sach_hoc_sinh, 
                      key=lambda hs: tinh_diem_trung_binh_ca_nam(hs['diem_mon']))
    
    diem_tb_ca_nam = tinh_diem_trung_binh_ca_nam(hs_cao_nhat['diem_mon'])
    xep_loai = xep_loai_hoc_sinh(diem_tb_ca_nam)
    
    print("\nHọc sinh có điểm cao nhất:")
    print("="*50)
    print(f"Họ tên: {hs_cao_nhat['ho_ten']}")
    print(f"Giới tính: {hs_cao_nhat['gioi_tinh']}")
    print(f"Ngày sinh: {hs_cao_nhat['ngay_sinh']}")
    print(f"ĐTB cả năm: {diem_tb_ca_nam:.2f}")
    print(f"Xếp loại: {xep_loai}")

# local storage
def local_storage():
    with open("data.json", "w+", encoding = "utf-8") as file:
        datas ={}
        for i, hs in enumerate(danh_sach_hoc_sinh, 1):
            diem_tb_hk1 = tinh_diem_trung_binh_hk(hs['diem_mon'], 1)
            diem_tb_hk2 = tinh_diem_trung_binh_hk(hs['diem_mon'], 2)
            diem_tb_ca_nam = tinh_diem_trung_binh_ca_nam(hs['diem_mon'])
            xep_loai = xep_loai_hoc_sinh(diem_tb_ca_nam)
            tuoi = tinh_tuoi(hs['ngay_sinh'])
            datas.update({
                "Họ và tên" : hs['ho_ten'],
                "Giới tính" : hs['gioi_tinh'],
                "Ngày sinh" : hs['ngay_sinh'],
                "Tuổi" : f"{tuoi}",
                "Điểm trung bình kì 1" : diem_tb_hk1,
                "Điểm trung bình kì 2" : diem_tb_hk2,
                "Điểm trung bình cả năm" : diem_tb_ca_nam,
                "Xếp loại" : xep_loai,
            })
            json.dump(datas, file, ensure_ascii=False, indent="\n")


def main():
    """Hàm chính chạy chương trình"""
    print("CHƯƠNG TRÌNH QUẢN LÝ HỌC SINH")
    print("="*50)
    
    # Nhập số lượng học sinh ban đầu
    n = nhap_so_luong_hoc_sinh()
    for i in range(n):
        print(f"\nNhập thông tin học sinh thứ {i+1}:")
        danh_sach_hoc_sinh.append(nhap_thong_tin_hoc_sinh())
    
    # Menu chính
    while True:
        print("\n" + "="*50)
        print("MENU CHƯƠNG TRÌNH")
        print("1. Thêm học sinh")
        print("2. Xóa học sinh (theo tên)")
        print("3. Sửa thông tin học sinh")
        print("4. Hiển thị danh sách học sinh")
        print("5. Tính điểm trung bình và xếp loại")
        print("6. Tính tuổi học sinh (đến năm 2026)")
        print("7. Thống kê số lượng học sinh theo xếp loại")
        print("8. Sắp xếp học sinh theo điểm")
        print("9. Tìm học sinh cao điểm nhất")
        print("10. Xuất danh sách học sinh ra file .json")
        print("11. Thoát chương trình")
        print("="*50)
        
        try:
            lua_chon = int(input("Chọn chức năng (1-11): "))
            
            if lua_chon == 1:
                them_hoc_sinh()
            elif lua_chon == 2:
                xoa_hoc_sinh()
            elif lua_chon == 3:
                sua_thong_tin_hoc_sinh()
            elif lua_chon == 4:
                hien_thi_danh_sach()
            elif lua_chon == 5:
                tinh_diem_va_xep_loai()
            elif lua_chon == 6:
                tinh_tuoi_hoc_sinh()
            elif lua_chon == 7:
                thong_ke_xep_loai()
            elif lua_chon == 8:
                sap_xep_theo_diem()
            elif lua_chon == 9:
                tim_hoc_sinh_cao_diem_nhat()
            elif lua_chon == 11:
                print("Cảm ơn đã sử dụng chương trình!")
                break
            elif lua_chon == 10: 
                local_storage()
                print("Đã xuất file .json thành công!")
                print("Cảm ơn đã sử dụng chương trình!")
                break
            else:
                print("Vui lòng chọn từ 1 đến 11!")
        
        except ValueError:
            print("Vui lòng nhập số!")

if __name__ == "__main__":
    main()
