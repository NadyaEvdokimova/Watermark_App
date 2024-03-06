from tkinter import *
from tkinter import filedialog
from PIL import Image

file = file2 = None


def watermark():
    if file and file2:
        logo_image = Image.open(file2).convert("RGBA")
        background_image = Image.open(file).convert("RGBA")
        logo_width, logo_height = logo_image.size
        background_width, background_height = background_image.size
        if logo_width > background_width or logo_height > background_height:
            logo_image.thumbnail((background_width, background_height))
        logo_x = background_image.width - logo_image.width - int(background_image.width/2)
        logo_y = background_image.height - logo_image.height - int(background_image.height/2)

        background_image_wm = Image.new('RGBA', background_image.size, (0, 0, 0, 0))
        background_image_wm.paste(background_image, (0, 0))
        background_image_wm.paste(logo_image, (logo_x, logo_y), mask=logo_image)
        background_image_wm.show()

        # Save watermarked photo
        finished_img = background_image_wm.convert("RGB")
        finished_img_name = file[:-4] + " WM.jpg"
        finished_img.save(finished_img_name)
        success_text.set(f"Success!  File saved to {finished_img_name}.")


# image uploader function
def open_file():
    global file
    f_types = [('Files', ('*.jpg', '*.png'))]  # type of files to select
    file = filedialog.askopenfilename(filetypes=f_types)


# logo uploader function
def open_filelogo():
    global file2
    f_types = [('Files', ('*.jpg', '*.png'))]  # type of files to select
    file2 = filedialog.askopenfilename(filetypes=f_types)


# Interface
window = Tk()

window.title("Place a watermark on your image")
window.minsize(width=400, height=400)
window.config(bg="floral white")
label_welcome = Label(text="Do you want to place a watermark on your image?",
                      font=("Broadway", 24, "normal"), fg='firebrick2')
label_welcome.grid(column=1, row=0, columnspan=3, ipady=20)
label_welcome.config(bg="floral white")
info_label = Label(text="Please upload your image and logo",
                   font=("Elephant", 14, "normal"), fg='black', bg='floral white')
info_label.grid(column=1, row=1, columnspan=3, ipady=20)
upload_button = Button(text='Select Image', command=open_file, bg='peach puff')
upload_button.grid(column=1, row=3, ipadx=50, pady=20, sticky='e')
logo_button = Button(text='Select Logo', command=open_filelogo, bg='peach puff')
logo_button.grid(column=3, row=3, ipadx=50, pady=20, sticky='w')
save_button = Button(text='Save Image', command=watermark, bg='peach puff')
save_button.grid(column=2, row=4, ipadx=50, pady=20)
# Success Message
success_text = StringVar()
success_text.set(" ")
success_label = Label(textvariable=success_text, font=("Elephant", 14, "normal"), bg='floral white')
success_label.grid(columnspan=3, column=1, row=6)

window.mainloop()
