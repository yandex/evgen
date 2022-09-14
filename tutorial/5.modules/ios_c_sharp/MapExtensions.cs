using System.Collections.Generic;

public static class MapExtensions {
    public static void putAll<TKey, TVal>(this Dictionary<TKey, TVal> d, Dictionary<TKey, TVal> dsum) {
        foreach (var dsum_el in dsum) d.put(dsum_el);
    }
    
    public static void put<TKey, TVal>(this Dictionary<TKey, TVal> d, KeyValuePair<TKey, TVal> pair) => d.put(pair.Key, pair.Value);
    
    public static void put<TKey, TVal>(this Dictionary<TKey, TVal> d, TKey key, TVal val) {
        if (d.ContainsKey(key)) d[key] = val;
        else d.Add(key, val);
    }
}
