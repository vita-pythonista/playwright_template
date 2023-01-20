# Playwright Template

Шаблон тестового фреймворка на playwright

## Запуск тестов

**Для запуска в режиме --headed**
- Запуск в виде браузера для веба с разрешением 1920х1080
```
pytest --headed
```
Параметры беруется из фикстуры browser_content_args

- Запуск в виде мобильного браузера iPhone 13
```commandline
pytest --device "iPhone 13" --headed
```
- Запуск в виде мобильного браузера Pixel 5
```commandline
pytest --device "Pixel 5" --headed
```
Можно запустить эмуляцию любого устройства из списка playwright

👇 Ссылка тут

[Список устройств](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json) 

**Для запуска в безголовом режиме**

Все тоже самое, только без --headed