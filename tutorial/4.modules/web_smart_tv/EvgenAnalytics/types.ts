/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable
export type UserId = string
export type ContentId = string
export type Timestamp = number
export type Price = number
export type ViewCount = number
export enum PageId {
    Home = 'home',
    Catalog = 'catalog',
    MovieCard = 'movie_card',
    SeriesCard = 'series_card',
}

export type MetadataV1 = { source: string; timestamp: number; }
export type MetadataV2 = { source: string; timestamp: number; tags: []; version: number; }
export type ContentItems = { id: string; title: string; rating: number; }[]
