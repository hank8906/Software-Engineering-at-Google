import re
import os
import opencc

# 創建OpenCC實例，s2twp.json是從簡轉凡的轉換規則
converter = opencc.OpenCC('s2t')

# 讀取Markdown文件
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    return markdown_text

# 寫入Markdown文件
def write_markdown_file(chinese_text, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(chinese_text)

# 正則表達式模式，匹配中文字符
pattern = re.compile("[\u4e00-\u9fa5，。、？！：；《》【】「」『』“”‘’（）〈〉<>『』《》【】·]*")

# 解析Markdown文件
def extract_chinese_from_markdown(markdown_text):
    
    # 根據空行分割成段落
    paragraphs = markdown_text.split('\n\n')  
    chinese_paragraphs = []

    for paragraph in paragraphs:
        chinese_text = "".join(pattern.findall(paragraph))
        if chinese_text:
            chinese_paragraphs.append(chinese_text)

    # 將中文段落用空行連接起來
    chinese_text = "\n\n".join(chinese_paragraphs)
    return chinese_text

# 輸入和輸出文件路徑
input_file_path = r'C:\Users\Hank\EnToCh\Software-Engineering-at-Google\zh-cn'
output_file_path = r'C:\Users\Hank\EnToCh\Software-Engineering-at-Google\zh-cn-chinese'

for folder_name in os.listdir(input_file_path):
    print(folder_name)
    
    chapter_folder = os.path.join(input_file_path, folder_name)
    print(chapter_folder)
    
    if not os.path.isdir(chapter_folder):
        continue
    
    input_folder_path = os.path.join(chapter_folder, f'{folder_name}.md')
    print(input_folder_path)

    # 檢查輸入文件是否存在
    if not os.path.exists(input_folder_path):
        print(f"文件 {input_folder_path} 不存在。")
        continue

    # 讀取Markdown文件
    markdown_text = read_markdown_file(input_folder_path)

    # 提取中文内容
    chinese_text = extract_chinese_from_markdown(markdown_text)

    # 進行簡轉繁
    traditional_text = converter.convert(chinese_text,)

    # 確定輸出文件夾是否存在，如果不存在則創建
    if not os.path.exists(output_file_path):
        os.makedirs(output_file_path)

    # 寫入Markdown文件
    output_folder_path = os.path.join(output_file_path, f'{folder_name}_Chinese.md')
    write_markdown_file(traditional_text, output_folder_path)

    print("提取的中文内容已保存到output.md文件中。\n")
