rule auto_rule_20250726153000_0788 {
  strings:
    $o0 = "x13144B5677153508LL" wide ascii nocase
    $o1 = "dword_140075638" wide ascii nocase
    $o2 = "dword_140075544" wide ascii nocase
    $o3 = "word_14006BC2E" wide ascii nocase
  condition:
    4 of ($o*)
}