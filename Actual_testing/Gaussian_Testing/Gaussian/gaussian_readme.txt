:::::::::::::::::::::::::::::::::::::::::::::::::
:: Gaussian Class Addition/Subtraction Dataset ::
:::::::::::::::::::::::::::::::::::::::::::::::::

Changing class distributions are modeled as a set of Gaussian 
distributions with changing parameters (mean and/or variance) over time. 
Class distributions are governed by the parametric equations in the table
below. The rate of drift for a particular class is dependent on the 
difference in mean and variance at the beginning (t = 0) and end (t = 1)
of a normalized time interval. 


::: Dataset Information ::::::::::::::::::::::::::::::::::::::
 Features: 2
 Classes: 4
 Time steps: 300
 Training instances per time step: 20
 Testing instances per time step: 1,024
 Total Training Instances: 200,960
 Total Testing Instances: 307,200


::: Training/Testing Procedure (Batch Learning) ::::::::::::::

 At each time step, train on a window of 20 samples from file
 "Gaussian_training_data.csv" (200,960 x 2) with associated class labels 
 in file "Gaussian_training_class.csv" (200,960 x 1). After training, you 
 may test with a window of size 1,024 from file "Gaussian_testing_data.csv"
 (307,200 x 2). Performance on the testing grid (size 32x32) is 
 accomplished using the known class probabilites from 
 "Gaussian_testing_priors.csv" (307,200 x 4), where the percentage of 
 samples labelled for a particular class may be compared to the known 
 probability of each class appearing in the testing data. For subsequent 
 time steps, shift the training and testing windows by 20 and 1,024, 
 respectively, and read in the next batch.


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Parametric equations for 4-class Gaussian drift with class addition/removal
------------------------------------------------------
         0 < t < 1/5      |      1/5 < t < 2/5
    µx    µy    sx    sy  |  µx    µy    sx    sy
------------------------------------------------------
C1  2     5     1    2+5t |  2     5    1+5t  3-5t
C2 5-5t   8    3-10t  1   | 4+20t  8     1     1
C3 5-5t   2    3-10t  1   | 4+20t  2     1     1
C4 N/A   N/A   N/A   N/A  | N/A   N/A   N/A   N/A
------------------------------------------------------

------------------------------------------------------
        2/5 < t < 3/5     |      3/5 < t < 4/5
    µx    µy    sx    sy  |  µx    µy    sx    sy
------------------------------------------------------
C1  2    5-15t 2-5t  2-5t | N/A   N/A   N/A    N/A
C2  8    8-20t  1    1+5t |  8    4+20t 1+2.5t 2-2.5t
C3 8-10t  2    1+10t  1   | 6-20t 2+30t 3-7.5t 1+2.5t
C4  5    5+15t  1     1   | 5+15t 8-30t 1+2.5t 1+2.5t
------------------------------------------------------

----------------------------
         4/5 < t < 1
    µx    µy    sx    sy  
----------------------------
C1 N/A    N/A   N/A   N/A
C2 8      8-30t 1.5   1.5
C3 2+30t   2    1.5   1.5
C4 8-30t   2    1.5   1.5
----------------------------


==========================================================
Ryan Elwell, Robi Polikar
Signal Processing & Pattern Recognition Laboratory (SPPRL)
Department of Electrical & Computer Engineering
Rowan University
==========================================================