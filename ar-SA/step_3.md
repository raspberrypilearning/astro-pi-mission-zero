## عرض رسالة

--- task ---

افتح [محاكي لوحة Sense HAT](https://trinket.io/mission-zero){:target="_blank"} الخاص بمشروع المهمة صفر (Mission Zero).

وسترى أنه قد تم إضافة ثلاثة أسطر من التعليمات البرمجية لك تلقائيًا:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
```

![محاكي لوحة Sense HAT](images/sense-hat-emulator2.png)

تتصل هذه التعليمة بنظام Astro Pi ويتأكد من أن العرض على شاشة العرض LED الخاصة بنظام Astro Pi يتم بشكل صحيح. اترك التعليمة البرمجية في ذلك المكان، لأنك ستحتاجه.

--- /task ---

--- task ---

فقد تود ترك رسالة ترحيبية لطيفة لرواد الفضاء الموجودين على متن محطة الفضاء الدولية والذين يعملون بالقرب من نظام Astro Pi؟ هيا بنا نمرر رسالة عبر شاشة العرض.

أضف هذا السطر أسفل التعليمة البرمجية:

```python
sense.show_message("Astro Pi")
```

--- /task ---

--- task ---

اضغط على زر **Run**(تشغيل) وشاهد تمرير الرسالة `Astro Pi` عبر شاشة العرض LED.

![لعرض رمز الرسالة، انقر run (تشغيل)](images/show-message-code-annotated.PNG)

--- /task ---

![تمرير رسالة](images/scroll-message.gif)

لعرض رسالة مختلفة، يمكنك كتابة أي رسالة ترغبها بين علامات الاقتباس (`""`).

--- collapse ---

---
title: ما الأحرف والرموز التي يمكن استخدامها؟
---

يمكن للوحة Sense HAT عرض مجموعة الأحرف والرموز اللاتينية 1، مما يعني عدم توفر سوى الأحرف والرموز التالية فقط. تُعرض الأحرف والرموز الأخرى على شكل `?`.

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

--- /collapse ---

--- task ---

يمكنك أيضًا تغيير سرعة تمرير الرسالة عبر الشاشة. أضف `scroll_speed` (سرعة_التمرير) إلى سطر التعليمة البرمجية التي لديك بالفعل، مثل هذا المثال:

```python
sense.show_message("Astro Pi", scroll_speed=0.05)
```

السرعة الافتراضية للرسالة هي `0.1`. تصغير الرقم يزيد من سرعة تمرير الرسالة، وتكبير الرقم يبطى من سرعة تمرير الرسالة.

--- /task ---

### Choose a name for the new Astro Pi computers

--- task --- If you'd like to enter the competition to choose the names of the new Mark II Astro Pi computers, start your message with the words "My name should be" and then add in your selection from this list.

For example, if you'd like to vote for Ada Lovelace, your code would look like this:

```python
sense.show_message("My name should be Ada Lovelace")
```
--- /task ---



