import telebot

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def detect_bird(path_img):
    np.set_printoptions(suppress=True)
    model = load_model("keras_model.h5", compile=False)
    class_names = open("labels.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open("<IMAGE_PATH>").convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)


bot = telebot.TeleBot('8181528627:AAGo7VlYk5xg4ZgXPgtuBuHQXLgsezOtsiI')


@bot.message_handler()
def start_message(message):
    bot.reply_to(message, 'Hello!')

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    if not message.photo:
        return bot.send_message(message.chat.id, 'Вы забыли загрузить картинку')
    
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    cl, proc = detect_bird(file_name)
    if cl == 'Голубь\n':
        bot.send_message(message.chat.id, 'Это голубь')
    elif cl == 'Синица\n':
        bot.send_message(message.chat.id, 'Это синица')


bot.polling()
