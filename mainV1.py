import qrcode as qr
import customtkinter as ctk
from tkinter import filedialog

class App (ctk.CTk) :
    def __init__(self):
        super().__init__()
        self.geometry("600x360")
        self.title("QR-Code Generater")
        self.resizable(False,False)
        self.link = None
        self.setup_UI()
    
    def setup_UI (self):
        """add widgets to app"""
        #title
        self.title_frame = ctk.CTkFrame(self,height=50,width=400,fg_color="transparent")
        self.title_frame.place(x = 100,y = 10)
        self.title_frame.pack_propagate(False)  # Prevents the frame from shrinking to fit the label
        
        self.title_label = ctk.CTkLabel(self.title_frame,text = "QR Code Generator",font = ("Consolas",24))
        self.title_label.place(relx=0.5, rely=0.5, anchor = "center")
        
        #input
        self.input_frame = ctk.CTkFrame(self,height = 36, width= 520, fg_color="transparent")
        self.input_frame.place(x = 40,y = 60)
        
        self.input_label = ctk.CTkLabel(self.input_frame,text = "Link :")
        self.input_label.place(relx = .05, rely = .5,anchor = "center")
        
        self.input_textbox = ctk.CTkTextbox(self.input_frame,width=400,height=28,wrap = 'none')
        self.input_textbox.place(relx = .1,rely = .5, anchor = "w")
        
        self.genQR_button = ctk.CTkButton(self.input_frame,width=12,text="Create",anchor="e",command= self.generate_qr)
        self.genQR_button.place (relx = .975,rely = .5, anchor = "e")        
        
        #result 
        self.result_frame = ctk.CTkFrame(self,height = 200,width = 200)
        self.result_frame.place(x= 200,y = 110)
        
        self.showLabel = ctk.CTkLabel(self.result_frame,image=None,text = "")
        self.showLabel.place(relx = .5,rely = .5,anchor = "center")
        
        #savebutton 
        self.save_button = ctk.CTkButton(self,text="Save",command=self.saveImage,width=24)
        self.save_button.place(relx = .5,rely = .925,anchor = "center")
        
    def generate_qr(self):
        data = self.input_textbox.get("1.0", "end-1c")  # Get text from textbox
        if not data:
            return 

        self.default_img = qr.make(data)
        qr_img = self.default_img.resize((200, 200))
        self.img = qr_img
        self.show_QRImg()

    def saveImage(self):
        # Check if QR code has been generated
        if not hasattr(self, 'img'):
            return
        
        # Open file dialog for saving
        file_path = ctk.filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[
                ('PNG files', '*.png'),
                ('JPEG files', '*.jpg'),
                ('All files', '*.*')
            ],
            title='Save QR Code'
        )
        
        if file_path:
            try:
                self.img.save(file_path)
            except Exception as e:
                ctk.messagebox.showerror('Error', f'Failed to save image: {str(e)}')

    def show_QRImg (self):
        self.ctk_QRImg = ctk.CTkImage(self.img,self.img,size = (200,200))
        self.showLabel.configure(image = self.ctk_QRImg)
        
def main ():
    app = App()
    app.mainloop()
    
if __name__ == "__main__" :
    main()
