import pandas as pd
from typing import NoReturn, Tuple
import os

MD_Template = """[$question$]($url$)

[ChatGPT](chat.openai.com)

---

## 1. 问题的内容
**1.1 题目描述**：

**1.2 示例**：

**1.3 提示**:

## 2. 边界情况和约束


## 3. 算法和策略

---

"""

class LeetCodeDirectoryManager:
    """
    A class to create directories and files for LeetCode problems based on an input DataFrame.
    
    Attributes:
        df (pd.DataFrame): A DataFrame containing columns for 'question', 'level', and possibly other metadata.
        base_dir (str): The base directory path where the structure will be created.
    
    Methods:
        create_directories_and_files(): Creates the directory structure and files.
        format_question_name(name: str): Formats the question name with a five-digit prefix.
        make_dir(path: str): Ensures a directory exists.
        create_file(path: str): Creates an empty file.
    """

    def __init__(self, df: pd.DataFrame, base_dir: str) -> NoReturn:
        """
        Initializes the LeetCodeDirectoryManager with a DataFrame and base directory path.
        
        Args:
            df (pd.DataFrame): The DataFrame containing LeetCode problems.
            base_dir (str): The base directory where the directories and files will be created.
        """
        self.df = df
        self.base_dir = base_dir

    def create_directories_and_files(self) -> NoReturn:
        """
        Creates directories based on difficulty levels and question names, and generates empty Python and Markdown files.
        """
        for _, row in self.df.iterrows():
            level_dir = self.format_level_directory(row['level'])
            question_dir = self.format_question_name(row['question'])
            full_path = os.path.join(self.base_dir, level_dir, question_dir)

            self.make_dir(full_path)
            self.create_file(os.path.join(full_path, f"{question_dir}.py"))
            self.create_file(os.path.join(full_path, f"{question_dir}.md"), row['question'], row['url'])

    @staticmethod
    def format_question_name(name: str) -> str:
        """
        Formats the question name to include a five-digit prefix and make it suitable for a directory name.
        
        Args:
            name (str): The original question name.
        
        Returns:
            str: The formatted question name suitable for a directory.
        """
        parts = name.split(". ", 1)
        if len(parts) == 2:
            num, rest = parts
            formatted_num = num.zfill(5)  # Fill the number to ensure it has five digits
            return f"{formatted_num}. {rest}".replace(" ", "_")
        return name.replace(" ", "_")

    @staticmethod
    def format_level_directory(level: str) -> str:
        """
        Maps the difficulty level to a directory name.
        
        Args:
            level (str): The difficulty level ('简单', '中等', '困难').
        
        Returns:
            str: The corresponding directory name ('1-Easy', '2-Medium', '3-Hard').
        """
        return {
            "简单": "1-Easy",
            "中等": "2-Medium",
            "困难": "3-Hard"
        }.get(level, "Unknown")

    @staticmethod
    def make_dir(path: str) -> NoReturn:
        """
        Ensures a directory exists; creates it if it does not.
        
        Args:
            path (str): The path to the directory.
        """
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def create_file(path: str, question = '', url = '') -> NoReturn:
        """
        Creates an empty file at the specified path.
        
        Args:
            path (str): The path where the file will be created.
        """
        with open(path, 'w') as file:
            if path.endswith(".md"):
                file.write(MD_Template.replace("$question$", question).replace("$url$", url))
            file.close()



class LeetCodeMarkdownGenerator:
    """
    A class to generate a Markdown file from an Excel file containing LeetCode problems.
    
    Attributes:
        file_path (str): The path to the Excel file.
        markdown_path (str): The path where the Markdown file will be saved.
    
    Methods:
        read_excel(): Reads the Excel file and returns a DataFrame.
        generate_markdown(df: pd.DataFrame): Generates a Markdown table from the DataFrame.
        save_markdown(content: str): Saves the Markdown content to a file.
        run(): The main method to execute the class functionality.
    
    Example:
        generator = LeetCodeMarkdownGenerator('leetcode_problems.xlsx', 'leetcode_problems.md')
        generator.run()
    """

    def __init__(self, file_path: str, markdown_path: str):
        """
        Initializes the LeetCodeMarkdownGenerator with file paths.
        
        Args:
            file_path (str): The path to the Excel file.
            markdown_path (str): The path to save the Markdown file.
        """
        self.file_path = file_path
        self.markdown_path = markdown_path

    def read_excel(self) -> pd.DataFrame:
        """
        Reads the Excel file and returns a DataFrame with necessary formatting.
        
        Returns:
            pd.DataFrame: The formatted DataFrame containing LeetCode problems.
        """
        df = pd.read_excel(self.file_path)
        df['formatted_question'] = df['question'].apply(self.format_question_name)
        return df

    @staticmethod
    def format_question_name(name: str) -> str:
        """
        Formats the question name to include a five-digit prefix.
        
        Args:
            name (str): The original question name.
        
        Returns:
            str: The formatted question name.
        
        Example:
            >>> LeetCodeMarkdownGenerator.format_question_name('2. 两数相加')
            '00002. 两数相加'
        """
        parts = name.split(". ", 1)
        if len(parts) == 2:
            num, rest = parts
            formatted_num = num.zfill(5)  # Fill the number to ensure it has five digits
            return f"{formatted_num}. {rest}"
        return name

    def generate_markdown(self, df: pd.DataFrame) -> str:
        """
        Generates a Markdown table string from the DataFrame.
        
        Args:
            df (pd.DataFrame): The DataFrame containing LeetCode problems.
        
        Returns:
            str: The Markdown table as a string.
        """
        # Define the Markdown table header
        markdown_content = "| Question | Markdown | People | Rate | Level |\n|---|---|---|---|---|\n"
        for _, row in df.iterrows():
            folder = '1-Easy' if row['level'] == '简单' else '2-Medium' if row['level'] == '中等' else '3-Hard'
            markdown_path = f"{folder}/{row['formatted_question'].replace(' ', '_')}/{row['formatted_question'].replace(' ', '_')}.md"
            markdown_content += f"| [{row['formatted_question']}]({row['url']}) | [Markdown]({markdown_path}) | {row['people']} | {row['rate']} | {row['level']} |\n"
        return markdown_content

    def save_markdown(self, content: str):
        """
        Saves the Markdown content to the specified file.
        
        Args:
            content (str): The Markdown content to save.
        """
        with open(self.markdown_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def run(self):
        """
        Executes the main functionality of the class: Processing the Excel file and generating a Markdown file.
        """
        df = self.read_excel()
        markdown_content = self.generate_markdown(df)
        self.save_markdown(markdown_content)
        print(f"Markdown file generated at {self.markdown_path}")

# Example usage
if __name__ == "__main__":
    # file_path = 'leetcode_problems.xlsx'  # Update with the actual path
    # markdown_path = 'Leetcode Problems.md'  # Update with the desired Markdown file path
    # generator = LeetCodeMarkdownGenerator(file_path, markdown_path)
    # generator.run()
    base_dir = "."
    df = pd.read_excel("leetcode_problems.xlsx")
    directory_manager = LeetCodeDirectoryManager(df, base_dir)
    directory_manager.create_directories_and_files()