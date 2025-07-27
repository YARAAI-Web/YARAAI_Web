rule auto_rule_20250726170054_0472 {
  strings:
    $o0 = "CharUpperBuffW" wide ascii nocase
    $o1 = "LibraryA" wide ascii nocase
    $o2 = "dword_4C1320" wide ascii nocase
  condition:
    3 of ($o*)
}