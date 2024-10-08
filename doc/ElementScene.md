### Оглавление
- Атрибуты
	- scene
	- point
	- bias
	- rotate
	- [image](#image)
-  Методы
	- remove_item


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
##### remove_item()
Удаление текущего элемента сцены, со сцены. 

> Не удаляется экземпляр класса данного объекта. Его позже можно отрисовать заново методом [.draw](#draw)

