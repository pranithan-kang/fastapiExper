# โปรดอ่าน

โปรเจค fastapiExper นี้เป็นโปรเจคทดลองเกี่ยวกับ การสร้าง Backend (Web API) เขียนด้วยภาษา Python ร่วมกับการใช้ FastAPI Library เป็นหลัก โปรเจคนี้ทำขึ้นเพื่อศึกษาและวางโครงสร้าง วางแผนการพัฒนาเป็นโปรเจคอื่นต่อไป

## โครงสร้างของโปรเจค

.  
├── README.md -- ไฟล์ README.md ที่ผู้อ่านเปิดอยู่  
├── app -- โฟลเดอร์เก็บ sourcecode หลักของทั้งโปรเจค  
│   ├── api -- โฟลเดอร์ที่เกี่ยวข้องกับส่วนที่ทำหน้าที่ API ทั้งหมด  
│   │   ├── dependencies -- โฟลเดอร์เก็บ FastAPI Dependencies  
│   │   ├── endpoints -- โฟลเดอร์เก็บ Endpoints หรือ Router ที่นำทาง URL ไปยัง Method ที่ระบุ  
│   │   └── middleware -- โฟลเดอร์เก็บ FastAPI Middleware  
│   ├── config.py -- ไฟล์ที่แปล Environment Variable และรวบรวม Configuration ออกมาเป็น Python Constant  
│   ├── helper -- โฟลเดอร์รวบรวม Utility และ Helper ต่างๆ ที่ใช้ร่วมกันได้หลายที่ภายในโปรเจค  
│   ├── model -- โฟลเดอร์ของ Class ตัวแทน Table เพื่อติดต่อกับ Database โดยใช้ SQLAlchemy ORM  
│   ├── crud -- โฟลเดอร์ที่เก็บ Query ที่ติดต่อกับ Database (อาจรวมถึง Business Logic)  
│   ├── schema -- โฟลเดอร์เก็บ Pydantic ซึ่งคือ Class ที่ใช้ Validate ข้อมูลขาเข้าและออกจาก Endpoint  
│   └── ext_service -- โฟลเดอร์เก็บ Service ที่ติดต่อกับ Service/API ภายนอก (ส่วนใหญ่ใช้ช่องทาง HTTP Request)  
├── main.py -- จุดเริ่มต้น Run โปรเจค  
├── pytest.ini -- Configuration ที่เกี่ยวข้องกับ Unit Test  
├── requirements.txt -- ไฟล์เก็บ pip Package  
├── requirements_dep.txt -- ไฟล์ pip Package Dependency โดยได้จากคำสั่ง pipdeptree  
└── test -- โฟลเดอร์เก็บ Unit Test ภายในโปรเจค  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── fixture -- โฟลเดอร์เก็บ Fixture ของ Unit Test  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── db.py -- ไฟล์ Fixture ซึ่งสร้าง Database เพื่อใช้สำหรับ Run หรือ Debug Unit Test  

## วิธีการเปิดโปรเจค

การเปิดโปรเจคนั้นสามารถทำได้สองวิธีคือ
  1. ใช้ VSCode DevContainer
  2. ใช้ Python Virtual Environment

### การเปิดโปรเจคด้วย VSCode DevContainer

หากเครื่องผู้อ่านมี Docker, VSCode และ Remote Development ติดตั้งอยู่แล้วก็สามารถเปิดโปรเจคได้โดยไม่ต้องทำอะไรเพิ่มเติม ก็สามารถ Run / Run Test หรือ Debug Test ได้ทันทีโดย <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>p</kbd> และพิมพ์ภายในกล่อง Quick Open ให้พิมพ์ _Reopen Folder in Container_ จากนั้นเลือก _Remote-Containers: Reopen Folder in Container_

### การเปิดโปรเจคด้วย Python Virtual Environment

1. สร้าง Virtual Environment ภายในโฟลเดอร์เดียวกับไฟล์ README นี้ โดยใช้คำสั่ง

        > virtualenv env

2. หากผู้อ่านใช้ Powershell ให้ Activate Virtual Environment โดยใช้คำสั่ง

        > .\env\Scripts\activate

  แต่ถ้าหากผู้อ่านไม่ได้ใช้ Powershell ให้ Activate Virtual Environment ตาม[ขั้นตอนนี้](https://virtualenv.pypa.io/en/latest/user_guide.html)

3. ใน VSCode ให้ชี้ Python Environment ไปยังที่ Virtual Environment ที่สร้างขึ้นมา

## การเพิ่ม Configuration ในการ Run (ช่วงขณะพัฒนาเท่านั้น)

ผู้อ่านสามารถใช้ประโยชน์จากไฟล์ `./vscode/launch.json` ในการฝัง Environment Variable ภายใน Attribute "env" ตามตัวอย่าง `CONNECTION_STRING` และสำหรับการทำ Configuration เพื่อทำ Unit Test นั้น ให้ใส่ไว้ภายในไฟล์ pytest.ini ตามตัวอย่าง `CONNECTION_STRING`

## การเพิ่ม Configuration ในการ Deploy

ผู้เขียนมีแนวทางโดยคร่าวประมาณสามแนวทางคือ

1. ใช้ .env.* (แต่ไม่ include ไฟล์เหล่านี้ลงไปใน Source Control Repository)
2. ใช้ Shell Script เพื่อ Set ค่า Environment Variable ภายใน OS (ไม่ include ไฟล์เหล่านี้ลงใน Source Control Repository เช่นกัน)
3. ใช้ Configuration ใน Container / Orchestration Tool

## Note เพิ่มเติม

- Roles in FastAPI is called scopes

## บันทึกทาง Business และ Architecture

ในหัวข้อถัดๆ ไปให้ผู้เขียนบันทึกรายละเอียดทางการพัฒนา และ Implement โปรเจคของผู้อ่านต่อไป