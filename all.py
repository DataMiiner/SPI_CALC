import streamlit as st

st.set_page_config(
  page_title="SPI_CALC",
  page_icon='🔣'
 
)
#data
dt={"A+":10,"A":9,"B+":8,"B":7,"C+":6,"C":5,"IF":0,"FF":0}
#heading
st.title("SPI CALCULATOR ")
st.text("By DATAMIINER")
st.title("  ")
st.title("  ")
col1,col2=st.columns([1,1])
col3,col4=st.columns([1,1])
col5,col6=st.columns([1,1])

with col1:
  st.subheader("SUBJECT-1")
  sub1=st.text_input("SUBJECT-1 NAME")
  sub_c1=st.selectbox("Enter SUBJECT-1 credit",[1,2,3,4,5,6,7,8,9,10])
  sub_g1=st.selectbox("Enter SUBJECT-1 Grade",["A+","A","B+","B","C+","C","IF","FF"])
  
with col2:
  st.subheader("SUBJECT-2")
  sub2=st.text_input("SUBJECT-2 NAME")
  sub_c2=st.selectbox("Enter SUBJECT-2 credit",[1,2,3,4,5,6,7,8,9,10])
  sub_g2=st.selectbox("Enter SUBJECT-2 Grade",["A+","A","B+","B","C+","C","IF","FF"])
st.title(" ")  

with col3:
   st.subheader("SUBJECT-3")
   sub3=st.text_input("SUBJECT-3 NAME")
   sub_c3=st.selectbox("Enter SUBJECT-3 credit",[1,2,3,4,5,6,7,8,9,10])
   sub_g3=st.selectbox("Enter SUBJECT-3 Grade",["A+","A","B+","B","C+","C","IF","FF"])
with col4:
    st.subheader("SUBJECT-4")
    sub4=st.text_input("SUBJECT-4 NAME")
    sub_c4=st.selectbox("Enter SUBJECT-4 credit",[1,2,3,4,5,6,7,8,9,10])
    sub_g4=st.selectbox("Enter SUBJECT-4 Grade",["A+","A","B+","B","C+","C","IF","FF"])
st.title(" ") 

with col5:
     st.subheader("SUBJECT-5")
     sub5=st.text_input("SUBJECT-5 NAME")
     sub_c5=st.selectbox("Enter SUBJECT-5 credit",[1,2,3,4,5,6,7,8,9,10])
     sub_g5=st.selectbox("Enter SUBJECT-5 Grade",["A+","A","B+","B","C+","C","IF","FF"])
with col6:
      st.subheader("SUBJECT-6")
      sub6=st.text_input("SUBJECT-6 NAME")
      sub_c6=st.selectbox("Enter SUBJECT-6 credit",[1,2,3,4,5,6,7,8,9,10])
      sub_g6=st.selectbox("Enter SUBJECT-6 Grade",["A+","A","B+","B","C+","C","IF","FF"])
but=st.button("calculate")  
if but==True:
  li= {sub1:[sub_c1,sub_g1],sub2:[sub_c2,sub_g2],sub3:[sub_c3,sub_g3],sub4:[sub_c4,sub_g4],sub5:[sub_c5,sub_g5],sub6:[sub_c6,sub_g6]}
  total_credit=0
  total_g=0
  for key,val in li.items():
    total_g=total_g+(val[0]*dt[val[1]])
    total_credit=total_credit+(val[0])
  re=total_g/total_credit 
  res=round(re,2)
  per=(res-0.5)*10
  PER=round(per,2)
  st.title(" ") 
  col6,col7=st.columns([1,1]) 
  with col6:  
      st.subheader("Your SPI:")
      st.success(f"{res}") 
  with col7:  
      st.subheader("Your Percentage(%):")
      st.success(f"{PER}")           
          