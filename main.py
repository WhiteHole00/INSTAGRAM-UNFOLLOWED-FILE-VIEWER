from datetime import datetime, timedelta, timezone
import json
import os

def isTimestampToTime(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    korea_timezone = timezone(timedelta(hours=9)) 
    korea_time = utc_time.replace(tzinfo=timezone.utc).astimezone(korea_timezone)
    
    return korea_time

def isReading(path):
    with open(path,"r",encoding="UTF-8") as f:
        data = json.load(f)
    return data

def main():
    from setting import PATH
    
    try:
        if os.path.exists(PATH):
            for data_ in isReading(PATH)["relationships_unfollowed_users"]:
                for info in data_["string_list_data"]:
                    link = info["href"]
                    insta_id = info["value"]
                    timestamp = info["timestamp"]

                    time = isTimestampToTime(timestamp).strftime(f"%Y년 %m월 %d일 | %H시 %M분 %S초")
                    
                    print(f"""
                        인스타그램 링크 : {link}
                        인스타그램 아이디 : {insta_id}
                        언팔로우 한 시간 : {time}
                    """,end="")
                print()
        else:
            return input(f"'{PATH}' 파일이 존재 하지 않습니다.")
    except Exception as e:
        return input(f"{PATH} 값은 비어 있으면 안됩니다.")


if __name__ == "__main__":
    main()

#by WhiteHole