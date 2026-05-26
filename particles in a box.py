#particles in a box
'''this programs simulates the random behavior of particles in a box'''

#import necessary modules
from random import randrange
import tkinter as tk
from math import sqrt
from time import sleep

class particles_in_a_box:

    def __init__(self,height = 1000,width = 1000,bg = 'white',no_ofballs = 30,T = 100,radius = 10,inc =.099):#initialise the instance of the class
        self.height = height
        self.width = width
        self.n = no_ofballs
        self.T = T
        self.r = radius
        self.inc = inc
        self.object_id = []
        self.current_coords =[]
        #border collision bug fixer
        self.bug_fix_x =[0 for i in range(len(self.object_id))]
        self.bug_fix_y =[0 for i in range(len(self.object_id))]
        
        self.window = tk.Tk()
        self.window.configure(bg = 'black')
        self.window.title("PARTICLES IN A BOX")
        self.window.geometry("{0}x{1}".format(width,height))
        self.canvas = tk.Canvas(height = height,width = width,bg = bg)
        self.canvas.pack()
        

        
        
        self.grid()
        self.create_balls()
        self.animate()
        
    def grid(self):
            #create grid
        #horizontal linew
        height = self.height
        width = self.width
        x1 = [0 for i in range(0,height,100) ]
        y1 = [i for i in range(0,height,100) ]
        x2 = [width for i in range(0,height,100) ]
        y2 = [i for i in range(0,height,100) ]

        #vertical lines
        x1+= [i for i in range(0,width,100) ]
        y1+= [0 for i in range(0,width,100) ]
        x2+= [i for i in range(0,width,100) ]
        y2+= [height for i in range(0,width,100) ]
        #Create lines
        for (a,b,c,d) in zip(x1,y1,x2,y2):
             self.canvas.create_line(a,b,c,d,fill = "black")
        
        
        
   

    def initial_condition(self):
        '''returns  list of random positon vectors and velocity vectors'''
        #Resultant list is 3 dimensional and first dimension contains list of objects, second dimension contains list of vectors of positon
        #and velocity
        resultant = []
        for i in range(self.n):
            object_ =[]
            object_.append(randrange(self.width))
            object_.append(randrange(self.height))
            object_.append(randrange(1,self.T))
            object_.append(randrange(1,self.T))
            resultant.append(object_)
        self.current_coords = resultant
        return resultant
            
    def create_balls (self):
        '''create balls and return the list of it's ids'''
        initial_coords = self.initial_condition()
        r = self.r
        for i in range(self.n):
            objectids = self.canvas.create_oval(initial_coords[i][0]-r,initial_coords[i][1] - r,initial_coords[i][0] + r,initial_coords[i][1]+r,fill = 'red')
            self.object_id.append(objectids)

        self.bug_fix_x1 =[0 for i in range(len(self.object_id))]
        self.bug_fix_y1 =[0 for i in range(len(self.object_id))]
        self.bug_fix_x2 =[0 for i in range(len(self.object_id))]
        self.bug_fix_y2 =[0 for i in range(len(self.object_id))]
        
        return self.object_id
           

    def update_position(self):
        '''update the position considering the velocities'''
        inc = self.inc
        coords = self.current_coords
        for i in range(len(self.object_id)):
                self.canvas.move(self.object_id[i],inc*coords[i][2],inc*coords[i][3])
                self.current_coords[i][0] = inc*coords[i][2] + coords[i][0]
                self.current_coords[i][1] = inc*coords[i][3]+ coords[i][1]
                      
        self.window.update()
            
    def distance(self,x,y,w,z):
         return sqrt((x-w)**2 + (y-z)**2)

    def update_velocity(self):
        '''update velocity of the particles.Velocity is changes during collisions with other particles and walls of the containers
and returns the 2d list of velocity vectors'''
        
        for i in range(len(self.object_id)):
            for j in range(len(self.object_id)):
                x,y =  self.current_coords[i][0],self.current_coords[i][1]
                
                w,z =  self.current_coords[j][0],self.current_coords[j][1]
                
                if j==i:
                    continue
                elif self.distance(x,y,w,z) <= 4*self.r :
                    tempvx,tempvy = self.current_coords[i][2],self.current_coords[i][3]
                    self.current_coords[i][2],self.current_coords[i][3] = self.current_coords[j][2],self.current_coords[j][3]
                    self.current_coords[j][2],self.current_coords[j][3] = tempvx,tempvy

            if x  <=0 :
                
                    self.current_coords[i][2]  = self.current_coords[i][2]*(-1)
                    self.current_coords[i][0] = 0
               

            if x >= (self.width ):
              
                    self.current_coords[i][2]  = self.current_coords[i][2]*(-1)
                    self.current_coords[i][0] = self.width
                 

            if y <= 0 :
               
                  self.current_coords[i][3]  = self.current_coords[i][3]*(-1)
                  self.current_coords[i][1] = 0
                  
    
            if y >= (self.height ):
                
                  self.current_coords[i][3]  = self.current_coords[i][3]*(-1)
                  self.current_coords[i][1] = self.height- self.r
               
    
          
            
    def single_frame(self):
        '''construct single frame'''
        self.update_position()
        self.update_velocity()
        

    def animate(self):
        '''Animate by calling single_frame'''
        while True:
            self.single_frame()
            #self.window.after(1)
            sleep(.0001)



test = particles_in_a_box()
    
        
    
