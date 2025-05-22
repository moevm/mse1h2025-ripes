# Инструкция по запуску

## Сборка

Сборка состоит из двух этапов:
- Сборка исходников Ripes
  - [Файл сборки Ripes](../docker/ripes.wasm.dockerfile)
- Сборка приложения через `docker compose`
  - [Файл сборки приложения](../docker/docker-compose.yaml)

Сборка проводится из корневой директории

### Сборка Ripes
Сборка Ripes на Windows с помощью wsl не работает.

Для сборки Ripes в консоли введите:

```bash
docker build --rm --tag ripes-wasm:latest -f ./docker/ripes.wasm.dockerfile .
```

### Сборка приложения
По умолчанию для сборки сервера используется [образ Ripes загруженный на docker.hub](https://hub.docker.com/r/jqnfxa/ripes.wasm/tags)

Если необходимо использовать локально собранный Ripes, то замените в [файле сборки сервера](../docker/server.dockerfile) первую строчку с
```dockerfile
FROM jqnfxa/ripes-wasm:latest AS wasm
```
на
```dockerfile
FROM ripes-wasm AS wasm
```

Для сборки приложения в консоли введите:

```bash
docker compose -f ./docker/docker-compose.yaml build
```

# Запуск
Для запуска необходимы файлы окружения созданные в соответствии с примерами:
- [env файл для сервисов БД](../docker/.env.example)
- [env файл для приложения](../moodle/server/.env.example)

Для запуска в консоль введите:
```bash
docker compose -f ./docker/docker-compose.yaml build && docker compose -f ./docker/docker-compose.yaml up
```
