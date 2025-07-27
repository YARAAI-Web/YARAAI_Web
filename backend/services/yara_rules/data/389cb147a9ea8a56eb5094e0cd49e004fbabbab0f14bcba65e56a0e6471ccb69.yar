rule auto_rule_20250726182515_8814 {
  strings:
    $o0 = "x301Bu" wide ascii nocase
    $o1 = "dword_426389" wide ascii nocase
    $o2 = "x8A9D" wide ascii nocase
    $o3 = "x8A29A147" wide ascii nocase
  condition:
    4 of ($o*)
}