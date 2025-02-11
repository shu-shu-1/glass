import io,base64
from PIL import Image
import maliang
import maliang.theme
def resize_image(image, new_height):
    original_image = image
    width, height = original_image.size
    new_width = int(width * new_height / height)
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    return maliang.PhotoImage(resized_image)
icon = {
    "eye_close": Image.open(io.BytesIO(base64.b64decode("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"))),
    "eye_close_black": Image.open(io.BytesIO(base64.b64decode("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"))),
    "eye": Image.open(io.BytesIO(base64.b64decode("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"))),
    "eye_black": Image.open(io.BytesIO(base64.b64decode("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"))),
}

root = maliang.Tk()
root.title("赛博玻璃")
root.iconbitmap("icon/icon.ico")
root.center()
maliang.theme.set_color_mode("dark")
maliang.theme.apply_theme(root,theme="acrylic")
canvas = maliang.Canvas(root,width=1280,height=720,auto_zoom=True, keep_ratio="max", free_anchor=True)
canvas.place(x=0,y=0)
t1=maliang.Text(canvas,text="置顶",fontsize=17,position=[10,650])
s1=maliang.Switch(canvas,command=lambda s:root.topmost(s),default=root.topmost(),position=[10,680])
t2=maliang.Text(canvas,text="隐藏标题栏",fontsize=17,position=[90,650])
s2=maliang.Switch(canvas,command=lambda s:maliang.theme.customize_window(root,hide_title_bar=s),position=[90,680])
t=maliang.Text(canvas, (10, 10), text="窗口透明度 (%d%%)" % (root.alpha()*100), fontsize=20, anchor="nw")
def update_window_alpha(p):
    t.set("窗口透明度 (%d%%)" % (p * 100))  
    root.alpha(p)  
    if p <= 0.1:
        root.alpha(1)
        alpha_slider.set(1)
        t.set("窗口透明度 (%d%%)" % (1 * 100))  



alpha_slider=maliang.Slider(canvas, (10, 45), (350, 30), command=update_window_alpha, default=root.alpha())
hide_flag=False
def hide_button():
    global hide_flag,iconB
    if hide_flag is not True:
        alpha_slider.forget(True)
        t.forget(True)
        s1.forget(True)
        s2.forget(True)
        t1.forget(True)
        t2.forget(True)
        t3.forget(True)
        c1.forget(True)
        iconB.destroy()
        if maliang.theme.get_color_mode() == "light":
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye_black"],new_height=35), command=hide_button,anchor="se")
        else:
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye"],new_height=35), command=hide_button,anchor="se")
        hide_flag=True
    else:
        alpha_slider.forget(False)
        t.forget(False)
        s1.forget(False)
        s2.forget(False)
        t1.forget(False)
        t2.forget(False)
        t3.forget(False)
        c1.forget(False)
        iconB.destroy()
        if maliang.theme.get_color_mode() == "light":
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye_close_black"],new_height=35), command=hide_button,anchor="se")
        else:
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye_close"],new_height=35), command=hide_button,anchor="se")
        hide_flag=False
iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye_close"],new_height=35), command=hide_button,anchor="se")
def change_icon_color():
    global iconB
    iconB.destroy()
    if maliang.theme.get_color_mode() == "light":
        
        if hide_flag:
            
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye_black"],new_height=35), command=hide_button,anchor="se")
        else:
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye_close_black"],new_height=35), command=hide_button,anchor="se")
    elif maliang.theme.get_color_mode() == "dark":
        
        if hide_flag:
            
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye"],new_height=35), command=hide_button,anchor="se")
        else:
            iconB=maliang.IconButton(canvas, (1270, 710), (50, 50), image=resize_image(icon["eye_close"],new_height=35), command=hide_button,anchor="se")

def change_glass(i):
    maliang.theme.apply_theme(root,theme="normal")
    maliang.theme.set_color_mode("light")
    maliang.theme.set_color_mode("dark")
    maliang.theme.apply_theme(root,theme=["acrylic","mica","normal"][i])
    if i == 2:
        maliang.theme.set_color_mode("light")
    change_icon_color()
t3=maliang.Text(canvas, (400, 10), text="玻璃材质", fontsize=20, anchor="nw")
c1=maliang.ComboBox(canvas,[400,45],[260,40],text=["磨砂","云母(需调整透明度)","普通(需调整透明度)"],default=0,command=change_glass)
root.mainloop()
