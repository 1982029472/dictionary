# conding=utf-8
import exrex


class zidian:
    def __init__(self, url, new_file_name="new_dict.txt", file_name="zidianmuben.txt"):
        self.url = url
        self.file_name = file_name
        self.new_file_name = new_file_name

    def get_url(self):
        # 切割获取域名
        url_list = self.url.split(".")
        # 检查长度
        len(url_list)

        # 获取第一位的字符串
        new_url_list = [url_list[0].split(".")[-1]]

        for value in url_list:
            if value == url_list[0] or value == url_list[-1]:
                continue
            new_url_list.append(value)
        # 更新new_url_list
        return new_url_list

    # 读字典母本，去除\n
    def get_txt_contents(self):
        with open(f"{self.file_name}", "r") as f:
            dict_list = f.read().splitlines()
            return dict_list

    def put_txt_contents(self):

        with open(f"new_{self.new_file_name}.txt", "a", newline="") as f:
            for value in self.get_txt_contents():
                for i in range(0, len(self.get_url())):
                    for j in range(0, len(self.get_url())):
                        a = self.get_url()[i]
                        b = self.get_url()[j]
                        dicts = list(exrex.generate(rf"{a}{value}{b}"))
                        f.write(dicts[0] + "\n")


