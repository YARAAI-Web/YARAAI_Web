rule auto_rule_20250726141421_2246 {
  strings:
    $o0 = "_String_base" wide ascii nocase
    $o1 = "dword_640334AC" wide ascii nocase
    $o2 = "dwErrCodec" wide ascii nocase
  condition:
    3 of ($o*)
}