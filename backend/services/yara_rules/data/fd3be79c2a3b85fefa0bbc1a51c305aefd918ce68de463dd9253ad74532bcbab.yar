rule auto_rule_20250726193115_7901 {
  strings:
    $o0 = "dword_44E960" wide ascii nocase
  condition:
    all of them
}