import sys
import streamlit as st
import pickle
import numpy as np

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://nabtahealth.com/wp-content/uploads/2020/07/Risk-Factors_CVD.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def load_model():
  with open('saved_steps.pkl','rb') as file:
      new_data = pickle.load(file)
  return new_data

new_data = load_model()

model = new_data["model"]



def show_predict_page():
    st.title("Prediction of coronary heart disease (CHD)")

    age= st.slider("Age",30,70,55)
    sex = {"Male","Female"}
    sex=st.selectbox("Sex",sex)
    totChol=st.text_input('Total cholesterol ( mg/dL )')
    cigsPerDay=st.text_input('Cigarettes per day')
    sysbp=st.text_input('Systolic blood pressure')
    glucose=st.text_input('Glucose ( mg/dL )')
       
    ok=st.button("Predict")

    errors=0
    if totChol=="":
      errors+=1
    if cigsPerDay=="":
      errors+=1
    if sysbp=="":
      errors+=1
    if glucose=="":
      errors+=1   

    if ok:   
      if errors==0:
        if sex == "Male":
          sex_number=1
        else:
          sex_number=0
        totChol=float(totChol)
        cigsPerDay=float(cigsPerDay)
        sysbp=float(sysbp)
        glucose=float(glucose)
        X = np.array([[age,sex_number,cigsPerDay,totChol,sysbp,glucose]])
        result = model.predict(X)
        if result==0 :
            st.success(f"You do not have a 10-year risk of future coronary heart disease")
        else:
            st.error(f"You have a 10-year risk of future coronary heart disease")         

      else:
         st.write("You didn't write all the necessary informations")

    with st.expander("Show details"):
      if errors==0:
        if age>50:
           st.write("*Age*")
           st.write("People over 50 have a higher risk of developing CHD")      
        if sex=="Male":
           st.write("*Gender*")
           st.write("Men have a higher risk of developing CHD than women")        
        totChol=float(totChol)
        st.write("*Total cholesterol*")
        if totChol>239.9:
          st.write("Your total cholesterol level is high. You should lower your fat intake and eat more fruits, vegetables and plant based protein. Exercise on most days of the week and increase your physical activity. Drink alcohol only in moderation and try to quit smoking(if you are a smoker).")
        elif totChol<200.0:
          st.write("Your total cholesterol level is normal")
        else:
          st.write("Your total cholesterol level is borderline high. It is recommended to lower your fat intake and eat more fruits, vegetables and plant based protein. You should also do regular exercise.")        
        cigsPerDay=float(cigsPerDay)
        st.write("*Smoking*")
        if cigsPerDay!=0:
          st.write("For every smoked cigarette your risk of CHD is higher")
        glucose=float(glucose)
        st.write("*Glucose*")
        if glucose<99.1:
          st.write("Your glucose level is normal")
        elif glucose<125.9:
          st.write("You have a prediabetes. Prediabetes is reversible which means you can prevent or slow down development of diabetes by making lifestyle changes and maintaining moderate weight.")
        else:
          st.write("You have a diabetes")
      else:
        st.write("There is nothing to show.")

    st.write("Please, do not use this as a substitute for a doctor. If you don't feel well or suspect you have a CHD, consult with your doctor ")

   
     