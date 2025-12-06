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