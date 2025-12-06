phonebook = []
def main():
    while True:
        print("\n--- DANH BẠ ĐIỆN THOẠI ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            interactive_add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            interactive_search_contact()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

def add_contact(name: str, phone: str) -> None:
    """
    Thêm 1 liên hệ mới vào phonebook.
    Không kiểm tra trùng lặp (có thể mở rộng).
    """
    contact = {'name': name.strip(), 'phone': phone.strip()}
    phonebook.append(contact)
    print(f"Đã thêm liên hệ: {contact['name']} - {contact['phone']}")

def interactive_add_contact() -> None:
    name = input("Nhập tên: ").strip()
    phone = input("Nhập số điện thoại: ").strip()
    if not name:
        print("Tên không được để trống.")
        return
    if not phone:
        print("Số điện thoại không được để trống.")
        return
    add_contact(name, phone)

def view_contacts() -> None:
    """
    In ra toàn bộ danh bạ. Nếu rỗng, báo rỗng.
    """
    if not phonebook:
        print("Danh bạ rỗng.")
        return
    print("\n--- DANH BẠ ---")
    for idx, c in enumerate(phonebook, start=1):
        print(f"{idx}. {c['name']} - {c['phone']}"
    print("---------------")

def search_contact(name: str) -> list:
    """
    Tìm các liên hệ có tên khớp (so sánh không phân biệt hoa/thường).
    Trả về danh sách các contact tìm được.
    """
    name_query = name.strip().lower()
    results = [c for c in phonebook if c['name'].lower() == name_query]
    return results