class Addr:
    def __init__(self, name, phonenumber, email, address, group): # 초기값(생성자) 설정
        self.name = name # 이름
        self.phonenumber = phonenumber # 전화번호
        self.email = email # 이메일
        self.address = address # 주소
        self.group = group #그룹(가족/친구)

    def print_info(self): # 객체를 문자열로 표현
        return (
            f"이름: {self.name}\n" 
            f"전화번호: {self.phonenumber}\n"
            f"이메일: {self.email}\n"
            f"주소: {self.address}\n"
            f"그룹: {self.group}"
        )