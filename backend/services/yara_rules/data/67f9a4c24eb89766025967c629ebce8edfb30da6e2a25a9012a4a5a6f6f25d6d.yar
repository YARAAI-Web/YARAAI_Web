rule auto_rule_20250726212342_9362 {
  strings:
    $o0 = "lpPoint" wide ascii nocase
    $o1 = "IsCharAlphaA" wide ascii nocase
    $o2 = "SHStrDupA" wide ascii nocase
  condition:
    3 of ($o*)
}