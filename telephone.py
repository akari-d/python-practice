import logging
import sys
class Logger_set:
    def __init__(self):
        self.logger = logging.getLogger("ロガー侍")

    def log_set(self):
        logger = self.logger
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("sales_analysis.log", encoding="utf-8")
        file_handler.setLevel(logging.ERROR)
        file_formatter = logging.Formatter("%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s")
        file_handler.setFormatter(file_formatter)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s")
        console_handler.setFormatter(console_formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger



class Contact:
    def __init__(self):
        self.contact = []
        self.logger = Logger_set().log_set()

    def add_contact(self, name_1, name_2, telephone_num, mail_address, group):
        try:
            logger = self.logger

            contact_add = {
            "姓":name_1,
            "名":name_2,
            "電話番号":telephone_num,
            "メールアドレス":mail_address,
            "グループ":group
            }
            self.contact.append(contact_add)
            logger.info(f"{name_1}{name_2}さんを連絡先に追加しました。詳細:{contact_add}")

            for k,v in contact_add.items()
                    logger.error("名前(SEIとmeIのどちらか））を入力してください")
                    print()

        except:
            pass

    def remove_contact(self, name_1, name_2):
        logger = self.logger
        try:
            for x in self.contact:
                if x["姓"] == name_1 and x["名"] == name_2:
                    self.contact.remove(x)
                    logger.info(f"{name_1}{name_2}さんを連絡先から除去しました")
                elif x["姓"] == name_1 or x["名"] == name_2:
                    logger.error(f"入力された情報は姓と名が不一致のため除去できませんでした。\n当てはまりそうな連絡先{x}")

                elif name_1 and name_2 == "":
                    logger.error(f"名前に空白の情報が入力されたため、検索できません")
                else:
                    logger.error("対象の連絡先がみつかりませんでした")
        except:
            pass


    def search_contact(self, contact_search):
        try:
            logger = self.logger
            for x in self.contact:
                if contact_search in x["姓"] or x["名"]:
                    logger.info(f"検索の結果を表示します：{x}")
                else:
                    logging.error("入力された名前の連絡先が見つかりませんでした")



        except:
            pass



contact = Contact()
add= contact.add_contact("檀上","アカリ", "080-6261-3212", "joru@gmail.com", "家族")
add_2= contact.add_contact("","", "090-8245-7276", "ayako@gmail.com", "家族")
#b = contact.remove_contact(input("削除したい人物を入力してください:"))
#c = contact.search_contact("檀")