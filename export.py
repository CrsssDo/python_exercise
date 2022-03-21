import pandas as pd
import query

def export_report():
    try: 

        vehicle_data  = query.get_all()

        #tính tổng tiền xe đã gửi
        vehicle_data.loc['Total'] = vehicle_data.sum(numeric_only = True, axis = 0)
        
        #viết dữ liệu vào Excel
        datatoexcel = pd.ExcelWriter('ParkingReportData.xlsx')
        
        vehicle_data.to_excel(datatoexcel)
        
        #lưu file excel
        datatoexcel.save()
        print('--> Xuất báo cáo thành công.')

    except Exception as error:
        print(error)    


