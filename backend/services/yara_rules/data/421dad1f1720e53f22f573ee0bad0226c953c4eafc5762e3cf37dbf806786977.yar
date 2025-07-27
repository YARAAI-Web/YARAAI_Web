rule auto_rule_20250726214936_9460 {
  strings:
    $o0 = "off_458134" wide ascii nocase
    $o1 = "off_458CB0" wide ascii nocase
    $o2 = "dword_4593A0" wide ascii nocase
    $o3 = "dword_459388" wide ascii nocase
  condition:
    4 of ($o*)
}