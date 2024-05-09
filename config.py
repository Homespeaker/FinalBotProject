TOKEN = "6182241691:AAFl3lahEdNLQGp3hurvMI8JeYbAIRlHc54"  # token телеграм-бота
FOLDER_ID = "b1g8ttv0k823647abdcg"
IAM_TOKEN = "t1.9euelZqKipKemMuOmIyPyprGmo-Zxu3rnpWaypuMipedjY-dxp2WipTKjJDl8_dDFA1O-e82BWMa_t3z9wNDCk757zYFYxr-zef1656VmpuOmoyNmpXPzpOQnp7Kj8eS7_zF656VmpuOmoyNmpXPzpOQnp7Kj8eSveuelZqcyJjJmIzLzpeMyJOWnZzNnbXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.InGQDuflSASZWrdh5c5aptrN579-8UnUK954pFHVI2kJBeFmIuG990iCbOllYrtONMFbNrysA_W4Tigv2qoTAw"

MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога
MAX_TTS_SYMBOLS = 1000

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов

HOME_DIR = '/home/student/FinalBotProject'  # путь к папке с проектом
LOGS = f'{HOME_DIR}/logs.txt'  # файл для логов
DB_FILE = f'{HOME_DIR}/messages.db'  # файл для базы данных
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]  # список с системным промтом

IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'  # файл для хранения iam_token
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'  # файл для хранения folder_id
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'  # файл для хранения bot_token