import argparse
import sys
from src.search_handler import FileSearchHandler
# import os

def main():
    parser = argparse.ArgumentParser(description='搜索文件中的每一行')
    parser.add_argument('-f', '--file', required=False, help='输入文件路径')

    args = parser.parse_args()

    handler = FileSearchHandler()
    try:
        if args.file:
            file_path = args.file
        else:
            # 交互模式：提示用户输入文件路径
            try:
                file_path = input("请输入文件路径: ").strip()
            except EOFError:
                print("\n错误: 未提供文件路径且无法读取输入")
                return
            if not file_path:
                print("错误: 文件路径不能为空")
                return

        results = handler.process_file_searches(file_path)
        handler.display_results(results)
    except FileNotFoundError as e:
        print(f"错误: {e}")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    main()
