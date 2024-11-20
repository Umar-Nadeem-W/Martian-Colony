import numpy as np




Colonies = np.array([
                    [ 50, 80, 65, 79, 0],
                    [ 50, 80, 65, 79, 0],
                    [ 50, 80, 65, 79, 0],
                    [ 50, 80, 65, 79,0],
                ], ndmin= 2)

Eventsholder =np.array([1,2,3,4])

Names =['Norse Vikings','Desert Bandits','Caribben Pirates','Amazon Warriors']  

def pick_events():
  e1=  np.random.randint(0,3)
  e2=  e1
  e3 = np.random.randint(0,3)
  while(e3 == e1):
     e3 = np.random.randint(0,3)
  e4 = np.random.randint(0,3)
  while(e4 == e1 or e4 == e3):
     e4 = np.random.randint(0,3)
     
     Eventsholder[0] = e1
     Eventsholder[1] = e2
     Eventsholder[2] = e3
     Eventsholder[3] = e4

def assignEvents():
   for i in range(0, Colonies.shape[0]):
      Colonies[i, -1] = Eventsholder[i]

def Storm(colony):
   colony_resources = colony[0:5]
   for i in range(0,4):
      colony_resources[i] = colony_resources[i] - 15
      if(colony_resources[i] < 0):
         colony_resources[i] =0
   colony[0:5] = colony_resources

def War(col1, col2):
    col_1_resources = col1[0:5]
    col_2_resources = col2[0:5]

    col1score =col_1_resources.sum() + (0.2 *col_1_resources[1]).astype(int)
    col2score = col_2_resources.sum() + (0.2 *col_2_resources[1]).astype(int)

    if col2score > col1score:
       col_2_resources = col_2_resources + ((35/100) * col_1_resources).astype(int)
       col_1_resources = col_1_resources - ((35/100) * col_1_resources).astype(int)
    
    elif col1score > col2score:
       col_1_resources = col_1_resources + ((35/100) * col_2_resources).astype(int)
       col_2_resources = col_2_resources - ((35/100) * col_2_resources).astype(int)
    
def Resource_Growth(colony):
   local_view = colony.view()
   local_view[0:5] = local_view[0:5] + (20/100 * local_view[0:5]).astype(int)

def victory():
   max = 0
   winner = 0
   for i in range(0, Colonies.shape[0]):
      if Colonies[i, 1:5].sum() >= max:
         max = Colonies[i, 1:5].sum()
         winner = i

   print("\n\n\n")
   print(Names[winner] +" Win!")

def Round(num): 
   pick_events()
   assignEvents()
   
   first_found= False
   second_found = False
   
   opp1 = Colonies[0]
   opp2 = Colonies[0]

   stormcolony =0
   rgcolony =0

   for i in range(0,Colonies.shape[0]):
      if (first_found == False and Colonies[i,-1] == 0):
         opp1 = Colonies[i]
      if (first_found == True and second_found == False and Colonies[i,-1] == 0):
         opp2 = Colonies[i]

      if (Colonies[i,-1] == 1):
         stormcolony =i

      if (Colonies[i,-1] == 2):
         rgcolony =i


   War(opp1,opp2) 
   Storm(Colonies[stormcolony])
   Resource_Growth(Colonies[rgcolony])

   print(f"After round {num}, the resources stand as follows:")

   print(Names[0], ": ", Colonies[0, 0:5])
   print(Names[1], ": ", Colonies[1, 0:5])
   print(Names[2], ": ", Colonies[2, 0:5])
   print(Names[3], ": ", Colonies[3, 0:5])
 
   print("\n\n\n")


def Game():
   for i in range (0, 10):
    Round(i)
   victory()

Game()
   
          

         
      
      







