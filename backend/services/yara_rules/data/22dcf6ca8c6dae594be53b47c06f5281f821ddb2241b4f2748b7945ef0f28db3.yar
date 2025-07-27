rule auto_rule_20250727021825_7986 {
  strings:
    $o0 = "GetStringTypeW" wide ascii nocase
    $o1 = "dword_411D70" wide ascii nocase
    $o2 = "padd" wide ascii nocase
  condition:
    3 of ($o*)
}