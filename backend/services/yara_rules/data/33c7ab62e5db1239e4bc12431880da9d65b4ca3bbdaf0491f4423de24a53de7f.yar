rule auto_rule_20250726115509_9614 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "dword_446020" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
    $o3 = "dword_446030" wide ascii nocase
    $o4 = "byte_445EDC" wide ascii nocase
  condition:
    4 of ($o*)
}