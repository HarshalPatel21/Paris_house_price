import streamlit as st
import pickle as pkl

model = pkl.load(open('K:\harshal\ML\Projects\House-paris-price\model.pkl','rb'))

st.title("House Price Predictor")
st.header("Please Enter Following Details")

col1, col2 = st.columns(2)

with col1:
    # squareMeters
    squareMeters_area = st.number_input("Enter the area of house in square meter ",min_value=100)
# numberOfRooms
with col2:
    numberOfRooms = st.number_input("Enter the No of rooms ", min_value=1)


col1, col2 = st.columns(2)
with col1:
    # hasYard
    has_yard = st.radio('Does your house has yard ?',('Yes','No'))
    has_yard = True if has_yard == 'Yes' else False

# hasPool
with col2:
    has_pool = st.radio('Does your house has pool ?',('Yes','No'))
    has_pool = True if has_pool == 'Yes' else False


col1, col2 = st.columns(2)

with col1:
    # floors
    floors = st.number_input("Enter the no of floors ",min_value=1)
# hasGuestRoom - no
with col2:
    no_GuestRoom = st.number_input("Enter the No of Guest room ", min_value=0)



# cityPartRange
st.header("Rate the Area of your city")
cityPartRange = st.slider("",0,10,5)

col1,col2 = st.columns(2)
with col1:
    # numPrevOwners 0-10
    numPrevOwners = st.number_input("Enter the no of previous owner", min_value=0)
    # year-made
with col2:
    year_made = st.number_input("Enter the year your house was made ", min_value=1980,max_value=2023)


col1, col2 , col3 = st.columns(3)
with col1:
    # isNewBuilt yes or no
    isNewBuilt = st.radio('Is your house newly built ?',('Yes','No'))
    isNewBuilt = True if isNewBuilt == 'Yes' else False


with col2:
    # hasStormProtector yes or no
    hasStormProtector = st.radio('Does your house have Storm Protector ?',('Yes','No'))
    hasStormProtector = True if hasStormProtector == 'Yes' else False

with col3:
    # hasStorageRoom - yes or no
    hasStorageRoom = st.radio('Does your house have Storage room ?', ('Yes', 'No'))
    hasStorageRoom = True if hasStorageRoom == 'Yes' else False

col1,col2,col3 = st.columns(3)
with col1:
    # basement - size
    basement = st.radio("Does your house have Basement ?",("No",'Yes'))
    basement = True if basement == 'Yes' else False
    basement_size = 0
    if basement:
        basement_size = st.number_input("Enter Basement size",min_value=5)

with col2:
    # attic - size
    attic = st.radio("Does your house have attic ?",("No",'Yes'))
    attic = True if attic == 'Yes' else False
    attic_size = 0
    if attic:
        attic_size = st.number_input("Enter attic size",min_value=5)

with col3:
    # garage - size
    garage = st.radio("Does your house have garage ?",("No",'Yes'))
    garage = True if garage == 'Yes' else False
    garage_size = 0
    if garage:
        garage_size = st.number_input("Enter garage size",min_value=5)


vals = [[squareMeters_area, numberOfRooms, has_yard, has_pool, floors, cityPartRange, numPrevOwners,
         year_made, isNewBuilt,  hasStormProtector, basement_size, attic_size, garage_size, hasStorageRoom,no_GuestRoom]]

if st.button("Predict") :
    predicted = model.predict(vals)
    st.header("The Value of your house is")
    st.title(int(predicted[0])*80)