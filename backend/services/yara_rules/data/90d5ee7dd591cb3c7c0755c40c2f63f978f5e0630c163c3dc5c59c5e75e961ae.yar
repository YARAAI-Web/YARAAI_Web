rule auto_rule_20250726203940_4523 {
  strings:
    $o0 = "start_byte_3" wide ascii nocase
    $o1 = "_commit" wide ascii nocase
    $o2 = "dword_45AF9C" wide ascii nocase
  condition:
    3 of ($o*)
}