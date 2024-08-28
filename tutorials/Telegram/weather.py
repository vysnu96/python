from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Updater, \
    CallbackQueryHandler, CallbackContext
import requests, json
import aiohttp
import datetime

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
API_KEY = "440679f383ee7dff65187940e5eed580"

# VISHNU BOT
# TOKEN: Final = '7422793066:AAGn7AxNO5dqF6wrf40uydFfw9vL_LygOHw'
# BOT_USERNAME: Final = '@Genie_vishnu_bot'

# Second BOT
TOKEN: Final = '6023330435:AAHZuszxtg8CIaGIkBKMJR1KpF7uCICZxS0'
BOT_USERNAME: Final = '@vysnuubuntubot'


# Gir BOT
# TOKEN: Final = '7423907569:AAFe0PcuSH8dH6GY7Gf9BjRRN6Sovk6sMGY'
# BOT_USERNAME: Final = '@Kirthi27_bot'


# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello!")


# async def chennai_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f"{BASE_URL}chennai&appid={API_KEY}") as response:
#             data = await response.json()
#             weather = data["weather"][0]["description"]
#             icon = data["weather"][0]["icon"]
#             get_icon = f"https://openweathermap.org/img/wn/{icon}@2x.png"
#             temp = round(data["main"]["temp"] - 273.15, 2)
#             feels_like = round(data["main"]["feels_like"] - 273.15, 2)
#             dict = (
#                 f"weather:<b>{weather}</b>\n"
#                 # f"<img src='{get_icon}'/>\n"
#                 f"Temperature:{temp}°C\n"
#                 f"Feels like:<b style=\"color: green;\">{feels_like}°C</b>\n"
#             )
# response = requests.get(f"{BASE_URL}chennai&appid={API_KEY}")
# await update.message.reply_text(dict, parse_mode='HTML')

# Sends the weather report of requested location
async def handle_response(text: str) -> str:
    processed: str = text.lower()
    # if 'hello' or 'hi' in processed:
    #     return "Hi there! Enter a place name to find the weather"
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}{processed}&appid={API_KEY}") as response:
            print(processed)
            data = await response.json()
            print(data)
            date = datetime.datetime.fromtimestamp(data["dt"])
            sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            dict = (
                f"Hi, Have a nice day\n"
                f"It's <b>{data["weather"][0]["description"]}</b>\n"
                f"Temperature:{round(data["main"]["temp"] - 273.15, 2)} °C\n"
                f"Feels like:<b style=\"color: green;\">{round(data["main"]["feels_like"] - 273.15, 2)}°C</b>\n"
                f"Minimum Temperature: {round(data["main"]["temp_min"] - 273.15, 2)} °C\n"
                f"Maximum Temperature: {round(data["main"]["temp_max"] - 273.15, 2)} °C\n"
                f"Pressure: {data["main"]["pressure"]} hPa\n"
                f"Humidity: {data["main"]["humidity"]} %\n"
                f"Visibility: {data["visibility"] / 1000} KM\n"
                f"Wind Speed: {data["wind"]["speed"]}m/s\n"
                f"Wind Direction: {data["wind"]["deg"]}°\n"
                f"Overall Cloudiness: {data["clouds"]["all"]}%\n"
                f"Sunrise at: {sunrise.strftime('%I:%M')}\n"
                f"Sunset at: {sunset.strftime('%I:%M')}\n"
                f"Weather calculated at: {date.strftime('%d-%b-%d,%I:%M:%S %p')}\n"
            )
    return dict


# Handles the location from the user for the weather report
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f"user {update.message.chat.id} in {message_type}: {text}")
    response: str = await handle_response(text)

    await update.message.reply_text(response, parse_mode='HTML')


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("I'm called")
    await update.message.reply_text("Please enter the location name to get the weather report")


# Sends weather report based on the provided live location using the latitude and longitude values
async def lat_lon(lat, lon) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}") as response:
            print(lat, lon)
            data = await response.json()
            print(data)
            date = datetime.datetime.fromtimestamp(data["dt"])
            sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            dict = (
                f"Hi, Have a nice day\n"
                f"It's <b>{data["weather"][0]["description"]}</b>\n"
                f"Temperature:{round(data["main"]["temp"] - 273.15, 2)} °C\n"
                f"Feels like:<b style=\"color: green;\">{round(data["main"]["feels_like"] - 273.15, 2)}°C</b>\n"
                f"Minimum Temperature: {round(data["main"]["temp_min"] - 273.15, 2)} °C\n"
                f"Maximum Temperature: {round(data["main"]["temp_max"] - 273.15, 2)} °C\n"
                f"Pressure: {data["main"]["pressure"]} hPa\n"
                f"Humidity: {data["main"]["humidity"]} %\n"
                f"Visibility: {data["visibility"] / 1000} KM\n"
                f"Wind Speed: {data["wind"]["speed"]}m/s\n"
                f"Wind Direction: {data["wind"]["deg"]}°\n"
                f"Overall Cloudiness: {data["clouds"]["all"]}%\n"
                f"Sunrise at: {sunrise.strftime('%I:%M')}\n"
                f"Sunset at: {sunset.strftime('%I:%M')}\n"
                f"Weather calculated at: {date.strftime('%d-%b-%d,%I:%M:%S %p')}\n"
            )
    return dict


# Obtain the location of the user with the co ordinates
async def reverse_geocode(lat, lon):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f"https://us1.locationiq.com/v1/reverse?key=pk.8d18acb371edd88cb226b467a01aefc1&lat={lat}&lon={lon}&format=json") as response:
            data = await response.json()
            user_loc = (f"{data["address"]["county"]}")
            return user_loc


# Start of the command to share location
async def live_weather(update: Update, context: CallbackContext):
    location_button = InlineKeyboardButton(text="Send Live Location", callback_data="Request Location")
    reply_markup = InlineKeyboardMarkup([[location_button]])
    await update.message.reply_text("Please share your location:", reply_markup=reply_markup)


# Sends a inline button to share live location
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    location_button = KeyboardButton(text="Send Live Location", request_location=True)
    reply_markup = ReplyKeyboardMarkup([[location_button]], one_time_keyboard=True)
    await query.message.reply_text("Click the button below to share your live location:", reply_markup=reply_markup)

    # await query.edit_message_text(text=f"Selected option: {query.data}")


# Handles the location data from the user
async def location_handler(update: Update, context: CallbackContext):
    user_location = update.message.location
    latitude = user_location.latitude
    longitude = user_location.longitude
    response: str = await lat_lon(latitude, longitude)
    location_name: str = await reverse_geocode(latitude, longitude)
    message = "Your current location is " + location_name + "\n" + response
    print(message)
    await update.message.reply_text(message, parse_mode='HTML')


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Sends a message with three inline buttons attached."""
#     keyboard = [
#         [
#             InlineKeyboardButton("Option 1", callback_data="1"),
#             InlineKeyboardButton("Option 2", callback_data="2"),
#         ],
#         [InlineKeyboardButton("Option 3", callback_data="3")],
#     ]
#
#     reply_markup = InlineKeyboardMarkup(keyboard)
#
#     await update.message.reply_text("Please choose:", reply_markup=reply_markup)


if __name__ == "__main__":
    print("starting bot...")
    app = Application.builder().token(TOKEN).build()

    # app.add_handler(CommandHandler('chennai_weather', chennai_weather))
    # app.add_handler(CommandHandler("reverse", reverse_command))
    app.add_handler(CommandHandler("live_weather", live_weather))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.LOCATION, location_handler))

    app.add_handler(CommandHandler("weather", location))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # app.add_handler(MessageHandler(filters.TEXT, handle_location))

    print("polling...")
    app.run_polling(poll_interval=3)
