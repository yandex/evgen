using System.Collections.Generic;

public static class MapExtensions {
    public static void PutAll<TKey, TVal>(this Dictionary<TKey, TVal> d, Dictionary<TKey, TVal> dsum) {
        foreach (var dsum_el in dsum) d.Put(dsum_el);
    }
    
    public static void Put<TKey, TVal>(this Dictionary<TKey, TVal> d, KeyValuePair<TKey, TVal> pair) => d.Put(pair.Key, pair.Value);
    
    public static void Put<TKey, TVal>(this Dictionary<TKey, TVal> d, TKey key, TVal val) {
        if (d.ContainsKey(key)) d[key] = val;
        else d.Add(key, val);
    }
}
