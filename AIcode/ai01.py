import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import pandas as pd
from datetime import datetime

def select_files():
    """打开文件对话框，选择PDF文件和Word文件"""
    global file_paths
    file_paths = filedialog.askopenfilenames(filetypes=[
        ("PDF files", "*.pdf"),
        ("Word files", "*.doc *.docx")
    ])
    file_listbox.delete(0, tk.END)  # 清空文件列表框
    for file_path in file_paths:
        file_listbox.insert(tk.END, os.path.basename(file_path))

def select_directory():
    """打开文件对话框，选择目录"""
    global file_paths
    directory = filedialog.askdirectory()
    if directory:
        file_paths = []
        file_listbox.delete(0, tk.END)  # 清空文件列表框
        for root_dir, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.pdf', '.doc', '.docx')):
                    full_path = os.path.join(root_dir, file)
                    file_paths.append(full_path)
                    file_listbox.insert(tk.END, os.path.basename(file))

def print_files():
    """批量打印选中的PDF文件和Word文件"""
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("警告", "请选择要打印的文件")
        return

    print_log = []
    output_text.delete(1.0, tk.END)  # 清空输出窗口

    for index in selected_indices:
        file_name = file_listbox.get(index)
        full_path = file_paths[index]
        print_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print_pages = "Unknown"  # 这里假设无法直接获取页数，需要根据实际情况调整
        print_status = "未知"

        try:
            # 使用Windows默认的打印命令
            subprocess.run(['rundll32.exe', 'url.dll,FileProtocolHandler', full_path], check=True)
            print_status = "成功"
            # 假设无法直接获取页数，需要根据实际情况调整
            print_log.append([file_name, print_time, print_pages, print_status])
            output_text.insert(tk.END, f"文件名: {file_name}\n")
            output_text.insert(tk.END, f"打印时间: {print_time}\n")
            output_text.insert(tk.END, f"打印页数: {print_pages}\n")
            output_text.insert(tk.END, f"打印状态: {print_status}\n")
            output_text.insert(tk.END, "--------------------------\n")
            output_text.see(tk.END)  # 自动滚动到底部
        except subprocess.CalledProcessError as e:
            print_status = "失败"
            messagebox.showerror("错误", f"打印文件 {file_name} 时出错: {e}")
            print_log.append([file_name, print_time, print_pages, print_status])
            output_text.insert(tk.END, f"文件名: {file_name}\n")
            output_text.insert(tk.END, f"打印时间: {print_time}\n")
            output_text.insert(tk.END, f"打印页数: {print_pages}\n")
            output_text.insert(tk.END, f"打印状态: {print_status}\n")
            output_text.insert(tk.END, "--------------------------\n")
            output_text.see(tk.END)  # 自动滚动到底部

    # 生成Excel文件
    df = pd.DataFrame(print_log, columns=["文件名", "打印时间", "打印页数", "打印状态"])
    df.to_excel("打印清单.xlsx", index=False)
    messagebox.showinfo("完成", "打印清单已生成")

def exit_app():
    """退出应用程序"""
    root.destroy()

def select_all(event):
    """全选文件列表框中的所有文件"""
    file_listbox.select_set(0, tk.END)

def main():
    """
    主函数，用于初始化图形界面元素并进入消息循环
    """
    global root, file_listbox, file_paths, output_text

    # 初始化Tkinter窗口
    root = tk.Tk()
    root.title("批量打印PDF和Word文件")
    root.geometry("600x600")

    # 文件选择和选择目录按钮并排显示
    button_frame_top = tk.Frame(root)
    button_frame_top.pack(pady=5)

    select_button = tk.Button(button_frame_top, text="选择文件", command=select_files)
    select_button.pack(side=tk.LEFT, padx=5)

    select_dir_button = tk.Button(button_frame_top, text="选择目录", command=select_directory)
    select_dir_button.pack(side=tk.LEFT, padx=5)

    # 文件列表框
    file_listbox = tk.Listbox(root, selectmode=tk.EXTENDED, width=50, height=10)
    file_listbox.pack(pady=5)

    # 绑定快捷键 Ctrl+A 全选
    root.bind('<Control-a>', select_all)

    # 提交和退出按钮并排显示
    button_frame_bottom = tk.Frame(root)
    button_frame_bottom.pack(pady=5)

    submit_button = tk.Button(button_frame_bottom, text="提交", command=print_files)
    submit_button.pack(side=tk.LEFT, padx=5)

    exit_button = tk.Button(button_frame_bottom, text="退出", command=exit_app)
    exit_button.pack(side=tk.LEFT, padx=5)

    # 输出窗口
    output_label = tk.Label(root, text="打印输出:")
    output_label.pack(pady=5)
    output_text = tk.Text(root, width=70, height=15)
    output_text.pack(pady=5)

    # 进入Tkinter消息循环
    root.mainloop()

if __name__ == "__main__":
    main()