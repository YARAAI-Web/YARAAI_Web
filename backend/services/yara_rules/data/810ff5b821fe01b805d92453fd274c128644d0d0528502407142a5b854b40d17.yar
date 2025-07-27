rule auto_rule_20250726140109_1037 {
  strings:
    $o0 = "leaks" wide ascii nocase
    $o1 = "dword_467D20" wide ascii nocase
    $o2 = "Offset" wide ascii nocase
  condition:
    3 of ($o*)
}