import tkinter as tk #import thư viện tkinter
# Khởi tạo các thuộc tính của Process
class Process:
    def __init__(self):
        self.pid = 0 #id của các tiến trình
        self.arrival_time = 0
        self.burst_time = 0
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0 
        self.response_time = 0

def calculate_processes():
    n = int(entry_processes.get())
    #lưu các thông số từ các entry vào các tiến trình tương ứng trong mảng processes
    processes = [{'pid': i + 1, 'arrival_time': int(process_entry[i].get()), 'burst_time': int(burst_entry[i].get()), 'burst': int(burst_entry[i].get())} for i in range(n)]
    is_completed = [0] * n

    current_time = 0
    completed = 0
    # arr=[0]*n
    total_turnaround_time = 0
    total_waiting_time = 0
    #Lặp qua các tiến trình đến khi completed = n
    while completed != n:
        min_rst = float('inf')
        idx = -1

        for i in range(n):
            if processes[i]['arrival_time'] <= current_time and is_completed[i] == 0:
                if processes[i]['burst_time'] <min_rst: 
                    min_rst = processes[i]['burst_time']
                    # arr[i]=processes[i]['burst_time']
                    idx = i
        if idx != -1:
            processes[idx]['start_time'] = current_time
            current_time += 1
            processes[idx]['burst_time'] -= 1

            if processes[idx]['burst_time'] == 0:
                processes[idx]['completion_time'] = current_time
                processes[idx]['turnaround_time'] = processes[idx]['completion_time'] - processes[idx]['arrival_time']
                processes[idx]['waiting_time'] = processes[idx]['turnaround_time'] - processes[idx]['burst']
                total_turnaround_time += processes[idx]['turnaround_time'] 
                total_waiting_time += processes[idx]['waiting_time']
                is_completed[idx] = 1
                completed += 1
        else:
            current_time += 1

    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n

    # hiển thị kết quả
    result_text = "\nPrc\tAT\tBT\tTAT\tWT\tCT\n"
    for p in processes:
        result_text += f"{p['pid']}\t{p['arrival_time']}\t{int(burst_entry[p['pid']-1].get())}\t{p['turnaround_time']}\t{p['waiting_time']}\t{p['completion_time']}\n\n"
    
    result_text += f"Trung bình thời gian lưu lại hệ thống = {avg_turnaround_time}\nThời gian chờ trung bình = {avg_waiting_time}\n"
    result_label.config(text=result_text)

# tạo giao diện
root = tk.Tk()
root.title("Process Calculation")
root.geometry("800x600")
label_processes = tk.Label(root, pady=24,text="Nhập số tiến trình: ")
label_processes.pack()

entry_processes = tk.Entry(root, width=100)
entry_processes.pack()

process_entry = []
burst_entry = []

#hàm tạo entry thời gian xuất hiện và thời gian sử dụng cpu ứng với mỗi tiến trình
def create_process_entries():
    global n
    n = int(entry_processes.get())
    for i in range(n): 
        process_label = tk.Label(root, text=f"Thời điểm xuất hiện {i+1}:")
        process_label.pack()
        process = tk.Entry(root, width=100) 
        process.pack()
        process_entry.append(process)
        
        burst_label = tk.Label(root, text=f"Thời gian sử dụng CPU {i+1}:")
        burst_label.pack()
        burst = tk.Entry(root, width=100)
        burst.pack()
        burst_entry.append(burst)

    calculate_button.pack()

calculate_button = tk.Button(root, text="Tạo bảng", command=create_process_entries)
calculate_button.pack()

calculate_button = tk.Button(root, text="Tính giá trị", command=calculate_processes)
calculate_button.pack()

# Thêm chú thích hiện lên giao diện
description_label = tk.Label(root, text="Prc  :  Tiến trình\nAT   :  Thời điểm xuất hiện\nBT   :  Thời gian sử dụng CPU\nTAT :  Thời gian lưu lại\nWT  :  Thời gian chờ\nCT   :  Thời gian hoàn thành", anchor="w", justify="left")
description_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
