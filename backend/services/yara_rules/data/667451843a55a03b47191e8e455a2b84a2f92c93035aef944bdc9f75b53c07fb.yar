rule auto_rule_20250727041628_3799 {
  strings:
    $o0 = "dword_454FF0" wide ascii nocase
    $o1 = "x429E94" wide ascii nocase
    $o2 = "_cinit" wide ascii nocase
  condition:
    3 of ($o*)
}