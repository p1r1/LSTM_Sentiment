import os
import srt
import re


#
# def cleanhtml(raw_html):
#     cleanr = re.compile(r'<.*?>')
#     cleantext = re.sub(cleanr, '', raw_html)
#     return cleantext

def convert_srt():
    for path, subdirs, files in os.walk("D:\\subtitle"):
        for name in files:
            file_path = os.path.join(path, name)
            print(file_path)
            if ".srt" in name:
                try:
                    subs = list(srt.parse(open(file_path, "r")))
                    full_text = ""
                    for sub in subs:
                        text = srt.make_legal_content(sub.content)
                        text = re.sub('<[^<]+?>', '', text)
                        text = text.replace('...', " ")
                        text = text.replace('-', "")
                        # text = text.replace('\r\n', " ")
                        text = text.replace('\n', " ")

                        full_text += text

                    print(full_text)
                    file = open("D:\\subtitle\\Converted\\" + name + "_converted.txt", "w")
                    file.write(full_text)
                    file.close()
                    print("___________________________________________")
                except:
                    pass
            elif ".sub" in name:
                pass
            else:
                pass
