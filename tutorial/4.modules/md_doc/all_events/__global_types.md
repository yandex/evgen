# Глобальные типы

| Имя | Тип |
|:----|:----|
| UserId | String |
| ContentId | String |
| Timestamp | Long Int |
| Price | Double |
| ViewCount | Int |
| PageId | Enum(PageId: home, catalog, movie_card, series_card) |
| Metadata.v1 | Dict(source: String, timestamp: Int) |
| Metadata.v2 | Dict(source: String, timestamp: Int, tags: List, version: Int) |
| ContentItems | List(id: String, title: String, rating: Double) |


