rule auto_rule_20250726072730_6498 {
  strings:
    $o0 = "dword_465470" wide ascii nocase
    $o1 = "start_byte_3" wide ascii nocase
    $o2 = "xFFFFFBF7" wide ascii nocase
  condition:
    3 of ($o*)
}