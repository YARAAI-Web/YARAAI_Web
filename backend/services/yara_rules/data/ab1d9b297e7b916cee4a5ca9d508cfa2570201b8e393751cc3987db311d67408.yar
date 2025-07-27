rule auto_rule_20250727044809_4739 {
  strings:
    $o0 = "fBlockIt" wide ascii nocase
    $o1 = "bShow" wide ascii nocase
    $o2 = "wOemChar" wide ascii nocase
    $o3 = "SetClassLongA" wide ascii nocase
  condition:
    4 of ($o*)
}