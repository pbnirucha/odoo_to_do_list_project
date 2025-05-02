# Mini Project To-Do List

เป็นโปรแกรมที่เขียนด้วย Python Odoo Framework สามารถใช้ในการบันทึกงาน / เป้าหมาย / สิ่งสำคัญที่ต้องทำ
และสามารถระบุผู้ที่มีส่วนร่วมใน To-do List นี้ได้

## ก่อนจะใช้ Odoo ต้องติดตั้งอะไรบ้าง ?

- ติดตั้ง Python (ในโปรแกรมใช้ Version 3.11)
- ติดตั้ง Postgresql (ในโปรแกรมใช้ Version 17)
- ติดตั้ง Odoo (ในโปรแกรมใช้ Version 18)
ศึกษาขั้นตอนการติดตั้งจาก
    - [Odoo Docs](https://www.odoo.com/documentation/18.0/administration/on_premise/source.html#source-install)
    - [How to Install Odoo 17 in Windows](https://www.cybrosys.com/blog/how-to-install-odoo-17-in-windows)
    - [Odoo 16 Developer EP.1 : ติดตั้ง Odoo 16 สำหรับการใช้งานและการพัฒนาระบบ](https://medium.com/@mango.root23/odoo-16-developer-ep-1-%E0%B8%95%E0%B8%B4%E0%B8%94%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87-odoo-16-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A-a1bbfb5b8f71)
    - [Youtube - Setup Odoo18 In Windows 10](https://www.youtube.com/watch?v=yyJjsQEo-SU)

## รายละเอียดของโปรแกรม

- กลุ่มผู้ใช้งาน To-do List คือ Internal User
    - โดยกำหนดสิทธิ์ให้สามารถ อ่าน / เพิ่ม / ลบ / แก้ไข
- สามารถระบุชื่อ To-do List ได้ **ต้องระบุเสมอ**
- สามารถระบุ Tags ของรายการได้
    - มี Tags เริ่มต้นคือ Work / Event / Life achievement
    - สามารถเพิ่ม Tags ในภายหลังได้
- สามารถระบุ วันที่เริ่มต้น / วันที่สิ้นสุด ของ To-do List ได้ **ต้องระบุเสมอ**
    - โดยวันที่สิ้นสุดต้องมากกว่าวันที่เริ่มต้น
- สามารถ Track Status Draft / In progress / Complete
- สามารถกดปุ่ม In progress เพื่อเปลี่ยนสถานะจาก Draft เป็น In progress
- สามารถบันทึกรายการสิ่งที่ต้องทำได้ ดังนี้
    - ชื่อรายการ
    - คำอธิบาย
    - Checkbox สำหรับเลือกรายการที่ทำสำเร็จแล้ว โดยจะแสดงเมื่อ Status เป็น In progress เท่านั้น
    - สามารถเพิ่มรายการสิ่งที่ต้องทำในแถวได้เลย (Add a line) โดยไม่ต้องเปิด Pop-up
- สามารถบันทึกผู้เข้าร่วมใน To-do List ได้
    - โดยอ้างอิงจากชื่อผู้ใช้งาน (res.user)
- เมื่อทุกรายการใน List สำเร็จ ให้แสดงปุ่ม Done เพื่อเปลี่ยนสถานะจาก In progress เป็น Done
และต้องไม่สามารถแก้ไขข้อมูลใด ๆ ได้อีก สามารถดูได้เท่านั้น
- สร้างเป็น Menu ใหม่ และเมื่อเปิดเข้าไปให้เป็นหน้าแสดง To-do List ทั้งหมดที่บันทึกไว้
- Menu bar ให้เห็นเป็น 3 หัวข้อ
    - All : ให้มองเห็น To-do List ทั้งหมดที่บันทึกไว้
    - Complete : ให้มองเห็นเฉพาะ To-do List ที่มีสถานะ `status = complete`
    - Uncomplete : ให้มองเห็นเฉพาะ To-do List ที่มีสถานะ `status != complete`
