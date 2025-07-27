rule auto_rule_20250726145142_2501 {
  strings:
    $o0 = "hObjecta" wide ascii nocase
    $o1 = "dword_6402ED90" wide ascii nocase
    $o2 = "hSCManager" wide ascii nocase
  condition:
    3 of ($o*)
}