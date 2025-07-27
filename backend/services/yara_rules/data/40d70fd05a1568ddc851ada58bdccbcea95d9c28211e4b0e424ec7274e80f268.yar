rule auto_rule_20250727015252_5453 {
  strings:
    $o0 = "qword_18069E3C8" wide ascii nocase
    $o1 = "qword_18069E768" wide ascii nocase
    $o2 = "qword_18069E028" wide ascii nocase
    $o3 = "qword_18069E320" wide ascii nocase
    $o4 = "qword_1804612B0" wide ascii nocase
  condition:
    4 of ($o*)
}