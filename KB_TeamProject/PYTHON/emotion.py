import random
class EMOTION:
    def __init__(self):
        return None
    
    def indiJoy(self, rn):
        indiJoySong = [
            # 완벽해 - 레터플로우
            'https://www.youtube.com/watch?v=56vTXXk5PSQ&pp=ygUZ66CI7YSw7ZSM66Gc7JqwIOyZhOuyve2VtA%3D%3D',
            # 예쁜 말 - 어나니머스 아티스트
            'https://www.youtube.com/watch?v=0Bk_8tEEYzA&pp=ygUZ7JiI7IGc66eQIOyWtOuCmOuLiOuouOyKpA%3D%3D',
            # UP DOWN - 어나니머스 아티스트
            'https://www.youtube.com/watch?v=nw_o_qymHoM&pp=ygUl7Ja064KY64uI66i47IqkIOyVhO2LsOyKpO2KuCB1cCBkb3duIA%3D%3D',
            # 뭘 믿고 그렇게 이쁜거니 - 레터플로우
            'https://www.youtube.com/watch?v=DnVm2LENTec&pp=ygUw662Y66-_6rOgIOq3uOugh-qyjCDsnbTsgZzqsbDri4gg66CI7YSw7ZSM66Gc7Jqw',
            # ocean view - 로시
            'https://www.youtube.com/watch?v=5wiW60inhgw&pp=ygUN66Gc7IucIOyYpOyFmA%3D%3D'
        ]
        return indiJoySong[rn]

    def indiSad(self, rn):
        indiSadSong = [
            # 내 맘이 어떻든 - 레터플로우
            'https://www.youtube.com/watch?v=0pg00YztwNI&pp=ygUk64K0IOunmOydtCDslrTrlrvrk6Ag66CI7YSw7ZSM66Gc7Jqw',
            # 꺼져 - 이민석
            'https://www.youtube.com/watch?v=XeR-_xlr608&pp=ygUQ7J2066-87ISdIOq6vOyguA%3D%3D',
            # 놓아 - 이민석
            'https://www.youtube.com/watch?v=CpBl_3LG8bI&pp=ygUQ7J2066-87ISdIOuGk-yVhA%3D%3D',
            # 무너져 - 바닐라 어쿠스틱
            'https://www.youtube.com/watch?v=xBY_9xf-u2A&pp=ygUg67CU64uQ6528IOyWtOy_oOyKpO2LsSDrrLTrhIjsoLg%3D',
            # 미안해 - 스웨덴 세탁소
            'https://www.youtube.com/watch?v=-CPQY3Qh1cE&pp=ygUd7Iqk7Juo6420IOyEuO2DgeyGjCDrr7jslYjtlbQ%3D'
        ]
        return indiSadSong[rn]

    def indiAnger(self, rn):
        indiAngerSong = [
            # Hi Bully - 터치드
            'https://www.youtube.com/watch?v=tOI2K1CD_Ik&pp=ygUW7ZWY7J2067aI66asIO2EsOy5mOuTnA%3D%3D',
            # lovers in the night - seori
            'https://www.youtube.com/watch?v=RLPWiQKqi-I&pp=ygUTbG92ZXJzIGluIHRoZSBuaWdodA%3D%3D',
            # 여우별 - 어나니머스 아티스트
            'https://www.youtube.com/watch?v=suUzX5EErFw&pp=ygUm7Ja064KY64uI66i47IqkIOyVhO2LsOyKpO2KuCDsl6zsmrDrs4Q%3D',
            # 퇴사 - 이민석
            'https://www.youtube.com/watch?v=bJkhBZ1ZcuY&pp=ygUQ7Ye07IKsIOydtOuvvOyEnQ%3D%3D',
            # 무음모드 - 와인루프
            'https://www.youtube.com/watch?v=0orGwjKVjJ4&pp=ygUZ66y07J2M66qo65OcIOyZgOyduOujqO2UhA%3D%3D'
        ]
        return indiAngerSong[rn]

    def indiUnrest(self, rn):
        indiUnrestSong = [
            # 아무도 그대를 바라지 않는 - 알레프
            'https://www.youtube.com/watch?v=2iczc21Czio&pp=ygUk7JWE66y064-EIOq3uOuMgOulvCDrsJTrnbzsp4Ag7JWK64qU',
            # 나는 왜 - O.O.O
            'https://www.youtube.com/watch?v=WtzwHG52v5Q&pp=ygUU64KY64qUIOyZnCDsmKTsmKTsmKQ%3D',
            # Abduvida - 맥거핀
            'https://www.youtube.com/watch?v=AacajtTL1Dk&pp=ygUIYWJkdXZpZGE%3D',
            # 자유 - 알레프
            'https://www.youtube.com/watch?v=uy2BlCSSLnA&pp=ygUQ7J6Q7JygIOyVjOugiO2UhA%3D%3D',
            # 두리번 - 맥거핀
            'https://www.youtube.com/watch?v=2i6CdoLIS5k&pp=ygUT65GQ66as67KIIOunpeqxsO2VgA%3D%3D'
        ]
        return indiUnrestSong[rn]


    def indiBoring(self, rn):
        indiBoringSong = [
            # 너를 사랑한다는 말이 발음 안돼 - WET BOY
            'https://www.youtube.com/watch?v=_g8GMN9Rt3I&pp=ygUq64SI66W8IOyCrOueke2VnOuLpOuKlCDrp5DsnbQg67Cc7J2M7JWI64-8',
            # 긴밤 - 서리
            'https://www.youtube.com/watch?v=SaoCdRyN3b4&pp=ygUG6ri067Ck',
            # T - 맥거핀
            'https://www.youtube.com/watch?v=FwT88Uyhfo8&pp=ygULVCDrp6XqsbDtlYA%3D',
            # DISCO - 맥거핀
            'https://www.youtube.com/watch?v=ubh44nZQk4A&pp=ygUT65SU7Iqk7L2UIOunpeqxsO2VgA%3D%3D',
            # 춘곤 - 징고
            'https://www.youtube.com/watch?v=4mR-lzkizoc&pp=ygUN7LaY6rOkIOynleqzoA%3D%3D'
        ]
        return indiBoringSong[rn]

        # 힙합
    def hipJoy(self, rn):
        hipJoySong = [
            #DPR LIVE - Martini Blue
            'https://www.youtube.com/watch?v=dGVWH6ojI0c',
            #Loopy - SAVE(feat.Paloalto)
            'https://www.youtube.com/watch?v=x7x0Agd5tjA',
            #lobonabeat! - 생일(feat.BILL STAX)
            'https://www.youtube.com/watch?v=C8BYNRR7V6k',
            #Crush - Ibiza
            'https://www.youtube.com/watch?v=E6OgcgFHFpc',
            #The Quiett - 귀감(feat.ZENE THE ZILLA)
            'https://www.youtube.com/watch?v=P1ijRTr2s_s'
        ]
        return hipJoySong[rn]

    def hipSad(self, rn):
        hipSadSong = [
            # PATEKO - Rainy day(feat.ASH ISLAND, Skinny Brown)
            'https://www.youtube.com/watch?v=R7L2QEm-BUY',
            # 미란이 - Daisy(feat.pH-1)
            'https://www.youtube.com/watch?v=co90cPpbcd8',
            # Crucial Star - I'm OK(생각보다)
            'https://www.youtube.com/watch?v=EWeEM7sNr0g',
            # Lil Boi - CREDIT(feat.염따,기리보이,Zion.T)
            'https://www.youtube.com/watch?v=UMWBdzQSr_I',
            # The Quiett - 한강 gang(feat.Byung Un,창모)
            'https://www.youtube.com/watch?v=O42lYtNTh50'
        ]
        return hipSadSong[rn]

    def hipAnger(self, rn):
        hipAngerSong = [
            # nafla - 선빵(feat.Gaeko,기리보이)
            'https://www.youtube.com/watch?v=iG1wG86hywk',
            # Dynamic Duo - 길을막지마
            'https://www.youtube.com/watch?v=4X29jjIjqK8',
            # 이센스 - RADAR(feat.김심야)
            'https://www.youtube.com/watch?v=mZlQNwGJCio',
            # Sik-k - FIRE
            'https://www.youtube.com/watch?v=bKJxo-yIcg0',
            # Uneducated Kid - 어쩌라고(feat.Beenzino)
            'https://www.youtube.com/watch?v=bZmRG814CLQ'
        ]
        return hipAngerSong[rn]

    def hipUnrest(self, rn):
        hipUnrestSong = [
            # ASH ISLAND - Paranoid
            'https://www.youtube.com/watch?v=USlZolbKXhg',
            # BLOO - Drama
            'https://www.youtube.com/watch?v=NBLvVhg5mpo',
            # Dok2 - On My Way(feat.Zion.T)
            'https://www.youtube.com/watch?v=QzLFcfCEm-I',
            # 창모 - S T A R T
            'https://www.youtube.com/watch?v=nZwu6fzXz7E',
            # 기리보이 - 호랑이소굴(feat.Jvcki Wai)
            'https://www.youtube.com/watch?v=xmXHQUAWLA8'
        ]
        return hipUnrestSong[rn]

    def hipBoring(self, rn):
        hipBoringSong = [
            # 죠지 - Boat
            'https://www.youtube.com/watch?v=OWL1RNX7p90',
            # 릴러말즈 - Trip(feat.Hannah)
            'https://www.youtube.com/watch?v=5C-UzW1FLiA',
            # 기리보이 - Party People(feat.염따,Uneducated Kid)
            'https://www.youtube.com/watch?v=gsLQpBEC7QA',
            # Lil Moshpit - Yooooo(feat.Kid Milli,sokodomo,Polodared)
            'https://www.youtube.com/watch?v=xyTRjWvyahc',
            # 한요한 - 범퍼카(feat.NO:EL,Young B)
            'https://www.youtube.com/watch?v=medo8dj_-28'
        ]
        return hipBoringSong[rn]

        # 아이돌
    def idolJoy(self, rn):
        idolJoySong = [
            # 달링 - 걸스데이
            'https://youtu.be/QB4dQcxgJPY?si=hOQxg4tgKkfY0F6s',
            # 살짝 설렜어 - 오마이걸
            'https://youtu.be/iDjQSdN_ig8?si=d5jx-lr6tYZfFQQd',
            # 사랑인가봐 - 김세정
            'https://youtu.be/V3qCiCv_WIo?si=amzebNvbSdOb7gvI',
            # Feel My Rhythm - 레드벨벳
            'https://youtu.be/R9At2ICm4LQ?si=Q63exDmjOkUvF9Vy',
            # 불꽃놀이 - 오마이걸
            'https://youtu.be/RrvdjyIL0fA?si=2Rt6oWxq0XfZBndk',
            # we go - 프로미스나인
            'https://youtu.be/HM6UpQZvbhY?si=mzZ9KBFVZvbMf4uG',
            # LOVEBOMB - 프로미스나인
            'https://youtu.be/-SK6cvkK4c0?si=iovWkSQq1ZlhULB6'
        ]
        return idolJoySong[rn]

    def idolSad(self, rn):
        idolSadSong = [
            # 사랑하는 법을 몰라서 - ft아일랜드
            'https://youtu.be/6OUFE-4o3M8?si=DrAvT2YzAt29zyAi',
            # 사랑했었다 - 이홍기,유회승
            'https://youtu.be/M9ptKKMsee0?si=wb51Xvt_hS2jecIr',
            # 헤어지자 - 휘인
            'https://youtu.be/XS0vz7wkyWU?si=wGROeo2JMLrxAdCN',
            # 잘 있어요 - 태일
            'https://youtu.be/tMzxABhUrCA?si=zkkYg7fwybxJIJGr',
            # I Miss you -소유
            'https://youtu.be/t9KpdoSxVZU?si=tzwxg84iTtyNClZm',
            # LOVE DIVE - IVE
            'https://youtu.be/Y8JFxS1HlDo?si=QzmPpSFjFvGUWy5S'
        ]
        return idolSadSong[rn]

    def idolAnger(self, rn):
        idolAngerSong = [
            # ETA - 뉴진스
            'https://youtu.be/DfX4F5a6JE8?si=cjJCqczu-AjbWtbq',
            # Tomboy - 여자아이들
            'https://youtu.be/0wezH4MAncY?si=qnQGed03dZIgA7Ux',
            # 미친거아니야?-2pm
            'https://youtu.be/YlqboB1mVnw?si=N_dqtFYGe9TAjsZd',
            # 멍청이 - 화사
            'https://youtu.be/Uw_dqBFYm8c?si=__5vU7f-p-QbGaHr',
            # 가시나 - 선미
            'https://youtu.be/hi6N_zl7f1s?si=3F_ly6d0Y2CJEvDt'
        ]
        return idolAngerSong[rn]

    def idolUnrest(self, rn):
        idolUnrestSong = [
            # 파이팅 해야지 -부석순
            'https://youtu.be/b8ch8cbIUxI?si=PzqjPrTh-OG3eXQQ',
            # Warning - 김세정
            'https://youtu.be/2_jo5WzZxic?si=1fkPAzux6ODTU1Hx',
            # When This Rain Stops - 웬디
            'https://youtu.be/yFKhEYrVLvY?si=b-UwlQg-kewotlis',
            # SMILEY - 예나
            'https://youtu.be/ax1niBPPig8?si=UbBeS0ANLMlJusm3',
            # 빛 - HOT
            'https://youtu.be/tWyIHYvshXI?si=F5FkDU3GtKrUnATs'
        ]
        return idolUnrestSong[rn]

    def idolBoring(self, rn):
        idolBoringSong = [
            # super shy - 뉴진스
            'https://youtu.be/ArmDp-zijuc?si=_GWsNt456XNaRM1f',
            # 롤리폴리 - 티아라
            'https://youtu.be/tTd9Gna50ls?si=txz2yhdEBc8ygy9t',
            # 뿜뿜 - 모모랜드
            'https://youtu.be/JQGRg8XBnB4?si=oSQvIzqW7yh2ZYBn',
            # Weekend - 태연
            'https://youtu.be/RmuL-BPFi2Q?si=frEyZnWHJ6aZNvmC',
            # Perfect Night - 르세라핌
            'https://youtu.be/6AOjwLeMKfk?si=ljXA5TlQkQ2oKcsv',
            # shake it - 씨스타
            'https://youtu.be/x9-TIy7WPQI?si=l8fCZPgbdC5No_77',
            # party - 소녀시대
            'https://youtu.be/YwN-CN9EjTg?si=ytcI_D9yUH8WLbqH'
        ]
        return idolBoringSong[rn]

        # 발라드
    def balJoy(self, rn):
        balJoySong = [
            # 걷자,집앞이야 - 스무살
            'https://www.youtube.com/watch?v=14hH4eSmRTo&pp=ygUW7Iqk66y07IK0IOynkeyVnuydtOyVvA%3D%3D',
            # 지그재그 - 맥거핀
            'https://www.youtube.com/watch?v=9yZMOVWiJ8c&pp=ygUW7KeA6re47J6s6re4IOunpeqxsO2VgA%3D%3D',
            # 케이윌 - Love Blossom
            'https://www.youtube.com/watch?v=WmCy7VJPPk4',
            # 에릭남,치즈 - 사랑인가요
            'https://www.youtube.com/watch?v=2-57ZGv7Deg',
            # Would u -레드벨벳 
            'https://youtu.be/Nu7OmSqHVng?si=u8RsG4UyFI-CC1ru',
            # 나의 오랜 연인에게 - 다비치
            'https://youtu.be/vTNuU_mKVnU?si=uAVKE3HlMUUWoqOn'
        ]
        return balJoySong[rn]

    def balSad(self, rn):
        balSadSong = [
            # 환상 - 하현우
            'https://www.youtube.com/watch?v=l7N7DGHv7Qk&pp=ygUQ7ZmY7IOBIO2VmO2YhOyasA%3D%3D',
            # 너의 번호를 누르고 - #안녕
            'https://www.youtube.com/watch?v=URZaPnGp5rI&pp=ygUa64SI7J2YIOuyiO2YuOulvCDriITrpbTqs6A%3D',
            # 에일리 - 첫눈처럼 너에게 가겠다.
            'https://www.youtube.com/watch?v=2FhBGUkI4vs',
            # V.O.S - 울어
            'https://www.youtube.com/watch?v=mOov1C0_4kE',
            # 혼자 - 거미
            'https://youtu.be/YrljfReXOUA?si=S87ASGzrv1vjIZVH',
            # 노력 - 박원
            'https://youtu.be/0cwZcqTh8IQ?si=fuxbacDJZb41fLxD'
        ]
        return balSadSong[rn]

    def balAnger(self, rn):
        balAngerSong = [
            # Fighting Another Day - Thyra
            'https://www.youtube.com/watch?v=m4E9CG-8RS0&pp=ygUaZmlnaHRpbmcgYW5vdGhlciBkYXkgdGh5cmE%3D',
            # Whiskey and Morphine - Alexander Jean
            'https://www.youtube.com/watch?v=ACDf9fhpuqo&pp=ygUV7JyE7Iqk7YKk7JWk66qo66W07ZWA',
            # 브라운아이드소울 - 비켜줄께
            'https://www.youtube.com/watch?v=4bKECOPvS2c',
            # 포맨 - 눈물
            'https://www.youtube.com/watch?v=hHIauY2P11A',
            # 헤어져줘서 고마워 - 벤
            'https://youtu.be/tp1uoFAfgHE?si=ZaxPteZJp5-qP9S5',
            # To.X - 태연
            'https://youtu.be/MpYuVButQ5A?si=NIHyLMYVM3WOrPdx'
        ]
        return balAngerSong[rn]

    def balUnrest(self, rn):
        balUnrestSong = [
            # 밤하늘의 별을 4 - 양정승
            'https://www.youtube.com/watch?v=aGP14gSVgIY&pp=ygUT67Ck7ZWY64qY7J2Y67OE7J2ENA%3D%3D',
            # Dangerously - 찰리 푸스
            'https://www.youtube.com/watch?v=qn-cSwgcXio&pp=ygUT7LCw66as7ZG47IqkIOuNtOyguA%3D%3D',
            # 케이윌 - 이러지마 제발
            'https://www.youtube.com/watch?v=3SaJeuwy1TY',
            # 버즈 - 겁쟁이
            'https://www.youtube.com/watch?v=G7eLG4Tnc9c',
            # 진심이 담긴 노래 - 케이시
            'https://youtu.be/nuUSmMZXgxI?si=ssJqDRl5Wrnaazc7',
            #한숨 - 이하이
            'https://youtu.be/AT9e7H-X4Pg?si=GWxq0mySmWqGdSly'
        ]
        return balUnrestSong[rn]

    def balBoring(self, rn):
        balBoringSong = [
            # 드라큘라 - 히미츠
            'https://www.youtube.com/watch?v=OPo5-e_XacE&pp=ygUW65Oc65287YGY6528IO2eiOuvuOy4oA%3D%3D',
            # 그거아세요 - 과나
            'https://www.youtube.com/watch?v=n0oBBQoE06g&pp=ygUP6re46rGw7JWE7IS47JqU',
            # 프라이머리 - ~42(feat.Sam Kim,eSNa)
            'https://www.youtube.com/watch?v=Ws9sG-6Eh68',
            # 폴킴 - 집돌이
            'https://www.youtube.com/watch?v=LrDCqP52SbE',
            # 별 보러가자 - 적재
            'https://youtu.be/Mz031oU0Xfw?si=Ac7TJhM41zJKuM27',
            # Think About Chu - 샘김
            'https://youtu.be/PJxuVLSf6uA?si=sVBoIn5_GAMswe92'
        ]
        return balBoringSong[rn]
