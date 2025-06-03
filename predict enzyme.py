import tkinter as tk
from app_utils.load_models import load_models
from app_utils.enzyme_predict import enzyme_predict

def show_result():
    seq = seq_text_field.get()
    result, probability = enzyme_predict(seq, client, model)
    result_label.config(text=result)
    predict_label.config(text=f"Probabilty: {probability:.4f}")

client, model = load_models()

main_window = tk.Tk()
main_window.title("Enzyme predict")
main_window.geometry('300x200')

seq_info = tk.Label(main_window, text='Type protein sequence')
seq_info.pack(pady=5)

seq_text_field = tk.Entry(main_window, width=30)
seq_text_field.pack(pady=5)

predict_button = tk.Button(main_window, text="PREDICT", command=show_result)
predict_button.pack(pady=5)

result_label = tk.Label(main_window, text='paste sequence and click PREDICT')
result_label.pack(pady=5)

predict_label = tk.Label(main_window, text='')
predict_label.pack(pady=5)

main_window.mainloop()