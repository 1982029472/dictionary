# conding=utf-8
import demo02
if __name__ == '__main__':

    url = input("请输入要处理的网址：")
    # 实例化
    zidian = demo02.zidian(url=url, file_name="zidianmuben.txt", new_file_name="new_dict")
    zidian.put_txt_contents()