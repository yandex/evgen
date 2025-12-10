# EvGen (Event Generator)

EvGen — это инструмент для генерации кода событий аналитики для различных платформ. Он позволяет создать единое описание событий в YAML-формате и автоматически генерировать код на разных языках программирования, а также документацию в различных форматах.

## Использование

Для работы нужны Node.js и pnpm.

```bash
pnpm install
pnpm evgen -e events -c evgen.yaml
```

## Поддерживаемые языки

- Kotlin
- Java
- Swift
- TypeScript
- Dart
- C#

## Содержание

- [Основные концепции](#основные-концепции)
- [Конфигурационный файл evgen.yaml](#конфигурационный-файл-evgenyaml)
- [Файл событий events.yaml](#файл-событий-eventsyaml)
- [Типы данных](#типы-данных)
- [Интерфейсы](#интерфейсы)
- [Платформозависимые параметры](#платформозависимые-параметры)
- [Шаблоны](#шаблоны)
- [Примеры использования](#примеры-использования)
- [Логика работы](#логика-работы)


## Основные концепции

EvGen работает с двумя основными параметрами:

1. **events(или events.yaml)** - yaml-файл или папка с yaml-файлами с событиями
2. **evgen.yaml** - конфигурация генерации кода и документации

Инструмент генерирует:
- Код для различных платформ
- Документацию в форматах Markdown, TXT, YAML
- Проверяет совместимость событий с интерфейсами

## Конфигурационный файл evgen.yaml

### Основная структура

```yaml
code:
  # Конфигурации для генерации кода
  ConfigName1:
    platform: string          # Название платформы
    output_dir: string         # Папка для генерируемого кода
    language: string           # Язык программирования
    class_name: string         # Имя генерируемого класса
    only_last_version: boolean # Генерировать только последние версии (опционально)
    param_name_case: string    # Стиль именования параметров (опционально)
    template_dir: string       # Путь к пользовательским шаблонам (опционально)
    disable_sending_meta: boolean # Отключить _meta для этой платформы (опционально)
    meta_to_send: array           # Какие поля включить в _meta: ['event', 'interfaces'] (опционально)

doc:
  # Конфигурации для генерации документации
  DocName1:
    extension: string          # Расширение файлов (md, txt, yaml)
    output_dir: string         # Папка для документации
    template_dir: string       # Путь к пользовательским шаблонам (опционально)
    tag: string               # Фильтр по тегам (опционально)

options:
  keepParametersOrder: boolean # Сохранять порядок параметров в событиях согласно YAML
  disable_sending_meta: boolean # Отключить добавление _meta атрибута в событиях
  meta_to_send: array           # Какие поля включить в _meta: ['event', 'interfaces']
```

### Поддерживаемые языки

- `kotlin` - Kotlin для Android
- `java` - Java для Android  
- `swift` - Swift для iOS
- `type_script` - TypeScript для веб-платформ
- `dart` - Dart для Flutter
- `c_sharp` - C# для Unity

### Пример конфигурации

```yaml
code:
  AndroidKotlin:
    platform: 'Android'
    output_dir: 'android_kotlin'
    language: 'kotlin'
    class_name: 'EvgenAnalytics'
    only_last_version: true
    param_name_case: 'camelCase'

  iOSSwift:
    platform: 'iOS'
    output_dir: 'ios_swift'
    language: 'swift'
    class_name: 'EvgenAnalytics'

doc:
  Markdown:
    extension: 'md'
    output_dir: 'md_doc'
  
  Txt:
    extension: 'txt' 
    output_dir: 'txt_doc'

options:
  keepParametersOrder: true
```

### Опции конфигурации

#### `keepParametersOrder`
Сохраняет порядок параметров в событиях согласно YAML-спецификации.
- `false` (по умолчанию) — параметры, включённые через `_included`, располагаются перед остальными (для совместимости с предыдущими версиями)
- `true` — порядок параметров соответствует порядку в YAML

#### `disable_sending_meta`
Отключает добавление атрибута `_meta` и генерацию функции `makeMeta` в сгенерированном коде.
- `false` (по умолчанию) — атрибут `_meta` добавляется к каждому событию с информацией о версии и интерфейсах
- `true` — атрибут `_meta` и функция `makeMeta` не генерируются

Эту опцию можно задать глобально в `options`, а также переопределить для конкретной платформы в конфигурации `code`. Настройка платформы имеет приоритет над глобальной.

**Пример с глобальным отключением:**
```yaml
options:
  disable_sending_meta: true  # Отключено для всех платформ

code:
  Android:
    platform: 'Android'
    output_dir: 'android'
    language: 'kotlin'
```

**Пример с переопределением для платформы:**
```yaml
options:
  disable_sending_meta: false  # Включено глобально

code:
  Android:
    platform: 'Android'
    output_dir: 'android'
    language: 'kotlin'
    disable_sending_meta: true  # Но отключено для Android

  iOS:
    platform: 'iOS'
    output_dir: 'ios'
    language: 'swift'
    # Использует глобальную настройку (false)
```

#### `meta_to_send`
Позволяет выборочно указать, какие поля включать в атрибут `_meta`. Работает только если `disable_sending_meta` не установлен в `true`.

- Массив, который может содержать значения: `'event'`, `'interfaces'`
- По умолчанию (не указано) — включаются все поля: `['event', 'interfaces']`

Доступные значения:
- `'event'` — включает информацию о версии события (`{ event: { version: N } }`)
- `'interfaces'` — включает информацию об интерфейсах (`{ interfaces: {...} }`)

Эту опцию можно задать глобально в `options`, а также переопределить для конкретной платформы.

> **Важно:** `disable_sending_meta: true` имеет больший приоритет — если он установлен, `meta_to_send` игнорируется.

**Пример — отправлять только версию события:**
```yaml
options:
  meta_to_send: ['event']  # Только версия события, без интерфейсов

code:
  Android:
    platform: 'Android'
    output_dir: 'android'
    language: 'kotlin'
```

**Пример — разная конфигурация для разных платформ:**
```yaml
options:
  meta_to_send: ['event', 'interfaces']  # Полная мета для всех

code:
  Android:
    platform: 'Android'
    output_dir: 'android'
    language: 'kotlin'
    meta_to_send: ['event']  # Только версия для Android

  iOS:
    platform: 'iOS'
    output_dir: 'ios'
    language: 'swift'
    disable_sending_meta: true  # Полностью отключить _meta для iOS
```

## Файл событий (один events.yaml в простейшем случае, но так же может быть и папка с такими файлами)

### Основная структура

```yaml
# Глобальные параметры (добавляются ко всем событиям)
.GlobalParams:
  parameters:
    globalParam:
      type: String
      description: "Глобальный параметр"
  description: "Глобальные параметры"

# Платформозависимые параметры (добавляются ко всем событиям платформы)
.PlatformParams:
  Android:
    description: "Параметры для Android"
    parameters:
      appVersion:
        type: String
        description: "Версия приложения"

# События
Events:
  Namespace:
    EventName:
      v1:
        description: "Описание события"
        parameters:
          param1:
            type: String
            description: "Описание параметра"
        platforms:
          Android:
            app_versions: "1.0.0"
            ticket: "https://tracker.com/TICKET-123"

# Интерфейсы
Interfaces:
  InterfaceName:
    v1:
      description: "Описание интерфейса"
      parameters:
        requiredParam:
          type: String
          description: "Обязательный параметр"
```

### Поля события

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| `description` | string | Да | Описание события |
| `parameters` | object | Нет | Параметры события |
| `platforms` | object | Да | Поддерживаемые платформы |
| `comment` | string | Нет | Дополнительный комментарий |
| `interface` | string/array | Нет | Интерфейсы, которым должно соответствовать событие |
| `namespaces` | array | Нет | Дополнительные пространства имен |
| `force_event_name` | string | Нет | Принудительное имя события |
| `tags` | string/array | Нет | Теги для фильтрации |

### Поля параметра

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| `type` | string/object | Да | Тип данных параметра |
| `description` | string | Нет | Описание параметра |
| `default_value` | any | Нет | Значение по умолчанию |
| `abstract` | boolean | Нет | Абстрактный параметр |
| `optional` | boolean | Нет | Опциональный параметр |
| `element_type` | string/object | Нет | Тип элементов для списков |

### Поля платформы

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| `app_versions` | string/number | Да | Версия приложения или статус |
| `ticket` | string | Нет | Ссылка на задачу в трекере |

Специальные значения для `app_versions`:
- `in_progress` - в разработке
- `not_supported` - не поддерживается
- Конкретная версия (например, `"1.0.0"`, `42`)

## Типы данных

### Примитивные типы

```yaml
parameters:
  stringParam:
    type: String
    description: "Строковый параметр"
    
  intParam:
    type: Int
    description: "Целочисленный параметр"
    
  longIntParam:
    type: "Long Int"
    description: "Длинное целое число"
    
  boolParam:
    type: Bool
    description: "Булевый параметр"
    
  doubleParam:
    type: Double
    description: "Параметр с плавающей точкой"
```

### Перечисления (Enum)

```yaml
parameters:
  # Простое перечисление
  enumParam:
    type:
      Enum:
        name: MyEnum  # Опциональное имя
        values:
          - option1
          - option2
          - option3
    description: "Перечисление"
    default_value: option1

  # Перечисление с описаниями
  enumWithDescriptions:
    type:
      Enum:
        name: PagesEnum
        values:
          - value: screen_1
            description: "Первый экран"
          - value: screen_2  
            description: "Второй экран"

  # Числовое перечисление
  enumInt:
    type:
      Enum:
        values: [1, 2, 3]
```

### Словари (Dict)

```yaml
parameters:
  # Простой словарь (String -> element_type)
  dictParam:
    type: Dict
    description: "Простой словарь"
    element_type: String # (optional)

  # Словарь с типом Enum
  dictWithElementType:
    type: Dict
    element_type:
      Enum:
        name: DictValueType
        values: [option1, option2]

  # Типизированный словарь с разными типами значений { stringField: String, intField: Int, boolField: Bool }
  typedDict:
    type:
      Dict:
        stringField: String
        intField: Int
        boolField: Bool

```

### Списки (List)

```yaml
parameters:
  # Простой список
  listParam:
    type: List
    element_type: String
    default_value: empty_list

  # Типизированный список словарей [{ itemName: String, itemId: Int}]
  typedList:
    type:
      List:
        itemName: String
        itemId: Int

  # Список перечислений
  enumList:
    type: List
    element_type:
      Enum:
        values: [val1, val2, val3]
```

### Константы

```yaml
parameters:
  # Простая константа
  constParam:
    type:
      Const: "FIXED_VALUE"
    description: "Константа"

  # Платформозависимая константа
  platformConst:
    type:
      PlatformConst:
        Android: "AndroidValue"
        iOS: "iOSValue"
        Flutter: "FlutterValue"
```

## Интерфейсы

Интерфейсы позволяют определить общие требования к событиям:

```yaml
Interfaces:
  Page:
    v1:
      description: "Протокол показа страницы"
      parameters:
        page:
          type: String
          description: "Название страницы"
        pageId:
          type: Int
          description: "ID страницы"

  Movie:
    v1:
      description: "Протокол фильма"
      parameters:
        movieName:
          type: String
          description: "Название фильма"
    
    v2:
      description: "Расширенный протокол фильма"  
      parameters:
        movieId:
          type: Int
          description: "ID фильма"
        movieName:
          type: String
          description: "Название фильма"

Events:
  Shop:
    Showed:
      v1:
        description: "Показ магазина"
        interface: Page  # Должно содержать параметры интерфейса Page
        parameters:
          page:
            type: String
            description: "Название страницы"
          pageId:
            type: Int  
            description: "ID страницы"

  MoviePage:
    Showed:
      v1:
        description: "Показ страницы фильма"
        interface: 
          - Page
          - Movie  # Несколько интерфейсов
        parameters:
          page:
            type: String
          pageId:
            type: Int
          movieId:
            type: Int
          movieName:
            type: String
```

## Платформозависимые параметры

Платформозависимые параметры добавляются автоматически ко всем событиям конкретной платформы:

```yaml
.PlatformParams:
  Android:
    description: "Параметры для Android"
    parameters:
      appVersion:
        type: String
        description: "Версия приложения"
      deviceModel:
        type: String
        description: "Модель устройства"

  iOS:
    description: "Параметры для iOS"
    parameters:
      hasSubscription:
        type: Bool
        description: "Наличие подписки"

Events:
  MyEvent:
    v1:
      description: "Мое событие"
      parameters:
        customParam:
          type: String
      platforms:
        Android:
          app_versions: "1.0.0"
        iOS:  
          app_versions: "1.0.0"
```

В результате для Android будут параметры: `customParam`, `appVersion`, `deviceModel`
Для iOS: `customParam`, `hasSubscription`

## Шаблоны

EvGen использует шаблоны Handlebars для генерации кода. Встроенные шаблоны находятся в папке `src/templates/`.

Доступные хелперы в шаблонах:
- Все из категорий 'comparison', 'array', 'string', 'object', 'collection', 'math' из [Handlebars-helpers](https://github.com/helpers/handlebars-helpers?tab=readme-ov-file#categories)
- Кастомные хелперы:
    * изменение кейса (эти были сделаны в основном для сохранения поведения кодогенерации для внутренних проектах по сравнению с предыдущим генератором, но также можно использовать другие хелперы из [Handlebars-helpers](https://github.com/helpers/handlebars-helpers?tab=readme-ov-file#string-helpers)):
      - `camelcase` - `{{camelcase "userName"}}` → `userName`
      - `pascalcase` - `{{pascalcase "userName"}}` → `UserName`
      - `snakecase` - `{{snakeCase userName}}` → `user_name`
      - `uppersnakecase` - `{{upperSnakeCase "userName"}}` → `USER_NAME`
      - `upperCase` - `{{upperCase "userName"}}` → `USERNAME`
      - `lowerFirstLetter` - `{{lowerFirstLetter "Hello"}}` → `hello`
      - `upperFirstLetter` - `{{upperFirstLetter "hello"}}` → `Hello`
    * проверка типа:
      - `isNumber` - `{{#if (isNumber value)}}число{{/if}}`
      - `isString` - `{{#if (isString value)}}строка{{/if}}`
      - `isEnum` - `{{#if (isEnum parameter.type)}}Enum {{parameter.name}}{{/if}}`
      - `isTypedList` - `{{#if (isTypedList parameter.type)}}список{{/if}}`
      - `isTypedDict` - `{{#if (isTypedDict parameter.type)}}словарь{{/if}}`
      - `isConst` - `{{#if (isConst parameter.type)}}"{{parameter.type.Const}}"{{/if}}`
      - `isPlatformConst` - `{{#if (isPlatformConst parameter.type)}}платформенная константа{{/if}}`
      - `isNamedEnum` - `{{#if (isNamedEnum parameter.type)}}именованный enum{{/if}}`
      - `isCustomParameter` - `{{#if (isCustomParameter parameter.type)}}пользовательский тип{{/if}}`
      - `isNamedCustomType` - `{{#if (isNamedCustomType parameter.type)}}именованный тип{{/if}}`
    * фильтрация:
      - `filterTruthy` - `{{#filterTruthy events "isActive"}}{{#each this}}{{name}} is truthy{{/each}}{{/filterTruthy}}`
      - `filterFalsy` - `{{#filterFalsy parameters "isOptional"}}{{#each}}{{name}} is required{{/each}}{{/filterFalsy}}`
      - `filterDefined` - `{{#filterDefined parameters "defaultValue"}}{{#each}}{{name}} с дефолтным значением{{/each}}{{/filterDefined}}`
      - `filterUndefined` - `{{#filterUndefined parameters "defaultValue"}}{{#each}}{{name}} без дефолтного значения{{/each}}{{/filterUndefined}}`
    * другие полезные хелперы:
      - `isDefined` - `{{#if (isDefined value)}}определено{{/if}}`
      - `toArray` - `{{#contains (toArray 'Int' 'Double') 'Int'}}Int{{/contains}}`
      - `splitByNewLine` - `{{splitByNewLine "line1\nline2"}}` → `["line1", "line2"]`
      - `escape` - `{{#escape newLine="\n"}}контент{{/escape}}`
      - `repeat` - `{{repeat "-" 3}}` → `"---"`
      - `entries` - `{{#each (entries object)}}{{key}}: {{value}}{{/each}}`
      - `groupBy` - `{{#each (groupBy events "namespace")}}группа{{/each}}`


### Пользовательские шаблоны

Можно создать собственные шаблоны и указать путь в конфигурации:

```yaml
code:
  CustomAndroid:
    platform: 'Android'
    language: 'kotlin'
    template_dir: 'my-templates/kotlin'
    # ... остальная конфигурация
```

### Доступные переменные в шаблонах

#### Основные переменные

- **`classname`** (`string`) - имя генерируемого класса из конфигурации
- **`onlyLastVersion`** (`boolean`) - флаг генерации только последних версий событий
- **`disableSendingMeta`** (`boolean`) - флаг полного отключения генерации `_meta` атрибута
- **`sendMetaEvent`** (`boolean`) - включать ли версию события в `_meta.event`
- **`sendMetaInterfaces`** (`boolean`) - включать ли интерфейсы в `_meta.interfaces`

#### Параметры

- **`globalParameters`** (`GlobalParameters`) - глобальные параметры
  - `parameters: EventParameter[]` - массив параметров
  - `description: string` - описание глобальных параметров
  - `comment?: string` - дополнительный комментарий

- **`platformParameters`** (`Record<string, PlatformParameters>`) - параметры для каждой платформы
  - `parameters: EventParameter[]` - массив параметров платформы
  - `description: string` - описание параметров платформы
  - `comment?: string` - дополнительный комментарий

#### События и пространства имен

- **`eventNamespaces`** (`EventNamespace[]`) - массив пространств имен событий
  - `name: string` - название пространства имен
  - `events: Event[]` - массив событий в пространстве имен
  - `documentationDir?: string` - директория для документации
  - `allVersions: EventVersion[]` - все версии событий (добавляется при обработке)
  - `actualVersions: EventVersion[]` - актуальные версии событий
  - `deprecatedVersions: EventVersion[]` - устаревшие версии событий
  - `allPlatforms: string[]` - все поддерживаемые платформы
  - `namedEnums: EventParameter[]` - именованные перечисления в пространстве имен
  - `namedCustomParameters: EventParameter[]` - именованные пользовательские типы

- **`allVersionsByEvent`** (`Record<string, EventVersion[]>`) - все версии событий, сгруппированные по имени события

#### Типы и перечисления

- **`namedEnums`** (`EventParameter[]`) - глобальные именованные перечисления
  - Каждый элемент содержит `type.Enum.name` для именованных enum'ов

- **`namedCustomParameters`** (`EventParameter[]`) - глобальные именованные пользовательские типы
  - Элементы с пользовательскими типами данных

#### Интерфейсы (только для документации)

- **`interfaces`** (`Record<string, InterfaceVersion[]>`) - интерфейсы, доступные только в шаблонах документации
  - `name: string` - название интерфейса
  - `namespace: string` - пространство имен
  - `version: number` - версия интерфейса
  - `parameters: EventParameter[]` - параметры интерфейса
  - `description: string` - описание интерфейса

#### Общие данные

- **`shared`** (произвольной структуры) - общие данные из блока `Shared` в YAML файлах

#### Структура EventParameter

```typescript
interface EventParameter {
  name: string;                    // Имя параметра
  namespace: string;               // Пространство имен
  version: number;                 // Версия
  type: ParameterType;            // Тип параметра (см. раздел "Типы данных")
  description: string;             // Описание параметра
  abstract: boolean;               // Абстрактный параметр
  optional: boolean;               // Опциональный параметр
  elementType?: PrimitiveType;     // Тип элементов для List/Dict
  defaultValue?: string;           // Значение по умолчанию
}
```

#### Структура EventVersion

```typescript
interface EventVersion {
  event: string;                           // Полное имя события
  name: string;                           // Короткое имя события
  namespace: string;                      // Пространство имен
  additionalNamespaces: string[];         // Дополнительные пространства имен
  version: number;                        // Версия события
  description: string;                    // Описание события
  interfaces: Record<string, number>;     // Используемые интерфейсы
  comment?: string;                       // Комментарий
  interfaceNames?: string[];              // Имена интерфейсов
  tags: string[];                         // Теги события
  platforms?: Record<string, Platform>;   // Поддерживаемые платформы
  parameters: EventParameter[];           // Параметры события
}
```

## Примеры использования

### Простое событие

```yaml
Events:
  User:
    Login:
      v1:
        description: "Вход пользователя в систему"
        parameters:
          userId:
            type: Int
            description: "ID пользователя"
          loginMethod:
            type:
              Enum:
                name: LoginMethod
                values: [email, phone, social]
            description: "Способ входа"
        platforms:
          Android:
            app_versions: "2.1.0"
            ticket: "https://tracker.com/USER-123"
          iOS:
            app_versions: "2.0.5"
```

### Событие с интерфейсами

```yaml
Interfaces:
  Trackable:
    v1:
      parameters:
        eventId:
          type: String
        timestamp:
          type: "Long Int"

Events:
  Product:
    Purchase:
      v1:
        description: "Покупка товара"
        interface: Trackable
        parameters:
          eventId:
            type: String
          timestamp:
            type: "Long Int"  
          productId:
            type: Int
          amount:
            type: Double
```

### Модульная структура

Можно разделить события на модули:

**events/user.yaml:**
```yaml
Events:
  User:
    Login:
      v1:
        # ... определение события
```

**events/product.yaml:**
```yaml  
Events:
  Product:
    Purchase:
      v1:
        # ... определение события
```

**events/interfaces.yaml:**
```yaml
Interfaces:
  Trackable:
    v1:
      # ... определение интерфейса
```

## Логика работы

### Процесс генерации

1. **Парсинг конфигурации** - чтение `evgen.yaml`
2. **Парсинг событий** - чтение `events.yaml` или папки с модулями
3. **Валидация** - проверка корректности данных и совместимости с интерфейсами
4. **Обработка для каждой платформы**:
   - Фильтрация событий по платформе
   - Добавление глобальных параметров
   - Добавление платформозависимых параметров
   - Применение версионности
5. **Генерация кода** - использование шаблонов для создания файлов
6. **Генерация документации** - создание документации в указанных форматах

### Именование событий

События именуются по принципу конкатенации неймспейсов через точку:

```yaml
Events:
  Namespace1:
    Namespace2:
      EventName:
        v1:
          # Итоговое имя: "Namespace1.Namespace2.EventName"
```

Можно принудительно задать имя:

```yaml
Events:
  Namespace1:
    EventName:
      v1:
        force_event_name: "custom-event-name"
        # Итоговое имя: "custom-event-name"
```

### Версионирование

События и интерфейсы поддерживают версионирование:

```yaml
Events:
  MyEvent:
    v1:
      # Первая версия
    v2:  
      # Вторая версия

Interfaces:
  MyInterface:
    v1:
      # Первая версия интерфейса
    v2:
      # Вторая версия
```

При указании `only_last_version: true` генерируются только последние версии.

### Проверка совместимости

EvGen проверяет, что события соответствуют указанным интерфейсам:

- Все параметры интерфейса должны присутствовать в событии
- Типы параметров должны совпадать
- Поддерживается проверка совместимости с любой версией интерфейса

### Переиспользование кода

#### Внутри одного файла
EvGen при парсинге полностью поддерживает YAML-якоря (`&anchor`) и ссылки (`*reference`):

```yaml
Constants:
  string: &string String
  description: &description description

Events:
  MyEvent:
    v1:
      parameters:
        param1:
          type: *string
          *description: "Параметр 1"
```

YAML поддерживает специальный синтаксис `<<:` для слияния содержимого якоря в текущий объект:

```yaml
Events:
  MyNamespace:
    # Определение переиспользуемых параметров в блоке inheritance
    inheritance:
      reused_params: &reused_params
        userId:
          type: Int
          description: "ID пользователя"
        timestamp:
          type: "Long Int"
          description: "Временная метка"
    
    Event1:
      v1:
        description: "Первое событие"
        parameters:
          <<: *reused_params  # Вставка всех параметров из якоря
          customParam:
            type: String
            description: "Дополнительный параметр"
        platforms:
          Android:
            app_versions: "1.0.0"
    
    Event2:
      v1:
        description: "Второе событие"
        parameters:
          <<: *reused_params  # Те же параметры переиспользуются
          anotherParam:
            type: Bool
        platforms:
          Android:
            app_versions: "1.0.0"
```

В результате оба события (`Event1` и `Event2`) будут содержать параметры `userId` и `timestamp`, а также свои уникальные параметры.

#### Из другого файла с помощью `!include`

EvGen поддерживает специальную логику для подключения данных из других файлов:

**1. Для подключения значений as is ** используйте тег `!include` с синтаксисом `filename:key.nested_key`:

```yaml
# params.yaml
reused_scalar_values:
  shop_page: shop_page
  default_timeout: 5000
```

```yaml
# events.yaml
Events:
  Shop:
    PageShowed:
      v1:
        parameters:
          pageName:
            type:
              Const: !include params:reused_scalar_values.shop_page
```

**2. Для мержа объекта из другого файла в объект текущего файла (аналог merge key `<<:` но между файлами)  ** используйте префикс `_included` к ключу:

```yaml
# params.yaml
reused_params:
  single_param:
    paramFromAnotherFile:
      type: String
      description: "Параметр из другого файла"
  
  several_params:
    batchParam1:
      type: String
      description: "Первый параметр"
    batchParam2:
      type: Int
      description: "Второй параметр"
```

```yaml
# events.yaml
Events:
  MyEvent:
    v1:
      description: "Событие с переиспользованием параметров"
      parameters:
        customParam:
          type: String
          description: "Кастомный параметр"
        # Включение одного параметра
        _included_single: !include params:reused_params.single_param
        # Включение нескольких параметров
        _included_batch: !include params:reused_params.several_params
```

**Примечания:**
- Путь к файлу указывается без расширения `.yaml`
- Можно использовать вложенные ключи через точку: `file:key.nested_key.deep_key`
- Префикс `_included` к ключу говорит парсеру, что нужно включить содержимое объекта из другого файла

Эта документация охватывает все основные возможности EvGen. Для более детального изучения рекомендуется изучить примеры в папке `tutorial/` пакета.

