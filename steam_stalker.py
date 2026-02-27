import streamlit as st
import requests

st.set_page_config(page_title="Steam Price Stalker", page_icon="🎮")
st.title("🎮 Steam Game Price Stalker (India)")

# 1. Input for Game Name
game_name = st.text_input("Enter Game Name (e.g., 'Cyberpunk 2077'):")

if game_name:
    # 2. Get AppID (Broad search works best for regional stores)
    search_url = f"https://store.steampowered.com/api/storesearch/?term={game_name}&l=english"
    search_res = requests.get(search_url).json()

    if search_res and search_res.get('total', 0) > 0:
        game = search_res['items'][0]
        app_id = str(game['id'])
        
        # 3. Get Indian Price Data
        price_url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=in"
        price_res = requests.get(price_url).json()
        
        # Safety Check: Does the data actually exist?
        if price_res and price_res.get(app_id, {}).get('success'):
            data = price_res[app_id]['data']
            st.header(data.get('name', 'Game Found'))
            st.image(data.get('header_image', ''))
            
            # 4. Smart Price Display
            if 'price_overview' in data:
                # This pulls the ₹ formatted price directly from Steam
                price_inr = data['price_overview'].get('final_formatted', 'Price Unknown')
                discount = data['price_overview'].get('discount_percent', 0)
                
                col1, col2 = st.columns(2)
                col1.metric("Current Price (INR)", price_inr)
                col2.metric("Discount", f"{discount}%")
                
                if discount > 0:
                    st.balloons()
                    st.success(f"🔥 SALE! Currently {discount}% off on the Indian Store!")
            else:
                # Some games like CS2 or Dota 2 don't have a 'price_overview'
                st.info("This game is either Free to Play or the Indian price hasn't been set yet.")
        else:
            st.error("Steam is having trouble loading Indian regional data for this game.")
    else:
        st.warning("Could not find that game. Try a more specific title.")                
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
