# Patient Treatment
Whether to patient should be admitted (in) or see the out-patient clinic (out)

## Work

Order to run: 
1. `get_data.py`
2. `eda.ipynb`
3. `feature_engineering.ipynb`
4. `base_model.ipynb`


## Background

1. **MCH** 
    - Normal range: 27-33 pg/cell
    
    Low MCH  
    - MCH levels below 27 pg/cell are considered low. This could indicate hypochromic anemia, which is when red blood cells have less hemoglobin than normal. Low MCH can be caused by iron deficiency, blood loss, or genetic conditions like thalassemia. 
    
    High MCH  
    - MCH levels above 34 pg/cell are considered high. This could indicate hyperchromic anemia, which is when red blood cells have more hemoglobin than normal. High MCH can be caused by low levels of vitamin B12 or folate, chemotherapy, liver disease, or certain medications. 
    
    Other factors to consider
    - MCH results are usually part of a complete blood count (CBC) test. 
    - Other red blood cell indices, like MCV, MCHC, and RDW, are also considered when interpreting MCH results. 
    - Treatment depends on the cause of the abnormal MCH levels. 

2. **MCHC**
- A normal MCHC result is between 32 and 36 grams per deciliter (g/dL)  

    *Low MCHC*  
    - May indicate iron deficiency anemia
    - May indicate thalassemia, an inherited blood disorder
    - May indicate vitamin B12 deficiency
    - May indicate folate deficiency
    - May indicate lead poisoning
    - May indicate kidney disease

    *High MCHC*  
    - May indicate hereditary spherocytosis
    - May indicate sickle cell anemia
    - May indicate thalassemia
    - May indicate dehydration
    - May indicate polycythemia vera
    - May indicate hemolytic anemia, when red blood cells die faster than they are produced
    
    How is MCHC measured?
    - MCHC is calculated by multiplying the hemoglobin result from a complete blood count (CBC) by 100 and then dividing by the hematocrit result 
    A small blood sample is drawn from a vein in your arm 

3. **MCV**
- test measures the average size of red blood cells in a blood sample. MCV results are reported in femtoliters (fL). 

    Normal MCV range 
    - A normal MCV is typically between 80 and 100 fL
    - A low MCV is less than 80 fL
    - A high MCV is more than 100 fL

    Low MCV
    - A low MCV indicates that red blood cells are smaller than normal 

    This could be a sign of microcytic anemia, which can be caused by: 
    - Iron deficiency 
    - Lead poisoning 
    - Thalassemia, a genetic condition 

    High MCV
    - A high MCV indicates that red blood cells are larger than normal 

    This could be a sign of macrocytic anemia, which can be caused by: 
    - Liver disease 
    - Deficiencies in essential nutrients like vitamin B12 or folate 
    - Other implications

    MCV levels can also be used to diagnose anemia and determine its causes 
    MCV levels may increase over time as part of the normal aging process 

4. **Hematocrit Test**
    Purpose: 
    - To measure the percentage of red blood cells (RBCs) in the blood 
    - To diagnose and monitor conditions that affect RBC production or loss 

    Procedure: 
    - A small amount of blood is drawn from a vein 
    - The blood is centrifuged to separate the RBCs from the other components of blood (plasma and white blood cells) 
    - The volume of RBCs is measured and expressed as a percentage of the total blood volume 

    Normal Range: 
    - Men: 40-54 and Women: 36-46. 

    Interpretation:
    - Low hematocrit (anemia): May indicate blood loss, iron deficiency, bone marrow disorders, or certain cancers 
    - High hematocrit (polycythemia): May indicate dehydration, bone marrow disorders, or blood clots 

    Additional Information: 
    - Hematocrit is often part of a complete blood count (CBC) 
    - Other factors that can affect hematocrit levels include age, altitude, and pregnancy 
    - It is important to inform your healthcare provider about any medications or supplements you are taking before undergoing a hematocrit test


| Name         | Data Type | Value Sample | Description                                      |
|--------------|------------|--------------|--------------------------------------------------|
| HEMATOCRIT  | Continuous | 35.1         | Patient laboratory test result of haematocrit    |
| HEMOGLOBINS | Continuous | 11.8         | Patient laboratory test result of haemoglobins   |
| ERYTHROCYTE  | Continuous | 4.65         | Patient laboratory test result of erythrocyte    |
| LEUCOCYTE    | Continuous | 6.3          | Patient laboratory test result of leucocyte      |
| THROMBOCYTE  | Continuous | 310          | Patient laboratory test result of thrombocyte    |
| MCH          | Continuous | 25.4         | Patient laboratory test result of mean corpuscular hemoglobin            |
| MCHC         | Continuous | 33.6         | Patient laboratory test result of mean corpuscular hemoglobin concentration           |
| MCV          | Continuous | 75.5         | Patient laboratory test result of mean corpuscular volume           |
| AGE          | Continuous | 12           | Patient age                                      |
| SEX          | Nominal – Binary | F     | Patient gender                                   |
| SOURCE       | Nominal    | {in, out}    | The class target: in = in care patient, out = out care patient |