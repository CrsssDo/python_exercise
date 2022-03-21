import connection
import pandas as pd
from datetime import datetime

def get_all():
        try:
                conn = connection.create_connection()
                cursor = conn.cursor()
                query = '''select * from vehicle'''
                cursor.execute(query)
                results = cursor.fetchall()
                results = pd.DataFrame(results, columns = ['stt','type','plate','time_in','time_out','deposits'])
                conn.close()
                return results

        except Exception as error:
                print(error)

def find(data):
        try:
                conn = connection.create_connection()
                cursor = conn.cursor()
                query = f'''select * from vehicle where license_plate = '{data}' '''
                cursor.execute(query)
                results = cursor.fetchall()
                conn.close()
                return results

        except Exception as error:
                print(error)


def is_exists(data):
        check = False
        vehicle_list = find(data)
        #kiểm tra phương tiện nhập vào có tồn tại trong hệ thống hay không
        if len(vehicle_list) > 0:
                #kiểm tra nếu giá trị giờ ra là rỗng thì phương tiện vẫn đang được gửi
                for i in vehicle_list:
                        if i[4] is None:
                                check = True
        return check
        
                        

def insert_vehicle_information(type,plate,time_in):
        try:
                conn = connection.create_connection()
                cursor = conn.cursor()
                query = f'''insert into vehicle(moto_type_name,license_plate,time_in) values('{type}','{plate}','{time_in}')'''
                cursor.execute(query)
                conn.commit()
                conn.close()
                print(f"---> Đã thêm {type} biển số {plate} vào lúc {time_in}")
        

        except Exception as error:
                print(error)


def update_vehicle_information(plate,time_out,deposit):
        try:
                conn = connection.create_connection()
                cursor = conn.cursor()
                query = f'''update vehicle set time_out = '{time_out}' , deposits = '{deposit}' where license_plate = '{plate}' '''
                cursor.execute(query)
                conn.commit()
                conn.close()
        
        except Exception as error:
                print(error)

def total_money(plate):
                #trả về danh sách phương tiện với giá trị biển số nhập vào
                results = find(plate)
                time_out = datetime.now()
                cal_time_out = datetime.timestamp(time_out)
                for i in results:
                        if i[5] is None:
                                #tìm trong danh sách phương tiện chưa được thanh toán
                                cal_time_in = datetime.timestamp(i[3])
                                #tính thời gian gửi thực tế, đơn vị là giây
                                real_time = cal_time_out - cal_time_in
                                day_in = int(real_time / 86400)
                                money = 0
                                if day_in <= 1:
                                        money = 5000
                                else:
                                        money = day_in * 20000
                                print("--> Số tiền phải trả: ",money)
                                #lưu giờ ra và tiền gửi vào db
                                update_vehicle_information(plate,time_out,money)
                        else:
                                print("--> Phương tiện đã hoàn tất thanh toán")        
                
                                         

        

        
        



