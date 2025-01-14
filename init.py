import tkinter as tk
import random

# 論理ゲートの辞書 (ゲート名と画像ファイル名)
logic_gates = {
    "AND": "and_gate.png",
    "OR": "or_gate.png",
    "NOT": "not_gate.png",
    "NAND": "nand_gate.png",
    "NOR": "nor_gate.png",
    "XOR": "xor_gate.png"
}

# グローバル変数
current_gate_name = None
current_image = None
# ウィンドウのセットアップ
root = tk.Tk()
root.title("論理ゲート当てゲーム")

# キャンバスの作成
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# 入力欄とボタン
entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="回答する")
check_button.pack()

# 結果ラベル
result_label = tk.Label(root, text="")
result_label.pack()

# ゲートの表示
def show_gate():
    global current_gate_name
    global current_image
    canvas.delete("all")  # キャンバスをクリア
    current_gate_name, image_file = random.choice(list(logic_gates.items()))
    current_image = tk.PhotoImage(file=image_file)
    canvas.create_image(200, 150, image=current_image)

# 回答をチェック
def check_answer():
    user_input = entry.get().strip().upper()
    if user_input == current_gate_name:
        result_label.config(text="正解！")
    else:
        result_label.config(text=f"不正解。正解は {current_gate_name} です。")
    entry.delete(0, tk.END)
    root.after(2000, start_game)  # 次の問題へ

# ゲーム開始
def start_game():
    result_label.config(text="")
    show_gate()

# ボタンの動作設定
check_button.config(command=check_answer)

# 初回のゲーム開始
start_game()

# メインループ
root.mainloop()
