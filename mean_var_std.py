import numpy as np


def calculate(lst):

   
    if len(lst)==9:
        a=np.array(lst).reshape((3,3))

        a0_mean=np.mean(a,axis=0).tolist()
        a1_mean=np.mean(a,axis=1).tolist()
        a_mean=np.mean(a).tolist()
        a0_var=np.var(a,axis=0).tolist()
        a1_var=np.var(a,axis=1).tolist()
        a_var=np.var(a).tolist()
        a0_std=np.std(a,axis=0).tolist()
        a1_std=np.std(a,axis=1).tolist()
        a_std=np.std(a).tolist()
        a0_max=np.max(a,axis=0).tolist()
        a1_max=np.max(a,axis=1).tolist()
        a_max=np.max(a).tolist()
        a0_min=np.min(a,axis=0).tolist()
        a1_min=np.min(a,axis=1).tolist()
        a_min=np.min(a).tolist()
        a0_sum=np.sum(a,axis=0).tolist()
        a1_sum=np.sum(a,axis=1).tolist()
        a_sum=np.sum(a).tolist()

        calculations={ 
                   'mean':[a0_mean,a1_mean,a_mean],
                   'variance':[a0_var,a1_var,a_var],
                   'standard deviation':[a0_std,a1_std,a_std],
                   'max':[a0_max,a1_max,a_max],
                   'min':[a0_min,a1_min,a_min],
                   'sum':[a0_sum,a1_sum,a_sum] 
                   }   

        return calculations    

    else:
         raise ValueError("List must contain nine numbers.")    


   

        
       


    

   