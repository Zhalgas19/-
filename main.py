import tkinter as tk
from tkinter import ttk, messagebox

class GlobalCyberLawExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Эксперттік жүйе: Киберқылмыстарды саралау (ҚР ҚК)")
        self.root.geometry("750x580")
        self.root.configure(bg="#f4f6f9")
        self.root.resizable(False, False)

        # =========================
        # 1. Тақырыптық блок
        # =========================
        header_frame = tk.Frame(root, bg="#1b365d", height=70)
        header_frame.pack(fill="x", side="top")

        title = tk.Label(
            header_frame,
            text="КИБЕР-ИНЦИДЕНТТЕРДІ ҚҰҚЫҚТЫҚ САРАЛАУ ЖҮЙЕСІ",
            font=("Arial", 12, "bold"),
            fg="#ffffff",
            bg="#1b365d"
        )
        title.pack(pady=(12, 2))

        subtitle = tk.Label(
            header_frame,
            text="Қазақстан Республикасының Қылмыстық кодексі (ҚР ҚК) бойынша бағалау",
            font=("Arial", 9, "italic"),
            fg="#ecf0f1",
            bg="#1b365d"
        )
        subtitle.pack(pady=(0, 10))

        # =========================
        # 2. Инцидент параметрлері
        # =========================
        frame = tk.LabelFrame(
            root,
            text=" Инцидент белгілерін таңдаңыз ",
            font=("Arial", 10, "bold"),
            fg="#1b365d",
            bg="#ffffff",
            padx=15,
            pady=10
        )
        frame.pack(fill="both", expand=True, padx=20, pady=15)

        # BooleanVar айнымалылары
        self.ransomware_attack = tk.BooleanVar(value=False)
        self.phishing_fraud = tk.BooleanVar(value=False)
        self.data_breach = tk.BooleanVar(value=False)
        self.ddos_attack = tk.BooleanVar(value=False)
        self.insider_threat = tk.BooleanVar(value=False)
        self.malware_distribution = tk.BooleanVar(value=False)
        self.critical_infrastructure = tk.BooleanVar(value=False)

        options = [
            ("1. Шифрлағыш-бопсалаушы шабуылы (Ransomware)", self.ransomware_attack),
            ("2. Фишинг және Интернет-алаяқтық (Phishing / Fraud)", self.phishing_fraud),
            ("3. Деректердің ағып кетуі мен сатылуы (Data Breach)", self.data_breach),
            ("4. Серверлерге жасалған DDoS-шабуыл (Denial of Service)", self.ddos_attack),
            ("5. Инсайдерлік қауіп және өкілеттікті теріс пайдалану", self.insider_threat),
            ("6. Зиянды бағдарламаларды жасау мен тарату (Malware)", self.malware_distribution),
            ("7. Аса маңызды инфрақұрылымдарға шабуыл (Critical Infrastructure)", self.critical_infrastructure)
        ]

        for text, var in options:
            chk = tk.Checkbutton(
                frame,
                text=text,
                variable=var,
                font=("Arial", 9, "bold"),
                bg="#ffffff",
                fg="#2c3e50",
                activebackground="#ffffff",
                activeforeground="#1b365d",
                selectcolor="#ffffff",
                anchor="w"
            )
            chk.pack(fill="x", pady=4)

        # =========================
        # 3. Батырмалар
        # =========================
        button_frame = tk.Frame(root, bg="#f4f6f9")
        button_frame.pack(pady=10)

        btn_analyze = tk.Button(
            button_frame,
            text="Саралау қорытындысын алу",
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            activebackground="#219150",
            activeforeground="white",
            padx=15,
            pady=6,
            relief="flat",
            cursor="hand2",
            command=self.analyze
        )
        btn_analyze.grid(row=0, column=0, padx=10)

        btn_clear = tk.Button(
            button_frame,
            text="Барлығын тазалау",
            font=("Arial", 10),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            padx=15,
            pady=6,
            relief="flat",
            cursor="hand2",
            command=self.clear
        )
        btn_clear.grid(row=0, column=1, padx=10)

    def analyze(self):
        results = []

        # 1. Ransomware
        if self.ransomware_attack.get():
            results.append(
                "[1] ШИФРЛАҒЫШ-БОПСАЛАУШЫ ШАБУЫЛЫ (RANSOMWARE)\n"
                "-----------------------------------------------------------------------\n"
                "• Құқықтық квалификация: Компьютердегі деректерді заңсыз бұғаттап, оны ашу үшін ақша талап ету (бопсалау).\n"
                "• ҚР ҚК сәйкес баптары:\n"
                "  — ҚР ҚК 194-бап (Бопсалау) — 3 жылдан 7 жылға дейін бас бостандығынан айыру;\n"
                "  — ҚР ҚК 206-бап (Ақпаратты бұғаттау) — 2 жылға дейін бас бостандығын шектеу/айыру;\n"
                "  — ҚР ҚК 210-бап (Вирус/зиянды программа қолдану) — 2 жылға дейін бас бостандығынан айыру.\n"
                "• Алғашқы дәлелдемелерді жинау нұсқаулығы:\n"
                "  1) Экранда ақша талап етіп шыққан хабарламаның толық фотосын немесе скриншотын түсіріп алу;\n"
                "  2) Бүлінген, ашылмай қалған 2-3 файлдың көшірмесін бөлек флешкаға сақтап қою;\n"
                "  3) Хакерлер қалдырған ақша аударатын криптовалюта әмиян номерін немесе байланыс поштасын/Telegram-ын жазып алу."
            )

        # 2. Phishing
        if self.phishing_fraud.get():
            results.append(
                "[2] ИНТЕРНЕТ-АЛАЯҚТЫҚ ЖӘНЕ ФИШИНГ (PHISHING / FRAUD)\n"
                "-----------------------------------------------------------------------\n"
                "• Құқықтық квалификация: Ғаламторды немесе жасанды сайттарды пайдаланып, адамдарды алдап ақшасын жымқыру.\n"
                "• ҚР ҚК сәйкес баптары:\n"
                "  — ҚР ҚК 190-бап, 2-бөлігі, 4-тармағы (Интернет-алаяқтық) — 4 жылға дейін бас бостандығынан айыру;\n"
                "  — ҚР ҚК 205-бап (Азаматтардың аккаунтына заңсыз кіру) — 160 МРП айыппұл.\n"
                "• Алғашқы дәлелдемелерді жинау нұсқаулығы:\n"
                "  1) Алдап кіргізген алаяқтық сайттың сілтемесін (веб-адресін) көшіріп алу;\n"
                "  2) Банк арқылы жасалған аударымдардың чектерін немесе квитанцияларын сақтау;\n"
                "  3) Алаяқпен мессенджердегі (WhatsApp/Telegram) барлық жазысқан хаттарды скриншоттап алу."
            )

        # 3. Data Breach
        if self.data_breach.get():
            results.append(
                "[3] ДЕРЕКТЕРДІҢ АҒЫП КЕТУІ ЖӘНЕ САТЫЛУЫ (DATA BREACH)\n"
                "-----------------------------------------------------------------------\n"
                "• Құқықтық квалификация: Азаматтардың жеке деректерін немесе мекеменің құпия базасын заңсыз ұрлап, тарату.\n"
                "• ҚР ҚК сәйкес баптары:\n"
                "  — ҚР ҚК 211-бап (Құпия деректерді заңсыз тарату/сату) — 3 жылға дейін бас бостандығынан айыру;\n"
                "  — ҚР ҚК 205-бап (Дерекқорға заңсыз кіру) — 2000 МРП айыппұл.\n"
                "• Алғашқы дәлелдемелерді жинау нұсқаулығы:\n"
                "  1) Деректер сатылып жатқан Telegram-каналдардың немесе сайттардың скриншоттарын түсіріп алу;\n"
                "  2) Тарап кеткен базаның үлгілерін (клиенттер тізімі, ЖСН, телефондар) дәлел ретінде тіркеу;\n"
                "  3) Сервердің кіру журналдарынан (логтардан) бөгде адамдардың қашан кіргенін тексеріп сақтау."
            )

        # 4. DDoS
        if self.ddos_attack.get():
            results.append(
                "[4] СЕРВЕРЛЕРГЕ ЖАСАЛҒАН DDOS-ШАБУЫЛ (DENIAL OF SERVICE)\n"
                "-----------------------------------------------------------------------\n"
                "• Құқықтық квалификация: Толассыз жалған сұраныстар арқылы сайттың немесе сервердің жұмысын әдейі тоқтатып тастау.\n"
                "• ҚР ҚК сәйкес баптары:\n"
                "  — ҚР ҚК 207-бап (Ақпараттық жүйенің жұмысын бұзу) — 2 жылға дейін бас бостандығынан айыру;\n"
                "  — ҚР ҚК 210-бап (Ботнет/заңсыз программаларды қолдану) — 2 жылға дейін бас бостандығынан айыру.\n"
                "• Алғашқы дәлелдемелерді жинау нұсқаулығы:\n"
                "  1) Сайттың өшіп, істемей қалған уақытын (сағаты мен минутын) дәл жазып алу;\n"
                "  2) Веб-сервердің кіріс трафик журналдарын (логтарды) системдік администратордан жүктеп алу;\n"
                "  3) Шабуыл жасаған бөгде IP-мекенжайлар тізімін сақтап қою."
            )

        # 5. Insider Threat
        if self.insider_threat.get():
            results.append(
                "[5] ИНСАЙДЕРЛІК ҚАУІП ЖӘНЕ ӨКІЛЕТТІКТІ ТЕРІС ПАЙДАЛАНУ\n"
                "-----------------------------------------------------------------------\n"
                "• Құқықтық квалификация: Мектеп, банк немесе компания қызметкерінің өзіне берілген логин-парольді жаман оймен пайдалануы.\n"
                "• ҚР ҚК сәйкес баптары:\n"
                "  — ҚР ҚК 205-бап, 3-бөлігі (Қызметтік бабын пайдаланып жүйеге заңсыз кіру) — 3 жылға дейін бас бостандығынан айыру;\n"
                "  — ҚР ҚК 206-бап, 2-бөлігі (Өкілеттігін пайдаланып файлдарды өшіру/өзгерту) — 3 жылға дейін бас бостандығынан айыру.\n"
                "• Алғашқы дәлелдемелерді жинау нұсқаулығы:\n"
                "  1) Жұмысшының жүйеге қай сағатта кіріп, не өшіргенін көрсететін ішкі журналды сақтау;\n"
                "  2) Күдікті қызметкердің жүйедегі аты-жөні мен логинін (User ID) белгілеу;\n"
                "  3) Онымен жасалған еңбек шарты мен құпиялылық келісімінің (NDA) көшірмесін дайындау."
            )

        # 6. Malware
        if self.malware_distribution.get():
            results.append(
                "[6] ЗИЯНДЫ БАҒДАРЛАМАЛАРДЫ ӘЗІРЛЕУ ЖӘНЕ ТАРАТУ\n"
                "-----------------------------------------------------------------------\n"
                "• Құқықтық квалификация: Компьютерлерді бұзатын вирустарды, трояндарды әдейі жасау, сату немесе тарату.\n"
                "• ҚР ҚК сәйкес баптары:\n"
                "  — ҚР ҚК 210-бап (Зиянды программаларды жасау және тарату) — 2 жылдан 7 жылға дейін бас бостандығынан айыру.\n"
                "• Алғашқы дәлелдемелерді жинау нұсқаулығы:\n"
                "  1) Табылған вирус файлын (.exe/.dll) антивирус өшіріп тастамай тұрғанда карантинге салып, флешкаға көшіру;\n"
                "  2) Антивирус бағдарламасы шығарған есепті (отчетты) сақтап алу;\n"
                "  3) Компьютерді сараптамаға берер алдында оны өшіріп, қайта қоспау."
            )

        # 7. Critical Infrastructure
        if self.critical_infrastructure.get():
            results.append(
                "[7] АСА МАҢЫЗДЫ ИНФРАҚҰРЫЛЫМДАРҒА КИБЕРШАБУЫЛ (АМИ)\n"
                "-----------------------------------------------------------------------\n"
                "• Құқықтық квалификация: Мемлекеттік органдардың, электр не су станцияларының компьютерлік жүйесін бұзу.\n"
                "• ҚР ҚК сәйкес баптары:\n"
                "  — ҚР ҚК 208-бап (Стратегиялық объектілерге кибершабуыл) — 3 жылдан 7 жылға дейін бас бостандығынан айыру;\n"
                "  — ҚР ҚК 207-бап, 3-бөлігі (Ауыр зардаптарға әкелу) — 3 жылдан 7 жылға дейін бас бостандығынан айыру.\n"
                "• Алғашқы дәлелдемелерді жинау нұсқаулығы:\n"
                "  1) Мекеменің қауіпсіздік жүйелері (SIEM/Firewall) тіркеген барлық оқиға журналдарын сақтау;\n"
                "  2) Өндірістік немесе мемлекеттік жүйедегі тоқтаулар туралы ресми акт жасау;\n"
                "  3) Мемлекеттік киберқауіпсіздік қызметіне (CERT/KZ-CERT) шұғыл хабарлама жіберу."
            )

        if not results:
            messagebox.showwarning(
                "Ескерту",
                "Өтініш, саралау жүргізу үшін кем дегенде 1 параметрді таңдаңыз!"
            )
            return

        self.show_result_window("\n\n".join(results))

    def show_result_window(self, verdict_text):
        res_win = tk.Toplevel(self.root)
        res_win.title("Сараптамалық юридикалық қорытынды")
        res_win.geometry("750x580")
        res_win.configure(bg="#f4f6f9")

        res_win.transient(self.root)
        res_win.focus_force()

        lbl = tk.Label(
            res_win,
            text="САРАПТАМАЛЫҚ ЮРИДИКАЛЫҚ ҚОРЫТЫНДЫ (ҚР ҚК)",
            font=("Arial", 11, "bold"),
            bg="#f4f6f9",
            fg="#1b365d"
        )
        lbl.pack(pady=10)

        txt_frame = tk.Frame(res_win, bg="#f4f6f9")
        txt_frame.pack(fill="both", expand=True, padx=15, pady=5)

        scrollbar = tk.Scrollbar(txt_frame)
        scrollbar.pack(side="right", fill="y")

        text_area = tk.Text(
            txt_frame,
            wrap="word",
            font=("Arial", 10),
            yscrollcommand=scrollbar.set,
            bg="#ffffff",
            fg="#2c3e50",
            padx=10,
            pady=10
        )
        text_area.insert("1.0", verdict_text)
        text_area.configure(state="disabled")
        text_area.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=text_area.yview)

        btn_close = tk.Button(
            res_win,
            text="Жабу",
            font=("Arial", 10, "bold"),
            bg="#1b365d",
            fg="white",
            command=res_win.destroy,
            padx=20,
            pady=5,
            relief="flat",
            cursor="hand2"
        )
        btn_close.pack(pady=10)

    def clear(self):
        self.ransomware_attack.set(False)
        self.phishing_fraud.set(False)
        self.data_breach.set(False)
        self.ddos_attack.set(False)
        self.insider_threat.set(False)
        self.malware_distribution.set(False)
        self.critical_infrastructure.set(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = GlobalCyberLawExpertSystem(root)
    root.mainloop()