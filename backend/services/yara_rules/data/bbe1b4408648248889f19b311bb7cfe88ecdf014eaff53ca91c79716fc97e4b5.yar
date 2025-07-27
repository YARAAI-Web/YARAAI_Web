rule auto_rule_20250726161326_9978 {
  strings:
    $o0 = "d1r0" wide ascii nocase
    $o1 = "dword_4C12EC" wide ascii nocase
    $o2 = "byte_4C17A8" wide ascii nocase
  condition:
    3 of ($o*)
}