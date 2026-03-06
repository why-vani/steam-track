import streamlit as st
import requests

st.set_page_config(page_title="Steam Price Stalker", page_icon="🎮")
st.title("🎮 Steam Game Price Stalker (India)")
st.write("Track prices in ₹ (INR) for your university project.")

# 1. Input for Game Name (don't u dare fkn type minecraft)
game_name = st.text_input("Enter Game Name (e.g., 'Elden Ring'):")

if game_name:
    # 2. Find the Game ID (AppID) - Setting cc=IN for Indian search results
    search_url = f"https://store.steampowered.com/api/storesearch/?term={game_name}&l=english&cc=IN"
    search_res = requests.get(search_url).json()

    if search_res.get('total', 0) > 0:
        game_data = search_res['items'][0]
        app_id = game_data['id']
        name = game_data['name']
        
        # 3. Get detailed Price Info - Setting cc=in for Indian Rupees
        price_url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=in"
        price_res = requests.get(price_url).json()
        
        if price_res[str(app_id)]['success']:
            data = price_res[str(app_id)]['data']
            
            st.header(f"Results for: {name}")
            st.image(data['header_image'])
            
            if 'price_overview' in data:
                current_price = data['price_overview']['final_formatted']
                discount = data['price_overview']['discount_percent']
                
                col1, col2 = st.columns(2)
                col1.metric("Current Price", current_price)
                col2.metric("Discount", f"{discount}%")
                
                if discount > 0:
                    st.success(f"🔥 SALE ALERT! {name} is currently {discount}% off in India!")
                else:
                    st.info("Currently at full price in the Indian Store.")
            else:
                st.write("This game appears to be Free to Play!")
    else:
        st.error("Could not find that game. Try checking the spelling on Steam!")
