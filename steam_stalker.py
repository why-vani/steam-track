import streamlit as st
import requests

st.set_page_config(page_title="Steam Stalker", page_icon="🎮")
st.title("🎮 Steam Game Price Stalker")

# 1. Sidebar for Currency Conversion
st.sidebar.header("Settings")
currency_mode = st.sidebar.radio("Display Price In:", ["USD ($)", "INR (₹)"])
# Current exchange rate for Feb 2026 - You can change this number
exchange_rate = 86.50 

# 2. Input Box
game_name = st.text_input("Enter Game Name (e.g., 'Elden Ring'):")

if game_name:
    try:
        # Search for the game ID using US store (most stable)
        search_url = f"https://store.steampowered.com/api/storesearch/?term={game_name}&l=english&cc=US"
        search_res = requests.get(search_url).json()

        if search_res and search_res.get('total', 0) > 0:
            game = search_res['items'][0]
            app_id = str(game['id'])
            
            # Get US Price Data
            price_url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=US"
            price_res = requests.get(price_url).json()
            
            if price_res and price_res.get(app_id, {}).get('success'):
                data = price_res[app_id]['data']
                st.header(data.get('name', 'Game Found'))
                st.image(data.get('header_image', ''))
                
                if 'price_overview' in data:
                    # Get the raw numeric price (in cents, e.g., 5999 for $59.99)
                    raw_price_usd = data['price_overview'].get('final', 0) / 100
                    discount = data['price_overview'].get('discount_percent', 0)
                    
                    # 3. Handle the Conversion Logic
                    if currency_mode == "INR (₹)":
                        final_price = raw_price_usd * exchange_rate
                        display_text = f"₹{final_price:,.2f}"
                        label = "Converted Price (INR)"
                    else:
                        display_text = f"${raw_price_usd:.2f}"
                        label = "Current Price (USD)"
                    
                    col1, col2 = st.columns(2)
                    col1.metric(label, display_text)
                    col2.metric("Discount", f"{discount}%")
                    
                    if discount > 0:
                        st.success(f"🔥 SALE ALERT! {discount}% off on Steam!")
                else:
                    st.info("This game appears to be Free to Play!")
            else:
                st.error("Could not fetch price data from Steam.")
        else:
            st.warning("Game not found. Try a more specific title.")
            
    except Exception as e:
        st.error(f"App Error: {e}")                col2.metric("Discount", f"{discount}%")
                
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
