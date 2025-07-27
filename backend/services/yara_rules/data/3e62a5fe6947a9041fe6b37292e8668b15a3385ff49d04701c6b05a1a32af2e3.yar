rule auto_rule_20250726125004_9488 {
  strings:
    $o0 = "x415660" wide ascii nocase
    $o1 = "dword_44B7D0" wide ascii nocase
    $o2 = "off_44B548" wide ascii nocase
  condition:
    3 of ($o*)
}