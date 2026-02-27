import streamlit as st
import requests

st.set_page_config(page_title="Steam Price Stalker", page_icon="🎮")
st.title("🎮 Steam Game Price Stalker (India)")
st.write("Now tracking in ₹ (INR) for your university project.")

# 1. Input for Game Name
game_name = st.text_input("Enter Game Name (e.g., 'Grand Theft Auto V'):")

if game_name:
    # 2. Find the Game ID (AppID)
    # We use a more general search first to ensure we find the game
    search_url = f"https://store.steampowered.com/api/storesearch/?term={game_name}&l=english"
    search_res = requests.get(search_url).json()

    if search_res and search_res.get('total', 0) > 0:
        game_data = search_res['items'][0]
        app_id = game_data['id']
        name = game_data['name']
        
        # 3. Get detailed Price Info - Specifically forcing India region (cc=in)
        price_url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=in"
        price_res = requests.get(price_url).json()
        
        # Safety check: ensure the app_id exists in the response
        if str(app_id) in price_res and price_res[str(app_id)]['success']:
            data = price_res[str(app_id)]['data']
            
            st.header(f"Results for: {name}")
            st.image(data.get('header_image', ''))
            
            # Check if 'price_overview' exists (paid games)
            if 'price_overview' in data:
                current_price = data['price_overview']['final_formatted']
                discount = data['price_overview']['discount_percent']
                
                col1, col2 = st.columns(2)
                col1.metric("Current Price (India)", current_price)
                col2.metric("Discount", f"{discount}%")
                
                if discount > 0:
                    st.success(f"🔥 SALE ALERT! {name} is currently {discount}% off in India!")
                else:
                    st.info("Currently at full price in the Indian Store.")
            else:
                st.write("This game appears to be Free to Play or has no price listed.")
        else:
            st.error("Steam returned an error for this game's Indian pricing data.")
    else:
        st.error("Could not find that game. Try a more specific title!")                col2.metric("Discount", f"{discount}%")
                
                if discount > 0:
                    st.success(f"🔥 SALE ALERT! {name} is currently {discount}% off in India!")
                else:
                    st.info("Currently at full price in the Indian Store.")
            else:
                st.write("This game appears to be Free to Play!")
    else:
        st.error("Could not find that game. Try checking the spelling on Steam!")                col2.metric("Discount", f"{discount}%")
                
                if discount > 0:
                    st.success(f"🔥 SALE ALERT! {name} is currently {discount}% off!")
                else:
                    st.info("Full price right now. Maybe wait for a Summer Sale?")
            else:
                st.write("This game appears to be Free to Play!")
    else:
        st.error("Could not find that game. Check the spelling!")
