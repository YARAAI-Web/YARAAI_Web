rule auto_rule_20250726212554_3245 {
  strings:
    $o0 = "aProgid" wide ascii nocase
    $o1 = "aClsid" wide ascii nocase
    $o2 = "LibraryA" wide ascii nocase
  condition:
    3 of ($o*)
}