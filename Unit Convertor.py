import streamlit as st

# Header
st.title("UNIT CONVERSION TOOLKIT")

st.divider()

# Caption
#st.subheader(" Please choose the field from the side bar")

#st.caption(" This tool help you in conversion process for Pressure, Volume and Temperature")

#Sidebar creation:
st.sidebar.subheader(" Please choose the field here:")

#Sidebar options
Field=st.sidebar.radio("FIELDS ",['Volume','Pressure','Temperature','Flow Rate'])

st.sidebar.divider()
#st.sidebar.markdown("**-------------------------------------------------------**")


#Now coding for respective fields:
#Volume

if Field=='Volume':
   fluid=st.radio(" Which Fluid",['Oil','Water','Condensate','Gas'])
   st.sidebar.title("VOLUME")
   st.sidebar.write(" Volume refers to the amount of fluid (oil, gas, or water) occupying a given space, measured under specific pressure and temperature conditions.")
   st.sidebar.markdown(" In oil fields, we mostly use *bbl* for Oil, water and condensate. For gas, we use *scf* as the unit of volume")
   

# Give the Comment
   if fluid == 'Oil'or fluid== 'Water' or fluid =='Condensate':
      if 'value' not in st.session_state:
         st.session_state.value= False

      if 'reset' not in st.session_state:
         st.session_state.reset= False

      if st.session_state.reset:
         st.session_state.value =0 
         st.session_state.reset= False     



      #st.write(fluid,'is your interested fluid')
        
      

      value= st.number_input("Enter the volume",min_value=0,key='value')

      unit=st.selectbox("Select the unit",['m3','liter','gal','ft3','bbl'])
      desired_unit= st.selectbox("Select the unit",['bbl', 'm3','liter','gal','ft3'])
      a=st.button("Calculate")
      rerun= st.button('Re-run')
      if a:
         
# m3 to other
         if unit =='m3' and desired_unit=='bbl':
              value1=  value* 6.2898
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='m3' and desired_unit=='m3':
              value1=  value* 1
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='m3' and desired_unit=='liter':
              value1=  value* 1000
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='m3' and desired_unit=='gal':
              value1=  value* 264.172052
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='m3' and desired_unit=='ft3':
              value1=  value* 35.3147
              st.success(f'the output is {value1:.3f} {desired_unit}')
# liter to other
         elif unit =='liter' and desired_unit=='bbl':
              value1=  value* 0.0062898
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='liter' and desired_unit=='m3':
              value1=  value* 0.001
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='liter' and desired_unit=='gal':
              value1=  value* 0.26417205
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='liter' and desired_unit=='ft3':
              value1=  value* 0.03531467
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='liter' and desired_unit=='liter':
              value1=  value* 1
              st.success(f'the output is {value1:.3f} {desired_unit}')
              
            

# gal to other
         elif unit =='gal' and desired_unit=='bbl':
              value1=  value* 0.02381
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='gal' and desired_unit=='gal':
              value1=  value* 1
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='gal' and desired_unit=='m3':
              value1=  value* 0.00378541
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='gal' and desired_unit=='ft3':
              value1=  value* 0.13368056
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='gal' and desired_unit=='liter':
              value1=  value* 3.78541178
              st.success(f'the output is {value1:.3f} {desired_unit}')



# ft3 to other
         elif unit =='ft3' and desired_unit=='bbl':
              value1=  value* 0.1781
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='ft3' and desired_unit=='m3':
              value1=  value* 0.02831685
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='ft3' and desired_unit=='liter':
              value1=  value* 28.3168466
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='ft3' and desired_unit=='gal':
              value1=  value* 7.48051948
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='ft3' and desired_unit=='ft3':
              value1=  value* 1
              st.success(f'the output is {value1:.3f} {desired_unit}')   
# bbl to other
         
         elif unit =='bbl' and desired_unit=='ft3':
              value1=  value* 5.614583334
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='bbl' and desired_unit=='m3':
              value1=  value* 0.1589873
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='bbl' and desired_unit=='liter':
              value1=  value* 158.9873
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='bbl' and desired_unit=='gal':
              value1=  value* 42
              st.success(f'the output is {value1:.3f} {desired_unit}')
         elif unit =='bbl' and desired_unit=='bbl':
              value1=  value* 1
              st.success(f'the output is {value1:.3f} {desired_unit}')

      if rerun:
         st.session_state.reset = True
         st.rerun()
                
          
    #fluid=st.radio(" Which Fluid",['Gas'])
   if fluid == 'Gas':
        
        if 'value' not in st.session_state:
           st.session_state.value= 'False'

         
        if 'reset' not in st.session_state:
           st.session_state.reset= 'False'


        if st.session_state.reset:
           st.session_state.value= 0
           st.session_state.reset= 'False'   




        #st.write(fluid,'is your interested fluid')
        value=st.number_input("Enter the volume", key='value')
        unit=st.selectbox("Select the unit",['m3','scf','mscf'])
        desired_unit= st.selectbox("Select the unit",['scf','mscf','m3'])
        a=st.button("Calculate")
        rerun = st.button('Re-run')

        if a:
    #m3 to others
           if unit =='m3' and desired_unit=='scf':
              value1=  value* 35.3147
              st.success(f'the output is {value1:.3f} {desired_unit}')
           elif unit == 'm3' and desired_unit=='m3':                
                value1=  value* 1
                st.success(f'the output is {value1:.3f} {desired_unit}')
           elif unit == 'm3' and desired_unit=='mscf':                
                value1=  value* (35.3147/1000)
                st.success(f'the output is {value1:.3f} {desired_unit}')
    #scf to others
           elif unit == 'scf' and desired_unit=='mscf':                
                value1=  value* (1/1000)
                st.success(f'the output is {value1:.3f} {desired_unit}')
           elif unit == 'scf' and desired_unit=='m3':                
                value1=  value* 0.0283168
                st.success(f'the output is {value1:.3f} {desired_unit}')
           elif unit == 'scf' and desired_unit=='scf':                
                value1=  value* 1
                st.success(f'the output is {value1:.3f} {desired_unit}')
    #mscf to others
           elif unit == 'mscf' and desired_unit=='mscf':                
                value1=  value* (1)
                st.success(f'the output is {value1:.3f} {desired_unit}')
           elif unit == 'mscf' and desired_unit=='scf':                
                value1=  value* (1000)
                st.success(f'the output is {value1:.3f} {desired_unit}')
           elif unit == 'mscf' and desired_unit=='m3':                
                value1=  value* (28.316)
                st.success(f'the output is {value1:.3f} {desired_unit}')

        if rerun:
            st.session_state.reset = True
            st.rerun()
               
           
              
if Field == 'Pressure':
   st.sidebar.title("PRESSURE")
   st.sidebar.markdown('Pressue refers to the force ecerted per unit area. In oil and gas operations, presure plays a critical role in reservoir performance, well productivity, and surfce facilities design. ')
   st.sidebar.markdown('In oil and gas fields, we commonly use  *psi (Pounds per square inch)*, *bar*, *KPa*')
   
   if 'value' not in st.session_state:
      st.session_state.value= False

   if 'reset' not in  st.session_state:
      st.session_state.reset= False

   if st.session_state.reset:
      st.session_state.value= 0
      st.session_state.reset= False   

   pressure_value= st.number_input("Please mention the Pressure value",min_value=0,key='value')
   given_unit= st.selectbox("Choose the given unit",['psi','Pa','KPa','MPa','kgf/cm2','bar','N/m2'])
   desired_unit= st.selectbox("Choose the desired unit",['psi','Pa','KPa','MPa','kgf/cm2','bar','N/m2'])
   a=st.button("Calculate")
   rerun = st.button ('Re-run')
   if a:
# psi to all
      if given_unit == 'psi' and desired_unit == 'psi':
         value1= pressure_value *1
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif given_unit == 'psi' and (desired_unit == 'Pa' or desired_unit =='N/m2'):
         value1= pressure_value * 6894.757
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif given_unit == 'psi' and desired_unit == 'KPa':
         value1= pressure_value *6.894757
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'psi' and desired_unit == 'MPa':
         value1= pressure_value *(6.894757/1000)
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'psi' and desired_unit == 'kgf/cm2':
         value1= pressure_value *0.070307
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'psi' and desired_unit == 'bar':
         value1= pressure_value *0.0689
         st.success(f'The output is {value1:.3f}{desired_unit}')

# Pa to all
      elif (given_unit == 'Pa' or given_unit== 'N/m2') and desired_unit == 'Pa':
         value1= pressure_value *1
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif (given_unit == 'Pa' or given_unit== 'N/m2') and desired_unit == 'psi':
         value1= pressure_value *0.000145
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif (given_unit == 'Pa' or given_unit== 'N/m2') and desired_unit == 'N/m2':
         value1= pressure_value *1
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif (given_unit == 'Pa' or'N/m2') and desired_unit == 'KPa':
         value1= pressure_value *0.001
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif (given_unit == 'Pa' or given_unit== 'N/m2') and desired_unit == 'MPa':
         value1= pressure_value *0.000001
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif (given_unit == 'Pa'or given_unit== 'N/m2') and desired_unit == 'bar':
         value1= pressure_value *0.00001
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif (given_unit == 'Pa' or given_unit== 'N/m2') and desired_unit == 'kgf/cm2':
         value1= pressure_value *(1.02*0.00001)
         st.success(f'The output is {value1:.3f}{desired_unit}')

# KPa to others
      elif given_unit == 'KPa' and desired_unit == 'KPa':
         value1= pressure_value *1
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'KPa' and (desired_unit == 'Pa' or desired_unit== 'N/m2'):
         value1= pressure_value *1000
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'KPa' and desired_unit == 'MPa':
         value1= pressure_value *0.001
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'KPa' and desired_unit == 'psi':
         value1= pressure_value *1000
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'KPa' and desired_unit == 'bar':
         value1= pressure_value *0.01
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'KPa' and desired_unit == 'kgf/cm2':
         value1= pressure_value *0.0101972  
         st.success(f'The output is {value1:.3f}{desired_unit}')
      
#MPa to others   

      elif given_unit == 'MPa' and desired_unit == 'MPa':
         value1= pressure_value *1
         st.success(f'The output is {value1:.3f}{desired_unit}')

      elif given_unit == 'MPa' and desired_unit == 'KPa':
         value1= pressure_value *1000
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'MPa' and desired_unit == 'bar':
         value1= pressure_value *10
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'MPa' and (desired_unit == 'Pa' or desired_unit == 'N/m2'):
         value1= pressure_value *1000000
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'MPa' and desired_unit == 'kgf/cm2':
         value1= pressure_value *10.197
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'MPa' and desired_unit == 'psi':
         value1= pressure_value *145.038
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
#bar to others

      elif given_unit == 'bar' and desired_unit == 'bar':
         value1= pressure_value *1
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
      elif given_unit == 'bar' and (desired_unit == 'Pa' or desired_unit == 'N/m2'):
         value1= pressure_value *100000
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
      elif given_unit == 'bar' and desired_unit == 'KPa':
         value1= pressure_value *10
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
      elif given_unit == 'bar' and desired_unit == 'bar':
         value1= pressure_value *0.1
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
      elif given_unit == 'bar' and desired_unit == 'kgf/cm2':
         value1= pressure_value *1.02
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
      elif given_unit == 'bar' and desired_unit == 'psi':
         value1= pressure_value *14.504
         st.success(f'The output is {value1:.3f}{desired_unit}')

#kgf/cm2 to all 

      elif given_unit == 'kgf/cm2' and desired_unit == 'kgf/cm2':
         value1= pressure_value *1
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
      elif given_unit == 'kgf/cm2' and (desired_unit == 'Pa' or desired_unit == 'N/m2'):
         value1= pressure_value *98066.5
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'kgf/cm2' and desired_unit == 'KPa':
         value1= pressure_value *98.0665
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'kgf/cm2' and desired_unit == 'MPa':
         value1= pressure_value *0.0980665
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'kgf/cm2' and desired_unit == 'bar':
         value1= pressure_value *0.981
         st.success(f'The output is {value1:.3f}{desired_unit}')
      elif given_unit == 'kgf/cm2' and desired_unit == 'psi':
         value1= pressure_value *14.223
         st.success(f'The output is {value1:.3f}{desired_unit}')
   
   if rerun:
      st.session_state.reset= True
      st.rerun()

# Field is Temperture
if Field == 'Temperature':
   st.sidebar.title("TEMPERTURE")
   st.sidebar.markdown('Temperature indicates the thermal condition of a fluid or a resrvoir. In oil and gas operations, temperature affects fluids properties, phase behaviour, viscosit and reservoir performance.')

   
   
   st.sidebar.markdown('Commonly used temperature units are **Celsius (°C), Fahrenheit (°F) & Kelvin (K)*')

   if 'reset' not in st.session_state:
      st.session_state.reset= False

   if st.session_state.reset:
      st.session_state.value = 0
      st.session_state.reset = False


   value= st.number_input(" Please enter the value",key = 'value')
   given_unit= st.selectbox("Select the given unit", ['K','degC','degF'])
   desired_unit= st.selectbox("Select the given unit", ['degC','K','degF'])

   a=st.button("Calculate")
   b=st.button('Re-run')
   if a:
   #Kelvin to others
      if given_unit == 'K' and desired_unit =='K':
         value1= value*1
         st.success(f'The output is {value1:.3f} {desired_unit}')

      elif given_unit == 'K' and desired_unit =='degC':
         value1= value - 273.15
         st.success(f'The output is {value1:.3f} {desired_unit}')

      elif given_unit == 'K' and desired_unit =='degF':
         value1= value - 459.67
         st.success(f'The output is {value1:.3f} {desired_unit}')

   #DegC to others

      elif given_unit == 'degC' and desired_unit == 'degC':
         value1= value*1
         st.success(f'The output is {value1:.3f} {desired_unit}')
   
      elif given_unit == 'degC' and desired_unit == 'K':
         value1= value +273.15
         st.success(f'The output is {value1:.3f} {desired_unit}')
   
      elif given_unit == 'degC' and desired_unit == 'degF':

         value1= (value*(9/5))+32
         st.success(f'The output is {value1:.3f} {desired_unit}')

   #DegF to othes
    
      elif given_unit == 'degF' and desired_unit == 'degF':
         value1= value*1
         st.success(f'The output is {value1:.3f} {desired_unit}')
      
      elif given_unit == 'degF' and desired_unit == 'degC':
         value1= (value-32)*(5/9)
         st.success(f'The output is {value1:.3f} {desired_unit}')
   
      elif given_unit == 'degF' and desired_unit == 'K':
         value1= value*273.15
         st.success(f'The output is {value1:.3f} {desired_unit}')

 #  rerun
   if b:
         st.session_state.reset=True
         st.rerun()
         #st.success(f'Enter the new value')        

# Field is Flow rate

if Field== 'Flow Rate':
   st.sidebar.title("FLOW RATE")
   st.sidebar.markdown('Flow rate represents the volume of fluid produced or injected per unit time. In oil and gas operations, flow rate is essential for production forecasting, well performance analysis, and facility design')
   st.sidebar.markdown('Common  field flow rate units include  *STB/day, bbl/day, m³/day, MSCFD, and MMSCMD.*')
   fluid= st.radio('Select the fluid',['Oil','Gas','Water','Condensate'])

   if 'reset' not in st.session_state:
      st.session_state.reset= False

   if 'value' not in st.session_state:
      st.session_state.value= False

   if st.session_state.reset:
      st.session_state.value=0
      st.session_state.reset= False      


   if fluid == 'Oil' or fluid == 'Condensate' or fluid== 'Water':
     value= st.number_input('Please enter the value',key='value')
     given_unit= st.selectbox('Choose the given unit',['m3/day','bbl/day','m3/hr','bbl/hr','m3/min','bbl/min'])

     desired_unit= st.selectbox('Choose the desired unit',['bbl/day','m3/day','m3/hr', 'm3/min','bbl/hr', 'bbl/min'])
     button= st.button('Calculate')
     rerun= st.button('Re-run')
     if button:
#m3/day to others        
        if given_unit == 'm3/day' and desired_unit == 'bbl/day':
           value1= value* 6.28981
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/day' and desired_unit == 'm3/day':
           value1= value* 1
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/day' and desired_unit == 'bbl/hr':
           value1= value* (6.28981/24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/day' and desired_unit == 'm3/hr':
           value1= value* (1/24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/day' and desired_unit == 'm3/min':
           value1= value* (1/(24*60))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/day' and desired_unit == 'bbl/min':
           value1= value* (6.28981/(24*60))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
   
#m3/hr to others
        elif given_unit == 'm3/hr' and desired_unit == 'm3/hr':
           value1= value* 1
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/hr' and desired_unit == 'm3/day':
           value1= value* 24
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/hr' and desired_unit == 'm3/min':
           value1= value* (1/60)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/hr' and desired_unit == 'bbl/hr':
           value1= value* 6.28981
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/hr' and desired_unit == 'bbl/day':
           value1= value* (6.28981*24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/hr' and desired_unit == 'bbl/min':
           value1= value* (6.28981/60)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

#m3/min to others
        elif given_unit == 'm3/min' and desired_unit == 'm3/min':
           value1= value* (1)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/min' and desired_unit == 'm3/hr':
           value1= value* (60)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/min' and desired_unit == 'm3/day':
           value1= value* ((60*24))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/min' and desired_unit == 'bbl/min':
           value1= value* (6.28981)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/min' and desired_unit == 'bbl/hr':
           value1= value* (6.28981*(60))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'm3/min' and desired_unit == 'bbl/day':
           value1= value* (6.28981*((60*24)))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
                 
#bbl/min to others
        elif given_unit == 'bbl/min' and desired_unit == 'bbl/min':
           value1= value* (1)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/min' and desired_unit == 'bbl/hr':
           value1= value* (60)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/min' and desired_unit == 'bbl/day':
           value1= value* (60*24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/min' and desired_unit == 'm3/min':
           value1= value* (1/6.28981)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/min' and desired_unit == 'm3/hr':
           value1= value* (1/6.28981)*60
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/min' and desired_unit == 'm3/day':
           value1= value* (1/6.28981)*60*24
           st.success(f'The output is {value1:.3f} {desired_unit} ')
           
#bbl/hr to others        
        elif given_unit == 'bbl/hr' and desired_unit == 'bbl/hr':
           value1= value* (1/6.28981)*1
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/hr' and desired_unit == 'bbl/min':
           value1= value* (1/60)
           st.success(f'The output is {value1:.3f} {desired_unit} ')   
        elif given_unit == 'bbl/hr' and desired_unit == 'bbl/day':
           value1= value* 24
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/hr' and desired_unit == 'm3/hr':
           value1= value* (1/6.28981)*1
           st.success(f'The output is {value1:.3f} {desired_unit} ')   
        elif given_unit == 'bbl/hr' and desired_unit == 'm3/day':
           value1= value* (1/6.28981)*24
           st.success(f'The output is {value1:.3f} {desired_unit} ')                    
        elif given_unit == 'bbl/hr' and desired_unit == 'm3/min':
           value1= value* (1/(6.28981*60))
           st.success(f'The output is {value1:.3f} {desired_unit} ')

#bbl/day to others
        elif given_unit == 'bbl/day' and desired_unit == 'bbl/day':
           value1= value*1
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/day' and desired_unit == 'bbl/hr':
           value1= value*(1/24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/day' and desired_unit == 'bbl/min':
           value1= value*(1/(24*60))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/day' and desired_unit == 'm3/day':
           value1= value*(1/6.28981)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/day' and desired_unit == 'm3/min':
           value1= value*(1/(6.28981*60*24))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
        elif given_unit == 'bbl/day' and desired_unit == 'm3/hr':
           value1= value*(1/(6.28981*24))
           st.success(f'The output is {value1:.3f} {desired_unit} ')

   if fluid == 'Gas':
      value= st.number_input('Please enter the value',key='value')

      if 'value' not in st.session_state:
         st.session_state.value= False

      if 'reset' not in st.session_state:
         st.session_State.reset= False

      if st.session_state.reset:
         st.session_state.value= 0
         st.session_state.reset= False     
   

      given_unit= st.selectbox('Choose the given unit',['m3/day','m3/hr','scf/day','Mscf/day','scf/hr','Mscf/day'])

      desired_unit= st.selectbox('Choose the desired unit',['m3/hr','scf/day','Mscf/day','scf/hr','Mscf/day','m3/day'])
      button= st.button('Calculate')
      rerun= st.button('Re-run')
      if button:
#m3/day to others         
         if given_unit == 'm3/day' and desired_unit == 'm3/day':
           value1= value* 1
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/day' and desired_unit == 'm3/hr':
           value1= value* (1/24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/day' and desired_unit == 'scf/day':
           value1= value* 35.3147
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/day' and desired_unit == 'scf/hr':
           value1= value*(35.3147/24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/day' and desired_unit == 'Mscf/hr':
           value1= value*(35.3147/(24*1000))
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/day' and desired_unit == 'Mscf/day':
           value1= value*(35.3147/(24*1000))
           st.success(f'The output is {value1:.3f} {desired_unit} ')


#m3/hr to others
         
         elif given_unit == 'm3/hr' and desired_unit == 'm3/hr':
           value1= value*(1)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/hr' and desired_unit == 'm3/day':
           value1= value*(24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/hr' and desired_unit == 'scf/hr':
           value1= value*(35.3147)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/hr' and desired_unit == 'scf/day':
           value1= value*((35.3147*24))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
         
         elif given_unit == 'm3/hr' and desired_unit == 'Mscf/hr':
           value1= value*((35.3147/1000))
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'm3/hr' and desired_unit == 'Mscf/day':
           value1= value*((35.3147/1000)*24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')


#scf/hr to others
                   
         elif given_unit == 'scf/hr' and desired_unit == 'scf/hr':
           value1= value*(1)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/hr' and desired_unit == 'scf/day':
           value1= value*(24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/hr' and desired_unit == 'Mscf/hr':
           value1= value*(1/1000)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/hr' and desired_unit == 'Mscf/day':
           value1= value*((1/1000)*24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/hr' and desired_unit == 'm3/hr':
           value1= value*(0.0283168)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/hr' and desired_unit == 'm3/day':
           value1= value*(0.0283168*24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
          

#scf/day to others

         elif given_unit == 'scf/day' and desired_unit == 'scf/day':
           value1= value*(1)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/day' and desired_unit == 'scf/hr':
           value1= value*(1/24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/day' and desired_unit == 'Mscf/day':
           value1= value*(1/1000)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
         
         elif given_unit == 'scf/day' and desired_unit == 'Mscf/hr':
           value1= value*(((1/1000)*24))
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/day' and desired_unit == 'm3/day':
           value1= value*(0.0283168)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'scf/day' and desired_unit == 'm3/hr':
           value1= value*((0.0283168/24))
           st.success(f'The output is {value1:.3f} {desired_unit} ')
  
  
#Mscf/hr to others

         elif given_unit == 'Mscf/day' and desired_unit == 'scf/day':
           value1= value*(1000)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/day' and desired_unit == 'Mscf/day':
           value1= value*(1)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/day' and desired_unit == 'm3/day':
           value1= value*(1/28.3168)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/day' and desired_unit == 'm3/hr':
           value1= value*(1/(28.3168*24))
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/day' and desired_unit == 'scf/day':
           value1= value*(1000)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/day' and desired_unit == 'scf/hr':
           value1= value*(1000/24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

#Mscf/hr to others

         elif given_unit == 'Mscf/hr' and desired_unit == 'Mscf/hr':
           value1= value*(1)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/hr' and desired_unit == 'Mscf/day':
           value1= value*(24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/hr' and desired_unit == 'scf/hr':
           value1= value*(1000)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/hr' and desired_unit == 'scf/day':
           value1= value*(1000*24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
  
         elif given_unit == 'Mscf/hr' and desired_unit == 'm3/hr':
           value1= value*(1/28.3168)
           st.success(f'The output is {value1:.3f} {desired_unit} ')

         elif given_unit == 'Mscf/hr' and desired_unit == 'm3/day':
           value1= value*((1/28.3168)*24)
           st.success(f'The output is {value1:.3f} {desired_unit} ')
   if rerun:
         st.session_state.reset= True
         st.rerun()     

#st.divider()           
         
           
           
          
   


   

    
    

