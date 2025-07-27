import os
import json
import csv
from tqdm import tqdm

def extract_unique_tags(data_raw_dir):
    unique_type_tags = set()
    unique_tags = set()

    json_files = []
    for root, _, files in os.walk(data_raw_dir):
        for file_name in files:
            if file_name.endswith(".json"):
                json_files.append(os.path.join(root, file_name))

    for file_path in tqdm(json_files, desc="JSON 파일 처리 중"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Extract type_tag
            if "virustotal" in data and "type_tag" in data["virustotal"]:
                type_tag = data["virustotal"]["type_tag"]
                if type_tag:
                    unique_type_tags.add(type_tag)

            # Extract tags
            if "virustotal" in data and "tags" in data["virustotal"]:
                tags = data["virustotal"]["tags"]
                if isinstance(tags, list):
                    for tag in tags:
                        if tag:
                            unique_tags.add(tag)

        except json.JSONDecodeError:
            print(f"경고: {file_path} 파일이 유효한 JSON 형식이 아닙니다. 건너킵니다.")
        except Exception as e:
            print(f"경고: {file_path} 파일 처리 중 오류 발생: {e}")

    return sorted(list(unique_type_tags)), sorted(list(unique_tags))

def save_to_csv(data_list, filename, header):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([header])
        for item in data_list:
            writer.writerow([item])

if __name__ == "__main__":
    data_raw_directory = "/home/ysw/robust-malware-graph/data/raw"
    
    # data/raw 디렉토리가 존재하는지 확인
    if not os.path.isdir(data_raw_directory):
        print(f"오류: 지정된 디렉토리 '{data_raw_directory}'를 찾을 수 없습니다.")
        print("data/raw 디렉토리에 JSON 파일이 있는지 확인해주세요.")
    else:
        type_tags, tags = extract_unique_tags(data_raw_directory)

        print("--- 모든 고유한 type_tag 종류 ---")
        if type_tags:
            for tt in type_tags:
                print(f"- {tt}")
            save_to_csv(type_tags, "unique_type_tags.csv", "type_tag")
            print("type_tag 정보가 unique_type_tags.csv 파일에 저장되었습니다.")
        else:
            print("type_tag 정보가 발견되지 않았습니다.")

        print("\n--- 모든 고유한 tags 종류 ---")
        if tags:
            for t in tags:
                print(f"- {t}")
            save_to_csv(tags, "unique_tags.csv", "tag")
            print("tags 정보가 unique_tags.csv 파일에 저장되었습니다.")
        else:
            print("tags 정보가 발견되지 않았습니다.")