# Tạo một danh sách sản phẩm rỗng
products = []

# Hàm hiển thị danh sách sản phẩm
def display_products():
    print("Danh sách sản phẩm:")
    if not products:
        print("Không có sản phẩm nào.")
    else:
        for index, product in enumerate(products):
            print(f"{index+1}. {product}")

# Hàm thêm sản phẩm mới
def add_product():
    product = input("Nhập tên sản phẩm: ")
    products.append(product)
    print(f"Đã thêm sản phẩm '{product}' vào danh sách.")

# Hàm sửa tên sản phẩm
def edit_product():
    index = int(input("Nhập số thứ tự của sản phẩm muốn sửa: "))
    if index < 1 or index > len(products):
        print("Số thứ tự không hợp lệ.")
    else:
        new_name = input("Nhập tên mới cho sản phẩm: ")
        products[index-1] = new_name
        print(f"Đã đổi tên sản phẩm thành '{new_name}'.")

# Hàm xoá sản phẩm
def delete_product():
    index = int(input("Nhập số thứ tự của sản phẩm muốn xoá: "))
    if index < 1 or index > len(products):
        print("Số thứ tự không hợp lệ.")
    else:
        product = products.pop(index-1)
        print(f"Đã xoá sản phẩm '{product}' khỏi danh sách.")

# Vòng lặp chính của chương trình
while True:
    print("\nChọn một trong các chức năng sau:")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Sửa tên sản phẩm")
    print("4. Xoá sản phẩm")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn (1-5): ")
    
    if choice == "1":
        display_products()
    elif choice == "2":
        add_product()
    elif choice == "3":
        edit_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
