import goocanvas
import gtk

ellipse1 = None
ellipse2 = None
rect1 = None
rect2 = None
rect3 = None
rect4 = None

def create_animation_page():
    
    #Lets set up a goocanvas
    vbox = gtk.VBox(False, 4)
    vbox.set_border_width(4)
    
    hbox = gtk.HBox(False, 4)
    vbox.pack_start(hbox, False, False, 0)
    
    w = gtk.Button("Start Animation")
    hbox.pack_start(w, False, False, 0)
    w.connect("clicked",start_animation)
    
    w = gtk.Button("Stop Animation")
    hbox.pack_start(w, False, False, 0)
    w.connect("clicked", stop_animation)
    
    scrolled_window = gtk.ScrolledWindow()
    vbox.add(scrolled_window)
    
    canvas = goocanvas.Canvas()
    canvas.set_size_request(640, 480)
    canvas.set_bounds(0, 0, 1000, 1000) #left, top, right, bottom
    
    scrolled_window.add(canvas)
    setup_canvas(canvas)
    
    return vbox

def setup_canvas(canvas):
    global ellipse1, ellipse2, rect1, rect2
    
    root = canvas.get_root_item()
    #The "root" is like the root/ parent node of tree in XML
    
    ellipse1 = goocanvas.Ellipse(parent = root,
                                 center_x = 0,
                                 center_y = 0,
                                 radius_x = 25,
                                 radius_y = 15,
                                 fill_color = "yellow")
    ellipse1.translate(100, 100)
    
    ellipse2 = goocanvas.Ellipse(parent = root,
                                 center_x = 0,
                                 center_y = 0,
                                 radius_x = 25,
                                 radius_y = 15,
                                 fill_color = "red")
    ellipse2.translate(100, 400)
    
    rect1 = goocanvas.Rect(parent = root,
                           x = -10,
                           y = -10,
                           width = 20,
                           height = 20,
                           fill_color = "blue")
    rect1.translate(100, 200)
    
    rect2 = goocanvas.Rect(parent = root,
                           x = -10,
                           y = -10,
                           width = 20,
                           height = 20,
                           fill_color = "blue")
    rect2.translate(300, 200)
    
   
    
def start_animation(button):
    global ellipse1, ellipse2, rect1, rect2
    
    ellipse1.set_simple_transform(100, 100, 1, 0)
    ellipse1.animate(500, 100, 2, 720, True, 2000, 40,
                     goocanvas.ANIMATE_BOUNCE)
    
    ellipse2.set_simple_transform(100, 400, 1, 0)
    ellipse2.animate(500,400,2, 720,True,2000, 40, 
                     goocanvas.ANIMATE_BOUNCE)
                     
    rect1.set_simple_transform(100, 200,1 ,0)
    rect1.animate(100, 200, 1, 350, True, 1300, 40,
                  goocanvas.ANIMATE_RESTART)
    
    rect2.set_simple_transform(300, 200,1 ,0)
    rect2.animate(300, 200, 3, 0, True, 400 , 40, goocanvas.ANIMATE_BOUNCE)
    
def stop_animation(button):
    global ellipse1, ellipse2, rect1, rect2
    
    ellipse1.stop_animation()
    ellipse2.stop_animation()
    rect1.stop_animation()
    rect2.stop_animation()
    
    
def main():
    v = create_animation_page()   
    w = gtk.Window()
    w.connect("destroy",gtk.main_quit)
    w.add(v)
    w.show_all()
    gtk.main() 
   
if __name__ == "__main__":
    main()