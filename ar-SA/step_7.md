## عرض مقدار الرطوبة

يمكنك دمج قراءة مقدار الرطوبة بصورة ما للإشارة إلى الرطوبة أيضًا بطريقة رسومية. على سبيل المثال ، قد تعرض محيطًا للرطوبة العالية وصحراء للرطوبة المنخفضة:

![درجات الحرارة الحارة ودرجات الحرارة الباردة](images/wet-dry.png)

--- task ---

في نهاية برنامجك، أنشئ مزيد من متغيرات اللون لأية ألوان تريد استخدامها في صورك. ربما تكون قد حددت بعضًا منها بالفعل في خطوة سابقة.

```python
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
```

--- /task ---

--- task ---

مثلما تم في السابق، ارسم صورك من خلال القيام أولاً بإنشاء قائمة لكل واحدة منها ثم ضبط عناصر القائمة على الألوان التي تريدها لوحدات البكسل.

```python
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
```

--- /task ---

--- task ---

أضف بعض التعليمات البرمجية للحصول على الرطوبة:

```python
humid = sense.humidity
```

--- /task ---

--- task ---

والآن قرر أي صورة ترغب في عرضها. في هذا المثال، سنعرض صورة `wet` إذا كانت قراءة الرطوبة ٪40 أو أعلى، وصورة `dry` إذا كانت الرطوبة أقل من ٪40.

```python
humid = sense.humidity
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```

--- /task ---

--- task ---

استخدم شريط تمرير ضبط الرطوبة لضبط مقدار الرطوبة في برنامج المحاكاة. شغِّل البرنامج وتحقق من أن الصورة التي حددتها لمقدار الرطوبة تلك يتم عرضها بشكل صحيح.

--- /task ---

--- task ---

غيِّر التعليمة البرمجية الخاصة بك بحيث تعرض البرنامج الرطوبة لرواد الفضاء بطريقتك المختارة.

--- /task ---

--- task --- Test your code with a few different humidity settings (using the slider) to make sure it always runs correctly. If you've followed the example above, is an image displayed both when the humidity is set to a value less than 40% and also when it is set to more than 40%?

--- /task ---
