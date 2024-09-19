import streamlit as st

st.image("static/3.png")
st.title("Abstract")
st.markdown("##### Based on computer graphics aided design, this software provides users with customized printing and dyeing pattern services and builds a community for users to share their own patterns.")
st.image("static/6.png",caption="workflow")
st.markdown("##### Through the introduction of public key cryptography and steganography, the software realizes the process of personalized pattern generation difficult to reverse. Pair(personal_words, image) is accessible to everyone, but only the original author of the pattern who holds the private key can reproducibly draw the pattern")
cols=st.columns(2)
cols[0].image("static/fulilian.jpg",caption="input_image")
cols[1].image("static/7.png",caption="generated_pattern")
st.markdown("##### In the process of custom patterns, we adopted ascii art, using ten molds of ascii symbol to express textures, shadows and other features. Using a limited number of molds for printing and dyeing allows us to reduce printing and dyeing costs, and it is possible to carry out pipeline production. Despite the problem of image distortion, the ascii art style has a unique aesthetic value")
st.divider()
st.title("User Guide")
multil='''***SIGNATURE PAGE***
    -> get a key (unless you have) 
    -> input your key
    -> upload your favorite image 
    -> leave personalized words
    -> generate pattern\n
***COMMUNITY PAGE***
    -> share your pattern (access key required)
    -> view, download others' pieces \n
***UNRIDDLE PAGE***
    -> input a processed image 
    -> uncover words hidden'''
st.code(multil)
