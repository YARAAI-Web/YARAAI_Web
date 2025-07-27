rule auto_rule_20250727035353_3411 {
  strings:
    $o0 = "byte_446AD8" wide ascii nocase
    $o1 = "SetStdHandle" wide ascii nocase
    $o2 = "dword_447024" wide ascii nocase
  condition:
    3 of ($o*)
}