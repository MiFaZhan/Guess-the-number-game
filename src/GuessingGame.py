import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("猜数字游戏")
        self.master.geometry("400x350")
        self.master.configure(bg="#F0F8FF")  # 背景色为淡蓝色

        self.target = None
        self.guess_count = 0
        self.debug = False  # 是否打印调试信息

        self.setup_ui()
        self.start_game()

    def setup_ui(self):
        # 标题标签
        self.header_label = tk.Label(self.master, text="欢迎来到猜数字游戏", font=("微软雅黑", 16, "bold"), bg="#F0F8FF", fg="#333")
        self.header_label.pack(pady=10)

        # 提示标签
        self.prompt_label = tk.Label(self.master, text="请输入 1–100 之间的数字", font=("微软雅黑", 12), bg="#F0F8FF", fg="#555")
        self.prompt_label.pack(pady=5)

        # 输入区域框架
        self.input_frame = tk.Frame(self.master, bg="#F0F8FF")
        self.input_frame.pack()

        # 输入框
        self.guess_entry = tk.Entry(self.input_frame, width=10, font=("微软雅黑", 12))
        self.guess_entry.grid(row=0, column=0, padx=5)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        # 提交按钮
        self.submit_btn = tk.Button(self.input_frame, text="提交", font=("微软雅黑", 11), bg="#4CAF50", fg="white", width=10,
                                    command=self.check_guess)
        self.submit_btn.grid(row=0, column=1, padx=5)

        # 提示反馈
        self.feedback_label = tk.Label(self.master, text="", font=("微软雅黑", 12, "bold"), bg="#F0F8FF", fg="black")
        self.feedback_label.pack(pady=10)

        # 猜测次数
        self.counter_label = tk.Label(self.master, text="猜测次数：0", font=("微软雅黑", 11), bg="#F0F8FF", fg="#333")
        self.counter_label.pack()

        # 重新开始按钮
        self.reset_btn = tk.Button(self.master, text="重新开始", font=("微软雅黑", 11), bg="#2196F3", fg="white", width=12,
                                   command=self.start_game, state=tk.DISABLED)
        self.reset_btn.pack(pady=10)

        # 退出按钮
        self.quit_btn = tk.Button(self.master, text="退出游戏", font=("微软雅黑", 11), bg="#f44336", fg="white", width=12,
                                  command=self.master.quit)
        self.quit_btn.pack()

    def start_game(self):
        self.target = random.randint(1, 100)
        self.guess_count = 0
        self.counter_label.config(text="猜测次数：0")
        self.feedback_label.config(text="", fg="black")
        self.submit_btn.config(state=tk.NORMAL)
        self.reset_btn.config(state=tk.DISABLED)
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()  # 自动聚焦输入框

        if self.debug:
            print(f"[调试] 新目标数字是：{self.target}")

    def check_guess(self):
        guess = self.guess_entry.get().strip()

        if not guess.isdigit():
            self.feedback_label.config(text="请输入有效的数字！", fg="red")
            return

        guess = int(guess)
        if guess < 1 or guess > 100:
            self.feedback_label.config(text="请输入 1 到 100 之间的数字！", fg="red")
            return

        self.guess_count += 1
        self.counter_label.config(text=f"猜测次数：{self.guess_count}")

        if guess < self.target:
            self.feedback_label.config(text="太小了", fg="#555")
        elif guess > self.target:
            self.feedback_label.config(text="太大了", fg="#555")
        else:
            self.feedback_label.config(text="🎉 猜对啦！", fg="green")
            messagebox.showinfo("恭喜", f"你猜对了！共猜测 {self.guess_count} 次")
            self.submit_btn.config(state=tk.DISABLED)
            self.reset_btn.config(state=tk.NORMAL)

        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
