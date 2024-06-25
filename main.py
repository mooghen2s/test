import subprocess
import time
import keyboard
import mss
import json
import random
import shutil
import argparse
import os

def nonton_youtube(profile_dir):
    try:
        json_file = f'videos.json'
        with open(json_file, 'r') as file:
            videos = json.load(file)
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6310.207 Safari/537.36"
            random_video = random.choice(videos)
            url = random_video['url']
            if profile_dir == 'Profile1':
                window_pos = "0000,1000"
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6310.207 Safari/537.36"
            if profile_dir == 'Profile2':
                window_pos = "0000,1500"
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6294.219 Safari/537.36"
            if profile_dir == 'Profile3':
                window_pos = "0000,2000"
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3"
            if profile_dir == 'Profile4':
                window_pos = "0000,2500"
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.61 Safari/537.36"
        print(url)            
        current_directory = os.getcwd()
        start_time_yt = random.randrange(1, 400)
        end_time_yt = random.randrange(1, 200)
        Url_browser = f'https://youtu.be/{url}&t={start_time_yt}'
        window_size = '300,300'
        command = [
            "C:/Program Files/Google/Chrome/Application/chrome.exe",
            f"--user-data-dir={current_directory}/profiles/{profile_dir}",
            f"--profile-directory={profile_dir}",
            f"--app={Url_browser}",
            f"--autoplay-policy=no-user-gesture-required",
            '--disable-extensions',
            f'--user-agent={user_agent}',
            #f"--window-position={window_pos}"
            
        ]
        chrome_process = subprocess.Popen(command)
    except Exception as e:
        print(f'Error on opening URL and profile: {e}')
        exit(1)

    # Tunggu selama 30 detik
    time.sleep(5)
    keyboard.press_and_release('f11')
    time.sleep(5)

    #keyboard.press_and_release('k') 
    # Tangkap layar dan simpan sebagai PNG
    time.sleep(10)
    print(profile_dir)
    with mss.mss() as sct:
        screenshot = sct.shot(output='screenshot.png')
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Nonton YouTube dengan profil tertentu.')
    parser.add_argument('profile_number', type=int, help='Nomor profil yang akan digunakan')
    args = parser.parse_args()
    profile_loop = f'Profile{args.profile_number}'
    for nujsi in range(1, 5):
        profile_dir = f'Profile{nujsi}'
        nonton_youtube(profile_dir)
    if profile_loop == 'Profile0':
        time.sleep(650)
