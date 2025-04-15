import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming your ALS model and data are loaded correctly
# Model, reviews2, train_sparse are pre-loaded

# Title
st.title("Product Recommendation System")

# Plot rating distribution
st.subheader("Distribution of Ratings")
plt.figure(figsize=(8, 5))
sns.countplot(x='Score', data=reviews)
plt.xlabel("Rating (Score)")
plt.ylabel("Count of Reviews")
plt.title("Distribution of Ratings in Amazon Fine Foods Reviews")
st.pyplot(plt)

# Input: Choose a user ID
user_id = st.number_input('Choose a User ID', min_value=1, max_value=len(train_sparse)-1, value=15)

# Get top 5 recommended items for the user
recommended = model.recommend(user_id, train_sparse[user_id], N=5)

# Convert item indices back to product IDs
product_mapping = dict(enumerate(reviews2['ProductId'].astype("category").cat.categories))
recommended_products = [product_mapping[i] for i in recommended[0]]

# Display recommended products
st.subheader(f"Recommended Products for User {user_id}")
st.write(recommended_products)

