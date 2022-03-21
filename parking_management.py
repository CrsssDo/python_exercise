from datetime import datetime
import query
import export
import validate
import connection

while True:
    connection.create_table()
    print('''\n
        <<--------------Parking Management------------->
        1.Thêm xe vào.
        2.Hiển thị danh sách xe.
        3.Thành tiền.
        4.Xuất báo cáo.
        0.Thoát chương trình
    ''')


    select = input("Mời nhập lựa chọn: ")

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break

        if select == 1:
            type = input("Mời nhập loại phương tiện: ")
            plate = str(input("Mời nhập biển số xe: ")) 
            time = datetime.now()
            #Ex: 50 E1 77777 || 59 AB 1111 || 55 A 88888
            if(validate.validate_plate(plate)):
                #kiểm tra tồn tại dữ liệu
                if(query.is_exists(plate)):
                    print("--> Xe hiện đã tổn tại trong hệ thống")
                else:
                #lưu dữ liệu vào db
                    query.insert_vehicle_information(type,plate,time)
            else:
                print("---> Biển số xe không hợp lệ")

        if select == 2:
            results = query.get_all()
            print(results['type'] +' | '+ results['plate'])
            print("--> Số xe hiện có: ", len(results))

        if select == 3:
            check_out_vehicle = input("Mời nhập biển số xe: ")
            query.total_money(check_out_vehicle)

        if select == 4:
            export.export_report()
            



        

