### Оглавление
- Атрибуты
	- scene
	- point
	- bias
	- rotate
	- [image](#image)
-  Методы
	- [remove_item](remove_item)


### Атрибуты
##### scene
##### point
##### bias
##### rotate
##### image
Путь до изображения необходимого для отображения в текущем элементе сцены.
```python
class Element(ElementScene):
	image: str = 'path/to/directory'

class Element(ElementScene):
	def __init__(*args, **kwargs):
		self.image = 'path/to/directory'
		super().__init__(*args, **kwargs)
```

### Методы
##### remove_item
Удаление текущего элемента сцены, со сцены. 

> Не удаляется экземпляр класса данного объекта. Его позже можно отрисовать заново методом [.draw](#draw)

##### set_image
```python
.set_image(bias: tuple[int, int], scaled: bool, scaled_size: tuple[int, int])
```

Отрисовка установленной в [image](#image) картинки элемента.

**bias**: - Опционально.  
**scaled**: - Опционально. Растягивание изображения под размер элемента.  
**svaled_size**: - Опционально. Растягивание изображения под пользовательский размер  

> Если атрибут [image](#image) указан при инициализации, то вызов set_image происходит автоматически.

