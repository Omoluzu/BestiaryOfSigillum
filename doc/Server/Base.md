
> [!info]  
> Предварительное наименование, так как я не придумал ничего получше пока.

### Оглавление
- [Описание](#Описание)
- [Подключение](#Подключение)
- [**Attributes**](#attributes)
	- [name](#name)
	- [elements](#elements)
	- [suffix](#suffix)
- [**Classmethods**](#classmethods)
	- [new](#new)
	- [imports](#imports)
- [**Methods**](#methods)
	- [export](#export)
	- [element_add](#element_add)

### Описание
Базовый класс для упрощения первоначального взаимодействия с группой односимвольных элементов игры хранимых в cvs.

### Подключение

Для подключения и использования необходимо наследоваться от базового класса и определить наименование группы для взаимодействия

```python
from dataclasses import dataclass

from src import models

@dataclass
class NameGroupElement(models.BaseList):
	name: 'name_group'
```


### Attributes

#### name
**type**: `str`  
**default**: `'base'`   
Наименование группы элементов.  
Используется как префикс для сохранения и изъятия элементов из [csv файла](doc/Server/FileCSV.md) игры

#### elements
**type**: `List[str, ...]`  
**default**: `[]`  
Список элементов.

#### suffix
**type**: `bool`  
**default**: `False`   
**Описание**:  
Указание на возможность использование дополнительна суффикса для [имени](#name) при [импорте](#imports) группы элементов.  
При установке флага в `True`, атрибут [name](#name) переопределяться на новое значение.  
При [импорте](#imports) с использовании суффикса, наименование должно начинаться с имени указанном в [name](#name), иначе будет исключение `AssertError`

**Пример**:  
```python
from src import models

class NewBase(models.BaseList)
    name = 'new'
    suffix = True

new = NewBase.imports(elements='newsuffix:---')
new.name
>> 'newsuffix'
new.exports()
>> 'newsuffix:---'

```

### Classmethods

#### new
Используется для инициализации группы элементов по определенным условиям.  
По умолчанию создается пустая группа без элементов.  
Возвращается инициализированный класс с группой

```python
group = NameGroupElement.new()
```

#### imports
> [!info]
> Хотел бы придумать другое наименование метода, но пока идей получше нет

Используется для импортирования группы элементов из структуры csv файла игры. 
> [!info]
> Данный метод должен автоматически вызываться в родительском классе с игрой. Но она находится в проработке и на данный момент все происходит руками.

```python
group = NameGroupElement.imports(elements="name_group:elements")
```

Args:  
	***elements***(`str`):   Принимает строковый список элементов в формате:   
	 *Наименование параметра [name](#name)* + *символ ":"* + *список элементов в виде строки*  
	 При установленном флаге в атрибуте [suffix](#suffix), принимает следующий вид:  
	 *Наименование параметра [name](#name)* + ***суффикс*** + *символ ":"* + *список элементов в виде строки* 

**Пример**:  
	'group:xrbg'  
	'groupone:xrbg'

### Methods

#### export
Экспорт группы элементов для сохранения его в [csv файл](doc/Server/FileCSV.md)  
Возвращает строковое значение вида **"[name](#name):''.join([elements](#elements))"**

#### element_add
Добавление элемента в конец списка

Args:
	***element***(`str`): Элемент группы элементов который необходимо добавить в конец списка [elements](#elements)