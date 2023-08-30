from modules.external.google_sheet import GoogleSheetManager
from datetime import datetime

class GoogleSheetController:
    def __init__(self):
        self.manager = GoogleSheetManager()

    def start_service(self,path_to_creds,sheet_id):
        self.manager.start_service(path_to_creds, sheet_id)

    def get_all_names(self):
        all_names = self.manager.reader.read_range("B:B")
        names = []
        for name in all_names:
            names.append(name[0])
        return names

    def get_names_to_bypass(self):
        row_ids = self.manager.reader.find_row_id_by_word("F:F", "TRUE")
        all_names = self.manager.reader.read_range("B:B")
        bypass_names = []
        for row_id in row_ids:
            bypass_names.append(all_names[row_id-1][0])
        return bypass_names

    def get_names_to_login(self):
        try:
            row_ids = self.manager.reader.find_row_id_by_word("G:G", "TRUE")
        except:
            return False
        all_names = self.manager.reader.read_range("B:B")
        login_names = []
        for row_id in row_ids:
            login_names.append(all_names[row_id-1][0])
        return login_names
    
    
    def get_login_data(self,profile_id, choosed_names:list):
        row_ids = self.manager.reader.find_row_id_by_word("I:I", profile_id)
        print(row_ids)
        all_names = self.manager.reader.read_range(f"B{row_ids[0]}:B{row_ids[len(row_ids)-1:][0]}")
        all_login = self.manager.reader.read_range(f"D{row_ids[0]}:D{row_ids[len(row_ids)-1:][0]}")
        all_password = self.manager.reader.read_range(f"E{row_ids[0]}:E{row_ids[len(row_ids)-1:][0]}")
        all_together = []
        
        for i in range(len(all_names)):
            all_together.append([all_names[i][0],all_login[i][0],all_password[i][0]])

        choosed_together = []
        for i in range(len(all_together)):
            for name in choosed_names:
                if name == all_together[i-1][0]:
                    choosed_together.append(all_together[i-1])
                    choosed_names.remove(name)
        print(choosed_together)
        return choosed_together
    
    def write_word_by_name(self, account_name:str, word:str, range_letter: str):
        cell_id = self.manager.reader.find_row_id_by_word('B2:B', account_name)
        self.manager.writer.write_cell(f"{range_letter}{cell_id[0]+1}", word)
        
    def mark_success_bypass(self,account_name:str):
        self.write_word_by_name(account_name, str(datetime.now().date()), "C")