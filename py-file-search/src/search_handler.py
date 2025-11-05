from everytools import Search
import os


class FileSearchHandler:
    
    def read_lines_from_file(self, file_path):
        """读取文件中的所有行"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件 {file_path} 不存在")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
        return lines
    
    def search_line(self, line):
        """搜索单行内容"""
        search = Search(line)
        search.execute()
        results = search.get_results()
        return results
    
    def process_file_searches(self, file_path):
        """处理文件中的所有搜索"""
        lines = self.read_lines_from_file(file_path)
        results = []
        
        for line in lines:
            search_results = self.search_line(line)
            exists = len(search_results) > 0
            results.append({
                'line': line,
                'exists': exists,
                'results': search_results
            })
        
        # 按不存在在前，存在在后排序
        results.sort(key=lambda x: x['exists'])
        return results
    
    def display_results(self, results):
        """显示结果"""
        for item in results:
            if item['exists']:
                print(f"{item['line']} - 存在")
            else:
                print(f"{item['line']} - 不存在")


