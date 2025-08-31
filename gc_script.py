from gigachat import GigaChat
from dotenv import load_dotenv, find_dotenv
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('GIGACHAT_API_KEY')

def main():
    try:
        with GigaChat(
                    credentials=API_KEY, 
                    verify_ssl_certs=False
                     ) as giga:
            print('GigaChat have been connected')
            print("To exit type 'exit' or 'выход'.")
            while True:
                user_input = input('Ask your question:').strip()
                
                # Проверка на команду выхода
                if user_input.lower() in ['exit', 'выход']:
                    print('End of work')
                    break
                    
                # Проверка, что ввод не пустой    
                if not user_input:
                    print('Ask your question, please')
                    continue
                    
                # Отправка запроса к API
                try:
                    responce = giga.chat(user_input)
                    answer = responce.choices[0].message.content
                    # Вывод ответа модели
                    print(f"\nGigaChat: {answer.encode('utf-8', errors='ignore').decode('utf-8')}\n")
    
                except Exception as e:
                    print(f'Error using API: {e}\n')
    except Exception as e:
        print(f'Client init error: {e}\n')

if __name__ == "__main__":
    main()