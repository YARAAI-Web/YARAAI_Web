rule auto_rule_20250726145929_9108 {
  strings:
    $o0 = "dword_44A3A4" wide ascii nocase
    $o1 = "byte_409E38" wide ascii nocase
    $o2 = "dword_449AC4" wide ascii nocase
  condition:
    3 of ($o*)
}