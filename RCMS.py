import os
import pandas as pd
from tkinter import messagebox
import customtkinter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

root = customtkinter.CTk()
root.title("Report Card Builder")
root.geometry("600x700")

file_path = "C:/Users/bbps/Desktop/rcms1.csv"

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("Dark")

def generate_pdf(record, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)

    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Student Report Card")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 700, f"Name: {record['Name']}")
    c.drawString(100, 685, f"Class: {record['Class']}")
    c.drawString(100, 670, f"Roll Number: {record['Roll Number']}")

    
    c.drawString(200, 570, "Subject                                       Marks")

    c.drawString(200, 525, f"Maths                                         {record['Maths']}")
    c.drawString(200, 510, f"Science                                      {record['Science']}")
    c.drawString(200, 495, f"Social Science                           {record['Social Science']}")
    c.drawString(200, 480, f"A.I.                                             {record['A.I.']}")
    c.drawString(200, 465, f"Hindi                                          {record['Hindi']}")
    c.drawString(200, 450, f"English                                      {record['English']}")
    c.drawString(200, 435, f"Punjabi                                      {record['Punjabi']}")


    c.drawString(200, 370, f"Percentage:                                {record['Percentage']:.2f}%")

 
    c.save()

def fetch_details():
    try:
        name = entry_name.get()
        cas = entry_class.get()
        rn = entry_roll.get()
        marks = [
            float(entry_maths.get()), float(entry_science.get()),
            float(entry_ssc.get()), float(entry_ai.get()),
            float(entry_hindi.get()), float(entry_english.get()),
            float(entry_punjabi.get())
        ]
        max_marks = entry_max_marks.get()

        if not name.isalpha():
            messagebox.showerror("Error", "Name must only contain alphabets.")
            return
        if int(max_marks) > 500:
            messagebox.showerror("Error", "Total maximum marks should be 500 or less.")
            return

        total_marks = sum(marks)
        max_marks1 = int(max_marks)
        percentage = (total_marks / max_marks1) * 100

        # Create the student record
        record = {
            "Name": name, "Class": cas, "Roll Number": rn,
            "Maths": marks[0], "Science": marks[1], "Social Science": marks[2],
            "A.I.": marks[3], "Hindi": marks[4], "English": marks[5],
            "Punjabi": marks[6], "Percentage": percentage
        }

        # Generate PDF
        pdf_filename = f"C:/Users/bbps/Desktop/{name}_report_card.pdf"
        generate_pdf(record, pdf_filename)

        messagebox.showinfo("Success", f"Report card generated successfully: {pdf_filename}")
        
    except ValueError:
        messagebox.showerror("Error", "Please ensure all fields are filled with valid numbers.")

frame = customtkinter.CTkFrame(root)
frame.pack(padx=20, pady=20, expand=True)

customtkinter.CTkLabel(frame, text="REPORT CARD BUILDER").pack(pady=10)

entry_name = customtkinter.CTkEntry(frame, placeholder_text="Student Name")
entry_name.pack(pady=5,padx=100)

entry_class = customtkinter.CTkEntry(frame, placeholder_text="Class and Section")
entry_class.pack(pady=5)

entry_roll = customtkinter.CTkEntry(frame, placeholder_text="Roll Number")
entry_roll.pack(pady=5)

entry_maths = customtkinter.CTkEntry(frame, placeholder_text="Maths")
entry_maths.pack(pady=5)

entry_science = customtkinter.CTkEntry(frame, placeholder_text="Science")
entry_science.pack(pady=5)

entry_ssc = customtkinter.CTkEntry(frame, placeholder_text="Social Science")
entry_ssc.pack(pady=5)

entry_ai = customtkinter.CTkEntry(frame, placeholder_text="Artificial Intelligence")
entry_ai.pack(pady=5)

entry_hindi = customtkinter.CTkEntry(frame, placeholder_text="Hindi")
entry_hindi.pack(pady=5)

entry_english = customtkinter.CTkEntry(frame, placeholder_text="English")
entry_english.pack(pady=5)

entry_punjabi = customtkinter.CTkEntry(frame, placeholder_text="Punjabi")
entry_punjabi.pack(pady=5)

entry_max_marks = customtkinter.CTkEntry(frame, placeholder_text="Maximum Marks")
entry_max_marks.pack(pady=5)

btn = customtkinter.CTkButton(frame, text="Submit", command=fetch_details)
btn.pack(pady=20)




root.mainloop()
