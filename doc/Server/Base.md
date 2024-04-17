
> [!info]  
> Предварительное наименование, так как я не придумал ничего получше пока.

### Оглавление
- [Описание](#Описание)
- [Подключение](#Подключение)
- [**Attributes**](#attributes)
	- [name](#name)
	- [elements](#elements)
	- [suffix](#suffix)
	- [limit](#limit)
- [**Classmethods**](#classmethods)
	- [new](#new)
	- [imports](#imports)
- [**Methods**](#methods)
	- [export](#export)
	- [element_add](#element_add)
- [**Logging**](#logging)
	- [element_add](#element_add)
	- [element_extra](#element_extra)

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

#### limit
**type**: `int`  
**default**: `0`   
**Описание**:  
Для указания лимита хранимых значений в массиве списка при определении класса можно указать максимальное кол-во элементов которое может содержать список [elements](#elements).
Излишние элементы списка которые должны были быть добавлены хранятся в [.log.element_extra](#element_extra)  
**Пример**
```python
from src import model

class NewBase(model.BaseList)
	limit = 1

new = NewBase()
new.element_add(element='rx')
new.element
>> ['r']
new.log.element_extra
>> ['x']
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

**Args**:  
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

**Args**:  
	***element***(`str`): Элемент группы элементов который необходимо добавить в конец списка [elements](#elements)

### Logging

#### element_add
Вывод кол-ва добавленных элементов методом [element_add](#element_add).
```python
.log.element_add
>> NoneType

element_add(element='bb')
.log.element_add
>> ['b', 'b']
```

**Returns**  
`None` или список добавленных элементов

#### element_extra
Если установлено значение [cls.limit](#limit) отличное от нуля. То в данном атрибуте будет хранится список элементов которые не вошли в основной список [элементов](#element) из-за установленного лимита элементов.
