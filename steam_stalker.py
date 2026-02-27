import streamlit as st
import requests

st.set_page_config(page_title="Steam Price Stalker", page_icon="🎮")
st.title("🎮 Steam Game Price Stalker (India)")
st.write("Track prices in ₹ (INR) for your university project.")

# 1. Input for Game Name
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
        st.error("Could not find that game. Try checking the spelling on Steam!")                    raw_price_usd = data['price_overview'].get('final', 0) / 100
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
